import random
from enum import Enum
from typing import Type

import spacy

from io_parser.io_parser import IoParser
from src.constants import SpecialTokens, FunctionPrefix


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def get_spacy_nlp():
        return spacy.load("en_core_web_sm")

    @staticmethod
    def create_sample_from_example(examples: list, task_type: Type[Enum]) -> list:
        for i, example in enumerate(examples):
            input_list = IoParser().create_value_list_from_input(
                example.get("inputStr")
            )
            output_list = IoParser().create_value_list_from_input(
                example.get("outputStr")
            )
            example["inputMap"] = Utility.create_io_map_from_io_tuple(input_list)
            example["outputMap"] = Utility.create_io_map_from_io_tuple(output_list)
            example["taskType"] = task_type.value
        return examples

    @staticmethod
    def create_io_map_from_io_tuple(input_list: list) -> list:
        result_list = []
        # print(input_list)
        for idx, (token, category_dict) in enumerate(input_list):
            # print(token)
            result_list.append(
                {"token": token, "category": category_dict, "position": idx}
            )
        return result_list

    @staticmethod
    def remove_spaces(input_string):
        return input_string.replace(" ", "")

    @staticmethod
    def create_masked_input_output_example(
            paragraph: str, nlp=get_spacy_nlp(), mask_prob=0.15
    ) -> list:
        sentences = Utility.separate_sentences(paragraph, nlp)
        data = []

        for sentence in sentences:
            tokens = sentence.split()  # You can use a more sophisticated tokenizer here
            input_tokens = []
            output_tokens = []
            for token in tokens:
                # Randomly decide whether to mask the token
                if random.random() < mask_prob:
                    input_tokens.append(
                        SpecialTokens.MASK_TOKEN.value
                    )  # Mask the token in the input
                    output_tokens.append(
                        token
                    )  # Output should predict the original token
                else:
                    input_tokens.append(token)  # Keep the token as it is in the input
                    output_tokens.append(token)  # Output should predict the same token

            # Convert the token lists back to strings
            input_string = " ".join(input_tokens)
            output_string = " ".join(output_tokens)
            data.append({"inputStr": input_string, "outputStr": output_string})

        return data

    @staticmethod
    def create_next_word_input_output_example(
            paragraph: str, nlp=get_spacy_nlp(), minimum_token_count=4
    ) -> list:
        sentences = Utility.separate_sentences(paragraph, nlp)
        data = []

        for sentence in sentences:
            words = sentence.split()
            for i in range(len(words) - minimum_token_count):
                input_text = " ".join(words[: i + minimum_token_count])
                output_text = " ".join(words[: i + minimum_token_count + 1])
                data.append({"inputStr": input_text, "outputStr": output_text})

        return data

    @staticmethod
    def separate_sentences(paragraph: str, nlp: spacy.Language):
        doc = nlp(paragraph)
        sentences = [sent.text for sent in doc.sents]
        return sentences

    @staticmethod
    def split_string_custom(input_string: str):
        # Initialize variables
        result = []
        current_word = ""
        is_special_word = False

        # Iterate through each character in the input string
        for char in input_string:
            if char == ' ' and not is_special_word:
                # If it's a space, and we're not in a special word, split the word
                result.append(current_word)
                current_word = ""
            elif current_word.startswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value) \
                    or current_word.startswith(FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value) \
                    or current_word.startswith(FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value) \
                    or current_word.startswith(FunctionPrefix.FUNCTION_IOR_REPRESENT.value):
                # If the current word starts with "##" or "$$", we're in a special word
                is_special_word = True
                current_word += char
                # if char == ' ':
                #     # If there's a space within a special word, remove it
                #     current_word = current_word.rstrip()
            elif char == ')' and is_special_word:
                # If we're in a special word and encounter ')', split the word
                current_word += char
                result.append(current_word)
                current_word = ""
                is_special_word = False
            elif char in ('(', ')') and not is_special_word:
                # If it's an adjacent '(' or ')' and we're not in a special word, split it
                if current_word:
                    result.append(current_word)
                result.append(char)
                current_word = ""
            else:
                # Otherwise, add the character to the current word
                current_word += char

        # Add the last word to the result
        if current_word:
            result.append(current_word)
        result = [word.replace(' ', '') if word.startswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value) \
                                           or word.startswith(FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value) \
                                           or word.startswith(FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value) \
                                           or word.startswith(FunctionPrefix.FUNCTION_IOR_REPRESENT.value) else word for
                  word in result]

        # Join the elements in the list into a single line with spaces
        result = ' '.join(result)
        return result

# if __name__ == "__main__":
#     raw_input = "This is a sample input for testing masked token prediction." \
#                 "This is an example sentence for testing next word prediction."
#
#     masked_data = Utility.create_masked_input_output_example(raw_input)
#     sample = Utility.create_sample_from_example(masked_data, PretrainTasks.MASKED_TOKEN_PREDICTION)
#     print(sample)
#
#     next_word_data = Utility.create_next_word_input_output_example(raw_input)
#     sample = Utility.create_sample_from_example(next_word_data, PretrainTasks.NEXT_TOKEN_PREDICTION)
#     print(sample)
