from src.interfaces.InstagramService import InstagramService
from src.services.instagrapi.InstagrapiService import InstagrapiService


class InstagramProvider:
    @staticmethod
    def inject() -> InstagramService:
        return InstagrapiService()