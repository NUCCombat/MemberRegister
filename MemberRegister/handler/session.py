from functools import wraps
from flask import session, redirect, url_for

from ..model import Admin


def login_required(fn):
    @wraps(fn)
    def wrapped(*args, **kwargs):
        if not is_auth_in():
            return redirect(url_for("login_page"))
        return fn(*args, **kwargs)

    return wrapped


def auth_in(admin: Admin):
    session['uid'] = admin.id


def is_auth_in() -> bool:
    return 'uid' in session


def auth_out():
    session.clear()


def get_admin() -> Admin:
    return Admin.query.get(session['uid'])