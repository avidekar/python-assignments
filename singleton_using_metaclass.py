# tested on python3.8 version

class MetaClass(type):

    _instance = None

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = type.__call__(cls, *args, **kwargs)
        return cls._instance


obj_one = Singleton()
print(obj_one)

obj_sec = Singleton()
print(obj_sec)