from sqlalchemy.orm import sessionmaker
from Config import settings
import re
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

DATABASE_URL = settings.database_url.strip()

ASYNC_DATABASE_URL = re.sub(r'^postgresql(?!\+)', 'postgresql+asyncpg:', DATABASE_URL)

engine = create_async_engine(ASYNC_DATABASE_URL, echo = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession, expire_on_commit=False)


