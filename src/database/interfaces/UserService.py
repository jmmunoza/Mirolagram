from abc import ABC, abstractmethod

from src.models.User import User


class UserService(ABC):
    @abstractmethod
    def getNewFollowers(self) -> list[User]:
        pass
    
    @abstractmethod
    def addFollowers(self, followers: list[User]) -> list[User]:
        pass
    
    def markFollowersAsOld(self, followers: list[User]) -> list[User]:
        pass