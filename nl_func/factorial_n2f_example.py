import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_factorial_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##factorial({num})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"The factorial of {a}",
        f"Find the factorial of {a}",
        f"The result of FACTORIAL({a})",
        f"Calculate the factorial of {a}",
        f"The product of all positive integers up to {a}",
        f"FACTORIAL calculation: {a}",
        f"The factorial of {a}, what is it",
        f"The factorial of {a}, what does it give",
        f"Let's find the factorial of {a}",
        f"The factorial of {a}, result is",
        f"Calculating the factorial of {a}",
        f"The result of multiplying all positive integers up to {a}",
        f"The factorial of {a}, what is its value",
        f"Let's determine the factorial of {a}",
        f"The product of all integers from 1 to {a}",
        f"{a}!, what is its value",
        f"Finding the factorial of {a}",
        f"The factorial of {a}, what is its value",
        f"Find the factorial of {a} and provide the result",
        f"The factorial of {a}, ignoring order",
        f"The result of multiplying all integers from 1 to {a}",
        f"The product of all positive integers less than or equal to {a}",
        f"The factorial of {a}, what is it",
        f"Calculate the factorial of {a}, find the answer",
        f"The factorial of {a}, what does it give",
        f"Let's find the result of multiplying all integers up to {a}",
        f"{a}!, its value, what is the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_factorial_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
