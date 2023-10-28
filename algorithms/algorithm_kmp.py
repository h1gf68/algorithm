import typing as tp
from algorithms.search_subtext import SearchSubText


class AlgorithmKnuthMorrisPratt(SearchSubText):
    """Doc AlgKMP"""
    def __init__(self, subtext: str, text: str):
        super().__init__(subtext, text)

    def __str__(self):
        return f"AlgorithmKMP search \"{self.subtext}\""

    def create_array(self) -> tp.Union[tp.List,None]:
        if not self.subtext:
            return None

        arr, j, i = [0], 0, 1
        while True:
            if i == len(self.subtext):
                break

            if self.subtext[i] != self.subtext[j]:
                if j == 0:
                    arr.append(0)
                    i += 1
                else:
                    j = arr[j-1]
            else:
                arr.append(j+1)
                i += 1
                j += 1
        return arr
    
    def search_subtext(self) -> tp.Union[int, None]:
        len_s = len(self.subtext)
        len_t = len(self.text)
        arr = self.create_array()

        if len_s > len_t or not arr:
            return None

        i, j = 0, 0
        while True:
            if self.subtext[j] == self.text[i]:
                i += 1
                j += 1
                if j == len_s:
                    return i-len_s
            else:
                if j > 0:
                    j = arr[j-1]
                else:
                    i += 1
                    if i == len_t:
                        return None

