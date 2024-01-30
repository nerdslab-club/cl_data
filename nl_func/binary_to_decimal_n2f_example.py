import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_binary_to_decimal_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        binary_string = RandomValueGenerator.generate_random_binary_string()
        examples.append({
            "inputStr": __random_explanation(binary_string, (None if identifier is None else identifier+i)),
            "outputStr": f"##binary_to_decimal('{binary_string}')",
        })
    return examples


def __random_explanation(binary_string: str, identifier: int | None) -> str:
    explanations = [
        f"Convert the binary string '{binary_string}' to decimal",
        f"Translate the binary representation '{binary_string}' to decimal",
        f"Convert the binary string '{binary_string}' to its decimal equivalent",
        f"The decimal value corresponding to the binary string '{binary_string}'",
        f"Converting the binary string '{binary_string}' to decimal",
        f"The result after converting the binary string '{binary_string}' to decimal, what is it",
        f"The decimal value of the binary string '{binary_string}', what does it give",
        f"Let's convert the binary string '{binary_string}' to decimal",
        f"The decimal value of the binary string '{binary_string}', result is",
        f"Translating the binary representation '{binary_string}' to decimal",
        f"The decimal result after converting the binary string '{binary_string}'",
        f"The decimal value of the binary string '{binary_string}', what is its value",
        f"Let's determine the decimal value of the binary string '{binary_string}'",
        f"The decimal value of the binary string '{binary_string}', what is the result",
        f"The result after converting the binary string '{binary_string}' to decimal",
        f"The decimal value of the binary string '{binary_string}', what is it",
        f"Calculate the decimal value of the binary string '{binary_string}', find the answer",
        f"The decimal value of the binary string '{binary_string}', what does it give",
        f"Let's find the result after converting the binary string '{binary_string}' to decimal",
        f"The decimal value of the binary string '{binary_string}', what is the output",
        f"The result after converting the binary string '{binary_string}' to decimal, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_binary_to_decimal_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
