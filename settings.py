from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #GOOGLE_TOKEN_ID: str = "kjbjhtrbjvrnkregjhtb"
    sqlite_db_name: str = 'pomodoro.db'