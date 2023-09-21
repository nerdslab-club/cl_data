import random

from pretrain_data.pretrain_example_batch_eight import get_batch_eight_example_paragraph
from pretrain_data.pretrain_example_batch_eleven import get_batch_eleven_example_paragraph
from pretrain_data.pretrain_example_batch_five import get_batch_five_example_paragraph
from pretrain_data.pretrain_example_batch_four import get_batch_four_example_paragraph
from pretrain_data.pretrain_example_batch_nine import get_batch_nine_example_paragraph
from pretrain_data.pretrain_example_batch_seven import get_batch_seven_example_paragraph
from pretrain_data.pretrain_example_batch_six import get_batch_six_example_paragraph
from pretrain_data.pretrain_example_batch_ten import get_batch_ten_example_paragraph
from pretrain_data.pretrain_example_batch_three import get_batch_three_example_paragraph
from pretrain_data.pretrain_example_batch_two import get_batch_two_example_paragraph
from pretrain_data.pretrain_example_batch_one import get_batch_one_example_paragraph
from src.constants import PretrainTasks
from src.utility import Utility


class MaskedTokenSamplesGenerator:
    TASK_TYPE = PretrainTasks.MASKED_TOKEN_PREDICTION

    def __init__(self):
        self.masked_token_example_generators = {}
        self.__set_masked_token_example_generators()
        self.__masked_token_samples = []

    def get_next_random_masked_token_sample(self):
        random_generator_index = random.randint(
            0, len(self.masked_token_example_generators) - 1
        )
        selected_generator = list(self.masked_token_example_generators.values())[
            random_generator_index
        ]
        return Utility.create_sample_from_example(
            selected_generator(1), MaskedTokenSamplesGenerator.TASK_TYPE
        )

    def get_masked_token_samples(self, each_example_count: int):
        self.__set_masked_token_samples(each_example_count)
        return self.__masked_token_samples

    def __set_masked_token_samples(self, each_example_count: int):
        for key, generator in self.masked_token_example_generators.items():
            self.__masked_token_samples.extend(
                Utility.create_sample_from_example(
                    MaskedTokenSamplesGenerator.create_masked_token_batches(generator(), each_example_count),
                    MaskedTokenSamplesGenerator.TASK_TYPE,
                ),
            )

    @staticmethod
    def create_masked_token_batches(
            paragraphs: list[str],
            count: int,
            nlp=Utility.get_spacy_nlp(),
    ):
        examples = []
        for _ in range(count):
            for paragraph in paragraphs:
                # Removes any space after any function and its closing bracket
                paragraph = Utility.split_string_custom(paragraph)
                masked_data = Utility.create_masked_input_output_example(paragraph, nlp)
                examples.extend(masked_data)
        return examples

    def __set_masked_token_example_generators(self):
        self.masked_token_example_generators = {
            "batch_one": get_batch_one_example_paragraph,
            "batch_two": get_batch_two_example_paragraph,
            "batch_three": get_batch_three_example_paragraph,
            "batch_four": get_batch_four_example_paragraph,
            "batch_five": get_batch_five_example_paragraph,
            "batch_six": get_batch_six_example_paragraph,
            "batch_seven": get_batch_seven_example_paragraph,
            "batch_eight": get_batch_eight_example_paragraph,
            "batch_nine": get_batch_nine_example_paragraph,
            "batch_ten": get_batch_ten_example_paragraph,
            "batch_eleven": get_batch_eleven_example_paragraph,
        }
