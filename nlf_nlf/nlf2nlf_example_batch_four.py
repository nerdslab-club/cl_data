import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_four_example(count: int, identifier: int | None, seed: int,):
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
    random_int_two = random_int_one + 7
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer(seed=seed)

    examples = [
        (
            f"{random_int_two} pizzas shared equally among {random_int_one} friends",
            f"each friend will receive ##division({random_int_two},{random_int_one}) pizzas",
        ),
        (
            f"taking away {random_int_one} from {random_int_three}",
            f"outcome of subtracting {random_int_one} from {random_int_three} is ##subtraction({random_int_three},{random_int_one})",
        ),
        (
            f"{random_int_three} divided by {random_int_one} what is the quotient",
            f"quotient after dividing {random_int_three} by {random_int_one} is ##division({random_int_three},{random_int_one})",
        ),
        (
            f"{random_int_one} boxes with {random_int_two} pencils",
            f"##multiplication({random_int_one},{random_int_two}) pencils in total",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_four_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
