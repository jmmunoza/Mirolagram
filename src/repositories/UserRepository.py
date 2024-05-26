from database.interfaces.UserService import UserService
from src.models.User import User


class UserRepository():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(UserRepository, cls).__new__(cls)
            cls._instance.service = None # TODO
            
        return cls._instance
    
    def getNewFollowers(self) -> list[User]:
        return self.service.getNewFollowers()

    def addFollowers(self, followers: list[User]) -> list[User]:
        return self.service.addFollowers(followers)
    
    def markFollowersAsOld(self, followers: list[User]) -> list[User]:
        return self.service.markFollowersAsOld(followers)