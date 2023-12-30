import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_isqrt_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(0, 1000000)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##isqrt({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"The integer square root of {x}",
        f"ISQRT({x})",
        f"Find the integer square root of {x}",
        f"The result of ISQRT({x})",
        f"Square root rounded down for {x}",
        f"Calculate the integer square root of {x}",
        f"Finding ISQRT for {x}",
        f"Square root of {x} (integer part)",
        f"The whole number part of the square root of {x}",
        f"ISQRT calculation: {x}",
        f"The greatest integer less than or equal to the square root of {x}",
        f"ISQRT({x}), what does it give?",
        f"The ISQRT for {x}",
        f"Let's find the integer square root of {x}",
        f"Find the ISQRT for {x}",
        f"The whole part of the square root when you have {x}",
        f"ISQRT({x}), result is",
        f"Whole number square root of {x}",
        f"The integer part of the square root of {x}",
        f"The greatest whole number that is less than or equal to the square root of {x}",
        f"ISQRT of {x}, find the answer",
        f"Calculate ISQRT({x})",
        f"The largest integer less than or equal to the square root of {x}",
        f"Let's determine the ISQRT of {x}",
        f"The greatest integer part of the square root of {x}",
        f"ISQRT({x}), what is its value?",
        f"Find the whole number part of the square root of {x}",
        f"The integer square root of numbers {x}",
        f"ISQRT: {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_isqrt_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
