import os
import sys

path = os.path.join(os.path.dirname(__file__), "../")
sys.path.append(path)

from ayataka import process
from ayataka import environment
from ayataka.environment import Require

class Env(Require):
    def __init__(self):
        self.aws_access_key = "hoge"
        self.aws_secret_access_key = "print"
        self.__name = 0
        return 
    
    def aws_access_key(self):
        return self.aws_access_key
    
    def monk(self):
        return 0

if __name__ == '__main__':
    e = Env()
    e, ok = process(prefix="ENV",obj=e)
    print(e, ok)