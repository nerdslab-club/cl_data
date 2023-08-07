import random

from src.constants import TaskTypes
from src.utility import Utility


class NlToNlSamples:
    TASK_TYPE = TaskTypes.NL_TO_NL_TRANSLATION.value

    def __init__(self):
        self.nlf2nlf_example_generators = {}
        self.__set_nlf2nlf_example_generators()
        self.nlf2nlf_samples = []

    def get_next_random_nlf2nlf_sample(self):
        random_generator_index = random.randint(0, len(self.nlf2nlf_example_generators)-1)
        selected_generator = list(self.nlf2nlf_example_generators.values())[random_generator_index]
        return Utility.create_sample_from_example(selected_generator(1), NlToNlSamples.TASK_TYPE)

    def get_nlf2nlf_samples(self, each_example_count: int):
        self.__set_nlf2nlf_samples(each_example_count)
        return self.nlf2nlf_samples

    def __set_nlf2nlf_samples(self, each_example_count: int):
        for key, generator in self.nlf2nlf_example_generators.items():
            self.nlf2nlf_samples.extend(
                Utility.create_sample_from_example(generator(each_example_count), NlToNlSamples.TASK_TYPE),
            )

    def __set_nlf2nlf_example_generators(self):
        self.f2f_example_generators = {}
