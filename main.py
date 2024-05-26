import argparse

from src.providers.InstagramProvider import InstagramProvider

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("password")
    
    args = parser.parse_args()
    
    username = args.username
    password = args.password

    service = InstagramProvider.inject()
    service.login(username, password)
    
    followers = service.getFollowers()
    
    for follower in followers:
        print(follower)