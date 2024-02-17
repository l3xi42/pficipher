#!/usr/bin/env python3


def duplicate(plaintext: str) -> str:
    """
    Duplicate chars in 'plaintext':
    duplicate('hello') -> 'hheelloo'
    """
    string = "" 
    for i in str:
        string += i*2
    return string


def intersection(a: str, b: str) -> str:
    """
    Return intersectioned string
    intersection('zirafa', 'karafa') -> 'rafa'
    """
    # TODO
    pass


def caesar(plaintext: str, move: int) -> str:
    """
    Move 'plaintext' by 'move' characters. 'move' could be negative
    caesar('hello', 1) -> 'ifmmp'
    """
    # TODO
    pass


def main() -> None:
    str = input()
    print(duplicate(str))
    pass


if __name__ == '__main__':
    main()
