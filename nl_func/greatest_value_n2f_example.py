import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_greatest_value_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        num2 = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(num1, num2),
            "outputStr": f"##greatest_value({num1}, {num2})",
        })
    return examples


def __random_explanation(x: float, y: float) -> str:
    explanations = [
        f"The greater value between {x} and {y}",
        f"GREATEST_VALUE({x}, {y})",
        f"Find the greatest value between {x} and {y}",
        f"The result of GREATEST_VALUE({x}, {y})",
        f"The larger value between {x} and {y}",
        f"Calculate the greatest value between {x} and {y}",
        f"Finding greatest value for {x} and {y}",
        f"The value greater than or equal to both {x} and {y}",
        f"The maximum value between {x} and {y}",
        f"greatest value calculation: {x}, {y}",
        f"The larger value between {x} and {y}, what is it?",
        f"The larger value between {x} and {y}, what does it give?",
        f"Let's find the greatest value between {x} and {y}",
        f"Find the greatest value for {x} and {y}",
        f"The larger value between {x} and {y}, result is",
        f"Calculating the greatest value between {x} and {y}",
        f"The value greater than or equal to both {x} and {y}, what is it?",
        f"The maximum value between {x} and {y}, find the answer",
        f"Calculate greatest value({x}, {y})",
        f"The greater value between {x} and {y}, what is its value?",
        f"Let's determine the greatest value between {x} and {y}",
        f"{x} and {y}, what is their larger value?",
        f"Finding the greatest value between {x} and {y}",
        f"The larger value between {x} and {y}, what is its value?",
        f"Find the greatest value between {x} and {y} and provide the result",
        f"greatest value({x}, {y}), what does it yield?",
        f"The greater value between {x} and {y}, ignoring direction",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_greatest_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
