import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_check_same_string_example(count: int):
    examples = []
    for _ in range(count):
        strings = ["".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))) for _ in range(2)]
        are_same = strings[0] == strings[1]
        examples.append(
            {
                "inputStr": f"##check_same_string('{strings[0]}', '{strings[1]}')",
                "outputStr": __random_explanation_check_same_string(strings[0], strings[1], are_same),
            }
        )
    return examples


def __random_explanation_check_same_string(str1, str2, are_same) -> str:
    explanations = [
        f"Checking if the strings '{str1}' and '{str2}' are the same",
        f"check_same_string('{str1}', '{str2}')",
        f"Determining if the strings '{str1}' and '{str2}' are equal",
        f"Calculation: check_same_string('{str1}', '{str2}')",
        f"Comparing the equality of the strings '{str1}' and '{str2}'",
        f"Checking whether the strings '{str1}' and '{str2}' are identical",
        f"Checking if the strings '{str1}' and '{str2}' have the same content",
        f"Determining whether the strings '{str1}' and '{str2}' are equal",
        f"The result of evaluating if the strings '{str1}' and '{str2}' are the same",
        f"Checking if the strings '{str1}' and '{str2}' match",
        f"The outcome of evaluating check_same_string('{str1}', '{str2}')",
        f"Checking if the strings '{str1}' and '{str2}' are identical",
        f"Checking whether the strings '{str1}' and '{str2}' are the same",
        f"Determining if the strings '{str1}' and '{str2}' have the same value",
        f"The result of determining if the strings '{str1}' and '{str2}' are the same",
        f"The outcome of checking if the strings '{str1}' and '{str2}' are equal",
        f"Verifying whether the strings '{str1}' and '{str2}' are the same",
        f"Checking if the strings '{str1}' and '{str2}' are equal",
        f"The result of comparing the strings '{str1}' and '{str2}' for equality",
        f"The outcome of evaluating check_same_string('{str1}', '{str2}')",
        f"Determining if the strings '{str1}' and '{str2}' are equal",
        f"Checking whether the strings '{str1}' and '{str2}' are the same",
        f"Verifying if the strings '{str1}' and '{str2}' are identical",
        f"The result obtained by evaluating check_same_string('{str1}', '{str2}')",
        f"The result of checking if the strings '{str1}' and '{str2}' are the same",
    ]
    if are_same:
        explanations.extend([
            f"The strings '{str1}' and '{str2}' are the same",
            f"The given strings '{str1}' and '{str2}' are identical",
            f"The strings '{str1}' and '{str2}' have the same content",
            f"The strings '{str1}' and '{str2}' match",
            f"The strings '{str1}' and '{str2}' are equal",
            f"The strings '{str1}' and '{str2}' are identical",
            f"The strings '{str1}' and '{str2}' have the same value",
            f"The strings '{str1}' and '{str2}' are equal",
            f"The given strings '{str1}' and '{str2}' are the same",
            f"The given strings '{str1}' and '{str2}' are equal",
            f"The strings '{str1}' and '{str2}' match",
        ])
    else:
        explanations.extend([
            f"The strings '{str1}' and '{str2}' are not the same",
            f"The given strings '{str1}' and '{str2}' are different",
            f"The strings '{str1}' and '{str2}' have different content",
            f"The strings '{str1}' and '{str2}' do not match",
            f"The strings '{str1}' and '{str2}' are not equal",
            f"The strings '{str1}' and '{str2}' are not the same",
            f"The strings '{str1}' and '{str2}' have different values",
            f"The strings '{str1}' and '{str2}' are different",
            f"The given strings '{str1}' and '{str2}' are not equal",
            f"The given strings '{str1}' and '{str2}' are different",
            f"The strings '{str1}' and '{str2}' do not match",
        ])
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_check_same_string_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
