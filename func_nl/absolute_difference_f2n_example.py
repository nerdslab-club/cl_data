import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_absolute_difference_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        y = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i+1))
        examples.append(
            {
                "inputStr": f"##absolute_difference({x}, {y})",
                "outputStr": __random_explanation_absolute_difference(x, y, (None if identifier is None else identifier+i)),
            }
        )
    return examples


def __random_explanation_absolute_difference(x: float, y: float, identifier: int | None) -> str:
    explanations = [
        f"The absolute difference between {x} and {y}",
        f"The positive value of the difference between {x} and {y}",
        f"The distance between {x} and {y}",
        f"The non-negative value of the difference between {x} and {y}",
        f"The absolute value of the subtraction of {x} from {y}",
        f"The result of calculating the absolute difference between {x} and {y}",
        f"The absolute positive value of the subtraction of {y} from {x}",
        f"The value of the absolute difference between {x} and {y}",
        f"The result of finding the absolute difference between {x} and {y}",
        f"The positive distance between {x} and {y}",
        f"The absolute value of the difference of {x} minus {y}",
        f"The magnitude of the subtraction of {x} from {y} is",
        f"The absolute value of the difference between {x} and {y} is",
        f"The value of the absolute positive difference between {x} and {y}",
        f"The absolute magnitude of the difference between {x} and {y}",
        f"The result of finding the non-negative difference between {x} and {y}",
        f"The value of the absolute difference of {x} minus {y}",
        f"The positive absolute difference between {x} and {y} is",
        f"The result of calculating absolute_difference({x}, {y}) is",
        f"The magnitude of the absolute difference between {x} and {y} is",
        f"The absolute result of {x} minus {y} is",
        f"The positive absolute value of the difference between {x} and {y} is",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_absolute_difference_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
