import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_gcd_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_integer(1, 1000)
        num2 = RandomValueGenerator.generate_random_integer(1, 1000)
        examples.append({
            "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            "outputStr": f"##gcd({num1}, {num2})",
        })
    return examples


def __random_explanation(f1: int, f2: int, identifier: int | None) -> str:
    explanations = [
        f"The greatest common divisor of {f1} and {f2}",
        f"GCD of {f1} and {f2}",
        f"Find the greatest common divisor of {f1} and {f2}",
        f"The result of finding GCD({f1}, {f2})",
        f"GCD for {f1} and {f2}",
        f"Calculate the greatest common divisor of {f1} and {f2}",
        f"Finding GCD for {f1} and {f2}",
        f"{f1} and {f2}, what is their greatest common divisor?",
        f"GCD calculation: {f1} and {f2}",
        f"The common factor of {f1} and {f2}",
        f"The largest number that divides both {f1} and {f2}",
        f"GCD({f1}, {f2}), what does it give?",
        f"The GCD for {f1} and {f2}",
        f"Let's find the greatest common divisor of {f1} and {f2}",
        f"Find the GCD for {f1} and {f2}",
        f"{f1} and {f2}, their GCD?",
        f"The greatest common divisor when you have {f1} and {f2}",
        f"GCD({f1}, {f2}), result is",
        f"Common divisor of {f1} and {f2}",
        f"The divisor common to {f1} and {f2}",
        f"GCD of {f1} and {f2}, find the answer",
        f"Calculate GCD({f1}, {f2})",
        f"The common factor for {f1} and {f2}",
        f"Let's determine the GCD of {f1} and {f2}",
        f"{f1} and {f2}, what is their common divisor?",
        f"GCD calculation for {f1} and {f2}",
        f"The greatest common divisor of numbers {f1} and {f2}",
        f"GCD: {f1} and {f2}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_gcd_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
