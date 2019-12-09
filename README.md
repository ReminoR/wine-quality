В качестве прогнозной модели был выбран Random Forest, так как показал лучшие результаты на валидационной выборке 
(Средняя F1-мера: 86.9%)

1. Зайти в директорию rest_api/Dockerfile 
2. Создать образ - docker build . -t  wine-quality-image
2. Создать контейнер docker run --name wine-quality-cont -p 9999:9999 wine-quality-image
3. Отправить POST-запрос любым удобным способом. Отправляемые данные должны быть представлены в виде массива (списка) из 11 элементов: 
[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]
endpoint: http://0.0.0.0:9999/rf_model/

Пример POST запроса Curl<br/>
curl -d "[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]" -X POST http://0.0.0.0:9999/rf_model/

Пример запроса в python скрипте через библиотеку requests находится в файле: requests_example.py

HTML версия Jupyter Notebook находится по ссылке: https://reminor.github.io/wine-quality/


