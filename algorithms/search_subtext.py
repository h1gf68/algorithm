from abc import ABC


class SearchSubText(ABC):
    """Doc SearchSubText class"""
    def __init__(self, subtext: str, text: str, **kwargs):
        self.text = text
        self.subtext = subtext

    def search_subtext(self):
        pass

    # def __del__(self):
    #     class_name = self.__class__.__name__
    #     print('{} уничтожен'.format(class_name))
