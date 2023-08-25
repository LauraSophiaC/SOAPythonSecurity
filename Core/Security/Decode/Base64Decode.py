#BASE 64 DECODE
import base64

class base64Decode:
    def decode(self, encoded_str):
        decoded_bytes = base64.b64decode(encoded_str.encode('utf-8'))
        decoded_str = decoded_bytes.decode('utf-8')
        return decoded_str