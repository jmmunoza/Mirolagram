class User:
    def __init__(self, id: str, username: str, name: str, image: str):
        self.id = id
        self.username = username
        self.name = name
        self.image = image

    def __str__(self):
        return f'@{self.username} ({self.name})'