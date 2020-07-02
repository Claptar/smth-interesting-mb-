import json
import functools


def to_json(fun):
    @functools.wraps(fun)
    def decorated(*args, **kwargs):
        return json.dumps(fun(*args, **kwargs))
    return decorated
