import os

import pdfplumber
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Configuração do caminho do Tesseract OCR
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Caminho da pasta com os PDFs
folder_path = "01_E02"

# Lista de TAGs para procurar
tags_procuradas = [
    "MEAT GRINDER",
    "LEAK TEST",
    "FLOWLINE",
    "5602-B",
    "8501",
    "8502",
]


# Caminhos para os arquivos de saída
output_found = "tags_encontradas.txt"
output_not_found = "tags_nao_encontradas.txt"


# Função para pré-processar imagem
def preprocess_image(image):
    # Aplicar filtros para melhorar a qualidade da imagem
    image = image.convert("L")  # Converter para escala de cinza
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(2)  # Aumentar contraste
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # Aumentar brilho
    image = image.filter(ImageFilter.MedianFilter())  # Remover ruído
    return image


# Função para extrair texto usando OCR
def extract_text_with_ocr(pdf_path, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        page = pdf.pages[page_number]
        image = page.to_image(resolution=300)  # Melhorar resolução
        pil_image = image.original  # Extrai a imagem PIL
        pil_image = preprocess_image(pil_image)  # Pré-processa a imagem
        # Configuração do OCR: PSM 6 assume um bloco de texto
        text = pytesseract.image_to_string(pil_image, config="--psm 6")
    return text


# Abrir os arquivos de saída
with open(output_found, "w", encoding="utf-8") as found_file, open(
    output_not_found, "w", encoding="utf-8"
) as not_found_file:
    # Procurar TAGs nos PDFs
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(folder_path, filename)
            tags_found = []  # Lista para armazenar TAGs encontradas
            with pdfplumber.open(pdf_path) as pdf:
                for page_number, page in enumerate(pdf.pages):
                    # Tente extrair texto diretamente da camada de texto
                    text = page.extract_text()
                    if not text or len(text.strip()) < 20:
                        # Se o texto for vazio ou insuficiente, usar OCR
                        text = extract_text_with_ocr(pdf_path, page_number)

                    # Verificar TAGs no texto
                    for tag in tags_procuradas:
                        if tag in text:
                            tags_found.append(
                                f"TAG {tag} : encontrada no arquivo: {filename} (Página {page_number + 1})"
                            )
                            break  # Parar de procurar tags nesta página

            # Salvar resultados
            if tags_found:
                for result in tags_found:
                    found_file.write(result + "\n")
            else:
                not_found_file.write(f"TAGs não encontradas no arquivo: {filename}\n")

    print(f"Resultados salvos em: {output_found} e {output_not_found}")
