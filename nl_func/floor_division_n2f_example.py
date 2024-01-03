import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_floor_division_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(1, 1000)  # Using random integer between 1 and 100
        num2 = random.randint(
            1, 1000
        )  # Using random integer between 1 and 100 (avoid division by zero)
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##floor_division({num1},{num2})",
            }
        )
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Floor dividing {a} by {b}",
        f"{a} floor divided by {b}",
        f"{a} divided by {b} using floor division",
        f"The result of {a} floor divided by {b}",
        f"{a} divided by {b} using floor division, what is it?",
        f"Calculation: {a} // {b}",
        f"{a} floor divided by {b}, equals?",
        f"Taking {a} and floor dividing by {b}",
        f"{a} divided by {b} with floor division, the answer?",
        f"Quotient when {a} is floor divided by {b}",
        f"{a} and {b} floor division",
        f"The floor division of {a} and {b}",
        f"{a} divided by {b} using floor division, is?",
        f"{a} divided by {b} using floor division, result is",
        f"{a} and {b} floor divided, the result?",
        f"Floor division: {a} // {b}",
        f"Let's floor divide {a} by {b}",
        f"Find the result of {a} divided by {b} using floor division",
        f"{a} and {b}, their floor division?",
        f"{a} divided by {b} using floor division, the outcome?",
        f"{a} and {b}, what will be the quotient using floor division?",
        f"Floor division calculation: {a} // {b}",
        f"{a} divided by {b} using floor division, result?",
        f"{a} divided into {b} parts using floor division",
        f"{a} distributed over {b} with floor division",
        f"The result when {a} is divided by {b} using floor division",
        f"{a} divided by {b} with floor division, in whole numbers",
        f"The quotient when {a} is floor divided by {b}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_floor_division_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
