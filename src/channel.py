import json
import os
from googleapiclient.discovery import build

from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv("YT_API_KEY")
youtube = build("youtube", "v3", developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""
    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = youtube.channels().list(id=self.channel_id, part="snippet,statistics").execute()

    # def printj(self, dict_to_print: dict) -> None:
    #     """Выводит словарь в json-подобном удобном формате с отступами"""
    #     print(json.dumps(dict_to_print, ensure_ascii=False, indent=2))

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, ensure_ascii=False, indent=2))
