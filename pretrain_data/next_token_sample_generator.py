import random

from pretrain_data.pretrain_example_batch_one import create_next_token_batch_one_example
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
        }
