from src.handlers.CreatePostHandler import CreatePostHandler
from src.interfaces.InstagramService import InstagramService
from src.models.Post import Post
from src.models.User import User
from src.repositories.UserRepository import UserRepository


class CreateNewFollowersPostHandler:
    @staticmethod
    def handle(service: InstagramService):
        CreateNewFollowersPostHandler._saveNewFollowers(service)
        followersToPost = CreateNewFollowersPostHandler._getFollowersToPost()
        CreateNewFollowersPostHandler._createPost(service, followersToPost)
            
    @staticmethod
    def _saveNewFollowers(service: InstagramService) -> None:
        followers = service.getFollowers()
        followers = UserRepository().getNotRepeatedFollowers(followers)
        
        UserRepository().addFollowers(followers)
        
    @staticmethod
    def _getFollowersToPost() -> list[User]:
        newFollowers = UserRepository().getNewFollowers()
        followersToPost = newFollowers[-10:]
        
        return followersToPost
    
    @staticmethod
    def _createPost(service: InstagramService, followersToPost: list[User]) -> Post:
        post = CreatePostHandler.handle(followersToPost)
        
        ok = service.uploadPost(post)
        
        if ok:
            UserRepository().markFollowersAsOld(followersToPost)