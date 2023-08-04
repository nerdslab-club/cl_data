import random

from func_nl.addition_func_to_nl_example import create_f2n_addition_example
from func_nl.division_func_to_nl_example import create_f2n_division_example
from func_nl.multiplication_func_to_nl_example import create_f2n_multiplication_example
from func_nl.subtraction_func_to_nl_example import create_f2n_subtraction_example
from src.constants import TaskTypes
from src.utility import Utility


class F2NSamples:
    TASK_TYPE = TaskTypes.FUNC_TO_NL_TRANSLATION.value

    def __init__(self):
        self.f2n_example_generators = {}
        self.__set_f2n_example_generators()
        self.f2n_samples = []

    def get_next_random_f2n_sample(self):
        random_generator_index = random.randint(0, len(self.f2n_example_generators)-1)
        selected_generator = list(self.f2n_example_generators.values())[random_generator_index]
        return Utility.create_sample_from_example(selected_generator(1), TaskTypes.FUNC_TO_NL_TRANSLATION)

    def get_f2n_samples(self):
        self.__set_f2n_samples()
        return self.f2n_samples

    def __set_f2n_samples(self):
        for key, generator in self.f2n_example_generators.items():
            self.f2n_samples.extend(
                Utility.create_sample_from_example(generator(2), TaskTypes.FUNC_TO_NL_TRANSLATION),
            )

    def __set_f2n_example_generators(self):
        self.f2n_example_generators = {
            "addition": create_f2n_addition_example,
            "subtraction": create_f2n_subtraction_example,
            "multiplication": create_f2n_multiplication_example,
            "division": create_f2n_division_example,
        }


