import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_greatest_value_example(count: int):
    examples = []
    for _ in range(count):
        x = random.uniform(-100.0, 100.0)
        y = random.uniform(-100.0, 100.0)
        examples.append(
            {
                "inputStr": f"##greatest_value({x}, {y})",
                "outputStr": __random_explanation_greatest_value(x, y),
            }
        )
    return examples


def __random_explanation_greatest_value(x: float, y: float) -> str:
    explanations = [
        f"The greater of {x} and {y}",
        f"greatest_value({x}, {y})",
        f"The larger value between {x} and {y}",
        f"Calculation: greatest_value({x}, {y})",
        f"The higher of the two numbers {x} and {y}",
        f"The maximum value between {x} and {y}",
        f"The greater number among {x} and {y}",
        f"The result of selecting the larger value from {x} and {y}",
        f"The more significant value of {x} and {y}",
        f"The outcome of comparing {x} and {y} and selecting the greater",
        f"The larger value among {x} and {y}",
        f"The number that is greater between {x} and {y}",
        f"The greater value of the two numbers {x} and {y}",
        f"The maximum of the numbers {x} and {y}",
        f"The larger of the values {x} and {y}",
        f"The result of picking the larger value from {x} and {y}",
        f"The higher value between {x} and {y}",
        f"The greater of the two values {x} and {y}",
        f"The greater value of the pair {x} and {y}",
        f"The outcome of choosing the larger number from {x} and {y}",
        f"The larger value in the pair {x} and {y}",
        f"The result of finding the maximum value between {x} and {y}",
        f"The greater of the two inputs {x} and {y}",
        f"The more substantial value among {x} and {y}",
        f"The result of evaluating greatest_value({x}, {y}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_greatest_value_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
