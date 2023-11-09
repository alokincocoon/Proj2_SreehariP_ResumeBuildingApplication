from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Declaring engine for DB
engine = create_engine("postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/resume_builder")
# Creating session object to interact with DB or manage transaction
Session = sessionmaker(bind=engine)
# Creating session instance
session = Session()
