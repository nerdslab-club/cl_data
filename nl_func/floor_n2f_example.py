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


def __random_explanation(f1: float) -> str:
    explanations = [
        f"The floor of {f1}",
        f"FLOOR({f1})",
        f"Round down {f1} to the nearest whole number",
        f"The largest integer less than or equal to {f1}",
        f"The result of FLOOR({f1})",
        f"Find the floor of {f1}",
        f"Rounding down {f1}",
        f"{f1}, rounded down to the nearest integer",
        f"The largest whole number not greater than {f1}",
        f"FLOOR calculation: {f1}",
        f"The largest integer less than or equal to {f1}, what is it?",
        f"The largest integer less than or equal to {f1}, what does it give?",
        f"Let's round down {f1} to the nearest whole number",
        f"Find the FLOOR for {f1}",
        f"The largest integer less than or equal to {f1}, result is",
        f"Rounding {f1} down",
        f"{f1}, what is its floor?",
        f"The largest whole number not greater than {f1}, find the answer",
        f"Calculate FLOOR({f1})",
        f"Round {f1} down to the nearest integer",
        f"The largest integer less than or equal to {f1}, what is its value?",
        f"Rounding down operation for {f1}",
        f"Let's determine the floor of {f1}",
        f"{f1}, rounded down, what is the result?",
        f"The largest whole number not greater than {f1}, what is it?",
        f"Find the floor of {f1} and provide the result",
        f"FLOOR({f1}), what does it yield?",
        f"Rounded down value for {f1}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_floor_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
