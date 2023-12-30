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


def __random_explanation(x: float) -> str:
    explanations = [
        f"Calculate the square of the number {x}",
        f"SQUARE({x})",
        f"Find the square value for the number {x}",
        f"The result of squaring the number {x}",
        f"Perform the square operation on the number {x}",
        f"Squaring the number {x}",
        f"The square of the number {x}",
        f"SQUARE calculation: {x}",
        f"The result after squaring the number {x}, what is it?",
        f"The square value of the number {x}, what does it give?",
        f"Let's square the number {x}",
        f"Square the number {x}, result is",
        f"Calculating the square for the number {x}",
        f"The squared result after squaring the number {x}",
        f"The square of the number {x}, what is its value?",
        f"Let's determine the square of the number {x}",
        f"The square value of the number {x}",
        f"Square {x}, what is the result?",
        f"The square of the number {x}, what does it give?",
        f"Square {x} and provide the result",
        f"SQUARE({x}), what does it yield?",
        f"The square value of the number {x}, ignoring order",
        f"The result after squaring the number {x}",
        f"The square of the number {x}, what is it?",
        f"Calculate the square for the number {x}, find the answer",
        f"The square value of the number {x}, what does it give?",
        f"Let's find the result after squaring the number {x}",
        f"Square {x}, what is the output?",
        f"The squared result after squaring the number {x}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_square_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
