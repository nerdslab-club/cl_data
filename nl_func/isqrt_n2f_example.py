import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_isqrt_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer(0, 1000000)
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##isqrt({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"The integer square root of {a}",
        f"ISQRT({a})",
        f"Find the integer square root of {a}",
        f"The result of ISQRT({a})",
        f"Square root rounded down for {a}",
        f"Calculate the integer square root of {a}",
        f"Finding ISQRT for {a}",
        f"Square root of {a} (integer part)",
        f"The whole number part of the square root of {a}",
        f"ISQRT calculation: {a}",
        f"The greatest integer less than or equal to the square root of {a}",
        f"ISQRT({a}), what does it give?",
        f"The ISQRT for {a}",
        f"Let's find the integer square root of {a}",
        f"Find the ISQRT for {a}",
        f"The whole part of the square root when you have {a}",
        f"ISQRT({a}), result is",
        f"Whole number square root of {a}",
        f"The integer part of the square root of {a}",
        f"The greatest whole number that is less than or equal to the square root of {a}",
        f"ISQRT of {a}, find the answer",
        f"Calculate ISQRT({a})",
        f"The largest integer less than or equal to the square root of {a}",
        f"Let's determine the ISQRT of {a}",
        f"The greatest integer part of the square root of {a}",
        f"ISQRT({a}), what is its value?",
        f"Find the whole number part of the square root of {a}",
        f"The integer square root of numbers {a}",
        f"ISQRT: {a}",
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
