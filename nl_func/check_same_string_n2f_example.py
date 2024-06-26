import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_check_same_string_example(count: int):
    examples = []
    for _ in range(count):
        str1 = RandomValueGenerator.generate_random_string()
        str2 = RandomValueGenerator.generate_random_string()
        examples.append({
            "inputStr": __random_explanation(str1, str2),
            "outputStr": f"##check_same_string('{str1}', '{str2}')",
        })
    return examples


def __random_explanation(str1: str, str2: str) -> str:
    explanations = [
        f"Check if the strings '{str1}' and '{str2}' are the same",
        f"CHECK_SAME_STRING('{str1}', '{str2}')",
        f"Determine if '{str1}' is the same as '{str2}'",
        f"Verify if the strings '{str1}' and '{str2}' are identical",
        f"Check if '{str1}' is equal to '{str2}'",
        f"The result of checking if '{str1}' and '{str2}' are the same",
        f"Performing the check_same_string operation for '{str1}' and '{str2}'",
        f"Are '{str1}' and '{str2}' the same?",
        f"CHECK_SAME_STRING operation: '{str1}', '{str2}'",
        f"The result after checking if '{str1}' and '{str2}' are the same, what is it?",
        f"Do '{str1}' and '{str2}' represent the same string?",
        f"Let's check if '{str1}' and '{str2}' are the same",
        f"The check_same_string result for '{str1}' and '{str2}', is it true?",
        f"Checking if '{str1}' is the same as '{str2}'",
        f"The check_same_string result after checking if '{str1}' is the same as '{str2}'",
        f"The result after checking if '{str1}' and '{str2}' are the same, what is its value?",
        f"Let's determine if '{str1}' is the same as '{str2}'",
        f"The check_same_string result for '{str1}' and '{str2}'",
        f"The check_same_string result for '{str1}' and '{str2}', what is the result?",
        f"Do '{str1}' and '{str2}' correspond to the same string?",
        f"The result after checking if '{str1}' and '{str2}' are the same and provide the result",
        f"CHECK_SAME_STRING('{str1}', '{str2}'), what does it yield?",
        f"Checking if '{str1}' and '{str2}' are the same, ignoring case",
        f"The result after checking if '{str1}' and '{str2}' are the same",
        f"Check if '{str1}' and '{str2}' are the same, find the answer",
        f"Checking if '{str1}' and '{str2}' represent the same string, what does it give?",
        f"Let's find the result after checking if '{str1}' and '{str2}' are the same",
        f"The check_same_string result for '{str1}' and '{str2}', what is the output?",
        f"The result after checking if '{str1}' and '{str2}' are the same, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_check_same_string_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
