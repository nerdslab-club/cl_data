from git_submodules.function_representation import FunctionManager, MathFunctions
import re


def parse_value_according_to_type(input_string: str) -> any:
    """Takes an input_string and return it into the correct format
    Supported formats are int, float, bool, str.

    :param input_string
    :return: correct format of the input_string
    """
    result = None
    if input_string.lower() == "true":
        result = True
    elif input_string.lower() == "false":
        result = False
    elif input_string.isdigit():
        result = int(input_string)
    elif re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", input_string):
        result = float(input_string)
    else:
        result = remove_quotes(input_string)
    return result


def extract_function_params(
    input_func_str: str, function_manager: FunctionManager
) -> list:
    """Give the function token it will extract function name and param
    According to their types

    :param function_manager: Instance of FunctionManager
    :param input_func_str: example can be "$$addition(3, 50.0)"
    :return: list of extracted tokens.
    """
    pattern = r"([\$\#@]+[a-zA-Z_][a-zA-Z0-9_]*)\(([^)]*)\)"
    matches = re.findall(pattern, input_func_str)

    if not matches:
        return []

    function_name, param_str = matches[0]
    function_token = convert_function_name_to_token(function_name, function_manager)

    params = [p.strip() for p in param_str.split(",")]

    internal_array = []
    processed_params = []
    for param in params:
        param = param.strip()
        if len(internal_array) != 0 and not param.endswith("]"):
            internal_array.append(parse_value_according_to_type(param))
        elif param.startswith("["):
            internal_array.append(parse_value_according_to_type(param[1:]))
        elif param.endswith("]"):
            internal_array.append(parse_value_according_to_type(param[:-1]))
            processed_params.append(internal_array)
            internal_array = []
        else:
            processed_params.append(parse_value_according_to_type(param))
    return [function_token] + processed_params


def convert_function_name_to_token(
    function_name: str, function_manager: FunctionManager
) -> tuple:
    """This function will convert function_name into function type string and proper function reference

    :param function_name: Example can be "$$addition"
    :param function_manager: Instance of FunctionManager
    :return: Tuple("function_type", function_reference)
    """
    return function_name[:2], function_manager.getNameToReference().get(
        function_name[2:]
    )


def create_list_from_str(list_str: str) -> list:
    """Recreate list from input string with proper data type

    :param list_str: example can be "[1,2,3]"
    :return: the recreated list [1,2,3]
    """
    params = [p.strip() for p in list_str.split(",")]
    return_list = []
    for param in params:
        param = param.strip()
        if len(return_list) != 0 and not param.endswith("]"):
            return_list.append(parse_value_according_to_type(param))
        elif param.startswith("["):
            return_list.append(parse_value_according_to_type(param[1:]))
        elif param.endswith("]"):
            return_list.append(parse_value_according_to_type(param[:-1]))
    return return_list


def remove_quotes(input_string: str):
    if input_string.startswith("'") and input_string.endswith("'"):
        return input_string[1:-1]
    elif input_string.startswith('"') and input_string.endswith('"'):
        return input_string[1:-1]
    else:
        return input_string


def split_string_by_space(input_string: str):
    return input_string.split()


def get_example_input_arrays():
    return [
        "$$addition(3,4)",
        "##addition(3,4)",
        "##division(##sum([2,3,4]),##length([2,3,4]))",
        "function for averaging list of number",
        "adding 3 plus 2",
        "@@average(@list)",
        "3 + 2 = 5",
        "3 + 2 = ##addition(3,2)",
    ]


def get_example_output_arrays():
    return [
        [
            7,
        ],
        [
            MathFunctions.addition,
            3,
            4,
        ],
        [
            MathFunctions.division,
            MathFunctions.sum,
            [2, 3, 4],
            MathFunctions.length,
            [2, 3, 4],
        ],
        [
            "function",
            "for",
            "averaging",
            "list",
            "of",
            "number",
        ],
        [
            "adding",
            3,
            "plus",
            2,
        ],
        [
            MathFunctions.average,
            "@list",
        ],
        [
            3,
            "+",
            2,
            "=",
            5,
        ],
        [
            3,
            "+",
            2,
            "=",
            MathFunctions.addition,
            3,
            2,
        ],
    ]
