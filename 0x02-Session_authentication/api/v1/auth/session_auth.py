#!/usr/bin/env python3
"""creating a session authentication module"""

from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """SessionAuth class"""

    User_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a session"""
        if user_id is None or type(user_id) != str:
            return None
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        self.User_id_by_session_id[session_id] = user_id
        return session_id
