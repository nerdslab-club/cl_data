import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_exponentiation_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(1, 100)  # Base: random float between 1 and 10
        num2 = random.randint(0, 50)  # Exponent: random integer between 0 and 5
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##exponentiation({num1},{num2})",
            }
        )
    return examples


def __random_explanation(f1: float, f2: int) -> str:
    explanations = [
        f"Raising {f1} to the power of {f2}",
        f"{f1} raised to the power of {f2}",
        f"{f1} to the power of {f2}",
        f"{f1} exponentiated by {f2}",
        f"The result of {f1} raised to {f2}",
        f"{f1} raised to {f2}, what is it?",
        f"Calculation: {f1} ** {f2}",
        f"{f1} raised to {f2}, equals?",
        f"Taking {f1} and exponentiating by {f2}",
        f"{f1} raised to {f2}, the answer?",
        f"{f1} to the power of {f2}, find the result",
        f"{f1} and {f2} exponentiation",
        f"The exponentiation of {f1} and {f2}",
        f"{f1} raised to {f2} is?",
        f"{f1} raised to {f2} is equal to?",
        f"{f1} and {f2} exponentiated, the result?",
        f"Exponentiation: {f1} ** {f2}",
        f"Let's raise {f1} to the power of {f2}",
        f"Find the result of {f1} raised to {f2}",
        f"{f1} and {f2}, their exponentiation?",
        f"{f1} raised to {f2}, result is",
        f"{f1} and {f2}, what will be the result?",
        f"Exponentiation: {f1} ** {f2}, what is it?",
        f"{f1} raised to {f2}, result?",
        f"{f1} exponentiated by {f2}, the outcome?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_exponentiation_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
