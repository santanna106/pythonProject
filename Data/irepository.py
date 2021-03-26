import abc


class IRepository(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def add(self):
      pass

   @abc.abstractmethod
   def delete(self):
       pass

   @abc.abstractmethod
   def update(self):
       pass

   @abc.abstractmethod
   def all(self):
       pass

   @abc.abstractmethod
   def findById(self):
       pass