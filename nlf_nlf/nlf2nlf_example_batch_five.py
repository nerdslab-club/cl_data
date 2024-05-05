import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_five_example(count: int, identifier: int | None, seed: int,):
    examples = []
    for i in range(count):
        example = __get_batch_one_example_pair((None if identifier is None else identifier+i), seed)
        examples.append(
            {
                "inputStr": example[0],
                "outputStr": example[1]
            }
        )
    return examples


def __get_batch_one_example_pair(identifier: int | None, seed: int,):
    random_int_one = RandomValueGenerator.generate_random_integer(seed=seed)
    random_int_two = random_int_one + 3
    random_float = RandomValueGenerator.generate_random_float(seed=seed)

    examples = [
        (
            f"what is the closest integer to {random_float}",
            f"rounded value of {random_float} is ##round({random_float})",
        ),
        (
            f"absolute difference between {random_int_one} and {random_int_two}",
            f"absolute difference between {random_int_one} and {random_int_two} is ##absolute_difference({random_int_one},{random_int_two})"
        ),
        (
            f"greater value between {random_int_one} and {random_int_two}",
            f"greater value between {random_int_one} and {random_int_two} is ##greatest_value({random_int_one},{random_int_two})"
        ),
        (
            f"smaller value between {random_int_one} and {random_int_two}",
            f"smaller value between {random_int_one} and {random_int_two} is ##smallest_value({random_int_one},{random_int_two})"
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_five_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
