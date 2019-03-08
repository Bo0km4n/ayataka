import os
import sys

path = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(path)

from ayataka import process

class Env:
    def __init__(self):
        self.aws_access_key = "hoge"
        self.aws_secret_access_key = "print"
        return 

if __name__ == '__main__':
    e = Env()
    process(prefix="ENV",obj=e)