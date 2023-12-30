import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_is_palindrome_example(count: int):
    examples = []
    for _ in range(count):
        word = RandomValueGenerator.generate_random_string()
        examples.append({
            "inputStr": __random_explanation(word),
            "outputStr": f"##is_palindrome('{word}')",
        })
    return examples


def __random_explanation(word: str) -> str:
    explanations = [
        f"Determine if the string '{word}' is a palindrome",
        f"IS_PALINDROME('{word}')",
        f"Check if '{word}' is a palindrome",
        f"Is '{word}' a palindrome?",
        f"Verify whether '{word}' is a palindrome",
        f"Checking if '{word}' is a palindrome",
        f"IS_PALINDROME calculation: '{word}'",
        f"Is '{word}' a palindrome?",
        f"Check if '{word}' is a palindrome string",
        f"Let's determine if '{word}' is a palindrome",
        f"Is '{word}' a palindrome or not?",
        f"Determine if '{word}' is a palindrome",
        f"Checking the palindrome property of '{word}'",
        f"Is '{word}' a palindrome?",
        f"Check if '{word}' is a palindrome, result is",
        f"Determine whether '{word}' is a palindrome",
        f"Verify if '{word}' is a palindrome",
        f"Check if '{word}' is a palindrome string",
        f"IS_PALINDROME('{word}'), what does it yield?",
        f"Checking if '{word}' is a palindrome without spaces",
        f"Is '{word}' a palindrome or not?",
        f"Determine if '{word}' is a palindrome, result is",
        f"Check if '{word}' is a palindrome or not, result is",
        f"Let's find out if '{word}' is a palindrome",
        f"Is '{word}' a palindrome without spaces?",
        f"Check if '{word}' is a palindrome string or not",
        f"Verify the palindrome property of '{word}'",
        f"IS_PALINDROME('{word}'), is it true or false?",
        f"Determine if '{word}' is a palindrome without spaces",
        f"Is '{word}' a palindrome or not, what is the answer?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_is_palindrome_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
