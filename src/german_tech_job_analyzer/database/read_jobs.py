from sqlalchemy import create_engine, text

DB_URL = (
    "postgresql+psycopg2://postgres:password@localhost:5432/job_analyzer"
)

engine = create_engine(DB_URL)

with engine.connect() as connection:
    result = connection.execute(
        text("SELECT * FROM jobs")
    )

    for row in result:
        print(row)