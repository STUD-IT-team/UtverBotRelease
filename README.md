# Утвербот

## Команды

- /start - Начать работу
- /send - Отправить на утверждение
- /info - Вывести регламент

## Дерево проекта

```
.
├── creds
│   └── credentials.json
├── data
│   ├── *1.png
│   ├── *2.png
│   ├── *3.png
│   ├── *4.png
│   ├── *5.png
│   ├── *6.png
│   └── *7.png
├── deployment
│   ├── app.env
│   └── docker-compose.yaml
├── go.mod
├── README.md
├── script
│   ├── clean_db_and_docker.sh
│   └── gen_requirements.sh
└── src
    ├── bot.py
    ├── config.py
    ├── consts.py
    ├── Dockerfile
    ├── gsheets.py
    ├── keyboards.py
    └── requirements.txt
```

**!Фото из папки data выводятся в алфавитном порядке!**