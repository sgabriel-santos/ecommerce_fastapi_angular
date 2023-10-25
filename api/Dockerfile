# imagem de referência para o container backend: baseada na imagem de python 3.10
FROM tiangolo/uvicorn-gunicorn:python3.10

# cria um diretório chamadao 'api' dentro no container criado
WORKDIR /api

# copia o arquivo requirements.txt para o diretório requirements.txt
COPY ./requirements.txt /api/requirements.txt

# instalada todas as dependências dentro da imagem
RUN pip install --no-cache-dir -r /api/requirements.txt

# copia o diretório atual para diretório api dentro do container
COPY ./ /api
