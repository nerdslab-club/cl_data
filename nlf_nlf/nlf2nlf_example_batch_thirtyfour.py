import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_thirtyfour_example(count: int, identifier: int | None):
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
            f"How many do you get when you add {random_int_two} to {random_int_three}",
            f"The sum is ##addition({random_int_two},{random_int_three})",
        ),
        (
            f"If you consume {random_int_four} out of {random_int_one} cookies, how many cookies do you have left",
            f"You have ##subtraction({random_int_one},{random_int_four}) cookies remaining",
        ),
        (
            f"If you evenly distribute {random_int_three} candies among {random_int_one} children, how many candies does each child receive",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies",
        ),
        (
            f"If you have {random_int_two} boxes, and each box holds {random_int_four} chocolates, how many chocolates do you have in total",
            f"The total number of chocolates is ##multiplication({random_int_two},{random_int_four})",
        ),
        (
            f"When you increase {random_float} by {random_int_three}, what is the new value",
            f"The new value after increasing {random_float} by {random_int_three} is ##addition({random_float},{random_int_three})",
        ),
        (
            f"If you remove {random_int_one} from {random_int_three}, what is the result",
            f"The result after subtracting {random_int_one} from {random_int_three} is ##subtraction({random_int_three},{random_int_one})",
        ),
        (
            f"If you divide {random_int_two} by {random_int_four}, what is the quotient",
            f"The quotient after dividing {random_int_two} by {random_int_four} is ##division({random_int_two},{random_int_four})",
        ),
        (
            f"Suppose you have {random_int_one} teams, and each team has {random_int_three} members How many members are there in total",
            f"The total number of members is ##multiplication({random_int_one},{random_int_three})",
        ),
        (
            f"If you add {random_int_two} to {random_float}, what is the sum",
            f"The sum of {random_int_two} and {random_float} is ##addition({random_int_two},{random_float})",
        ),
        (
            f"When you subtract {random_int_four} from {random_int_three}, what is the outcome",
            f"The outcome after subtracting {random_int_four} from {random_int_three} is ##subtraction({random_int_three},{random_int_four})",
        ),
        (
            f"If you distribute {random_int_three} candies evenly among {random_int_one} children, how many candies does each child get",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies",
        ),
        (
            f"What do you get when you add {random_int_one} to {random_int_four}",
            f"The result is ##addition({random_int_one},{random_int_four})",
        ),
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
            create_nlf2nlf_batch_thirtyfour_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
