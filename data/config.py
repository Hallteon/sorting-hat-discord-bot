"""Модуль config.py отвечает за загрузку различных ключей доступа для
бота и бд."""

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
DB_URI = env.str("DB_URI")

PREFIX = "/"
