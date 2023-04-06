<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <H1 style="text-align:center;">
        Database Snapshot taker
    </H1>
    <div style="text-align:center;">
        <img src="./docs/database_snapshot.jpg" width="600" height="400">
    </div>
</body>
</html>

# About
Takes snapshot of database that you configured. After you give database cridentials and table_names in configuration file, you will have to give config file name in `.env` file separating them with (,) comma signs.

# Configure and run in your environment.
## 1 Clone the source code
#### Clone using git 
``` 
git clone https://github.com/uzbekman2005/postgres-snapshot-taker.git 
```
#### Download zip file. 
After installing zip file unzip it a path you write code. 

## 2 Configuration
Add your database configuration files to ./database/db_config/config_files. Configuration template is given there.

## 3 Set environment variables
Add your environment variables to .env file as shown there.
```
DB_FILES=my_db_config # names of database config files separating them with (,).
ADMIN_TG_ID=123456  # telegram id of admin
BOT_TOKEN=your_bot_token_generated_by_bot_father
SLEEP_TIME=600 # send snapshot in every {sleep time} minutes
```

## 4 Run the source code using docker
Make sure that you docker installed and run the following command to start the bot.
```
cd /path/to/project && docker compose up -d --build
```