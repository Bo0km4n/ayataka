from typing import Any

def process(prefix: str, obj: Any) -> bool:
    instances_keys = obj.__dict__.keys()
    print(instances_keys)
    for key in instances_keys:
        print(key.upper())
    return False