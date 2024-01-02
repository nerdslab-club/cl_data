import random
from enum import Enum
from typing import Type
import spacy
from deprecated import deprecated

from io_parser.category_parser_utility import create_category_map
from io_parser.io_parser import IoParser
from src.constants import (
    SpecialTokens,
    FunctionPrefix,
    Constants,
    CategoryType,
    CategorySubType,
    CategorySubSubType,
)


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def get_spacy_nlp():
        return spacy.load("en_core_web_sm")

    @staticmethod
    def create_sample_from_example(
        examples: list,
        task_type: Type[Enum],
        max_encoder_sequence_length=None,
        max_decoder_sequence_length=None,
    ) -> list:
        for i, example in enumerate(examples):
            input_list = IoParser().create_value_list_from_input(
                example.get("inputStr")
            )
            output_list = IoParser().create_value_list_from_input(
                example.get("outputStr")
            )
            example["inputMap"] = Utility.create_io_map_from_io_tuple(
                input_list, True, max_encoder_sequence_length, is_eos_finishing_token=False
            )
            example["outputMap"] = Utility.create_io_map_from_io_tuple(
                output_list, True, max_decoder_sequence_length, is_eos_finishing_token=False
            )
            example["taskType"] = task_type.value
        return examples

    @staticmethod
    def create_io_map_from_io_tuple(
            input_list: list,
            add_bos_and_eos: bool,
            max_length: int | None,
            default_padding=SpecialTokens.PADDING,
            is_eos_finishing_token: bool = True,
    ) -> list:
        result_list = []
        start = 0
        if add_bos_and_eos:
            result_list.append(Utility.get_special_token(0, SpecialTokens.BEGINNING))
            start = 1
            if max_length is not None and is_eos_finishing_token:
                max_length = max_length - 1
        for idx, (token, category_dict) in enumerate(input_list, start=start):
            result_list.append(
                {
                    Constants.TOKEN: token,
                    Constants.CATEGORY: category_dict,
                    Constants.POSITION: idx,
                }
            )
        if add_bos_and_eos and not is_eos_finishing_token:
            result_list.append(
                Utility.get_special_token(len(result_list), SpecialTokens.ENDING)
            )
        if max_length is not None:
            current_length = len(result_list)
            if current_length >= max_length:
                # Truncate if result length is greater than the max length
                result_list = result_list[:max_length]
            else:
                num_padding = max_length - current_length
                for i in range(num_padding):
                    result_list.append(
                        Utility.get_special_token(current_length + i, default_padding)
                    )
        if add_bos_and_eos and is_eos_finishing_token:
            result_list.append(
                Utility.get_special_token(len(result_list), SpecialTokens.ENDING)
            )
        return result_list

    @staticmethod
    def get_special_token(position: int, special_token=SpecialTokens.PADDING):
        return {
            Constants.TOKEN: special_token.value,
            Constants.CATEGORY: create_category_map(
                CategoryType.SPECIAL,
                CategorySubType.WORD,
                CategorySubSubType.NONE,
            ),
            Constants.POSITION: position,
        }

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
    @deprecated("Function moved to io_parser_utility and apply in io_parser level")
    def split_string_custom(input_string: str):
        # Initialize variables
        result = []
        current_word = ""
        is_special_word = False

        # Iterate through each character in the input string
        for char in input_string:
            if char == " " and not is_special_word:
                # If it's a space, and we're not in a special word, split the word
                result.append(current_word)
                current_word = ""
            elif (
                current_word.startswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value)
                or current_word.startswith(
                    FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value
                )
                or current_word.startswith(
                    FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value
                )
                or current_word.startswith(FunctionPrefix.FUNCTION_IOR_REPRESENT.value)
            ):
                # If the current word starts with "##" or "$$", we're in a special word
                is_special_word = True
                current_word += char
            elif char == ")" and is_special_word:
                # If we're in a special word and encounter ')', split the word
                current_word += char
                result.append(current_word)
                current_word = ""
                is_special_word = False
            elif char in ("(", ")") and not is_special_word:
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
        result = [
            word.replace(" ", "")
            if word.startswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value)
            or word.startswith(FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value)
            or word.startswith(FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value)
            or word.startswith(FunctionPrefix.FUNCTION_IOR_REPRESENT.value)
            else word
            for word in result
        ]

        # Join the elements in the list into a single line with spaces
        result = " ".join(result)
        return result
