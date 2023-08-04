import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_subtraction_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, num1)  # To ensure no negative results
        examples.append({
            "inputStr": f"##subtraction({num1},{num2})",
            "outputStr": __random_explanation(num1, num2)
        })
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"Subtracting {y} from {x}",
        f"{x} - {y}",
        f"Taking away {y} from {x}...",
        f"The result of subtracting {y} from {x}",
        f"{x} minus {y} equals?",
        f"Calculation: {x} - {y}",
        f"{y} subtracted from {x} is?",
        f"Subtracting {y} from {x}",
        f"{x} minus {y}",
        f"The difference between {x} and {y}",
        f"{x} - {y} =",
        f"{x} take away {y}",
        f"{x} - {y} results in",
        f"{y} removed from {x}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(create_f2n_subtraction_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION)
