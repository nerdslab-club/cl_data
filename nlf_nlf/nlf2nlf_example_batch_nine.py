import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_nlf2nlf_batch_nine_example(count: int, identifier: int | None, seed: int,):
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
    random_int_two = random_int_one + 10
    random_int_four = RandomValueGenerator.generate_random_integer(seed=seed)

    examples = [
        (
            f"{random_int_two} apples packed into boxes of {random_int_one} each how many will be left unpacked",
            f"unpacked apples is ##modulus({random_int_two},{random_int_one})",
        ),
        (
            f"sine of angle {random_int_one} degrees",
            f"sine of angle {random_int_one} is ##sine({random_int_one})",
        ),
        (
            f"cosine of angle {random_int_two} degrees",
            f"cosine value angle {random_int_two} is ##cosine({random_int_two})",
        ),
        (
            f"tangent of angle {random_int_four} degrees",
            f"tangent value of the angle {random_int_four} is ##tangent({random_int_four})",
        )
    ]
    if identifier is not None:
        return examples[identifier % len(examples)]
    else:
        return random.choice(examples)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_nlf2nlf_batch_nine_example(2, 34), TaskTypes.NL_TO_NL_TRANSLATION
        )
    )
