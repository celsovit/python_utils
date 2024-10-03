# Deletes JPEG files from the current directory

import glob
import os

# Obtém o diretório corrente
diretorio = os.getcwd()

# Exclui todos os arquivos .jpg no diretório
for caminho_jpg in glob.glob(os.path.join(diretorio, '*.jpg')):
    os.remove(caminho_jpg)
    print(f'Excluído: {caminho_jpg}')
