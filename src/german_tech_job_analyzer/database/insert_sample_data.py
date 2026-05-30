from sqlalchemy import create_engine, text

DB_URL = (
    "postgresql+psycopg2://postgres:password@localhost:5432/job_analyzer"
)

engine = create_engine(DB_URL)

insert_query = """
INSERT INTO jobs (title, company, city)
VALUES
    ('Data Analyst', 'Tech GmbH', 'Köln'),
    ('Python Developer', 'Data Solutions', 'Berlin'),
    ('Java Backend Developer', 'Cloud Systems', 'Hamburg');
"""

with engine.connect() as connection:
    connection.execute(text(insert_query))
    connection.commit()

print("Sample data inserted")