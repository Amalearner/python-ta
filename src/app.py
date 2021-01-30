import sys
import os


def palindrome(s):
    # your code goes here

    is_palindrome = False
    word = s.lower()
    for i in range(len(word)):
        if word[i] == word[-1 -i]:
            is_palindrome = True
        else:
            is_palindrome = False
            break
    if is_palindrome:
        return s + " is a palindrome"
    return  s + " is not a palindrome"

def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
