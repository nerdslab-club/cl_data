import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_gcd_example(count: int):
    examples = []
    for _ in range(count):
        num1 = RandomValueGenerator.generate_random_integer(1, 1000)
        num2 = RandomValueGenerator.generate_random_integer(1, 1000)
        examples.append({
            "inputStr": __random_explanation(num1, num2),
            "outputStr": f"##gcd({num1}, {num2})",
        })
    return examples


def __random_explanation(x: int, y: int) -> str:
    explanations = [
        f"The greatest common divisor of {x} and {y}",
        f"GCD of {x} and {y}",
        f"Find the greatest common divisor of {x} and {y}",
        f"The result of finding GCD({x}, {y})",
        f"GCD for {x} and {y}",
        f"Calculate the greatest common divisor of {x} and {y}",
        f"Finding GCD for {x} and {y}",
        f"{x} and {y}, what is their greatest common divisor?",
        f"GCD calculation: {x} and {y}",
        f"The common factor of {x} and {y}",
        f"The largest number that divides both {x} and {y}",
        f"GCD({x}, {y}), what does it give?",
        f"The GCD for {x} and {y}",
        f"Let's find the greatest common divisor of {x} and {y}",
        f"Find the GCD for {x} and {y}",
        f"{x} and {y}, their GCD?",
        f"The greatest common divisor when you have {x} and {y}",
        f"GCD({x}, {y}), result is",
        f"Common divisor of {x} and {y}",
        f"The divisor common to {x} and {y}",
        f"GCD of {x} and {y}, find the answer",
        f"Calculate GCD({x}, {y})",
        f"The common factor for {x} and {y}",
        f"Let's determine the GCD of {x} and {y}",
        f"{x} and {y}, what is their common divisor?",
        f"GCD calculation for {x} and {y}",
        f"The greatest common divisor of numbers {x} and {y}",
        f"GCD: {x} and {y}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_gcd_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
