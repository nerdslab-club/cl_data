import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_ceil_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float()
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##ceil({num})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"The ceiling of {f1}",
        f"Round up {f1} to the nearest whole number",
        f"The smallest integer greater than or equal to {f1}",
        f"Find the ceiling of {f1}",
        f"{f1}, rounded up to the nearest integer",
        f"ceil calculation: {f1}",
        f"The smallest integer greater than or equal to {f1}, what is it",
        f"Find the ceil for {f1}",
        f"Rounding {f1} up",
        f"{f1}, what is its ceiling",
        f"The smallest whole number not less than {f1}, find the answer",
        f"The smallest integer greater than or equal to {f1}, what is its value",
        f"Rounding up operation for {f1}",
        f"Let's determine the ceiling of {f1}",
        f"The smallest whole number not less than {f1}, what is it",
        f"Find the ceiling of {f1} and provide the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_ceil_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
