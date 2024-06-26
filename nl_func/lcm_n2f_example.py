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


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"The least common multiple of {a} and {b}",
        f"LCM of {a} and {b}",
        f"Find the least common multiple of {a} and {b}",
        f"The result of finding LCM({a}, {b})",
        f"LCM for {a} and {b}",
        f"Calculate the least common multiple of {a} and {b}",
        f"Finding LCM for {a} and {b}",
        f"{a} and {b}, what is their least common multiple?",
        f"LCM calculation: {a} and {b}",
        f"The smallest number that is a multiple of both {a} and {b}",
        f"LCM({a}, {b}), what does it give?",
        f"The LCM for {a} and {b}",
        f"Let's find the least common multiple of {a} and {b}",
        f"Find the LCM for {a} and {b}",
        f"{a} and {b}, their LCM?",
        f"The least common multiple when you have {a} and {b}",
        f"LCM({a}, {b}), result is",
        f"Common multiple of {a} and {b}",
        f"The multiple common to {a} and {b}",
        f"LCM of {a} and {b}, find the answer",
        f"Calculate LCM({a}, {b})",
        f"The smallest number that is divisible by both {a} and {b}",
        f"Let's determine the LCM of {a} and {b}",
        f"{a} and {b}, what is their common multiple?",
        f"LCM calculation for {a} and {b}",
        f"The least common multiple of numbers {a} and {b}",
        f"LCM: {a} and {b}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_lcm_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
