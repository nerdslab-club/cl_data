
import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_fourtysix_example(count: int, identifier: int | None):
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
    random_list = Utility.remove_spaces(
        str(RandomValueGenerator.generate_random_list())
    )
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()

    examples = [
        (
            f"If you divide {random_int_three} by {random_int_one}, what is the quotient",
            f"The quotient after dividing {random_int_three} by {random_int_one} is ##division({random_int_three},{random_int_one})",
        ),
        (
            f"If you have {random_int_two} boxes, and each box contains {random_int_four} pencils, how many pencils are there in total",
            f"The total number of pencils is ##multiplication({random_int_two},{random_int_four})",
        ),
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_fourtysix_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
