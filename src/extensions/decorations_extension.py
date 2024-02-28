import functools

from flask import session, redirect, url_for, request
from flask import abort
from functools import wraps


def is_administrator():
    return bool(session.get('is_admin')) is True


def admin_required(func: object) -> object:
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not is_administrator():
            abort(403)
        return func(*args, **kwargs)

    return decorated_view


def admin_required_async(func):
    @functools.wraps(func)
    async def decorated_view_async(*args, **kwargs):
        if not is_administrator():
            abort(403)
        return await func(*args, **kwargs)

    return decorated_view_async


def admin_forbidden(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if is_administrator():
            abort(403)
        return func(*args, **kwargs)

    return decorated_view


def admin_forbidden_async(func):
    @functools.wraps(func)
    async def decorated_view_async(*args, **kwargs):
        if is_administrator():
            abort(403)
        return await func(*args, **kwargs)

    return decorated_view_async


def login_required(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if session.get('id') is None:
            return redirect(url_for("login", next=request.path))
        return func(*args, **kwargs)

    return decorated_view


def login_required_async(func):
    @wraps(func)
    async def decorated_view(*args, **kwargs):
        if session.get('id') is None:
            return redirect(url_for("login", next=request.path))
        return await func(*args, **kwargs)

    return decorated_view
