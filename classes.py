# from abc import ABC, abstractmethod


class Area:
    """Создаёт игровое поле по шаблонам Синглтон и Моносостояние"""
    __instance = None
    __shared_fields = {

    }

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.__dict__ = self.__shared_fields
