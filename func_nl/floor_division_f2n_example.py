import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_floor_division_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(1, 1000)
        num2 = random.randint(1, num1)  # To ensure non-zero denominator
        examples.append(
            {
                "inputStr": f"##floor_division({num1},{num2})",
                "outputStr": __random_explanation_floor_div(
                    num1,
                    num2,
                ),
            }
        )
    return examples


def __random_explanation_floor_div(x: int, y: int) -> str:
    explanations = [
        f"The floor division of {x} by {y}",
        f"{x} // {y}",
        f"The result of floor dividing {x} by {y}",
        f"{x} divided by {y} using floor division",
        f"Calculation: {x} // {y}",
        f"The floor quotient of {x} and {y}",
        f"{x} floor divided by {y}",
        f"{x} divided by {y} using the floor division operator",
        f"The integer division result of {x} by {y}",
        f"{x} // {y} equals?",
        f"{x} divided by {y} using floor division gives",
        f"The largest integer quotient of {x} and {y}",
        f"The floor division of {x} and {y} is",
        f"{x} // {y} is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_floor_division_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
