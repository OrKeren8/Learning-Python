from sqlalchemy import create_engine, Column, Integer, String, inspect
from sqlalchemy.orm import declarative_base, sessionmaker

def main():

    # Set up database engine
    engine = create_engine("sqlite:///example.db", echo=True)
    Base = declarative_base()

    # Define a User model
    class User(Base):
        __tablename__ = "users"
        id = Column(Integer, primary_key=True)
        name = Column(String)
        email = Column(String)

    # Create the table
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add a user
    session.add(User(name="Alice", email="alice@example.com"))
    session.commit()

    # Query users
    for user in session.query(User).all():
        print(user.email)

    # inspect the database
    print("\n\nDatabase inspection:")
    inspector = inspect(engine)
    print(inspector.get_table_names())
    print(inspector.get_columns("users"))



if __name__ == "__main__":
    main()
