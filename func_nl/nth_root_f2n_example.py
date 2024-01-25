import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_nth_root_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = random.uniform(0.0, 1000.0)
        m = random.randint(1, 10)
        examples.append(
            {
                "inputStr": f"##nth_root({x}, {m})",
                "outputStr": __random_explanation_nth_root(x, m, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_nth_root(x: float, m: int, identifier: int | None) -> str:
    explanations = [
        f"The {m}th root of the number {x}",
        f"nth_root({x}, {m})",
        f"The result of finding the {m}th root of {x}",
        f"Calculation: nth_root({x}, {m})",
        f"The value obtained by taking the {m}th root of {x}",
        f"The outcome of calculating the {m}th root of {x}",
        f"The {m}th root value of {x}",
        f"The result of finding the {m}th root of the number {x}",
        f"The computed result of finding the {m}th root of {x}",
        f"The value of {x} under the {m}th root",
        f"The {m}th root of the quantity {x}",
        f"The {m}th root result of the number {x}",
        f"The outcome of evaluating nth_root({x}, {m}) is",
        f"The value calculated by finding the {m}th root of {x} is",
        f"The result of evaluating nth_root({x}, {m}) is",
        f"The {m}th root of the number {x} is",
        f"The computed {m}th root of the number {x} is",
        f"The value obtained by finding the {m}th root of {x} is",
        f"The outcome of finding the {m}th root value of {x} is",
        f"The result of finding the {m}th root among {x} is",
        f"The calculated outcome of evaluating nth_root({x}, {m}) is",
        f"The value of the {m}th root of {x} is",
        f"The computed value of nth_root({x}, {m}) is",
        f"The calculated result of finding the {m}th root of {x} is",
        f"The {m}th root value of {x} is",
        f"The result of finding the {m}th root of the number {x} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_nth_root_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
