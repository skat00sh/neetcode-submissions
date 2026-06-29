class Solution:
    DELIMITER = "§"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += str + self.DELIMITER
        return encoded_str

    def decode(self, s: str) -> List[str]:
        return s.split(self.DELIMITER)[:-1]