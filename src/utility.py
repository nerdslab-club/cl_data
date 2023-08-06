from io_parser.io_parser import IoParser
from src.constants import TaskTypes


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def create_sample_from_example(examples: list, task_type: TaskTypes) -> list:
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
