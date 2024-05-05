import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_square_root_example(count: int, identifier: int | None, seed: int):
    examples = []
    for i in range(count):
        number = RandomValueGenerator.generate_random_float(seed=seed)
        examples.append(
            {
                "inputStr": f"##square_root({number})",
                "outputStr": __random_explanation_sqrt(
                    number,
                    (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_sqrt(f: float, identifier: int | None) -> str:
    explanations = [
        f"square root of {f}",
        f"radical of {f}",
        f"result of taking the square root of {f}",
        f"√ {f}",

        f"The square root of {f} is",
        f"The value of √ {f}",
        f"The square root of {f} gives",
        f"The square root of {f} is approximately",
        f"The principal square root of {f}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_square_root_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
