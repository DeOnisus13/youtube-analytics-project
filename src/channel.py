import json
import os
from googleapiclient.discovery import build

from dotenv import load_dotenv


load_dotenv()


class Channel:
    """Класс для ютуб-канала"""
    api_key = os.getenv("YT_API_KEY")
    youtube = build("youtube", "v3", developerKey=api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        # self.channel_id = channel_id
        self.__channel_id = channel_id
        self.channel = self.youtube.channels().list(id=self.channel_id, part="snippet,statistics").execute()

        self.id = self.channel["items"][0]["id"]
        self.title = self.channel["items"][0]["snippet"]["title"]
        self.description = self.channel["items"][0]["snippet"]["description"]
        self.url = f"https://www.youtube.com/channel/{self.channel_id}"
        self.subscribers = self.channel["items"][0]["statistics"]["subscriberCount"]
        self.video_count = self.channel["items"][0]["statistics"]["videoCount"]
        self.views = self.channel["items"][0]["statistics"]["viewCount"]

    @property
    def channel_id(self):
        return self.__channel_id

    @channel_id.setter
    def channel_id(self, channel_id):
        self.__channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, ensure_ascii=False, indent=2))

    @classmethod
    def get_service(cls):
        """Класс-метод, возвращающий объект для работы с YouTube API"""
        return cls.youtube

    def to_json(self, filename: str) -> None:
        """Метод для записи информации в json файл"""
        channel_info = {
            "title": self.title,
            "channel_id": self.channel_id,
            "description": self.description,
            "url": self.url,
            "count_subscriberCount": self.subscribers,
            "video_count": self.video_count,
            "count_views": self.views,
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(channel_info, file, ensure_ascii=False, indent=4)
