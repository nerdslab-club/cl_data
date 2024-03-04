import random

from cl_data.nlf_nlf.nlf2nlf_example_batch_eight import create_nlf2nlf_batch_eight_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_eighteen import create_nlf2nlf_batch_eighteen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_eleven import create_nlf2nlf_batch_eleven_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fifteen import create_nlf2nlf_batch_fifteen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_five import create_nlf2nlf_batch_five_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_four import create_nlf2nlf_batch_four_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourteen import create_nlf2nlf_batch_fourteen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourty import create_nlf2nlf_batch_fourty_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtyfive import create_nlf2nlf_batch_fourtyfive_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtyfour import create_nlf2nlf_batch_fourtyfour_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtyone import create_nlf2nlf_batch_fourtyone_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtyseven import create_nlf2nlf_batch_fourtyseven_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtysix import create_nlf2nlf_batch_fourtysix_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtythree import create_nlf2nlf_batch_fourtythree_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_fourtytwo import create_nlf2nlf_batch_fourtytwo_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_nine import create_nlf2nlf_batch_nine_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_nineteen import create_nlf2nlf_batch_nineteen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_one import create_nlf2nlf_batch_one_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_seven import create_nlf2nlf_batch_seven_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_seventeen import create_nlf2nlf_batch_seventeen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_six import create_nlf2nlf_batch_six_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_sixteen import create_nlf2nlf_batch_sixteen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_ten import create_nlf2nlf_batch_ten_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirteen import create_nlf2nlf_batch_thirteen_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirty import create_nlf2nlf_batch_thirty_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtyeight import create_nlf2nlf_batch_thirtyeight_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtyfive import create_nlf2nlf_batch_thirtyfive_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtyfour import create_nlf2nlf_batch_thirtyfour_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtynine import create_nlf2nlf_batch_thirtynine_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtyone import create_nlf2nlf_batch_thirtyone_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtyseven import create_nlf2nlf_batch_thirtyseven_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtysix import create_nlf2nlf_batch_thirtysix_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtythree import create_nlf2nlf_batch_thirtythree_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_thirtytwo import create_nlf2nlf_batch_thirtytwo_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_three import create_nlf2nlf_batch_three_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twelve import create_nlf2nlf_batch_twelve_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twenty import create_nlf2nlf_batch_twenty_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentyeight import create_nlf2nlf_batch_twentyeight_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentyfive import create_nlf2nlf_batch_twentyfive_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentyfour import create_nlf2nlf_batch_twentyfour_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentynine import create_nlf2nlf_batch_twentynine_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentyone import create_nlf2nlf_batch_twentyone_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentyseven import create_nlf2nlf_batch_twentyseven_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentysix import create_nlf2nlf_batch_twentysix_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentythree import create_nlf2nlf_batch_twentythree_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_twentytwo import create_nlf2nlf_batch_twentytwo_example
from cl_data.nlf_nlf.nlf2nlf_example_batch_two import create_nlf2nlf_batch_two_example
from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility

from cl_data.src.constants import Constants


