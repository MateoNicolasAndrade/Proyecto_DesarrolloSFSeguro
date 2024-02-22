import os

def get_key():
    key1 = ""
    with open(".env") as f:
        for line in f:
            key, value = line.strip().split('=')
            os.environ[key] = value
            key1 = str(value)
    return key1
