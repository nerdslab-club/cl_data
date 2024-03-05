

import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_sixtyeight_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        example = __get_batch_two_example_pair((None if identifier is None else identifier + i))
        examples.append({"inputStr": example[0], "outputStr": example[1]})
    return examples


def __get_batch_two_example_pair(identifier: int | None):
    random_degree = round(random.uniform(0, 2 * 3.14159), 1)

    examples = [
        (
            f"If you have an angle of {random_degree} degrees, what is the equivalent value in radians",
            f"The conversion of {random_degree} degrees to radians is ##degrees_to_radians({random_degree})",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_sixtyeight_example(2, None), TaskTypes.NL_TO_NL_TRANSLATION
        )

    )


