from typing import Dict, List, Tuple

from django.conf import settings


class HXMessageTags:
    DEBUG = 10
    INFO = 20
    SUCCESS = 25
    WARNING = 30
    ERROR = 40


class HXMessages:
    messages: List[Tuple[str, str]]
    tags: Dict[int, str]
    # TODO USE json script tag (and use include template for this) and would also need context processr

    def __init__(self) -> None:
        self.messages = []
        self.settings_dict = getattr(settings, "HX_REQUESTS_HX_MESSAGES", {})
        self.set_tags()

    def debug(self, message):
        self.messages.append((message, self.tags.get(10)))

    def info(self, message):
        self.messages.append((message, self.tags.get(20)))

    def success(self, message):
        self.messages.append((message, self.tags.get(25)))

    def warning(self, message):
        self.messages.append((message, self.tags.get(30)))

    def error(self, message):
        self.messages.append((message, self.tags.get(40)))

    def set_tags(self):
        if self.settings_dict.get("USE_DJANGO_MESSAGE_TAGS"):
            self.tags = getattr(settings, "MESSAGE_TAGS")
        else:
            self.tags = self.settings_dict.get("HX_MESSAGE_TAGS")

        if not self.tags:
            raise Exception(
                "HX_MESSAGE_TAGS must be defined in settings to use messages with hx-requests, or set USE_DJANGO_MESSAGE_TAGS to 'True'."
            )

    def get_message(self):
        if self.messages:
            return self.messages[-1]