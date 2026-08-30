class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
           separator = s.find("#", i)
           length = int(s[i:separator])
           strs.append(s[separator + 1:separator + length + 1])
           i = separator + length + 1

        return strs