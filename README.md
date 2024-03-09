# API YaMDb    
### Авторы  
- Кобелев Андрей Андреевич  
    - [email](mailto:andrey.pydev@gmail.com)  
- Никита Макаренко  
    - [github](https://github.com/wArahh)  
  
  
## Краткое описание  
  
**YaMDb** — собирает **отзывы** пользователей на произведения.   
#### Категории  
Произведения делятся на **категории**, такие как «Книги», «Фильмы», «Музыка». Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки» и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»).  
  
#### Жанры  
Произведению может быть присвоен **жанр** из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»).  
  
#### Отзывы  
Благодарные или возмущённые пользователи оставляют к произведениям текстовые **отзывы** и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — **рейтинг** (целое число). На одно произведение пользователь может оставить только один отзыв.  
  
## Примечания  
- Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.  
- Добавлять произведения, категории и жанры может только администратор.  
- Добавлять отзывы, комментарии и ставить оценки могут только аутентифицированные пользователи.  
  
## Ресурсы API **YaMDb**/Документация  
### Ресурсы API
- Ресурс **auth:** аутентификация.  
- Ресурс **users:** пользователи.  
- Ресурс **titles:** произведения, к которым пишут отзывы (определённый фильм, книга или песенка).  
- Ресурс **categories:** категории (типы) произведений («Фильмы», «Книги», «Музыка»). Одно произведение может быть привязано только к одной категории.  
- Ресурс **genres**: жанры произведений. Одно произведение может быть привязано к нескольким жанрам.  
- Ресурс **reviews:** отзывы на произведения. Отзыв привязан к определённому произведению.  
- Ресурс **comments:** комментарии к отзывам. Комментарий привязан к определённому отзыву.  

### Полная документация
Каждый ресурс описан в [документации](http://127.0.0.1:8000/redoc/): указаны эндпоинты (адреса, по которым можно сделать запрос), разрешённые типы запросов, права доступа и дополнительные параметры, когда это необходимо.  
  
## Пользовательские роли и права доступа  
  
- **Аноним** — может просматривать описания произведений, читать отзывы и комментарии.  
- **Аутентифицированный пользователь (**`user`**)** — может читать всё, как и **Аноним**, может публиковать отзывы и ставить оценки произведениям (фильмам/книгам/песенкам), может комментировать отзывы; может редактировать и удалять свои отзывы и комментарии, редактировать свои оценки произведений. Эта роль присваивается по умолчанию каждому новому пользователю.  
- **Модератор (**`moderator`**)** — те же права, что и у **Аутентифицированного пользователя**, плюс право удалять и редактировать **любые** отзывы и комментарии.  
- **Администратор (**`admin`**)** — полные права на управление всем контентом проекта. Может создавать и удалять произведения, категории и жанры. Может назначать роли пользователям.  
- **Суперюзер Django** должен всегда обладать правами администратора, пользователя с правами `admin`. Даже если изменить пользовательскую роль суперюзера — это не лишит его прав администратора. Суперюзер — всегда администратор, но администратор — не обязательно суперюзер.  
  
## Регистрация новых пользователей  
### Самостоятельная регистрация  
1. Пользователь отправляет POST-запрос с параметрами `email` и `username` на эндпоинт `/api/v1/auth/signup/`.  
2. Сервис **YaMDB** отправляет письмо с кодом подтверждения (`confirmation_code`) на указанный адрес `email`.  
3. Пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен).  
  
### Создание пользователя администратором  
Пользователей создаёт администратор — через админ-зону сайта или через POST-запрос на специальный эндпоинт `api/v1/users/` (описание полей запроса для этого случая есть в документации). При создании пользователя не предполагается автоматическая отправка письма пользователю с кодом подтверждения.  
  
После этого пользователь должен самостоятельно отправить свой `email` и `username` на эндпоинт `/api/v1/auth/signup/` , в ответ ему должно прийти письмо с кодом подтверждения.  
  
Далее пользователь отправляет POST-запрос с параметрами `username` и `confirmation_code` на эндпоинт `/api/v1/auth/token/`, в ответе на запрос ему приходит `token` (JWT-токен), как и при самостоятельной регистрации.  
  
  
В результате пользователь получает токен и может работать с API проекта, отправляя этот токен с каждым запросом.  
  
После регистрации и получения токена пользователь может отправить PATCH-запрос на эндпоинт `/api/v1/users/me/` и заполнить поля в своём профайле (описание полей — в документации).  
  
## Как запустить проект: 
  
Клонировать репозиторий и перейти в него в командной строке:  
  
```  
git clone https://github.com/wArahh/api_yamdb.git  
```  
  
```  
cd api_yamdb  
```  
  
Cоздать и активировать виртуальное окружение:  
  
```  
python3 -m venv env  
```  
  
```  
source env/bin/activate  
```  
  
Установить зависимости из файла requirements.txt:  
  
```  
python3 -m pip install --upgrade pip  
```  
  
```  
pip install -r requirements.txt  
```  
  
Выполнить миграции:  
  
```  
python3 manage.py migrate  
```  
  
Запустить проект:  
  
```  
python3 manage.py runserver  
```  
  
## Management command: populatingdb - наполнить базу данных

После того как вы выполните все шаги из «**Как запустить проект**» - запустите команду:

```
python3 manage.py populatingdb
```

команда `populatingdb` наполнит БД всеми необходимыми данными для дальнейшей работы с проектом.

Во время успешного выполнения команды в терминале должен быть вот такой текст:

```
START!
Подготовка модели users... (ok)
Подготовка модели genre... (ok)
Подготовка модели category... (ok)
Подготовка модели titles... (ok)
Подготовка модели genre_title... (ok)
Подготовка модели review... (ok)
Подготовка модели comments... (ok)
FINISH!
```

### Откуда идет загрузка данных
В  директории `/api_yamdb/static/data`, подготовлены несколько файлов в формате `csv` с контентом для ресурсов **Users**, **Titles**, **Categories**, **Genres**, **Reviews** и **Comments**.

## Примеры запроса и ответа  
  
### Получение списка всех произведений  
  
Сделайте GET-запрос на адрес:  
  
http://127.0.0.1:8000/api/v1/titles/  
  
Вывод будет таким:  
  
```json
{
  "count": 0,
  "next": "string",
  "previous": "string",
  "results": [
    {
      "id": 0,
      "name": "string",
      "year": 0,
      "rating": 0,
      "description": "string",
      "genre": [
        {
          "name": "string",
          "slug": "string"
        }
      ],
      "category": {
        "name": "string",
        "slug": "string"
      }
    }
  ]
}
```  
  
## Технологии  
- [Python](https://www.python.org/)  
- [Django REST Framework](https://www.django-rest-framework.org/)  
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)