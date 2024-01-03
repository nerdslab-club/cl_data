import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_square_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_float(1.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##square({num})",
        })
    return examples


def __random_explanation(f1: float) -> str:
    explanations = [
        f"Calculate the square of the number {f1}",
        f"SQUARE({f1})",
        f"Find the square value for the number {f1}",
        f"The result of squaring the number {f1}",
        f"Perform the square operation on the number {f1}",
        f"Squaring the number {f1}",
        f"The square of the number {f1}",
        f"SQUARE calculation: {f1}",
        f"The result after squaring the number {f1}, what is it?",
        f"The square value of the number {f1}, what does it give?",
        f"Let's square the number {f1}",
        f"Square the number {f1}, result is",
        f"Calculating the square for the number {f1}",
        f"The squared result after squaring the number {f1}",
        f"The square of the number {f1}, what is its value?",
        f"Let's determine the square of the number {f1}",
        f"The square value of the number {f1}",
        f"Square {f1}, what is the result?",
        f"The square of the number {f1}, what does it give?",
        f"Square {f1} and provide the result",
        f"SQUARE({f1}), what does it yield?",
        f"The square value of the number {f1}, ignoring order",
        f"The result after squaring the number {f1}",
        f"The square of the number {f1}, what is it?",
        f"Calculate the square for the number {f1}, find the answer",
        f"The square value of the number {f1}, what does it give?",
        f"Let's find the result after squaring the number {f1}",
        f"Square {f1}, what is the output?",
        f"The squared result after squaring the number {f1}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_square_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
