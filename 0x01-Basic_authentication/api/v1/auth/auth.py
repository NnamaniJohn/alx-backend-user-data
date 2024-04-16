#!/usr/bin/env python3
"""Auth module."""
from flask import request
from typing import List, TypeVar


class Auth:
    """Auth class."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authentication."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        for p in excluded_paths:
            if p.endswith('*') and path.startswith(p[:-1]):
                return False
            if path == p:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """Authorization header."""
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Current user."""
        return None
