from abc import ABC, abstractmethod

from models.Post import Post
from src.models.User import User


class InstagramService(ABC):
    @abstractmethod
    def login(self, username: str, password: str):
        pass
    
    @abstractmethod
    def getFollowers(self) -> list[User]:
        pass
    
    @abstractmethod
    def uploadPost(self, post: Post) -> bool:
        pass