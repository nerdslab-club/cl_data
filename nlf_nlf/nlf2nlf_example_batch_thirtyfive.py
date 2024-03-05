
import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_thirtyfive_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        example = __get_batch_one_example_pair((None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": example[0],
                "outputStr": example[1]
            }
        )
    return examples


def __get_batch_one_example_pair(identifier: int | None):
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()

    examples = [
        (
            f"If you consume {random_int_four} out of {random_int_one} cookies how many cookies do you have left",
            f"You have ##subtraction({random_int_one},{random_int_four}) cookies remaining",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_thirtyfive_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
