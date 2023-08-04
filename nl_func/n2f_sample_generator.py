import random

from nl_func.addition_n2f_example import create_n2f_addition_example
from nl_func.division_n2f_example import create_n2f_division_example
from nl_func.multiplication_n2f_example import create_n2f_multiplication_example
from nl_func.subtraction_n2f_example import create_n2f_subtraction_example
from src.constants import TaskTypes
from src.utility import Utility


class N2FSamples:
    TASK_TYPE = TaskTypes.NL_TO_FUNC_TRANSLATION

    def __init__(self):
        self.n2f_example_generators = {}
        self.__set_n2f_example_generators()

        self.n2f_samples = []

    def get_next_random_n2f_sample(self):
        random_generator_index = random.randint(0, len(self.n2f_example_generators)-1)
        selected_generator = list(self.n2f_example_generators.values())[random_generator_index]
        return Utility.create_sample_from_example(selected_generator(1), N2FSamples.TASK_TYPE)

    def get_n2f_samples(self, each_example_count: int):
        self.__set_n2f_samples(each_example_count)
        return self.n2f_samples

    def __set_n2f_samples(self, each_example_count: int):
        for key, generator in self.n2f_example_generators.items():
            self.n2f_samples.extend(
                Utility.create_sample_from_example(generator(each_example_count), N2FSamples.TASK_TYPE),
            )

    def __set_n2f_example_generators(self):
        self.n2f_example_generators = {
            "addition": create_n2f_addition_example,
            "subtraction": create_n2f_subtraction_example,
            "multiplication": create_n2f_multiplication_example,
            "division": create_n2f_division_example,
        }
