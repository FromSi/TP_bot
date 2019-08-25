# Привет!
Это [телеграм бот](https://core.telegram.org/bots), работающий на фреймворке [Flask](https://palletsprojects.com/p/flask/) и использующий библиотеку [SQLAlchemy](https://www.sqlalchemy.org).<br /> 
Бот изначально создавался для ежедневного нахождения ***ГЕЯ*** в конкретном чате. <br />
Сейчас бот разрастается функционалом.. пока нет слов по этому поводу.

## Команды бота
Пока пишется...

## Установка
Предпологается, что Ваша система <strong>UNIX</strong> подобная! [WIKI](https://en.wikipedia.org/wiki/Env) на установку переменных в систему <strong>UNIX</strong>. <br />
<strong>Не обязательно</strong> создавать переменые в Вашей системе! Можно заменить значения в коде, где присутствует ```os.environ```, но этого лучше не делать.

### База Данных
Для начала Вам необходимо будет установить и [СУБД](http://drach.pro/blog/hi-tech/item/145-db-comparison) и создать в ней новую БД. После сделать ссылку [WIKI](https://docs.sqlalchemy.org/en/13/core/engines.html) и вставить эту ссылку в переменные [Вашей системы](https://ru.wikipedia.org/wiki/Переменная_среды). <br />
Сохранить ссылку нужно в переменную c названием ```DATABASE_URL```.

### Телеграм
Создайте телеграм бота и сохраните токен (Токен бота можно получить после создания, у [@BotFather](https://t.me/BotFather)) в переменную с названием  ```TOKEN_BOT```.<br />
Так же нужно будет найти ID чата, где будут происходить действия с ботом (ссылку не предоставлю).

### Прочее, что может понадобится (Прочтите всю документацию и вернитесь сюда)
Во-первых вам придется подключать WebHook. Разверните локально сервер через команду ```python run.py```, запомните порт (он по дефолту <strong>5000</strong>), посмотрите и подключите <strong>ssh</strong> туннель на [ЭТОМ САЙТЕ](http://localhost.run/). [ССЫЛКА](https://core.telegram.org/bots/api#setwebhook) на изменение хука в телеграме. Ваша ссылка для хука ```CUSTOM.localhost.run``` после привязки тунеля к Вашему ПК. <br />
Во-вторых придется запускать [CRON](https://en.wikipedia.org/wiki/Cron) задачи на роутер бота. Например: ```CUSTOM.localhost.run/{os.environ['PATH_CRON_SEARCH']}/```. И да, нужно разобрать код бота, чтобы понять какие там имеются переменные :3

### Установка библиотек (Python3.7)
Для начала необходимо будет установить виртуальное окружение данного проекта и использовать файл <strong>requirements.txt</strong>.<br />
Например:
* Виртуальным окружением будет ```pipenv```. [WIKI](https://habr.com/ru/post/413009/);
* Устанавливаем окружение на ПК ```pip install pipenv```;
* Заходим в корневую директорию проекта и создаем виртуальное окружение ```pipenv shell```;
* Устанавливаем библиотеки ```pipenv install -r requirements.txt```.

### Настройка Базы Данных (СУБД)
Для создания нужного в Вашей БД, нам нужно будет воспользоваться командой ```python migration.py db upgrade```. <br />
Если есть вопросы по тому, что эта команда означает, то вот [ССЫЛКА](https://flask-migrate.readthedocs.io/en/latest/). Файл миграций находится в корневой директории, под названием ```migration.py```.

### Повторим
Еще раз, но кратко.
* Создать бота у [@BotFather](https://t.me/BotFather) и скопировать токен;
* Создать системную переменную ```"TOKEN_BOT" => "SajnasdjnJSNDjoasnAJOSndoj"```;
* Установить и создать базу данный СУБД;
* Создать переменную со ссылкой на БД по [ГАЙДУ](https://docs.sqlalchemy.org/en/13/core/engines.html) ```"DATABASE_URL" => "postgres://root:root@localhost:5432/db_name"```;
* [Как нибудь узнать](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id/32572159#32572159) ID чата и записать в переменную ```"CHAT_ID" => "123456789"```;
* Придумать название пути, по котоому будет вычисляться ГЕЙ и записать в переменную ```"PATH_CRON_SEARCH" => "custom-path"```. После чего, локально это будет выглядеть ```http://localhost:5000/custom-path```. Можно через Cron делать запросы по этой ссылке и ждать нового ГЕЯ;
* Зайти в директорию и создать виртуальное окружение ```pipenv shell```;
* Установить библиотеки ```pipenv install -r requirements.txt```;
* Сделать миграцию ```python migration.py db upgrade```;
* Запустить Flask ```python run.py```. Теперь мы можем делать запросы по ссылке ```http://localhost:5000```;
* Подключить туннель localhost.run WIKI. И теперь наш сервер в публичной сети ```http://name.localhost.run```;
* Подключить ВебХук через веб-браузер ```https://api.telegram.org/bot<token>/setWebhook?url=localhost:5000``` [WIKI](https://core.telegram.org/bots/api#setwebhook);
* Запустить Крон на ```http://localhost:5000/custom-path```;
* Готов!
Так же можно почитать про [Heroku](https://www.heroku.com) и [Temporize Scheduler](https://elements.heroku.com/addons/temporize).

### Пример установки env (ОС переменных) в UNIX
Заходим в домашнюю директорию и находим файл ```.bash_profile``` (или наберите команду ```nano ~/.bash_profile```). И ниже в файл вносим следующие строки (изменяя под себя):
```
export CHAT_ID="1"
export DATABASE_URL="postgres://root:root@127.0.0.1:5432/db_name"
export PATH_CRON_SEARCH="search"
export TOKEN_BOT="123456789:AAHbsQMW2boRQRGAsbq1t28ImmxaXnabXRY"
```

## License
```
The MIT License (MIT)

Copyright (c) 2019 FromSi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
