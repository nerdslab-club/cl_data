import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_floor_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##floor({num})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"The floor of {f1}",
        f"Round down {f1} to the nearest whole number",
        f"The largest integer less than or equal to {f1}",
        f"The result of FLOOR({f1})",
        f"Find the floor of {f1}",
        f"Rounding down {f1}",
        f"{f1}, rounded down to the nearest integer",
        f"Find the FLOOR for {f1}",
        f"The largest integer less than or equal to {f1}, result is",
        f"Rounding {f1} down",
        f"The largest whole number not greater than {f1}, find the answer",
        f"Round {f1} down to the nearest integer",
        f"Rounding down operation for {f1}",
        f"Let's determine the floor of {f1}",
        f"{f1}, rounded down, what is the result",
        f"Find the floor of {f1} and provide the result",
        f"Rounded down value for {f1}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_floor_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
