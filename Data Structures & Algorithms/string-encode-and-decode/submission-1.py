class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0

        while i < len(s):
            j = s.find("#", i)
            l = int(s[i:j])
            strs.append(s[j + 1:j + 1 + l])
            i = j + 1 + l

        return strs
