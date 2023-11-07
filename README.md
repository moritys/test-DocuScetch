# test-DocuScetch

Тестовое задание для DocuScetch на позицию "Python Developer/DevOps Trainee"

## Задача

##### Часть 1

Написать bash или python или groovy скрипт, который будет контролировать потребление памяти и генерировать alarm путем отправки http запроса на API

##### Часть 2

Создать docker-compose.yml разворачивающий приложение на python с простой реализацией REST API. Решение должно состоять из двух контейнеров:

1. Любая NoSQL DB.
2. Приложение на python, с использованием Flask, которое слушает на порту 8080 и принимает только методы GET, POST, PUT.

- Создаем значение ключ=значение, изменяем ключ=новое_значение, читаем значение ключа.
- Вновь созданные объекты должны создаваться, изменяться и читаться из NoSQL DB.

## Выбранные технологии для реализации

- python 3.11
- psutil, requests libralies
- docker
- flask

## Запуск приложения
