import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_is_palindrome_example(count: int):
    examples = []
    for _ in range(count):
        word = "".join(
            random.choice("abccbadeffeghihgjklmnonmlkjpqrstuuuvwxwvyvz")
            for _ in range(random.randint(2, 10))
        )
        examples.append(
            {
                "inputStr": f"##is_palindrome('{word}')",
                "outputStr": __random_explanation_is_palindrome(word),
            }
        )
    return examples


def __random_explanation_is_palindrome(word: str) -> str:
    explanations = [
        f"Whether the string '{word}' is a palindrome",
        f"is_palindrome('{word}')",
        f"Whether the word '{word}' reads the same forwards and backwards",
        f"Calculation: is_palindrome('{word}')",
        f"Whether '{word}' is a word that is the same when reversed",
        f"Whether '{word}' is a palindrome or not",
        f"Whether '{word}' is a string that remains unchanged when reversed",
        f"Whether '{word}' is a sequence that equals its reverse",
        f"Whether the string '{word}' forms a palindrome",
        f"Whether '{word}' is a word that is symmetric when reversed",
        f"Whether the word '{word}' forms a palindrome",
        f"Whether the string '{word}' is unchanged when reversed",
        f"Whether '{word}' is a string that reads the same both ways",
        f"Whether '{word}' is a sequence that remains unaltered when reversed",
        f"Whether the word '{word}' is the same forwards and backwards",
        f"Whether '{word}' is a sequence that remains the same when reversed",
        f"Whether '{word}' is a string that is identical in reverse",
        f"Whether the string '{word}' is symmetrical",
        f"Whether '{word}' is a sequence that is mirrored when reversed",
        f"Whether the word '{word}' is a palindrome",
        f"Whether '{word}' is a string that appears the same in reverse",
        f"Whether '{word}' is a sequence that appears identical when reversed",
        f"Whether the string '{word}' is a mirror image of itself",
        f"Whether '{word}' is a sequence that forms a palindrome",
        f"Whether '{word}' is a string that mirrors itself when reversed",
        f"Whether the string '{word}' is a palindromic sequence",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_is_palindrome_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
