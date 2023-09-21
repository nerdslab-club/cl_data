import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_reverse_string_example(count: int):
    examples = []
    for _ in range(count):
        input_strings = [
            "".join(
                random.choices("abcdefghijklmnopqrstuvwxyz", k=random.randint(1, 10))
            )
            for _ in range(1)
        ]
        reversed_strings = [s[::-1] for s in input_strings]
        examples.append(
            {
                "inputStr": f"##reverse_string('{input_strings[0]}')",
                "outputStr": __random_explanation_reverse_string(
                    input_strings[0], reversed_strings[0]
                ),
            }
        )
    return examples


def __random_explanation_reverse_string(input_str, reversed_str) -> str:
    explanations = [
        f"Reversing the string '{input_str}'",
        f"reverse_string('{input_str}')",
        f"The result of reversing the string '{input_str}'",
        f"Calculation: reverse_string('{input_str}')",
        f"The reversed form of the string '{input_str}'",
        f"The outcome of reversing the string '{input_str}'",
        f"The string '{input_str}' in reverse order",
        f"The result of determining the reverse of the string '{input_str}'",
        f"The computed result of reversing the string '{input_str}'",
        f"The reverse of the given string '{input_str}'",
        f"The outcome of evaluating reverse_string('{input_str}')",
        f"The value obtained by reversing the string '{input_str}'",
        f"The result of evaluating reverse_string('{input_str}')",
        f"The string '{input_str}' reversed",
        f"The computed reversed string of '{input_str}'",
        f"The string '{input_str}' in reverse",
        f"The calculated result of determining the reverse of the string '{input_str}'",
        f"The reversed version of the string '{input_str}'",
        f"The outcome of evaluating reverse_string('{input_str}')",
        f"The computed reversed form of the string '{input_str}'",
        f"The calculated outcome of reversing the string '{input_str}'",
        f"The computed reverse of the string '{input_str}'",
        f"The calculated reverse of the string '{input_str}'",
        f"The outcome of finding the reverse of the string '{input_str}'",
        f"The calculated reverse version of the string '{input_str}'",
        f"The calculated reversed string of '{input_str}'",
        f"The outcome of evaluating reverse_string('{input_str}')",
        f"The outcome of calculating the reverse of the string '{input_str}'",
    ]
    if input_str == reversed_str:
        explanations.extend(
            [
                f"The string '{input_str}' is already a palindrome",
                f"The given string '{input_str}' is already the same when reversed",
                f"The string '{input_str}' remains the same when reversed",
                f"The string '{input_str}' is unchanged when reversed",
                f"The string '{input_str}' is a palindrome",
                f"The given string '{input_str}' is a palindrome",
                f"The string '{input_str}' is already symmetric",
            ]
        )
    else:
        explanations.extend(
            [
                f"The reversed string of '{input_str}' is '{reversed_str}'",
                f"The string '{input_str}' becomes '{reversed_str}' when reversed",
                f"The reverse of the string '{input_str}' is '{reversed_str}'",
                f"The string '{input_str}' changes to '{reversed_str}' when reversed",
                f"The reversed form of the string '{input_str}' is '{reversed_str}'",
                f"The string '{input_str}' transforms into '{reversed_str}' when reversed",
                f"The reversed version of the string '{input_str}' is '{reversed_str}'",
                f"The string '{input_str}' turns into '{reversed_str}' when reversed",
                f"The reversed string of '{input_str}' becomes '{reversed_str}'",
                f"The string '{input_str}' is transformed into '{reversed_str}' when reversed",
            ]
        )
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_reverse_string_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
