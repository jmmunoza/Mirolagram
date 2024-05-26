from handlers.CreatePostHandler import CreatePostHandler
from interfaces.InstagramService import InstagramService
from repositories.UserRepository import UserRepository


class CreateNewFollowersPostHandler:
    @staticmethod
    def handle(self, service: InstagramService):
        followers = service.getFollowers()
        
        UserRepository().addFollowers(followers)
        
        newFollowers = UserRepository().getNewFollowers()
        
        # take last 10 followers
        followersToPost = newFollowers[-10:]
        
        post = CreatePostHandler.handle(followersToPost)
        
        ok = service.uploadPost(post)
        
        if ok:
            UserRepository().markFollowersAsOld(followersToPost)