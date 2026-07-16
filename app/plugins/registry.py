PLUGINS = {}


def register(name, func):
    PLUGINS[name] = func


def get(name):
    return PLUGINS.get(name)


def all():
    return PLUGINS


def load_plugins():
    import app.plugins.builtin