import time


def millis() -> int:
    return int(round(time.time() * 1000))
