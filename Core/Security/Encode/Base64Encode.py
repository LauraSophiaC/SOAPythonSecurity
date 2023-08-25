#BASE 64 ENCODE
import base64

class base64Encode:
    def encode(self, data):
        encoded_bytes = base64.b64encode(data.encode('utf-8'))
        encoded_str = encoded_bytes.decode('utf-8')
        return encoded_str


    