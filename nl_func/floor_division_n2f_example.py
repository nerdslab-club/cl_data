import random

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_floor_division_example(count: int):
    examples = []
    for _ in range(count):
        num1 = random.randint(1, 10000)  # Using random integer between 1 and 100
        num2 = random.randint(
            1, 19990
        )  # Using random integer between 1 and 100 (avoid division by zero)
        examples.append(
            {
                "inputStr": __random_explanation(num1, num2),
                "outputStr": f"##floor_division({num1},{num2})",
            }
        )
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"Floor dividing {x} by {y}",
        f"{x} floor divided by {y}",
        f"{x} divided by {y} using floor division",
        f"The result of {x} floor divided by {y}",
        f"{x} divided by {y} using floor division, what is it?",
        f"Calculation: {x} // {y}",
        f"{x} floor divided by {y}, equals?",
        f"Taking {x} and floor dividing by {y}",
        f"{x} divided by {y} with floor division, the answer?",
        f"Quotient when {x} is floor divided by {y}",
        f"{x} and {y} floor division",
        f"The floor division of {x} and {y}",
        f"{x} divided by {y} using floor division, is?",
        f"{x} divided by {y} using floor division, result is",
        f"{x} and {y} floor divided, the result?",
        f"Floor division: {x} // {y}",
        f"Let's floor divide {x} by {y}",
        f"Find the result of {x} divided by {y} using floor division",
        f"{x} and {y}, their floor division?",
        f"{x} divided by {y} using floor division, the outcome?",
        f"{x} and {y}, what will be the quotient using floor division?",
        f"Floor division calculation: {x} // {y}",
        f"{x} divided by {y} using floor division, result?",
        f"{x} divided into {y} parts using floor division",
        f"{x} distributed over {y} with floor division",
        f"The result when {x} is divided by {y} using floor division",
        f"{x} divided by {y} with floor division, in whole numbers",
        f"The quotient when {x} is floor divided by {y}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_floor_division_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
