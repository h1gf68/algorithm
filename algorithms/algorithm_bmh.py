import typing as tp
from algorithms.search_subtext import SearchSubText


class AlgorithmBoyerBoyerMooreHorspool(SearchSubText):
    def __init__(self, subtext: str, text: str, **kwargs):
        super().__init__(subtext, text, **kwargs)

    def create_dict(self) -> tp.Union[dict, None]:
        if not self.subtext:
            return None

        offset_table = {}
        for i, sym in enumerate(self.subtext[-2::-1], 1):
            if sym not in offset_table:
                offset_table[sym] = i
        if self.subtext[-1] not in offset_table:
            offset_table[self.subtext[-1]] = len(self.subtext)

        offset_table['all'] = len(self.subtext)

        return offset_table

    def search_subtext(self):
        pass