import random

from pretrain_data.pretrain_example_batch_one import create_next_token_batch_one_example
from pretrain_data.pretrain_example_batch_two import create_next_token_batch_two_example
from pretrain_data.pretrain_example_batch_three import create_next_token_batch_three_example
from pretrain_data.pretrain_example_batch_four import create_next_token_batch_four_example
from pretrain_data.pretrain_example_batch_five import create_next_token_batch_five_example
from pretrain_data.pretrain_example_batch_six import create_next_token_batch_six_example
from pretrain_data.pretrain_example_batch_seven import create_next_token_batch_seven_example
from pretrain_data.pretrain_example_batch_eight import create_next_token_batch_eight_example
from pretrain_data.pretrain_example_batch_nine import create_next_token_batch_nine_example
from pretrain_data.pretrain_example_batch_ten import create_next_token_batch_ten_example
from src.constants import PretrainTasks
from src.utility import Utility


class NextTokenSamples:
    TASK_TYPE = PretrainTasks.MASKED_TOKEN_PREDICTION.value

    def __init__(self):
        self.next_token_example_generators = {}
        self.__set_next_token_example_generators()
        self.next_token_samples = []

    def get_next_random_next_token_sample(self):
        random_generator_index = random.randint(
            0, len(self.next_token_example_generators) - 1
        )
        selected_generator = list(self.next_token_example_generators.values())[
            random_generator_index
        ]
        return Utility.create_sample_from_example(
            selected_generator(1), NextTokenSamples.TASK_TYPE
        )

    def get_next_token_samples(self, each_example_count: int):
        self.__set_next_token_samples(each_example_count)
        return self.next_token_samples

    def __set_next_token_samples(self, each_example_count: int):
        for key, generator in self.next_token_example_generators.items():
            self.next_token_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), NextTokenSamples.TASK_TYPE
                ),
            )

    def __set_next_token_example_generators(self):
        self.f2f_example_generators = {
            "batch_one": create_next_token_batch_one_example,
            "batch_two": create_next_token_batch_two_example,
            "batch_three": create_next_token_batch_three_example,
            "batch_four": create_next_token_batch_four_example,
            "batch_five": create_next_token_batch_five_example,
            "batch_six": create_next_token_batch_six_example,
            "batch_seven": create_next_token_batch_seven_example,
            "batch_eight": create_next_token_batch_eight_example,
            "batch_nine": create_next_token_batch_nine_example,
            "batch_ten": create_next_token_batch_ten_example,
        }
