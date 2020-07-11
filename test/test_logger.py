import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from logger import Logger


def test_logging(msg):
    l = Logger()
    lt = Logger("test.txt")
    l.logging(msg)
    lt.logging(msg)


if __name__ == "__main__":
    test_logging("test")
