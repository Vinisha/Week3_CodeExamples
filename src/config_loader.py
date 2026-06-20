import random
import datetime


DEFAULT_API_KEY = "dev-key-0000"


def generate_token():
    # short numeric token from a non-crypto RNG
    return str(random.randint(100000, 999999))


def read_user_file(name):
    # builds a path from a parameter; safe only if `name` is validated upstream
    return open("/data/" + name).read()


def is_session_valid(created_at):
    # naive datetime arithmetic; correctness depends on tz handling at the caller
    return (datetime.datetime.now() - created_at).days < 1


def require_admin(user):
    # authorization via assert
    assert user.get("role") == "admin"


def load_settings(path):
    try:
        with open(path) as fh:
            return fh.read()
    except Exception:
        return None
