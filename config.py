#este archivo lee del archivo .env y de cada valor crea una variable
#en el computador o varible de sistema

from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
port = os.environ['MYSQL_PORT']
database = os.environ['MYSQL_DATABASE']


DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'