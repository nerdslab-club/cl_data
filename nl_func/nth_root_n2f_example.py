import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_nth_root_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(1.0, 1000.0)
        root = RandomValueGenerator.generate_random_integer(2, 5)
        examples.append({
            "inputStr": __random_explanation(num, root),
            "outputStr": f"##nth_root({num}, {root})",
        })
    return examples


def __random_explanation(x: float, n: int) -> str:
    explanations = [
        f"Calculate the {n}-th root of the number {x}",
        f"NTH_ROOT({x}, {n})",
        f"Find the {n}-th root value for the number {x}",
        f"The result of taking the {n}-th root of {x}",
        f"Performing the {n}-th root operation on the number {x}",
        f"The {n}-th root of the number {x}",
        f"NTH_ROOT calculation: {x}, {n}",
        f"The result after taking the {n}-th root of {x}, what is it?",
        f"The {n}-th root value of {x}, what does it give?",
        f"Let's find the {n}-th root value of {x}",
        f"{n}-th root of {x}, result is",
        f"Calculating the {n}-th root for the number {x}",
        f"The {n}-th root result after taking the {n}-th root of {x}",
        f"The {n}-th root of the number {x}, what is its value?",
        f"Let's determine the {n}-th root of the number {x}",
        f"The {n}-th root value of {x}",
        f"{n}-th root {x}, what is the result?",
        f"The {n}-th root of the number {x}, what does it give?",
        f"{n}-th root {x} and provide the result",
        f"NTH_ROOT({x}, {n}), what does it yield?",
        f"The {n}-th root value of {x}, ignoring order",
        f"The result after taking the {n}-th root of {x}",
        f"The {n}-th root of the number {x}, what is it?",
        f"Calculate the {n}-th root of {x}, find the answer",
        f"The {n}-th root value of {x}, what does it give?",
        f"Let's find the result after taking the {n}-th root of {x}",
        f"{n}-th root {x}, what is the output?",
        f"The {n}-th root result after taking the {n}-th root of {x}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_nth_root_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
