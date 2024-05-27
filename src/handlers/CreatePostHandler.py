from src.models.Post import Post
from src.models.User import User


class CreatePostHandler:
    @staticmethod
    def handle(newFollowers: list[User]) -> Post:
        media = [("image1.jpg"), ("image2.jpg")]
        caption = "Welcome to my profile!"
        caption += "\n\n"
        caption += "New followers: "
        
        for follower in newFollowers:
            caption += f"{follower.username}, "
            
        post = Post(media, caption)
        
        return post