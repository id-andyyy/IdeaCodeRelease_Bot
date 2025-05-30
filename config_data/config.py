from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    db_name: str


@dataclass
class TgBot:
    token: str


@dataclass
class ApiConfig:
    base_url: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    api: ApiConfig


def load_config(path: str | None) -> Config:
    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')), db=DatabaseConfig(db_name=env('DB_NAME')), api=ApiConfig(base_url=env('BASE_URL')))
