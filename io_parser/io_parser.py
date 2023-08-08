from function_representation import FunctionManager
from src.constants import FunctionPrefix
from .io_parser_utility import (
    parse_value_according_to_type,
    extract_function_params,
    split_string_by_space,
)


class IoParser:
    def __init__(self):
        self.f_m = FunctionManager()

    def create_value_list_from_input(self, input_string) -> list:
        raw_input_list = split_string_by_space(input_string)
        processed_params = []
        for i, item in enumerate(raw_input_list):
            if (
                item.startswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value)
                or item.startswith(FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value)
                or item.startswith(FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value)
                or item.startswith(FunctionPrefix.FUNCTION_IOR_REPRESENT.value)
            ):
                processed_params.extend(extract_function_params(item, self.f_m))
            else:
                processed_params.append(parse_value_according_to_type(item))
        return processed_params


if __name__ == "__main__":
    input_strings = [
        "$$addition(3,50)",
        "##division(4.5,2)",
        "&&division(4.5,2)",
        "@@average(@list)",
        "##combination(10,4)",
        "##division(##sum([1,2,3]),##length([4,5,6]))",
        "$$division($$sum([1,2,3]),$$length([4,5,6]))",
        "Adding 3 plus 2 is ##addition(3,2)",
    ]
    for input_string in input_strings:
        output_list = IoParser().create_value_list_from_input(input_string)
        print(output_list)

# additional functionality 1. batch parse
