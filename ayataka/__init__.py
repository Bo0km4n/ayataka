from typing import Any
import inspect
import ayataka.environment

def process(prefix: str, obj: Any) -> bool:
    print(isinstance(obj, ayataka.environment.Environment))
    return False