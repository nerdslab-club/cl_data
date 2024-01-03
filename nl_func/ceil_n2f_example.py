import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_ceil_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##ceil({num})",
        })
    return examples


def __random_explanation(f1: float) -> str:
    explanations = [
        f"The ceiling of {f1}",
        f"CEIL({f1})",
        f"Round up {f1} to the nearest whole number",
        f"The smallest integer greater than or equal to {f1}",
        f"The result of CEIL({f1})",
        f"Find the ceiling of {f1}",
        f"Rounding up {f1}",
        f"{f1}, rounded up to the nearest integer",
        f"The smallest whole number not less than {f1}",
        f"CEIL calculation: {f1}",
        f"The smallest integer greater than or equal to {f1}, what is it?",
        f"The smallest integer greater than or equal to {f1}, what does it give?",
        f"Let's round up {f1} to the nearest whole number",
        f"Find the CEIL for {f1}",
        f"The smallest integer greater than or equal to {f1}, result is",
        f"Rounding {f1} up",
        f"{f1}, what is its ceiling?",
        f"The smallest whole number not less than {f1}, find the answer",
        f"Calculate CEIL({f1})",
        f"Round {f1} up to the nearest integer",
        f"The smallest integer greater than or equal to {f1}, what is its value?",
        f"Rounding up operation for {f1}",
        f"Let's determine the ceiling of {f1}",
        f"{f1}, rounded up, what is the result?",
        f"The smallest whole number not less than {f1}, what is it?",
        f"Find the ceiling of {f1} and provide the result",
        f"CEIL({f1}), what does it yield?",
        f"Rounded up value for {f1}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_ceil_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
