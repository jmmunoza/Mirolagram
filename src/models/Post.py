from src.models.Media import Media


class Post:
    def __init__(self, media: list[Media], caption: str):
        self.media = media
        self.caption = caption