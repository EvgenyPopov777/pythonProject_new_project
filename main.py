from sqlalchemy.orm import (
Session as SessionType,
scoped_session,
sessionmaker,
)
from models.author import Author
# from models.book import Book
from models.base import engine
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
def create_author (session: SessionType,Name_author:str)-> Author:
    """
    :param session:
    :param Name_author:
    :return:
    """
    author = Author(Name_author=Name_author)
    print("create author", author)
    session.add(author)
    session.commit()
    print("saved author", author)
    return author
def main():
    """
    :return:
    """
    session = Session()
    create_author(session, "Author number one")
    create_author(session, "Author number two")

if __name__=='main':
    main()