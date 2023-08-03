from git_submodules.function_representation import FunctionManager
import io_parser_utility


class IoParser:
    def __init__(self):
        self.f_m = FunctionManager()

    def create_value_list_from_input(self, input_string) -> list:
        raw_input_list = io_parser_utility.split_string_by_space(input_string)
        processed_params = []
        for i, item in enumerate(raw_input_list):
            if item.startswith("@@") or item.startswith("##") or item.startswith("$$"):
                processed_params.extend(
                    io_parser_utility.extract_function_params(item, self.f_m)
                )
            else:
                processed_params.append(
                    io_parser_utility.parse_value_according_to_type(item)
                )
        return processed_params


if __name__ == "__main__":
    input_strings = [
        "$$addition(3,50)",
        "##division(4.5,2)",
        "@@average(@list)",
        "##combination([1,2,3],'hello',True,2.5)",
        "##division(##sum([1,2,3]),##length([4,5,6]))",
        "Adding 3 plus 2 is ##addition(3,2)"
    ]
    for input_string in input_strings:
        output_list = IoParser().create_value_list_from_input(input_string)
        print(output_list)

# additional functionality
# batch parse
