import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_seven_example(count: int, identifier: int | None, seed: int,):
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
    random_int_two = random_int_one + 8
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer(seed=seed)
    random_float = RandomValueGenerator.generate_random_float(seed=seed)

    examples = [
        (
            f"area of a circle with radius {random_float}",
            f"area of a circle with radius {random_float} is ##circle_area({random_float})"
        ),
        (
            f"permutation of {random_int_two} items taken {random_int_one} at a time",
            f"permutation of {random_int_two} items taken {random_int_one} at a time is ##permutation({random_int_two},{random_int_one})"
        ),
        (
            f"combination of {random_int_three} items taken {random_int_one} at a time",
            f"combination of {random_int_three} items taken {random_int_one} at a time is ##combination({random_int_three},{random_int_one})"
        ),
        (
            f"What is the sigmoid value for {random_float}",
            f"sigmoid value for {random_float} is ##sigmoid({random_float})"
        ),
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_seven_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
