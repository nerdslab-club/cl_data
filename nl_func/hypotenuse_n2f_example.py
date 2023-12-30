import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_hypotenuse_example(count: int):
    examples = []
    for _ in range(count):
        side_a = RandomValueGenerator.generate_random_float(1.0, 10.0)
        side_b = RandomValueGenerator.generate_random_float(1.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(side_a, side_b),
            "outputStr": f"##hypotenuse({side_a}, {side_b})",
        })
    return examples


def __random_explanation(side_a: float, side_b: float) -> str:
    explanations = [
        f"Calculate the hypotenuse for the sides {side_a} and {side_b}",
        f"HYPOTENUSE({side_a}, {side_b})",
        f"Determine the hypotenuse for the sides {side_a} and {side_b}",
        f"Find the hypotenuse value for the sides {side_a} and {side_b}",
        f"The result of calculating the hypotenuse for sides {side_a} and {side_b}",
        f"Performing the hypotenuse operation on the sides {side_a} and {side_b}",
        f"The hypotenuse for sides {side_a} and {side_b}",
        f"HYPOTENUSE calculation: ({side_a}, {side_b})",
        f"The result after calculating the hypotenuse for sides {side_a} and {side_b}, what is it?",
        f"The hypotenuse value of sides {side_a} and {side_b}, what does it give?",
        f"Let's calculate the hypotenuse for the sides {side_a} and {side_b}",
        f"The hypotenuse value for the sides {side_a} and {side_b}, result is",
        f"Calculating the hypotenuse for the sides {side_a} and {side_b}",
        f"The hypotenuse result after calculating the hypotenuse for sides {side_a} and {side_b}",
        f"The hypotenuse for sides {side_a} and {side_b}, what is its value?",
        f"Let's determine the hypotenuse for the sides {side_a} and {side_b}",
        f"The hypotenuse value for the sides {side_a} and {side_b}",
        f"The hypotenuse for the sides {side_a} and {side_b}, what is the result?",
        f"The hypotenuse for the sides {side_a} and {side_b}, what does it give?",
        f"The hypotenuse for the sides {side_a} and {side_b} and provide the result",
        f"HYPOTENUSE({side_a}, {side_b}), what does it yield?",
        f"The hypotenuse value for the sides {side_a} and {side_b}, ignoring order",
        f"The result after calculating the hypotenuse for sides {side_a} and {side_b}",
        f"The hypotenuse for the sides {side_a} and {side_b}, what is it?",
        f"Calculate the hypotenuse for the sides {side_a} and {side_b}, find the answer",
        f"The hypotenuse for the sides {side_a} and {side_b}, what does it give?",
        f"Let's find the result after calculating the hypotenuse for sides {side_a} and {side_b}",
        f"The hypotenuse for the sides {side_a} and {side_b}, what is the output?",
        f"The result after calculating the hypotenuse for sides {side_a} and {side_b}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_hypotenuse_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
