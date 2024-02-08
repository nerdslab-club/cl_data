import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_square_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##square({num})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the square of the number {f1}",
        f"Find the square value for the number {f1}",
        f"The result of squaring the number {f1}",
        f"Perform the square operation on the number {f1}",
        f"Squaring the number {f1}",
        f"The square of the number {f1}",
        f"Let's square the number {f1}",
        f"Square the number {f1}, result is",
        f"Calculating the square for the number {f1}",
        f"The squared result after squaring the number {f1}",
        f"Let's determine the square of the number {f1}",
        f"The square value of the number {f1}",
        f"Square {f1}, what is the result",
        f"Square {f1} and provide the result",
        f"The result after squaring the number {f1}",
        f"Calculate the square for the number {f1}, find the answer",
        f"Let's find the result after squaring the number {f1}",
        f"Square {f1}, what is the output",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_square_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
