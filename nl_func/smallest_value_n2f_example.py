import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_smallest_value_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append({
            "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            "outputStr": f"##smallest_value({num1}, {num2})",
        })
    return examples


def __random_explanation(x: float, y: float, identifier: int | None) -> str:
    explanations = [
        f"The smaller value between {x} and {y}",
        f"Find the smallest value between {x} and {y}",
        f"The minimum value between {x} and {y}",
        f"Calculate the smallest value between {x} and {y}",
        f"Finding smallest value for {x} and {y}",
        f"The value less than or equal to both {x} and {y}",
        f"The minimum value between {x} and {y}",
        f"Let's find the smallest value between {x} and {y}",
        f"Find the smallest value for {x} and {y}",
        f"Calculating the smallest value between {x} and {y}",
        f"The minimum value between {x} and {y}, find the answer",
        f"The smaller value between {x} and {y}, what is its value",
        f"Let's determine the smallest value between {x} and {y}",
        f"{x} and {y}, what is their smaller value",
        f"Finding the smallest value between {x} and {y}",
        f"The smaller value between {x} and {y}, what is its value",
        f"Find the smallest value between {x} and {y} and provide the result",
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
