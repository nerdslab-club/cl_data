import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_addition_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(0, 1000)
        num2 = random.randint(0, 1000)
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##addition({num1},{num2})",
            }
        )
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"Adding {x} to {y}",
        f"{x} plus {y}",
        f"Summing {x} and {y}",
        f"The result of {x} plus {y}",
        f"{x} plus {y}, what is it?",
        f"Calculation: {x} + {y}",
        f"{x} plus {y}, equals?",
        f"Summing up {x} with {y}",
        f"{x} combined with {y}",
        f"The sum of {x} and {y}",
        f"{x} plus {y} is?",
        f"{x} plus {y} is equal to?",
        f"{x} added to {y}",
        f"{x} plus {y}, what does it give?",
        f"{x} and {y} added together",
        f"{x} + {y}, the result?",
        f"{x} summed with {y}",
        f"Calculate the sum of {x} and {y}",
        f"The total when you add {x} to {y}",
        f"{x} plus {y}, find the answer",
        f"Sum: {x} + {y}",
        f"Let's add {x} and {y}",
        f"Find the sum of {x} and {y}",
        f"{x} and {y}, their sum?",
        f"{x} plus {y}, result is",
        f"{x} and {y}, what will be the sum?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(Utility.create_sample_from_example(
        create_n2f_addition_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
    ))
