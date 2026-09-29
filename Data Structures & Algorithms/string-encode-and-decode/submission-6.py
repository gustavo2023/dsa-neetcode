class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        words = []
        i = 0

        while i < len(s):
            separator = s.find("#", i)
            word_len = int(s[i:separator])
            words.append(s[separator + 1:separator + 1 + word_len])
            i = separator + 1 + word_len

        return words