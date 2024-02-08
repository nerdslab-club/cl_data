import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_greatest_value_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append({
            "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            "outputStr": f"##greatest_value({num1}, {num2})",
        })
    return examples


def __random_explanation(f1: float, f2: float, identifier: int | None) -> str:
    explanations = [
        f"The greater value between {f1} and {f2}",
        f"Find the greatest value between {f1} and {f2}",
        f"The larger value between {f1} and {f2}",
        f"Calculate the greatest value between {f1} and {f2}",
        f"Finding greatest value for {f1} and {f2}",
        f"The value greater than or equal to both {f1} and {f2}",
        f"The maximum value between {f1} and {f2}",
        f"greatest value calculation: {f1}, {f2}",
        f"Let's find the greatest value between {f1} and {f2}",
        f"Find the greatest value for {f1} and {f2}",
        f"The larger value between {f1} and {f2}, result is",
        f"Calculating the greatest value between {f1} and {f2}",
        f"Calculate greatest value({f1}, {f2})",
        f"Let's determine the greatest value between {f1} and {f2}",
        f"{f1} and {f2}, what is their larger value",
        f"Finding the greatest value between {f1} and {f2}",
        f"Find the greatest value between {f1} and {f2} and provide the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_greatest_value_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
