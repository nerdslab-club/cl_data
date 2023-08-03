from git_submodules.function_representation import FunctionManager, MathFunctions
import re
import types

from category_parser_utility import get_sub_sub_type_for_param, create_category_map
from src.constants import CategoryType, CategorySubType, CategorySubSubType


def parse_value_according_to_type(input_string: str) -> any:
    """Takes an input_string and return it into the correct format
    Supported formats are int, float, bool, str and list

    :param input_string
    :return: correct format of the input_string
    """
    if input_string.lower() == "true":
        result = (
            True,
            create_category_map(
                CategoryType.BOOL,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            ),
        )
    elif input_string.lower() == "false":
        result = (
            False,
            create_category_map(
                CategoryType.BOOL,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            ),
        )
    elif input_string.isdigit():
        result = (
            int(input_string),
            create_category_map(
                CategoryType.INTEGER,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            ),
        )
    elif re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", input_string):
        result = (
            float(input_string),
            create_category_map(
                CategoryType.FLOAT,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            ),
        )
    elif input_string.startswith("["):
        result = (
            create_list_from_str(input_string),
            create_category_map(
                CategoryType.LIST,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            ),
        )
    else:
        temp_token = remove_quotes(input_string)
        result = (
            temp_token,
            create_category_map(
                CategoryType.WORD,
                CategorySubType.PLACEHOLDER
                if temp_token.startswith("@")
                else CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            ),
        )
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
    (
        function_reference,
        function_category,
        function_type,
    ) = convert_function_name_to_token(function_name, function_manager)
    param_str = extract_content_between_brackets(input_func_str)
    separated_params = separate_params(param_str)
    # print(separated_params)

    total_param = len(separated_params)
    processed_params = []
    for i, param in enumerate(separated_params):
        if type(param) is str and (
            param.startswith("@@") or param.startswith("##") or param.startswith("$$")
        ):
            param = param.strip()
            param_func_params = extract_function_params(param, function_manager)
            param_func_params[0][1]["subSubType"] = get_sub_sub_type_for_param(
                i, total_param
            )
            processed_params.extend(param_func_params)
        else:
            param[1]["subSubType"] = get_sub_sub_type_for_param(i, total_param)
            processed_params.append(param)

    if function_type == "$$":
        return_value = execute_function(
            function_reference, [item[0] for item in processed_params]
        )
        return [
            (
                return_value,
                create_category_map(
                    get_category_type(
                        FunctionManager.get_function_return_type(function_reference)
                    ),
                    CategorySubType.RETURN_VALUE,
                    CategorySubSubType.NONE,
                ),
            )
        ]

    return [(function_reference, function_category)] + processed_params


def execute_function(function_reference: types.FunctionType, param_list: list) -> any:
    try:
        return function_reference(*param_list)
    except Exception as e:
        raise e


def separate_params(input_string: str) -> list:
    """Given the params as string of a function, this function will
    Return a list of the params according to their proper type.
    Supported types: function, str, int, float, list, bool

    :param input_string: params as comma seperated string
    :return: list of param with proper type
    """
    result = []
    stack = []
    current_substring = ""

    for char in input_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if stack:
                stack.pop()
        current_substring += char

        if not stack:
            if current_substring.startswith(","):
                current_substring = current_substring[1:]

            if "(" in current_substring:
                result.append(current_substring)
                current_substring = ""

            if (
                current_substring.endswith("##")
                or current_substring.endswith("@@")
                or current_substring.endswith("$$")
            ) and len(current_substring) > 2:
                result.extend(parse_param_according_to_type(current_substring[:-3]))
                current_substring = current_substring[-2:]
    if current_substring:
        result.extend(parse_param_according_to_type(current_substring))
    return result


def parse_param_according_to_type(input_string):
    """This function will parser comma seperated param into the following types,
    list, int, float, bool and str

    :param input_string: comma seperated params
    :return: list of params with proper type
    """
    params = [p.strip() for p in input_string.split(",")]
    internal_array = []
    processed_params = []
    for param in params:
        param = param.strip()
        if len(internal_array) != 0 and not param.endswith("]"):
            internal_array.append(parse_value_according_to_type(param)[0])
        elif param.startswith("["):
            internal_array.append(parse_value_according_to_type(param[1:])[0])
        elif param.endswith("]"):
            internal_array.append(parse_value_according_to_type(param[:-1])[0])
            processed_params.append(
                (
                    internal_array,
                    create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.NONE,
                    ),
                )
            )
            internal_array = []
        else:
            processed_params.append(parse_value_according_to_type(param))
    return processed_params


def convert_function_name_to_token(
    function_name: str, function_manager: FunctionManager
) -> tuple:
    """This function will convert function_name into function type string and proper function reference

    :param function_name: Example can be "$$addition"
    :param function_manager: Instance of FunctionManager
    :return: Tuple("function_type", function_reference)
    """
    function_reference = function_manager.getNameToReference().get(function_name[2:])
    function_type = function_name[:2]
    function_return_type = get_sub_category_type(
        FunctionManager.get_function_return_type(function_reference)
    )

    return (
        function_reference,
        create_category_map(
            CategoryType.FUNCTION,
            function_return_type,
            CategorySubSubType.PLACEHOLDER
            if function_type == "@@"
            else CategorySubSubType.NONE,
        ),
        function_name[:2],
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
            return_list.append(parse_value_according_to_type(param)[0])
        elif param.startswith("["):
            return_list.append(parse_value_according_to_type(param[1:])[0])
        elif param.endswith("]"):
            return_list.append(parse_value_according_to_type(param[:-1])[0])
    return return_list


def extract_content_between_brackets(input_string):
    """For function this function will extract the param string

    :param input_string: function string
    :return: comma separated params
    """
    start_index = input_string.find("(")
    end_index = input_string.rfind(")")  # Find last occurrence of ')'

    if start_index != -1 and end_index != -1:
        content_between_brackets = input_string[start_index + 1 : end_index]
        return content_between_brackets.strip()  # Trim leading and trailing whitespaces
    else:
        return None


def remove_quotes(input_string: str):
    """Remove quotes in case of string.

    :param input_string: string with quote
    :return: string without quote
    """
    if input_string.startswith("'") and input_string.endswith("'"):
        return input_string[1:-1]
    elif input_string.startswith('"') and input_string.endswith('"'):
        return input_string[1:-1]
    else:
        return input_string


def get_category_type(return_type):
    type_mapping = {
        type(lambda x: x): CategoryType.FUNCTION,
        str: CategoryType.WORD,
        int: CategoryType.INTEGER,
        float: CategoryType.FLOAT,
        list: CategoryType.LIST,
        bool: CategoryType.BOOL,
    }
    return type_mapping.get(return_type, None)


def get_sub_category_type(return_type):
    type_mapping = {
        str: CategorySubType.WORD,
        int: CategorySubType.INTEGER,
        float: CategorySubType.FLOAT,
        list: CategorySubType.LIST,
        bool: CategorySubType.BOOL,
    }
    return type_mapping.get(return_type, CategorySubType.DEFAULT)


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
