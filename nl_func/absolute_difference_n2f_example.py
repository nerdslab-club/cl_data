import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_absolute_difference_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        f1 = RandomValueGenerator.generate_random_float()
        f2 = RandomValueGenerator.generate_random_float()
        examples.append({
            "inputStr": __random_explanation(f1, f2, (None if identifier is None else identifier+i)),
            "outputStr": f"##absolute_difference({f1}, {f2})",
        })
    return examples


def __random_explanation(f1: float, f2: float, identifier: int | None) -> str:
    explanations = [
        f"The absolute difference between {f1} and {f2}",
        f"Absolute difference({f1}, {f2})",
        f"Find the absolute difference of {f1} and {f2}",
        f"The result of absolute difference({f1}, {f2})",
        f"The positive difference between {f1} and {f2}",
        f"Calculate the absolute difference of {f1} and {f2}",
        f"Finding absolute difference for {f1} and {f2}",
        f"The difference between {f1} and {f2}, ignoring direction",
        f"The absolute value of the difference between {f1} and {f2}",
        f"Absolute difference calculation: {f1}, {f2}",
        f"The positive difference between {f1} and {f2}, what is it",
        f"The positive difference between {f1} and {f2}, what does it give",
        f"Let's find the absolute difference of {f1} and {f2}",
        f"Find the absolute difference for {f1} and {f2}",
        f"The positive difference between {f1} and {f2}, result is",
        f"Calculating the absolute difference between {f1} and {f2}",
        f"{f1} and {f2}, what is their absolute difference",
        f"The absolute value of the positive difference between {f1} and {f2}",
        f"The non-negative difference between {f1} and {f2}",
        f"Absolute difference of {f1} and {f2}, find the answer",
        f"Calculate absolute difference({f1}, {f2})",
        f"The absolute value of the difference between {f1} and {f2}",
        f"Let's determine the absolute difference of {f1} and {f2}",
        f"{f1} and {f2}, what is their positive difference",
        f"Finding the absolute difference between {f1} and {f2}",
        f"The positive difference between {f1} and {f2}, what is its value",
        f"Find the absolute difference of {f1} and {f2} and provide the result",
        f"Absolute difference({f1}, {f2}), what does it yield",
        f"The absolute difference between {f1} and {f2}, ignoring direction",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_absolute_difference_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
