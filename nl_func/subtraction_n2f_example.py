import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_subtraction_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, num1)  # Ensure num2 is less than or equal to num1
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##subtraction({num1},{num2})",
            }
        )
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"Subtracting {y} from {x}",
        f"{x} minus {y}",
        f"Deducting {y} from {x}",
        f"The result of {x} minus {y}",
        f"{x} minus {y}, what is it?",
        f"Calculation: {x} - {y}",
        f"{x} minus {y}, equals?",
        f"Taking away {y} from {x}",
        f"{y} subtracted from {x}",
        f"The subtraction of {y} from {x}",
        f"{x} minus {y} is?",
        f"{x} minus {y} is equal to?",
        f"{y} subtracted from {x}, what does it give?",
        f"{x} and {y} subtracted, the result?",
        f"{x} less {y}, the answer?",
        f"{x} take away {y}, find the answer",
        f"Difference: {x} - {y}",
        f"Let's subtract {y} from {x}",
        f"Find the difference between {x} and {y}",
        f"{y} and {x}, their subtraction?",
        f"{x} minus {y}, result is",
        f"{x} and {y}, what will be the difference?",
        f"Subtraction: {x} - {y}",
        f"{x} decreased by {y}",
        f"{y} reduced from {x}",
        f"The remainder when {y} is subtracted from {x}",
        f"{x} take away {y} equals?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_n2f_subtraction_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
    )
