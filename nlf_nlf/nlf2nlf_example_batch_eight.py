import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_eight_example(count: int, identifier: int | None, seed: int,):
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
    random_int_two = random_int_one + 12
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer(seed=seed)
    random_float = RandomValueGenerator.generate_random_float(seed=seed)

    examples = [
        (
            f"greatest common divisor of {random_int_one} and {random_int_two}",
            f"greatest common divisor of {random_int_one} and {random_int_two} is ##gcd({random_int_one},{random_int_two})",
        ),
        (
            f"least common multiple of {random_int_two} and {random_int_three}",
            f"least common multiple of {random_int_two} and {random_int_three} is ##lcm({random_int_two},{random_int_three})",
        ),
        (
            f"square root of {random_int_two}",
            f"square root of {random_int_two} is ##isqrt({random_int_two})",
        ),
        (
            f"smallest integer greater than or equal to {random_float}",
            f"ceiling of {random_float} is ##ceil({random_float})",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_eight_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
