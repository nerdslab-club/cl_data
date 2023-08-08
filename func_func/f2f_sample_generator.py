import random

from func_func.avg_f2f_example import create_f2f_average_example
from func_func.combination_f2f_example import create_f2f_combination_example
from func_func.permutation_f2f_example import create_f2f_permutation_example
from src.constants import TaskTypes
from src.utility import Utility


class F2FSamples:
    TASK_TYPE = TaskTypes.FUNC_TO_FUNC_TRANSLATION.value

    def __init__(self):
        self.f2f_example_generators = {}
        self.__set_f2f_example_generators()
        self.f2f_samples = []

    def get_next_random_f2f_sample(self):
        random_generator_index = random.randint(0, len(self.f2f_example_generators) - 1)
        selected_generator = list(self.f2f_example_generators.values())[
            random_generator_index
        ]
        return Utility.create_sample_from_example(
            selected_generator(1), F2FSamples.TASK_TYPE
        )

    def get_f2f_samples(self, each_example_count: int):
        self.__set_f2f_samples(each_example_count)
        return self.f2f_samples

    def __set_f2f_samples(self, each_example_count: int):
        for key, generator in self.f2f_example_generators.items():
            self.f2f_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), F2FSamples.TASK_TYPE
                ),
            )

    def __set_f2f_example_generators(self):
        self.f2f_example_generators = {
            "average": create_f2f_average_example,
            "subtraction": create_f2f_permutation_example,
            "multiplication": create_f2f_combination_example,
        }
