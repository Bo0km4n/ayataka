import functools
from abc import ABC, abstractmethod
from enum import Enum

class EnvType(Enum):
    REQUIRE = 1
    DEFAULT = 2

class Environment(ABC):
    @abstractmethod
    def env_type(self):
        raise NotImplementedError

class Require:
    def env_type(self):
        return EnvType.REQUIRE

class Default:
    def env_type(self):
        return EnvType.DEFAULT

Environment.register(Require)
Environment.register(Default)