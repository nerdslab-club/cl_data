

import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_sixty_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        example = __get_batch_two_example_pair((None if identifier is None else identifier + i))
        examples.append({"inputStr": example[0], "outputStr": example[1]})
    return examples


def __get_batch_two_example_pair(identifier: int | None):
    random_arc_int = RandomValueGenerator.generate_random_integer(-1, 1)

    examples = [
        (
            f"If you want to find the arcsine of a random value, what is the arcsine value",
            f"The arcsine value of the random value is ##arcsine({random_arc_int})",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_sixty_example(2, None), TaskTypes.NL_TO_NL_TRANSLATION
        )

    )


