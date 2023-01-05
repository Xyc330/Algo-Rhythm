import base64
import json

def encrypt(key, msg):
    enc = []
    for i in range(len(msg)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(msg[i]) + ord(key_c)) % 256))

    encryption = base64.urlsafe_b64encode("".join(enc).encode()).decode()
    return encryption



def decrypt(msg, key):
    dec = []
    message = base64.urlsafe_b64decode(msg).decode()
    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))

    return "".join(dec)


def set_key(key):
    with open("encryption.json", "r+") as enc_json:
        data = json.load(enc_json)

        data["key"] = key

        enc_json.seek(0)  # rewind
        json.dump(data, enc_json)
        enc_json.truncate()