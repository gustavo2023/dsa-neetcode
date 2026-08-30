class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_str = []

        while i < len(s):
           separator = s.find("#", i)
           word_len = int(s[i:separator])
           decoded_str.append(s[separator + 1:separator + 1 + word_len])

           i = word_len + separator + 1

        return decoded_str 