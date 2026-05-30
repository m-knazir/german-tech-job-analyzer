from sqlalchemy import create_engine

DB_URL = (
    "postgresql+psycopg2://postgres:password@localhost:5432/job_analyzer"
)

engine = create_engine(DB_URL)

try:
    with engine.connect() as connection:
        print("Database Connection successful!")
except Exception as error:
    print("❌ Database Connection failed:")
    print(error)