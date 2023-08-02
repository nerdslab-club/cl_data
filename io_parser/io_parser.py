from git_submodules.function_representation import MathFunctions, FunctionManager
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

    def create_value_tuple_with_category_from_input(self, input_string) -> list:
        # TODO
        pass


if __name__ == "__main__":
    input_strings = [
        "$$addition(3,50.0)",
        "##division(4.5,2)",
        "@@average(1.5,2.5,3.5)",
        "$$combination([1,2,3],'hello',True,2.5)",
        "##division(##sum([1,2,3]),##length([4,5,6]))",
    ]
    fm = FunctionManager()
    for input_string in input_strings:
        output_list = io_parser_utility.extract_function_params(input_string, fm)
        print(output_list)

    # input_string = "[1,2,4],##sum([1,2,3]),##division(##sum([1,2,3]),10),30,40,True,##length([4,5,6]), 10.4, True, [3,4,5]"
    # result_list = separate_params(input_string)
    # print(result_list)

# additional functionality
# batch parse
# tuple creating
# N.B. no space in function please, other than between params.
