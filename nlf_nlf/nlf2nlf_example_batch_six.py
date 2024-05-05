import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_six_example(count: int, identifier: int | None, seed: int,):
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
    random_int_two = random_int_one + 6
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer(seed=seed)

    examples = [
        (
            f"What is the total when you add {random_int_two} and {random_int_three}",
            f"The answer is ##addition({random_int_two},{random_int_three})",
        ),
        (
            f"If you have {random_int_two} cookies and you eat {random_int_one} of them how many are left",
            f"##subtraction({random_int_two},{random_int_one}) cookies remaining",
        ),
        (
            f"What is the factorial of {random_int_one}",
            f"The factorial of {random_int_one} is ##factorial({random_int_one})"
        ),
        (
            f"Distributing {random_int_three} candies among {random_int_one} children",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_six_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
