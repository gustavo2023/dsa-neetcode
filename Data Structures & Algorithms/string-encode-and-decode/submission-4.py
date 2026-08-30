class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            delimiter = s.find("#", i)
            length = int(s[i:delimiter])
            word = s[delimiter + 1:delimiter + length + 1]
            strs.append(word)
            i = delimiter + 1 + length

        return strs


