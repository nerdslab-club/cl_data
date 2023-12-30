import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_factorial_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(0, 10)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##factorial({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"The factorial of {x}",
        f"FACTORIAL({x})",
        f"Find the factorial of {x}",
        f"The result of FACTORIAL({x})",
        f"Calculate the factorial of {x}",
        f"Finding FACTORIAL for {x}",
        f"The product of all positive integers up to {x}",
        f"FACTORIAL calculation: {x}",
        f"The factorial of {x}, what is it?",
        f"The factorial of {x}, what does it give?",
        f"Let's find the factorial of {x}",
        f"Find the FACTORIAL for {x}",
        f"The factorial of {x}, result is",
        f"Calculating the factorial of {x}",
        f"The result of multiplying all positive integers up to {x}",
        f"The factorial of {x}, what is its value?",
        f"Let's determine the factorial of {x}",
        f"The product of all integers from 1 to {x}",
        f"{x}!, what is its value?",
        f"Finding the factorial of {x}",
        f"The factorial of {x}, what is its value?",
        f"Find the factorial of {x} and provide the result",
        f"FACTORIAL({x}), what does it yield?",
        f"The factorial of {x}, ignoring order",
        f"The result of multiplying all integers from 1 to {x}",
        f"The product of all positive integers less than or equal to {x}",
        f"The factorial of {x}, what is it?",
        f"Calculate the factorial of {x}, find the answer",
        f"The factorial of {x}, what does it give?",
        f"Let's find the result of multiplying all integers up to {x}",
        f"{x}!, its value, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_factorial_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
