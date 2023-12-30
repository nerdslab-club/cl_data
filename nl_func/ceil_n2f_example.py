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


def __random_explanation(x: float) -> str:
    explanations = [
        f"The ceiling of {x}",
        f"CEIL({x})",
        f"Round up {x} to the nearest whole number",
        f"The smallest integer greater than or equal to {x}",
        f"The result of CEIL({x})",
        f"Find the ceiling of {x}",
        f"Rounding up {x}",
        f"{x}, rounded up to the nearest integer",
        f"The smallest whole number not less than {x}",
        f"CEIL calculation: {x}",
        f"The smallest integer greater than or equal to {x}, what is it?",
        f"The smallest integer greater than or equal to {x}, what does it give?",
        f"Let's round up {x} to the nearest whole number",
        f"Find the CEIL for {x}",
        f"The smallest integer greater than or equal to {x}, result is",
        f"Rounding {x} up",
        f"{x}, what is its ceiling?",
        f"The smallest whole number not less than {x}, find the answer",
        f"Calculate CEIL({x})",
        f"Round {x} up to the nearest integer",
        f"The smallest integer greater than or equal to {x}, what is its value?",
        f"Rounding up operation for {x}",
        f"Let's determine the ceiling of {x}",
        f"{x}, rounded up, what is the result?",
        f"The smallest whole number not less than {x}, what is it?",
        f"Find the ceiling of {x} and provide the result",
        f"CEIL({x}), what does it yield?",
        f"Rounded up value for {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_ceil_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
