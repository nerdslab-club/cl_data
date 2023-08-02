from git_submodules.function_representation import MathFunctions, FunctionManager
import io_parser_utility


class IoParser:
    def __init__(self):
        self.f_m = FunctionManager()
        pass

    def create_value_list_from_input(self, input_string) -> list:
        raw_input_list = io_parser_utility.split_string_by_space(input_string)
        processed_params = []
        for i, item in enumerate(raw_input_list):
            if item.startswith("@@") or item.startswith("##") or item.startswith("$$"):
                processed_params.extend(
                    io_parser_utility.extract_function_params(item, self.f_m)
                )
            elif item.startswith("["):
                processed_params.append(io_parser_utility.create_list_from_str(item))
            else:
                processed_params.append(
                    io_parser_utility.parse_value_according_to_type(item)
                )
        return processed_params

    def create_value_tuple_with_category_from_input(self, input_string) -> list:
        pass


if __name__ == "__main__":
    # Test the function with different input strings
    input_strings = [
        "$$addition(3,50.0)",
        "##division(4.5,2)",
        "@@average(1.5,2.5,3.5)",
        "$$combination([1,2,3],'hello',True,2.5)",
        # "##division(##sum([2,3,4]),##length([2,3,4]))",
    ]
    fm = FunctionManager()

    input_string = "3 + 2 = ##addition(3,2) [1,2,3]"
    result = IoParser().create_value_list_from_input(input_string)
    print(result)

    # for input_string in input_strings:
    #     output_list = io_parser_utility.extract_function_params(input_string, fm)
    #     print(output_list)

# additional functionality
# batch parse
# tuple creating
# N.B. no space in function please, other than between params.
