import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_floor_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##floor({num})",
        })
    return examples


def __random_explanation(x: float) -> str:
    explanations = [
        f"The floor of {x}",
        f"FLOOR({x})",
        f"Round down {x} to the nearest whole number",
        f"The largest integer less than or equal to {x}",
        f"The result of FLOOR({x})",
        f"Find the floor of {x}",
        f"Rounding down {x}",
        f"{x}, rounded down to the nearest integer",
        f"The largest whole number not greater than {x}",
        f"FLOOR calculation: {x}",
        f"The largest integer less than or equal to {x}, what is it?",
        f"The largest integer less than or equal to {x}, what does it give?",
        f"Let's round down {x} to the nearest whole number",
        f"Find the FLOOR for {x}",
        f"The largest integer less than or equal to {x}, result is",
        f"Rounding {x} down",
        f"{x}, what is its floor?",
        f"The largest whole number not greater than {x}, find the answer",
        f"Calculate FLOOR({x})",
        f"Round {x} down to the nearest integer",
        f"The largest integer less than or equal to {x}, what is its value?",
        f"Rounding down operation for {x}",
        f"Let's determine the floor of {x}",
        f"{x}, rounded down, what is the result?",
        f"The largest whole number not greater than {x}, what is it?",
        f"Find the floor of {x} and provide the result",
        f"FLOOR({x}), what does it yield?",
        f"Rounded down value for {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_floor_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
