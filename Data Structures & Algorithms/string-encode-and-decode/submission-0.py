class Solution:
    DELIMITER = "§"
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for str in strs:
            encoded_str += str + self.DELIMITER
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        temp = ""
        for i in range(len(s)):
            if s[i] != self.DELIMITER:
                temp = temp + s[i]
            else:
                decoded_strs.append(temp)
                temp = ""
        return decoded_strs