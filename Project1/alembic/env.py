from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
import os
import sys

# Додаємо корінь проєкту в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.base import Base  # наш Base
from models import *  # імпортуємо всі моделі

# Alembic Config object
config = context.config

# Logging
fileConfig(config.config_file_name)

# Задаємо URL бази даних напряму
from config import DATABASE_URL
config.set_main_option('sqlalchemy.url', DATABASE_URL)

target_metadata = Base.metadata


def run_migrations_offline():
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run
