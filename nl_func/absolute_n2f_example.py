import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_absolute_example(count: int):
    examples = []
    for _ in range(count):
        f1 = RandomValueGenerator.generate_random_float(-10.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(f1),
            "outputStr": f"##absolute({f1})",
        })
    return examples


def __random_explanation(f1: float) -> str:
    explanations = [
        f"Calculate the absolute value of the number {f1}",
        f"ABSOLUTE({f1})",
        f"Find the absolute value for the number {f1}",
        f"The result of taking the absolute value of {f1}",
        f"Performing the absolute operation on the number {f1}",
        f"The absolute value of the number {f1}",
        f"ABSOLUTE calculation: {f1}",
        f"The result after taking the absolute value of {f1}, what is it?",
        f"The absolute value of {f1}, what does it give?",
        f"Let's find the absolute value of {f1}",
        f"Absolute value of {f1}, result is",
        f"Calculating the absolute value for {f1}",
        f"The absolute result after taking the absolute value of {f1}",
        f"The absolute value of the number {f1}, what is its value?",
        f"Let's determine the absolute value of {f1}",
        f"The absolute value of {f1}",
        f"Absolute value of {f1}, what is the result?",
        f"The absolute value of {f1}, what does it give?",
        f"Absolute value of {f1} and provide the result",
        f"ABSOLUTE({f1}), what does it yield?",
        f"The absolute value of {f1}, ignoring order",
        f"The result after taking the absolute value of {f1}",
        f"The absolute value of the number {f1}, what is it?",
        f"Calculate the absolute value for {f1}, find the answer",
        f"The absolute value of {f1}, what does it give?",
        f"Let's find the result after taking the absolute value of {f1}",
        f"Absolute value of {f1}, what is the output?",
        f"The absolute result after taking the absolute value of {f1}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_absolute_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
