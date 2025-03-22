from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    #GOOGLE_TOKEN_ID: str = "kjbjhtrbjvrnkregjhtb"
    #sqlite_db_name: str = 'pomodoro.db'
    DB_HOST: str = '0.0.0.0'
    DB_PORT: int = 5432
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = 'password'
    DB_DRIVER: str = 'sqlite:///pomodoro.db'
    DB_NAME: str = 'pomodoro'
    CACHE_HOST: str = '0.0.0.0'
    CACHE_PORT: int = 5432
    CACHE_DB: int = 0

    @property
    def db_url(self):
        return f'{self.DB_PASSWORD}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'