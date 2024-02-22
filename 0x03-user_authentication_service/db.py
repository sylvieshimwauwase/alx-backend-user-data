#!/usr/bin/env python3
"""db module"""

from sqlalchemy.exc import IntegrityError
from user import Base, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine


class DB:
    """DB class"""

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add user"""
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)

        try:
            self._session.commit()

        except IntegrityError:
            self._session.rollback()
            raise
        return user
