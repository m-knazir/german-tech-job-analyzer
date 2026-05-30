from sqlalchemy import create_engine, text

DB_URL = (
    "postgresql+psycopg2://postgres:password@localhost:5432/job_analyzer"
)

engine = create_engine(DB_URL)

create_jobs_table = """
CREATE TABLE IF NOT EXISTS jobs (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT,
    city TEXT
);
"""

with engine.connect() as connection:
    connection.execute(text(create_jobs_table))
    connection.commit()

print("Jobs Table created")