import abc


class IRepository(metaclass=abc.ABCMeta):
   @abc.abstractmethod
   def add(self,object):
      pass

   @abc.abstractmethod
   def delete(self,object):
       pass

   @abc.abstractmethod
   def update(self,object):
       pass

   @abc.abstractmethod
   def all(self,object):
       pass

   @abc.abstractmethod
   def findById(self,Id):
       pass