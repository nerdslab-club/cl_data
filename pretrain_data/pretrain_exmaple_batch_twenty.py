import random

from src.constants import PretrainTasks
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def get_batch_twenty_example_paragraph():
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()
    random_bool = RandomValueGenerator.generate_random_boolean()
    random_list = Utility.remove_spaces(
        str(RandomValueGenerator.generate_random_list())
    )
    random_binary_str = RandomValueGenerator.generate_random_binary_string()

    examples = [
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
        [

        ],
    ]
    return random.choice(examples)


if __name__ == "__main__":
    from masked_token_sample_generator import MaskedTokenSamplesGenerator

    masked_example = MaskedTokenSamplesGenerator.create_masked_token_batches(
        get_batch_twenty_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        masked_example,
        PretrainTasks.MASKED_TOKEN_PREDICTION,
    )
    print(sample)

    from next_token_sample_generator import NextTokenSamplesGenerator

    next_token_example = NextTokenSamplesGenerator.create_next_token_batches(
        get_batch_twenty_example_paragraph(),
    )
    sample = Utility.create_sample_from_example(
        next_token_example,
        PretrainTasks.NEXT_TOKEN_PREDICTION
    )
    print(sample)
