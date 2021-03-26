import abc


class Entity(metaclass=abc.ABCMeta):
    @property
    def Id(self):
        raise NotImplementedError

    @property
    def TableName(self):
        raise NotImplementedError

