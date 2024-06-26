from instagrapi import Client

from src.interfaces.InstagramService import InstagramService
from src.models.Post import Post
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
                    str(follower.profile_pic_url)
                )
                
                users.append(user)
                
        except Exception as e:
            return []
            
        return users
    
    def uploadPost(self, post: Post) -> bool:
        try:
            self.client.album_upload(post.media, post.caption)
        except Exception as e:
            return False
        
        return True