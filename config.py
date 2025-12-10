env_vars = {
  # Get From my.telegram.org
  "API_HASH": "26047636",
  # Get From my.telegram.org
  "API_ID": "d8b1ed69ae1f937c5dd4d3cc8c8de440",
  #Get For @BotFather
  "BOT_TOKEN": "",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "mongodb+srv://rohitreddyathuru:R6Co7MOjTYQOAqcq@cluster0.xrwjpl9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "Logfuckers",
  # Force Subs Channel username without @
  "CHANNEL": "",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
