# Привет!
Это [телеграм бот](https://core.telegram.org/bots), работающий на фреймворке [Flask](https://palletsprojects.com/p/flask/) и использующий библиотеку [SQLAlchemy](https://www.sqlalchemy.org).<br /> 
Бот изначально создавался для ежедневного нахождения ***ГЕЯ*** в конкретном чате. <br />
Сейчас бот разрастается функционалом.. пока нет слов по этому поводу.

## Установка
Предпологается, что Ваша система <strong>UNIX</strong> подобная! [WIKI](https://en.wikipedia.org/wiki/Env) на установку переменных в систему <strong>UNIX</strong>. <br />
<strong>Не обязательно</strong> создавать переменые в Вашей системе! Можно заменить значения в коде, где присутствует ```os.environ```, но этого лучше не делать.

### База Данных
Для начала Вам необходимо будет установить и [СУБД](http://drach.pro/blog/hi-tech/item/145-db-comparison) и создать в ней новую БД. После сделать ссылку [WIKI](https://docs.sqlalchemy.org/en/13/core/engines.html) и вставить эту ссылку в переменные [Вашей системы](https://ru.wikipedia.org/wiki/Переменная_среды). <br />
Сохранить ссылку нужно в переменную c названием ```DATABASE_URL```.

### Телеграм
Создайте телеграм бота и сохраните токен в переменную с названием  ```TOKEN_BOT```.<br />
Так же нужно будет найти ID чата, где будут происходить действия с ботом (ссылку не предоставлю).

### Прочее, что может понадобится (Прочтите всю документацию и вернитесь сюда)
Во-первых вам придется подключать WebHook. Разверните локально сервер через команду ```python run.py```, запомните порт (он по дефолту <strong>5000</strong>), посмотрите и подключите <strong>ssh</strong> тунель на [ЭТОМ САЙТЕ](http://localhost.run/). [ССЫЛКА](https://core.telegram.org/bots/api#setwebhook) на изменение хука в телеграме. Ваша ссылка для хука ```CUSTOM.localhost.run``` после привязки тунеля к Вашему ПК. <br />
Во-вторых придется запускать [CRON](https://en.wikipedia.org/wiki/Cron) задачи на роутер бота. Например: ```CUSTOM.localhost.run/{os.environ['PATH_CRON_SEARCH']}/```. И да, нужно разобрать код бота, чтобы понять какие там имеются переменные :3

### Пока не до конца, но ДОКА питется
