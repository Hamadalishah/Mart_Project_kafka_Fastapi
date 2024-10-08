from sqlmodel import SQLModel, Session, create_engine



connection_string = '.env'

engine = create_engine(connection_string)


    
  
def create_table():
    SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session
