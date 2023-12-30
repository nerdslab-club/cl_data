import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_absolute_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(-10.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##absolute({num})",
        })
    return examples


def __random_explanation(x: float) -> str:
    explanations = [
        f"Calculate the absolute value of the number {x}",
        f"ABSOLUTE({x})",
        f"Find the absolute value for the number {x}",
        f"The result of taking the absolute value of {x}",
        f"Performing the absolute operation on the number {x}",
        f"The absolute value of the number {x}",
        f"ABSOLUTE calculation: {x}",
        f"The result after taking the absolute value of {x}, what is it?",
        f"The absolute value of {x}, what does it give?",
        f"Let's find the absolute value of {x}",
        f"Absolute value of {x}, result is",
        f"Calculating the absolute value for {x}",
        f"The absolute result after taking the absolute value of {x}",
        f"The absolute value of the number {x}, what is its value?",
        f"Let's determine the absolute value of {x}",
        f"The absolute value of {x}",
        f"Absolute value of {x}, what is the result?",
        f"The absolute value of {x}, what does it give?",
        f"Absolute value of {x} and provide the result",
        f"ABSOLUTE({x}), what does it yield?",
        f"The absolute value of {x}, ignoring order",
        f"The result after taking the absolute value of {x}",
        f"The absolute value of the number {x}, what is it?",
        f"Calculate the absolute value for {x}, find the answer",
        f"The absolute value of {x}, what does it give?",
        f"Let's find the result after taking the absolute value of {x}",
        f"Absolute value of {x}, what is the output?",
        f"The absolute result after taking the absolute value of {x}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_absolute_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
