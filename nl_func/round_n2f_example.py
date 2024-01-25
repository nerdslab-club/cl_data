import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_round_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##round({num})",
        })
    return examples


def __random_explanation(x: float, identifier: int | None) -> str:
    explanations = [
        f"The rounded value of {x}",
        f"ROUND({x})",
        f"Round {x} to the nearest whole number",
        f"The result of ROUND({x})",
        f"Find the rounded value of {x}",
        f"Rounding {x}",
        f"{x}, rounded to the nearest integer",
        f"The closest whole number to {x}",
        f"ROUND calculation: {x}",
        f"The closest whole number to {x}, what is it?",
        f"The closest whole number to {x}, what does it give?",
        f"Let's round {x} to the nearest whole number",
        f"Find the ROUND for {x}",
        f"The closest whole number to {x}, result is",
        f"Rounding {x} to the nearest integer",
        f"{x}, what is its rounded value?",
        f"The closest whole number to {x}, find the answer",
        f"Calculate ROUND({x})",
        f"Round {x} to the nearest integer",
        f"The closest whole number to {x}, what is its value?",
        f"Rounding operation for {x}",
        f"Let's determine the rounded value of {x}",
        f"{x}, rounded, what is the result?",
        f"The closest whole number to {x}, what is it?",
        f"Find the rounded value of {x} and provide the result",
        f"ROUND({x}), what does it yield?",
        f"Rounded value for {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_round_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
