import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_lcm_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_integer(1, 1000)
        num2 = RandomValueGenerator.generate_random_integer(1, 1000)
        examples.append({
            "inputStr": __random_explanation(num1, num2),
            "outputStr": f"##lcm({num1}, {num2})",
        })
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"The least common multiple of {x} and {y}",
        f"LCM of {x} and {y}",
        f"Find the least common multiple of {x} and {y}",
        f"The result of finding LCM({x}, {y})",
        f"LCM for {x} and {y}",
        f"Calculate the least common multiple of {x} and {y}",
        f"Finding LCM for {x} and {y}",
        f"{x} and {y}, what is their least common multiple?",
        f"LCM calculation: {x} and {y}",
        f"The smallest number that is a multiple of both {x} and {y}",
        f"LCM({x}, {y}), what does it give?",
        f"The LCM for {x} and {y}",
        f"Let's find the least common multiple of {x} and {y}",
        f"Find the LCM for {x} and {y}",
        f"{x} and {y}, their LCM?",
        f"The least common multiple when you have {x} and {y}",
        f"LCM({x}, {y}), result is",
        f"Common multiple of {x} and {y}",
        f"The multiple common to {x} and {y}",
        f"LCM of {x} and {y}, find the answer",
        f"Calculate LCM({x}, {y})",
        f"The smallest number that is divisible by both {x} and {y}",
        f"Let's determine the LCM of {x} and {y}",
        f"{x} and {y}, what is their common multiple?",
        f"LCM calculation for {x} and {y}",
        f"The least common multiple of numbers {x} and {y}",
        f"LCM: {x} and {y}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_lcm_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
