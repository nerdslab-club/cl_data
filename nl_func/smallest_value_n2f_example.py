import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_smallest_value_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        num2 = RandomValueGenerator.generate_random_float(-100.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            "outputStr": f"##smallest_value({num1}, {num2})",
        })
    return examples


def __random_explanation(x: float, y: float, identifier: int | None) -> str:
    explanations = [
        f"The smaller value between {x} and {y}",
        f"SMALLEST_VALUE({x}, {y})",
        f"Find the smallest value between {x} and {y}",
        f"The result of smallest value({x}, {y})",
        f"The minimum value between {x} and {y}",
        f"Calculate the smallest value between {x} and {y}",
        f"Finding smallest value for {x} and {y}",
        f"The value less than or equal to both {x} and {y}",
        f"The minimum value between {x} and {y}",
        f"smallest value calculation: {x}, {y}",
        f"The smaller value between {x} and {y}, what is it?",
        f"The smaller value between {x} and {y}, what does it give?",
        f"Let's find the smallest value between {x} and {y}",
        f"Find the smallest value for {x} and {y}",
        f"The smaller value between {x} and {y}, result is",
        f"Calculating the smallest value between {x} and {y}",
        f"The value less than or equal to both {x} and {y}, what is it?",
        f"The minimum value between {x} and {y}, find the answer",
        f"Calculate smallest value({x}, {y})",
        f"The smaller value between {x} and {y}, what is its value?",
        f"Let's determine the smallest value between {x} and {y}",
        f"{x} and {y}, what is their smaller value?",
        f"Finding the smallest value between {x} and {y}",
        f"The smaller value between {x} and {y}, what is its value?",
        f"Find the smallest value between {x} and {y} and provide the result",
        f"smallest value({x}, {y}), what does it yield?",
        f"The smaller value between {x} and {y}, ignoring direction",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_smallest_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
