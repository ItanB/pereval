На сайте https://pereval.online/ ФСТР ведёт базу горных перевалов, которая пополняется туристами. ФСТР заказала студентам SkillFactory разработать мобильное приложение для Android и IOS, которое упростило бы туристам задачу по отправке данных о перевале и сократило время обработки запроса до трёх дней. Пользоваться мобильным приложением будут туристы. В горах они будут вносить данные о перевале в приложение и отправлять их в ФСТР, как только появится доступ в Интернет. Модератор из федерации будет верифицировать и вносить в базу данных информацию, полученную от пользователей, а те в свою очередь смогут увидеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

В данном проекте реализовано REST API, позволяющее туристу через мобильное приложение отправлять информацию о перевале, а модератору ФСТР верифицировать и вносить в базу данных информацию, полученную от туристов. Туристы смогут видеть в мобильном приложении статус модерации и просматривать базу с объектами, внесёнными другими.

Турист с помощью мобильного приложения должен будет передавать на сервер следующие данные:

Имя пользователя;

Почта и телефон пользователя;
Название перевала;
Координаты перевала и его высота;
Несколько фотографий перевала.
Модератор проверит и установит статус:

на модерации
принят
не принят
Методы API для работы с JSON файлами:

POST/submitData/ Принимает JSON в теле запроса с информацией о перевале.

GET/submitData/ Получает 1 запись по ее id с выведением всей информации об перевале

PATCH/submitData/ Позволяет редактировать запись, если status='new'. Кроме полей относящихся к users.
