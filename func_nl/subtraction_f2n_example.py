import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_subtraction_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, num1)  # To ensure no negative results
        examples.append(
            {
                "inputStr": f"##subtraction({num1},{num2})",
                "outputStr": __random_explanation(num1, num2),
            }
        )
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Subtracting {b} from {a}",
        f"{a} - {b}",
        f"Taking away {b} from {a} ...",
        f"The result of subtracting {b} from {a}",
        f"{a} minus {b} equals?",
        f"Calculation: {a} - {b}",
        f"{b} subtracted from {a} is?",
        f"Subtracting {b} from {a}",
        f"{a} minus {b}",
        f"The difference between {a} and {b}",
        f"{a} - {b} =",
        f"{a} take away {b}",
        f"{a} - {b} results in",
        f"{b} removed from {a}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    Utility.create_sample_from_example(
        create_f2n_subtraction_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
    )
