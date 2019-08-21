def airbrake(f):
    def __inner__(*args, **kwargs):
        try:
            f(*args, **kwargs)
        except Exception as e:
            from .utils.client import Client
            c = Client()
            c.notify(exception=e)
            raise e

    return __inner__
