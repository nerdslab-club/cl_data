import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_isqrt_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##isqrt({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"The integer square root of {a}",
        f"Find the integer square root of {a}",
        f"Square root rounded down for {a}",
        f"Calculate the integer square root of {a}",
        f"Finding ISQRT for {a}",
        f"The whole number part of the square root of {a}",
        f"ISQRT calculation: {a}",
        f"The greatest integer less than or equal to the square root of {a}",
        f"The ISQRT for {a}",
        f"Let's find the integer square root of {a}",
        f"Find the ISQRT for {a}",
        f"The whole part of the square root when you have {a}",
        f"Whole number square root of {a}",
        f"The integer part of the square root of {a}",
        f"The largest integer less than or equal to the square root of {a}",
        f"Let's determine the ISQRT of {a}",
        f"The greatest integer part of the square root of {a}",
        f"Find the whole number part of the square root of {a}",
        f"The integer square root of numbers {a}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_isqrt_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
