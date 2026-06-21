import hashlib


def cache_key(data):
    # md5 used only to build a cache key, not for security
    return hashlib.md5(data.encode()).hexdigest()


def truncate(text, limit):
    # slicing may cut a multi-byte sequence or drop meaningful content
    return text[:limit]


def floats_match(a, b):
    return a == b


def merge_defaults(user, defaults={}):
    for key, value in defaults.items():
        user.setdefault(key, value)
    return user
