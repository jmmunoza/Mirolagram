from instagrapi import Client

from src.interfaces.InstagramService import InstagramService
from src.models.User import User


class InstagrapiService(InstagramService):
    def login(self, username: str, password: str):
        self.client = Client()
        self.client.login(username, password)

    def getFollowers(self) -> list[User]:
        users = []
        
        try:
            followers = self.client.user_followers(self.client.user_id)
        
            for pk in followers:
                follower = followers[pk]
                user = User(
                    follower.pk, 
                    follower.username, 
                    follower.full_name,
                    follower.profile_pic_url
                )
                
                users.append(user)
                
        except Exception as e:
            return []
            
        return users