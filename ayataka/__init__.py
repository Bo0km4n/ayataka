from typing import Any, Tuple
import inspect
import ayataka.environment

def process(prefix: str, obj: Any) -> Tuple[Any, bool]:
    if not isinstance(obj, ayataka.environment.Environment):
        return None, False
    return None, True