class Nl2NlSamples:
    TASK_TYPE = TaskTypes.NL_TO_NL_TRANSLATION

    def __init__(self):
        self.nlf2nlf_example_generators = {}
        self.__set_nlf2nlf_example_generators()
        self.nlf2nlf_samples = []

    def get_length_of_sample_generators(self):
        return len(self.nlf2nlf_example_generators)

    def get_next_random_sample(self, batch_size: int, generator_index: int | None, identifier: int | None):
        if generator_index is not None:
            random_generator_index = generator_index
        else:
            random_generator_index = random.randint(
                0, len(self.nlf2nlf_example_generators) - 1
            )
        selected_generator = list(self.nlf2nlf_example_generators.values())[
            random_generator_index
        ]
        list_of_samples = selected_generator(batch_size, identifier)
        for my_dict in list_of_samples:
            my_dict[Constants.TASK_TYPE] = Nl2NlSamples.TASK_TYPE.value
        return list_of_samples

    def get_nlf2nlf_samples(self, each_example_count: int):
        self.__set_nlf2nlf_samples(each_example_count)
        return self.nlf2nlf_samples

    def __set_nlf2nlf_samples(self, each_example_count: int):
        for key, generator in self.nlf2nlf_example_generators.items():
            self.nlf2nlf_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), Nl2NlSamples.TASK_TYPE
                ),
            )

    def __set_nlf2nlf_example_generators(self):
        self.nlf2nlf_example_generators = {
            "batch_one": create_nlf2nlf_batch_one_example,
            "batch_two": create_nlf2nlf_batch_two_example,
            "batch_three": create_nlf2nlf_batch_three_example,
            "batch_four": create_nlf2nlf_batch_four_example,
            "batch_five": create_nlf2nlf_batch_five_example,
            "batch_six": create_nlf2nlf_batch_six_example,
            "batch_seven": create_nlf2nlf_batch_seven_example,
            "batch_eight": create_nlf2nlf_batch_eight_example,
            "batch_nine": create_nlf2nlf_batch_nine_example,
            "batch_ten": create_nlf2nlf_batch_ten_example,
            "batch_eleven": create_nlf2nlf_batch_eleven_example,
            "batch_twelve": create_nlf2nlf_batch_twelve_example,
            "batch_thirteen": create_nlf2nlf_batch_thirteen_example,
            "batch_fourteen": create_nlf2nlf_batch_fourteen_example,
            "batch_fifteen": create_nlf2nlf_batch_fifteen_example,
            "batch_sixteen": create_nlf2nlf_batch_sixteen_example,
            "batch_seventeen": create_nlf2nlf_batch_seventeen_example,
            "batch_eighteen": create_nlf2nlf_batch_eighteen_example,
            "batch_nineteen": create_nlf2nlf_batch_nineteen_example,
            "batch_twenty": create_nlf2nlf_batch_twenty_example,
            "batch_twentyone": create_nlf2nlf_batch_twentyone_example,
            "batch_twentytwo": create_nlf2nlf_batch_twentytwo_example,
            "batch_twentythree": create_nlf2nlf_batch_twentythree_example,
            "batch_twentyfour": create_nlf2nlf_batch_twentyfour_example,
            "batch_twentyfive": create_nlf2nlf_batch_twentyfive_example,
            "batch_twentysix": create_nlf2nlf_batch_twentysix_example,
            "batch_twentyseven": create_nlf2nlf_batch_twentyseven_example,
            "batch_twentyeight": create_nlf2nlf_batch_twentyeight_example,
            "batch_twentynine": create_nlf2nlf_batch_twentynine_example,
            "batch_thirty": create_nlf2nlf_batch_thirty_example,
            "batch_thirtyone": create_nlf2nlf_batch_thirtyone_example,
            "batch_thirtytwo": create_nlf2nlf_batch_thirtytwo_example,
            "batch_thirtythree": create_nlf2nlf_batch_thirtythree_example,
            "batch_thirtyfour": create_nlf2nlf_batch_thirtyfour_example,
            "batch_thirtyfive": create_nlf2nlf_batch_thirtyfive_example,
            "batch_thirtysix": create_nlf2nlf_batch_thirtysix_example,
            "batch_thirtyseven": create_nlf2nlf_batch_thirtyseven_example,
            "batch_thirtyeight": create_nlf2nlf_batch_thirtyeight_example,
            "batch_thirtynine": create_nlf2nlf_batch_thirtynine_example,
            "batch_fourty": create_nlf2nlf_batch_fourty_example,
            "batch_fourtyone": create_nlf2nlf_batch_fourtyone_example,
            "batch_fourtytwo": create_nlf2nlf_batch_fourtytwo_example,
            "batch_fourtythree": create_nlf2nlf_batch_fourtythree_example,
            "batch_fourtyfour": create_nlf2nlf_batch_fourtyfour_example,
            "batch_fourtyfive": create_nlf2nlf_batch_fourtyfive_example,
            "batch_fourtysix": create_nlf2nlf_batch_fourtysix_example,
            "batch_fourtyseven": create_nlf2nlf_batch_fourtyseven_example
        }

