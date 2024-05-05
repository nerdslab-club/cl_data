

import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_eighty_example(count: int, identifier: int | None, seed: int,):
    examples = []
    for i in range(count):
        example = __get_batch_two_example_pair((None if identifier is None else identifier + i), seed)
        examples.append({"inputStr": example[0], "outputStr": example[1]})
    return examples


def __get_batch_two_example_pair(identifier: int | None, seed: int,):
    random_int_four = RandomValueGenerator.generate_random_integer(seed=seed)
    random_float = RandomValueGenerator.generate_random_float(seed=seed)

    examples = [
        (
            f"cube root of {random_int_four}",
            f"cube root of {random_int_four} is ##cube_root({random_int_four})"
        ),
        (
            f"What is the cube of {random_float}",
            f"cube of {random_float} is ##cube({random_float})"
        ),
        (
            f"What is the absolute value of {random_float}",
            f"absolute value of {random_float} is ##absolute({random_float})"
        ),
        (
            f"What is the square of {random_float}",
            f"square of {random_float} is ##square({random_float})"
        )

    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_eighty_example(2, None), TaskTypes.NL_TO_NL_TRANSLATION
        )

    )


