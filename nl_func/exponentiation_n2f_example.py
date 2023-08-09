import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_exponentiation_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.uniform(1, 1000)  # Base: random float between 1 and 10
        num2 = random.randint(0, 50)  # Exponent: random integer between 0 and 5
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##exponentiation({num1},{num2})",
            }
        )
    return examples


def __random_explanation(base: float, exponent: int) -> str:
    explanations = [
        f"Raising {base} to the power of {exponent}",
        f"{base} raised to the power of {exponent}",
        f"{base} to the power of {exponent}",
        f"{base} exponentiated by {exponent}",
        f"The result of {base} raised to {exponent}",
        f"{base} raised to {exponent}, what is it?",
        f"Calculation: {base} ** {exponent}",
        f"{base} raised to {exponent}, equals?",
        f"Taking {base} and exponentiating by {exponent}",
        f"{base} raised to {exponent}, the answer?",
        f"{base} to the power of {exponent}, find the result",
        f"{base} and {exponent} exponentiation",
        f"The exponentiation of {base} and {exponent}",
        f"{base} raised to {exponent} is?",
        f"{base} raised to {exponent} is equal to?",
        f"{base} and {exponent} exponentiated, the result?",
        f"Exponentiation: {base} ** {exponent}",
        f"Let's raise {base} to the power of {exponent}",
        f"Find the result of {base} raised to {exponent}",
        f"{base} and {exponent}, their exponentiation?",
        f"{base} raised to {exponent}, result is",
        f"{base} and {exponent}, what will be the result?",
        f"Exponentiation: {base} ** {exponent}, what is it?",
        f"{base} raised to {exponent}, result?",
        f"{base} exponentiated by {exponent}, the outcome?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_exponentiation_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
