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


def __random_explanation(f1: float, f2: float) -> str:
    explanations = [
        f"The greater value between {f1} and {f2}",
        f"GREATEST_VALUE({f1}, {f2})",
        f"Find the greatest value between {f1} and {f2}",
        f"The result of GREATEST_VALUE({f1}, {f2})",
        f"The larger value between {f1} and {f2}",
        f"Calculate the greatest value between {f1} and {f2}",
        f"Finding greatest value for {f1} and {f2}",
        f"The value greater than or equal to both {f1} and {f2}",
        f"The maximum value between {f1} and {f2}",
        f"greatest value calculation: {f1}, {f2}",
        f"The larger value between {f1} and {f2}, what is it?",
        f"The larger value between {f1} and {f2}, what does it give?",
        f"Let's find the greatest value between {f1} and {f2}",
        f"Find the greatest value for {f1} and {f2}",
        f"The larger value between {f1} and {f2}, result is",
        f"Calculating the greatest value between {f1} and {f2}",
        f"The value greater than or equal to both {f1} and {f2}, what is it?",
        f"The maximum value between {f1} and {f2}, find the answer",
        f"Calculate greatest value({f1}, {f2})",
        f"The greater value between {f1} and {f2}, what is its value?",
        f"Let's determine the greatest value between {f1} and {f2}",
        f"{f1} and {f2}, what is their larger value?",
        f"Finding the greatest value between {f1} and {f2}",
        f"The larger value between {f1} and {f2}, what is its value?",
        f"Find the greatest value between {f1} and {f2} and provide the result",
        f"greatest value({f1}, {f2}), what does it yield?",
        f"The greater value between {f1} and {f2}, ignoring direction",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_greatest_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
