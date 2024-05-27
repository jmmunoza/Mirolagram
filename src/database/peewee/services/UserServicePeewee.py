from src.database.interfaces.UserService import UserService
from src.database.peewee.PeeweeDB import UserPeewee
from src.models.User import User


class UserServicePeewee(UserService):  
    def getNotRepeatedFollowers(self, followers: list[User]) -> list[User]:                
        follower_ids = [follower.id for follower in followers]
        existing_users = UserPeewee.select().where(UserPeewee.idIG.in_(follower_ids))

        existing_user_ids = [user.idIG for user in existing_users]
        new_followers = [follower for follower in followers if follower.id not in existing_user_ids]

        return new_followers
    
    def getNewFollowers(self) -> list[User]:
        return [User(id=user.idIG, username=user.username, name=user.name, image=user.image) for user in UserPeewee.select().where(UserPeewee.isNew == True).order_by(UserPeewee.createdAt.desc())]
    
    def addFollowers(self, followers: list[User]) -> list[User]:
        followersToInsert = []
        
        for follower in followers:
            followersToInsert.append({
                'idIG': follower.id,
                'username': follower.username,
                'name': follower.name,
                'image': follower.image
            })

        UserPeewee.insert_many(followersToInsert).on_conflict_ignore().execute()
        
        return followers
    
    def markFollowersAsOld(self, followers: list[User]) -> list[User]:
        UserPeewee.update(isNew=False).where(UserPeewee.idIG.in_([follower.id for follower in followers])).execute()
        
        return followers
        
        