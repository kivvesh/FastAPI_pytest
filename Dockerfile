FROM python:3.11

LABEL authors="kivvesh"

# Папка, в которой будут размещаться файлы проекта внутри контейнера
WORKDIR /opt/app

# Копирование в контейнер файлов, которые редко меняются
COPY ./requirements.txt ./requirements.txt

# Установка зависимостей
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копирование остального (для ускорения сборки образа эту команду стоит размещать ближе к концу файла)
COPY . .

EXPOSE 8000

#RUN python -m gunicorn ./src/main:app -k uvicorn.workers.UvicornWorker
ENTRYPOINT ["python", "-m", "gunicorn","-w", "4","-k", "uvicorn.workers.UvicornWorker", "src.main:app","--bind", "0.0.0.0:8000"]