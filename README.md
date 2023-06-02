[![foodgram](https://github.com/Oktut/foodgram-project-react/actions/workflows/foodgram.yml/badge.svg)](https://github.com/Oktut/foodgram-project-react/actions/workflows/foodgram.yml)

### Описание
Проект "Foodgram" – это "продуктовый помощник". На этом сервисе авторизированные пользователи могут публиковать рецепты, 
подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд. 
Для неавторизированных пользователей доступны просмотр рецептов и страниц авторов.

http://yafood.sytes.net/admin/
или
http://130.193.34.105/admin/

http://yafood.sytes.net/
или
http://130.193.34.105/

## Технологии: 
  - Python
  - Django REST Framework
  - API REST
  - Postman
  - Simple-JWT
  - Docker
  - Nginx
  - Яндекс.Облако(Ubuntu 20.04 LTS)
 
### Запуск проекта 
## Клонируйте репозиторий на локальный компьютер:
```
git clone git@github.com:Oktut/foodgram-project-react.git
```
### Как запустить проект на боевом сервере:   

Установить на сервере docker и docker-compose.
```
sudo apt install curl
sudo curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo apt update 
sudo apt upgrade -y 
sudo apt install python3-pip python3-venv git -y
mkdir nginx
sudo apt install docker.io
```

Установите docker-compose Проверить версию можно тут:

https://github.com/docker/compose/releases

Установить docker-compose: 
```
sudo curl -SL https://github.com/docker/compose/releases/download/v2.17.2/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose
```

Затем необходимо задать правильные разрешения, чтобы сделать команду docker-compose исполняемой:

```
sudo chmod +x /usr/local/bin/docker-compose
sudo apt install apt-transport-https
sudo apt install ca-certificates
sudo apt install curl
sudo apt install gnupg-agent
sudo apt install software-properties-common -y 
```

Чтобы проверить успешность установки, запустите следующую команду:

```
docker-compose --version
```

Добавить в Secrets на Github следующие данные:

```
DB_ENGINE=django.db.backends.postgresql # указать, что проект работает с postgresql
DB_NAME=postgres # имя базы данных
POSTGRES_USER=postgres # логин для подключения к базе данных
POSTGRES_PASSWORD=postgres # пароль для подключения к БД
DB_HOST=db # название сервиса БД (контейнера) 
DB_PORT=5432 # порт для подключения к БД
DOCKER_PASSWORD= # Пароль от аккаунта на DockerHub
DOCKER_USERNAME= # Username в аккаунте на DockerHub
HOST= # IP удалённого сервера
USER= # Логин на удалённом сервере
SSH_KEY= # SSH-key компьютера, с которого будет происходить подключение к удалённому серверу
PASSPHRASE= #Если для ssh используется фраза-пароль
TELEGRAM_TO= #ID пользователя в Telegram
TELEGRAM_TOKEN= #ID бота в Telegram
```


на локальном компе из папки infra
```
scp docker-compose.yml <логин_на_сервере>@<IP_сервера>:/home/<логин_на_сервере>/docker-compose.yml
scp nginx.conf <логин_на_сервере>@<IP_сервера>:/home/<логин_на_сервере>/nginx.conf

```

### Шаблон наполнения файла .env с переменными окружения (infra/.env)
```
cd foodgram-project-react/infra/
```
С помощью команды ниже в папке будет создан .env-файл
```
echo 'DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=postgres
DB_PORT=5432
' > .env
```
На сервере запустить
```
sudo docker-compose exec backend python manage.py migrate
sudo docker-compose exec backend python manage.py createsuperuser
sudo docker-compose exec backend python manage.py collectstatic --no-input
sudo docker-compose exec backend python manage.py load_ingredients
```
### Документация
Документация с доступными для запросов эндпоинтами после запуска DEV-сервера проекта доступна по адресу:

```
1) http://yafood.sytes.net/ - главная страница;
3) http://yafood.sytes.net/admin/ - администрирование;
4) http://yafood.sytes.net/api/ - API проекта;
5) http://yafood.sytes.net/api/docs/redoc.html - документация к API;
```

### Об авторе

Над проектом работал:
-YaOktut- Кирилов Андрей
[GitHub](https://github.com/Oktut/)
Студент курса "Разработчик Python" (51 когорта). 2022-2023 год.
