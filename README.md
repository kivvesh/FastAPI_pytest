# Инструкция по развертыванию и тестированию приложения

- Находясь в директории FastAPI_pytest необходимо развернуть docker командой```docker compose up --build```
- После того как docker развернулся необходимо установить все зависимости локально командой ```pip install -r requirements.txt```
- Если необходимо развернуть сервис fastapi локально, то можно командой ```uvicorn src.main:app```
- Swagger будет доступен по url ```http://127.0.0.1:8000/api/openapi/```
- Запускам тесты командой ```pytest -vv```
- Для проверки  тестового покрытия endpoints выполним команду ```pytest --cov=src/tests/functional/points```
- Для генерации отчета по тестам необходимо установить ```sudo dpkg -i allure_2.18.1-1_all.deb``` после запустить тесты  ```pytest --alluredir allure-results```
- Генерируем отчеты на основе созданных json файлов ```allure serve allure-results```
- Перейдя по url ```http://127.0.1.1:34505/index.html``` будет отображаться  графический в формате .html отчет по запущенным тестам
