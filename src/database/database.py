from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.conf.config import settings
# SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://postgres:567234@195.201.150.230:5433/a_makusheva_fa"
# SQLALCHEMY_DATABASE_URL_FOR_WORK = "sqlite:///contacts.db"

SQLALCHEMY_DATABASE_URL_FOR_WORK = settings.sqlalchemy_database_url
#####SQLALCHEMY_DATABASE_URL_FOR_WORK = "sqlite:///for_testing.db"
class Connect_db:

  """
  class Connect_db is responsible for the connection with the database

  :param url: url of the database
  :type url: str
  :param engine: database engine
  :type engine: sqlalchemy engine type
  :param session: session
  :type session: Session
  """

  def __init__(self, url: str):
    """
    constructor
    """
    self.url = url
    ############self.engine = create_engine(url,connect_args={"check_same_thread": False})
    self.engine = create_engine(url)

    self.session = sessionmaker(autocommit=False,
                                autoflush=False,
                                bind=self.engine)

  def __call__(self):
    
    db = self.session()
    try:
      yield db
    finally:
      db.close()

class Connect_db_sqlite:

  """
  class Connect_db_sqlite is responsible for the connection with the sqlite database

  :param url: url of the database
  :type url: str
  :param engine: database engine
  :type engine: sqlalchemy engine type
  :param session: session
  :type session: Session
  """

  def __init__(self, url: str):
    """
    constructor
    """
    self.url = url
    self.engine = create_engine(url,connect_args={"check_same_thread": False})

    self.session = sessionmaker(autocommit=False,
                                autoflush=False,
                                bind=self.engine)

  def __call__(self):
    
    db = self.session()
    try:
      yield db
    finally:
      db.close()