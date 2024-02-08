import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_absolute_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        f1 = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(f1, (None if identifier is None else identifier+i)),
            "outputStr": f"##absolute({f1})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the absolute value of the number {f1}",
        f"Find the absolute value for the number {f1}",
        f"The result of taking the absolute value of {f1}",
        f"Performing the absolute operation on the number {f1}",
        f"The absolute value of the number {f1}",
        f"Let's find the absolute value of {f1}",
        f"Absolute value of {f1}, result is",
        f"Calculating the absolute value for {f1}",
        f"The absolute result after taking the absolute value of {f1}",
        f"Let's determine the absolute value of {f1}",
        f"The absolute value of {f1}",
        f"Absolute value of {f1}, what is the result",
        f"Absolute value of {f1} and provide the result",
        f"The result after taking the absolute value of {f1}",
        f"Let's find the result after taking the absolute value of {f1}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_absolute_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
