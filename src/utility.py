import random
from enum import Enum
from typing import Type

from io_parser.io_parser import IoParser
from src.constants import TaskTypes, PretrainTasks, SpecialTokens


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def create_sample_from_example(examples: list, task_type: Type[Enum]) -> list:
        for i, example in enumerate(examples):
            input_list = IoParser().create_value_list_from_input(example.get("inputStr"))
            output_list = IoParser().create_value_list_from_input(example.get("outputStr"))
            example["inputMap"] = Utility.create_io_map_from_io_tuple(input_list)
            example["outputMap"] = Utility.create_io_map_from_io_tuple(output_list)
            example["taskType"] = task_type.value
        return examples

    @staticmethod
    def create_io_map_from_io_tuple(input_list: list) -> list:
        result_list = []
        for idx, (token, category_dict) in enumerate(input_list):
            result_list.append({"token": token, "category": category_dict, "position": idx})
        return result_list

    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(" ", "")

    @staticmethod
    def create_masked_input_output(raw_input, mask_prob=0.15):
        # Tokenize the raw input string
        tokens = raw_input.split()  # You can use a more sophisticated tokenizer here

        input_tokens = []
        output_tokens = []

        for token in tokens:
            # Randomly decide whether to mask the token
            if random.random() < mask_prob:
                input_tokens.append(SpecialTokens.MASK_TOKEN.value)  # Mask the token in the input
                output_tokens.append(token)  # Output should predict the original token
            else:
                input_tokens.append(token)  # Keep the token as it is in the input
                output_tokens.append(token)  # Output should predict the same token

        # Convert the token lists back to strings
        input_string = " ".join(input_tokens)
        output_string = " ".join(output_tokens)

        return {
            "inputStr": input_string,
            "outputStr": output_string
        }

    @staticmethod
    def create_next_word_input_output(raw_input: str, max_seq_length=1000):
        # Tokenize the raw input string
        tokens = raw_input.split()  # You can use a more sophisticated tokenizer here

        # Ensure the sequence length does not exceed the maximum
        tokens = tokens[:max_seq_length - 1]  # Leave space for the [SEP] token

        input_tokens = tokens
        output_tokens = tokens[8:] + [SpecialTokens.SEPARATOR_TOKEN.value]  # Shift tokens by 1 position

        # Convert the token lists back to strings
        input_string = " ".join(input_tokens)
        output_string = " ".join(output_tokens)

        return input_string, output_string




if __name__ == "__main__":
    # raw_input = "This is a sample input for testing masked token prediction."
    # masked_data = Utility.create_masked_input_output(raw_input)
    # print("Input:", masked_data)
    #
    # sample = Utility.create_sample_from_example([masked_data], PretrainTasks.MASKED_TOKEN_PREDICTION)
    # print(sample)

    raw_input = "This is a sample input for testing masked token prediction. This is an example sentence for testing next word prediction."
    input_string, output_string = Utility.create_next_word_input_output(raw_input)
    print("Input:", input_string)
    print("Output:", output_string)
