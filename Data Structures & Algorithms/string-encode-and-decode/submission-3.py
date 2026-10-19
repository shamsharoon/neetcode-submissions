class Solution:
    
    def encode(self, strs: List[str]) -> str:
        encoded_list = []
        for st in strs:
            encoded_str = ""
            for c in st:
                encoded_str += chr(ord(c) + 1)
            encoded_list.append(encoded_str)
        return encoded_list


    def decode(self, s: str) -> List[str]:
        decoded_list = []
        for st in s:
            decoded_str = ""
            for c in st:
                decoded_str += chr(ord(c) - 1)
            decoded_list.append(decoded_str)
        return decoded_list
