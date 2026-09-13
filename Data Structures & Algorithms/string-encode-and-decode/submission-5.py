class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            word_len = int(s[i:j])
            word = s[j + 1:j + word_len + 1]
            words.append(word)
            i = word_len + j + 1

        return words
