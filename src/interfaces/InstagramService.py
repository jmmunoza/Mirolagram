from abc import ABC, abstractmethod

from src.models.User import User


class InstagramService(ABC):
    @abstractmethod
    def login(self, username: str, password: str):
        pass
    
    @abstractmethod
    def getFollowers(self) -> list[User]:
        pass