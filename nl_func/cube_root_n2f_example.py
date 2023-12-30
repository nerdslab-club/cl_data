import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_cube_root_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(1.0, 1000.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##cube_root({num})",
        })
    return examples


def __random_explanation(x: float) -> str:
    explanations = [
        f"Calculate the cube root of the number {x}",
        f"CUBE_ROOT({x})",
        f"Find the cube root value for the number {x}",
        f"The result of taking the cube root of {x}",
        f"Performing the cube root operation on the number {x}",
        f"The cube root of the number {x}",
        f"CUBE_ROOT calculation: {x}",
        f"The result after taking the cube root of {x}, what is it?",
        f"The cube root value of {x}, what does it give?",
        f"Let's find the cube root value of {x}",
        f"Cube root of {x}, result is",
        f"Calculating the cube root for the number {x}",
        f"The cube root result after taking the cube root of {x}",
        f"The cube root of the number {x}, what is its value?",
        f"Let's determine the cube root of the number {x}",
        f"The cube root value of {x}",
        f"Cube root {x}, what is the result?",
        f"The cube root of the number {x}, what does it give?",
        f"Cube root {x} and provide the result",
        f"CUBE_ROOT({x}), what does it yield?",
        f"The cube root value of {x}, ignoring order",
        f"The result after taking the cube root of {x}",
        f"The cube root of the number {x}, what is it?",
        f"Calculate the cube root for the number {x}, find the answer",
        f"The cube root value of {x}, what does it give?",
        f"Let's find the result after taking the cube root of {x}",
        f"Cube root {x}, what is the output?",
        f"The cube root result after taking the cube root of {x}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cube_root_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
