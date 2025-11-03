from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    BOT_TOKEN: str

    class Config:
        env_file = "C:/Users/rika5/PycharmProjects/nntuWashingMachine/.env"

    def get_db_url(self):
        return (f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@"
                f"{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}")

    def get_sqlite_url(self):
        return "sqlite+aiosqlite:///db.sqlite3"


settings = Settings()
