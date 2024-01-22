import random

from cl_data.nlf_nlf.nlf2nlf_example_batch_one import create_nlf2nlf_batch_one_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_two import create_nlf2nlf_batch_two_example
from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility

from cl_data.src.constants import Constants


class NlToNlSamples:
    TASK_TYPE = TaskTypes.NL_TO_NL_TRANSLATION

    def __init__(self):
        self.nlf2nlf_example_generators = {}
        self.__set_nlf2nlf_example_generators()
        self.nlf2nlf_samples = []

    def get_length_of_sample_generators(self):
        return len(self.nlf2nlf_example_generators)

    def get_next_random_sample(self, count: int, generator_index: int | None, identifier: int | None):
        if generator_index is not None:
            random_generator_index = generator_index
        else:
            random_generator_index = random.randint(
                0, len(self.nlf2nlf_example_generators) - 1
            )
        selected_generator = list(self.nlf2nlf_example_generators.values())[
            random_generator_index
        ]
        list_of_samples = selected_generator(count, identifier)
        for my_dict in list_of_samples:
            my_dict[Constants.TASK_TYPE] = NlToNlSamples.TASK_TYPE.value
        return list_of_samples

    def get_nlf2nlf_samples(self, each_example_count: int):
        self.__set_nlf2nlf_samples(each_example_count)
        return self.nlf2nlf_samples

    def __set_nlf2nlf_samples(self, each_example_count: int):
        for key, generator in self.nlf2nlf_example_generators.items():
            self.nlf2nlf_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), NlToNlSamples.TASK_TYPE
                ),
            )

    def __set_nlf2nlf_example_generators(self):
        self.nlf2nlf_example_generators = {
            "batch_one": create_nlf2nlf_batch_one_example,
            "batch_two": create_nlf2nlf_batch_two_example,
        }
