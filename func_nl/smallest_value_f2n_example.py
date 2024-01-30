import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_smallest_value_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float()
        y = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": f"##smallest_value({x}, {y})",
                "outputStr": __random_explanation_smallest_value(x, y, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_smallest_value(f: float, g: float, identifier: int | None) -> str:
    explanations = [
        f"The smaller of {f} and {g}",
        f"The lesser value between {f} and {g}",
        f"Calculation: smallest_value({f}, {g})",
        f"The lower of the two numbers {f} and {g}",
        f"The minimum value between {f} and {g}",
        f"The smaller number among {f} and {g}",
        f"The result of selecting the smaller value from {f} and {g}",
        f"The less significant value of {f} and {g}",
        f"The outcome of comparing {f} and {g} and selecting the smaller",
        f"The lesser value among {f} and {g}",
        f"The number that is smaller between {f} and {g}",
        f"The smaller value of the two numbers {f} and {g}",
        f"The minimum of the numbers {f} and {g}",
        f"The lesser of the values {f} and {g}",
        f"The result of picking the smaller value from {f} and {g}",
        f"The lower value between {f} and {g}",
        f"The smaller of the two values {f} and {g}",
        f"The smaller value of the pair {f} and {g}",
        f"The outcome of choosing the smaller number from {f} and {g}",
        f"The smaller value in the pair {f} and {g}",
        f"The result of finding the minimum value between {f} and {g}",
        f"The lesser of the two inputs {f} and {g}",
        f"The less substantial value among {f} and {g}",
        f"The result of evaluating smallest_value({f}, {g}) is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_smallest_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
