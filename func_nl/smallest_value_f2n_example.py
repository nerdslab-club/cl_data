import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_smallest_value_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-100.0, 100.0)
        y = random.uniform(-100.0, 100.0)
        examples.append(
            {
                "inputStr": f"##smallest_value({x}, {y})",
                "outputStr": __random_explanation_smallest_value(x, y),
            }
        )
    return examples


def __random_explanation_smallest_value(x: float, y: float) -> str:
    explanations = [
        f"The smaller of {x} and {y}",
        f"smallest_value({x}, {y})",
        f"The lesser value between {x} and {y}",
        f"Calculation: smallest_value({x}, {y})",
        f"The lower of the two numbers {x} and {y}",
        f"The minimum value between {x} and {y}",
        f"The smaller number among {x} and {y}",
        f"The result of selecting the smaller value from {x} and {y}",
        f"The less significant value of {x} and {y}",
        f"The outcome of comparing {x} and {y} and selecting the smaller",
        f"The lesser value among {x} and {y}",
        f"The number that is smaller between {x} and {y}",
        f"The smaller value of the two numbers {x} and {y}",
        f"The minimum of the numbers {x} and {y}",
        f"The lesser of the values {x} and {y}",
        f"The result of picking the smaller value from {x} and {y}",
        f"The lower value between {x} and {y}",
        f"The smaller of the two values {x} and {y}",
        f"The smaller value of the pair {x} and {y}",
        f"The outcome of choosing the smaller number from {x} and {y}",
        f"The smaller value in the pair {x} and {y}",
        f"The result of finding the minimum value between {x} and {y}",
        f"The lesser of the two inputs {x} and {y}",
        f"The less substantial value among {x} and {y}",
        f"The smallest value is",
        f"The result of evaluating smallest_value({x}, {y}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_smallest_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
