# Converts WebP files to JPEG
# The files are compressed into ZIP format

# Requires Pillow library for image processing
# Install it using: pip install Pillow

import os
import zipfile
import shutil
from PIL import Image

diretorio = os.getcwd()

nova_pasta = os.path.join(diretorio, 'imagens_jpeg')

# Cria a nova pasta, se não existir
os.makedirs(nova_pasta, exist_ok=True)

for arquivo in os.listdir(diretorio):
    if arquivo.endswith('.webp'):

        caminho_webp = os.path.join(diretorio, arquivo)
        
        nome_jpeg = os.path.splitext(arquivo)[0] + '.jpg'
        caminho_jpeg = os.path.join(nova_pasta, nome_jpeg)  # Salva na nova pasta

        with Image.open(caminho_webp) as img:
            img.convert('RGB').save(caminho_jpeg, 'JPEG')

        print(f'Convertido: {caminho_webp} para {caminho_jpeg}')

# Cria um arquivo ZIP com o conteúdo da nova pasta
zip_filename = os.path.join(diretorio, 'imagens_jpeg.zip')
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for root, dirs, files in os.walk(nova_pasta):
        for file in files:
            # Adiciona o arquivo ao ZIP, mantendo a estrutura de diretórios
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), nova_pasta))

# Exclui a nova pasta e seu conteúdo
shutil.rmtree(nova_pasta)

print(f'Arquivo ZIP criado: {zip_filename}')
