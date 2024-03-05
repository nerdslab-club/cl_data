import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_check_same_string_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        strings = [
            "".join(
                random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))
            )
            for _ in range(2)
        ]
        examples.append(
            {
                "inputStr": f"##check_same_string('{strings[0]}', '{strings[1]}')",
                "outputStr": __random_explanation_check_same_string(
                    strings[0], strings[1], (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_check_same_string(str1, str2, identifier: int | None) -> str:
    explanations = [
        f"Checking if the strings {str1} and {str2} are the same",
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
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_check_same_string_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
