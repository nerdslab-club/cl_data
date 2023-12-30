import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_absolute_difference_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        num2 = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(num1, num2),
            "outputStr": f"##absolute_difference({num1}, {num2})",
        })
    return examples


def __random_explanation(x: float, y: float) -> str:
    explanations = [
        f"The absolute difference between {x} and {y}",
        f"Absolute difference({x}, {y})",
        f"Find the absolute difference of {x} and {y}",
        f"The result of absolute difference({x}, {y})",
        f"The positive difference between {x} and {y}",
        f"Calculate the absolute difference of {x} and {y}",
        f"Finding absolute difference for {x} and {y}",
        f"The difference between {x} and {y}, ignoring direction",
        f"The absolute value of the difference between {x} and {y}",
        f"Absolute difference calculation: {x}, {y}",
        f"The positive difference between {x} and {y}, what is it?",
        f"The positive difference between {x} and {y}, what does it give?",
        f"Let's find the absolute difference of {x} and {y}",
        f"Find the absolute difference for {x} and {y}",
        f"The positive difference between {x} and {y}, result is",
        f"Calculating the absolute difference between {x} and {y}",
        f"{x} and {y}, what is their absolute difference?",
        f"The absolute value of the positive difference between {x} and {y}",
        f"The non-negative difference between {x} and {y}",
        f"Absolute difference of {x} and {y}, find the answer",
        f"Calculate absolute difference({x}, {y})",
        f"The absolute value of the difference between {x} and {y}",
        f"Let's determine the absolute difference of {x} and {y}",
        f"{x} and {y}, what is their positive difference?",
        f"Finding the absolute difference between {x} and {y}",
        f"The positive difference between {x} and {y}, what is its value?",
        f"Find the absolute difference of {x} and {y} and provide the result",
        f"Absolute difference({x}, {y}), what does it yield?",
        f"The absolute difference between {x} and {y}, ignoring direction",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_absolute_difference_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
