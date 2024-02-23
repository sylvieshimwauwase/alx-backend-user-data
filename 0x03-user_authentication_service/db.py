#!/usr/bin/env python3
"""db module"""

from user import Base, User
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
import logging

DATA = ['id', 'email', 'hashed_password', 'session_id', 'reset_token']

logging.basicConfig()
logging.getLogger('sqlalchemy').setLevel(logging.WARNING)


class DB:
    """DB class"""

    def __init__(self):
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add user"""
        if not email or not hashed_password:
            raise ValueError("Email and hashed_password are required.")

        user = User(email=email, hashed_password=hashed_password)
        session = self._session
        session.add(user)
        session.commit()

        return user

    def find_user_by(self, **kwargs) -> User:
        """Find user by"""
        user = self._session.query(User).filter_by(**kwargs).first()
        if user is None:
            raise NoResultFound
        return user
