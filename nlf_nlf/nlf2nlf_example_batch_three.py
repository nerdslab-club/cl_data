import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_three_example(count: int, identifier: int | None, seed: int,):
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
    random_int_two = random_int_one + 9
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer(seed=seed)
    random_float = RandomValueGenerator.generate_random_float(seed=seed)

    examples = [
        (
            f"rectified linear unit of {random_float}",
            f"rectified linear unit of {random_float} is ##relu({random_float})"
        ),
        (
            f"Is {random_int_one} a perfect cube",
            f"{random_int_one} perfect cube ##is_perfect_cube({random_int_one})"
        ),
        (
            f"What are the prime factors of {random_int_three}",
            f"prime factors of {random_int_three} are ##prime_factors({random_int_three})"
        ),
        (
            f"Is {random_int_one} a perfect square",
            f"{random_int_one} perfect square ##is_perfect_square({random_int_one})"
        )

    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_three_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
