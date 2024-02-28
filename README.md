1. `pip install poetry`
2. `poetry install`
3. `rename file .env.example for .env`
4. `refactor file .env where:
    Для получения хеша (hash) и идентификатора (ID) приложения в Telegram (TG) вы должны создать новое приложение через BotFather, который является официальным ботом для создания и управления ботами в Telegram. Вот как это сделать:

   Откройте чат с BotFather в Telegram, нажав на эту ссылку или найдите его через поиск в Telegram.
   
   Напишите /start, чтобы начать взаимодействие с BotFather.
   
   Затем напишите /newbot, чтобы создать нового бота.
   
   BotFather попросит вас выбрать имя для вашего бота. Выберите уникальное имя, оканчивающееся на "bot", например, "my_cool_bot".
   
   После выбора имени BotFather предложит вам токен доступа к вашему боту. Этот токен — это ваш идентификатор приложения (ID). Сохраните его в надежном месте, так как он используется для аутентификации вашего бота в API Telegram.
   
   В дополнение к токену доступа BotFather может предложить вам создать короткое имя для вашего бота (username). Это будет уникальное имя вашего бота в Telegram. Оно должно заканчиваться на "bot" и быть уникальным. Пользователи смогут найти вашего бота по этому имени, добавив его в свои контакты или в чаты.
   
   После завершения этого процесса BotFather предоставит вам ссылку для приглашения вашего бота в группы и чаты.
   
   Вот теперь ваш бот готов к использованию! Вы можете использовать токен доступа (ID) для взаимодействия с API Telegram от имени вашего бота.
   
   Таким образом, в данном контексте "hash" и "ID" соответствуют токену доступа, который вы получаете от BotFather при создании нового бота.`
5.  chanell 