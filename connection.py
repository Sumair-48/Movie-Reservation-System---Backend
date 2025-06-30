from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .Config import settings

# dotenv_path = find_dotenv()

# load_dotenv(dotenv_path)

# DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_URL = settings.database_url
# print(DATABASE_URL)
# URL = str(DATABASE_URL)
# DATABASE_URL = "mysql+pymysql://root:118162@127.0.0.1:3306/Movie_Rev"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
