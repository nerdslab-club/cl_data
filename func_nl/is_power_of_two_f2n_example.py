import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_is_power_of_two_example(count: int):
    examples = []
    for _ in range(count):
        x = 2 ** random.randint(0, 10)
        examples.append(
            {
                "inputStr": f"##is_power_of_two({x})",
                "outputStr": __random_explanation_is_power_of_two(x),
            }
        )
    return examples


def __random_explanation_is_power_of_two(x: int) -> str:
    explanations = [
        f"Whether the number {x} is a power of two",
        f"is_power_of_two({x})",
        f"Whether {x} can be expressed as 2 raised to some positive integer",
        f"Calculation: is_power_of_two({x})",
        f"Whether {x} is a number that has only one '1' bit in its binary representation",
        f"Whether {x} is a power of 2",
        f"Whether {x} is a value that can be written as 2 to the power of some non-negative integer",
        f"Whether {x} is of the form 2^k for some non-negative integer k",
        f"Whether {x} can be written in the form of 2 raised to a non-negative integer power",
        f"Whether the integer {x} can be represented as 2 to the power of some non-negative exponent",
        f"Whether {x} is a power of two or not",
        f"Whether {x} can be expressed as 2^k where k is a non-negative integer",
        f"Whether {x} is a value that can be written as 2 raised to a non-negative exponent",
        f"Whether {x} is a power of two (2^k)",
        f"Whether {x} is a value that can be represented as 2 to the power of a non-negative integer",
        f"Whether {x} is a power of 2 (2^k) or not",
        f"Whether {x} can be expressed in the form of 2 raised to a non-negative integer power",
        f"Whether the binary representation of {x} has only one '1' bit",
        f"Whether {x} is a power of 2 or not (2^k)",
        f"Whether {x} is of the form 2^k where k is a non-negative integer",
        f"Whether {x} is a value that can be represented as 2 raised to the power of a non-negative integer",
        f"Whether the integer {x} can be expressed in the form of 2 to the power of some non-negative exponent",
        f"Whether {x} is a power of two (2^k) or not",
        f"Whether {x} can be written in the form of 2^k where k is a non-negative integer",
        f"Whether the binary representation of {x} has only one '1' bit in it",
        f"Whether {x} is a power of two or not (2^k)",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_is_power_of_two_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
