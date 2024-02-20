#!/usr/bin/env python3
"""creating a session authentication module"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """SessionAuth class"""

    User_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = uuid4()

        self.User_id_by_session_id[str(session_id)] = user_id

        return str(session_id)
