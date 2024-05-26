from msilib.schema import Media

from models.Post import Post
from models.User import User


class CreatePostHandler:
    @staticmethod
    def handle(self, newFollowers: list[User]) -> Post:
        media = [Media("image1.jpg"), Media("image2.jpg")]
        caption = "Welcome to my profile!"
        caption += "\n\n"
        caption += "New followers: "
        
        for follower in newFollowers:
            caption += f"{follower.username}, "
            
        post = Post(media, caption)
        
        return post