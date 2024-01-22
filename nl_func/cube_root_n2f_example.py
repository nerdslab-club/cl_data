import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_cube_root_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(1.0, 1000.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##cube_root({f1})",
        })
    return examples


def __random_explanation(f1: float) -> str:
    explanations = [
        f"Calculate the cube root of the number {f1}",
        f"CUBE_ROOT({f1})",
        f"Find the cube root value for the number {f1}",
        f"The result of taking the cube root of {f1}",
        f"Performing the cube root operation on the number {f1}",
        f"The cube root of the number {f1}",
        f"CUBE_ROOT calculation: {f1}",
        f"The result after taking the cube root of {f1}, what is it?",
        f"The cube root value of {f1}, what does it give?",
        f"Let's find the cube root value of {f1}",
        f"Cube root of {f1}, result is",
        f"Calculating the cube root for the number {f1}",
        f"The cube root result after taking the cube root of {f1}",
        f"The cube root of the number {f1}, what is its value?",
        f"Let's determine the cube root of the number {f1}",
        f"The cube root value of {f1}",
        f"Cube root {f1}, what is the result?",
        f"The cube root of the number {f1}, what does it give?",
        f"Cube root {f1} and provide the result",
        f"CUBE_ROOT({f1}), what does it yield?",
        f"The cube root value of {f1}, ignoring order",
        f"The result after taking the cube root of {f1}",
        f"The cube root of the number {f1}, what is it?",
        f"Calculate the cube root for the number {f1}, find the answer",
        f"The cube root value of {f1}, what does it give?",
        f"Let's find the result after taking the cube root of {f1}",
        f"Cube root {f1}, what is the output?",
        f"The cube root result after taking the cube root of {f1}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_cube_root_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
