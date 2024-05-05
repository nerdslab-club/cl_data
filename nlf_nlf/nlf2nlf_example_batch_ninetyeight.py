

import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_ninetyeight_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        example = __get_batch_two_example_pair((None if identifier is None else identifier + i))
        examples.append({"inputStr": example[0], "outputStr": example[1]})
    return examples


def __get_batch_two_example_pair(identifier: int | None):
    random_list = RandomValueGenerator.generate_random_list()
    lst_str = " , ".join(str(num) for num in random_list)
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()

    examples = [
        (
            f"What is the maximum value in the numbers {lst_str}",
            f"The maximum value in the numbers {lst_str} is ##max_value([{random_list}])"
        ),
        (
            f"What is the minimum value in the numbers {lst_str}",
            f"The minimum value in the numbers {lst_str} is ##min_value([{random_list}])"
        ),
        (
            f"What is the sum of the numbers {lst_str}",
            f"The sum of {lst_str} is ##sum({random_list})"
        ),
        (
            f"What is the length of the vector {lst_str}",
            f"The length of the vector {lst_str} is ##length({random_list})"
        ),
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_ninetyeight_example(2, None), TaskTypes.NL_TO_NL_TRANSLATION
        )

    )


