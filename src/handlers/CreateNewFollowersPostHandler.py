from handlers.CreatePostHandler import CreatePostHandler
from interfaces.InstagramService import InstagramService
from models.Post import Post
from models.User import User
from repositories.UserRepository import UserRepository


class CreateNewFollowersPostHandler:
    @staticmethod
    def handle(self, service: InstagramService):
        self._saveNewFollowers(service)
        followersToPost = self._getFollowersToPost()
        self._createPost(service, followersToPost)
            
    @staticmethod
    def _saveNewFollowers(self, service: InstagramService) -> None:
        followers = service.getFollowers()
        followers = UserRepository().getNotRepeatedFollowers(followers)
        
        UserRepository().addFollowers(followers)
        
    @staticmethod
    def _getFollowersToPost(self) -> list[User]:
        newFollowers = UserRepository().getNewFollowers()
        
        # take last 10 followers
        followersToPost = newFollowers[-10:]
        
        return followersToPost
    
    @staticmethod
    def _createPost(self, service: InstagramService, followersToPost: list[User]) -> Post:
        post = CreatePostHandler.handle(followersToPost)
        
        ok = service.uploadPost(post)
        
        if ok:
            UserRepository().markFollowersAsOld(followersToPost)