from .config import settings
from psycopg2.extras import RealDictCursor
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus
#to convert special characters in password to normal string
password = quote_plus(settings.database_password)

SQLALCHEMY_DATABASE_URL=f'postgresql://{settings.database_name}:{password}@{settings.database_hostname}:{settings.database_port}/{settings.database_username}'
engine=create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while loop so that until database connects successfully it is stuck
#while True:     
    #try:
        #conn=psycopg2.connect(host='localhost',database='fastapi',user='postgres',password='Sangbit@2004',cursor_factory=RealDictCursor)
        #cursor=conn.cursor()
        #print("Database connected successfully")
        #break
    #except Exception as error:
     #   print("Database could not be connected")
      #  print("Error:",error)
       # time.sleep(4)
