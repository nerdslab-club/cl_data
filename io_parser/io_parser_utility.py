from cl_data.function_representation import FunctionManager, MathFunctions
from .category_parser_utility import (
    get_sub_sub_type_for_param,
    create_category_map,
    get_sub_category_type,
    get_category_type,
    get_func_sub_sub_type,
)
from cl_data.src.constants import (
    Constants,
    CategoryType,
    CategorySubType,
    CategorySubSubType,
    FunctionPrefix,
)

import re
import types


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
    elif input_string.startswith("<") and input_string.endswith(">"):
        result = (
            remove_quotes(input_string),
            create_category_map(
                CategoryType.SPECIAL,
                CategorySubType.WORD,
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
                if temp_token.startswith(Constants.PARAM_PLACEHOLDER_PRIOR)
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
    pattern = r"([\$\#@\&]+[a-zA-Z_][a-zA-Z0-9_]*)\(([^)]*)\)"
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
            param.startswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value)
            or param.startswith(FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value)
            or param.startswith(FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value)
            or param.startswith(FunctionPrefix.FUNCTION_IOR_REPRESENT.value)
        ):
            param = param.strip()
            param_func_params = extract_function_params(param, function_manager)
            param_func_params[0][1][
                Constants.CATEGORY_SUB_SUB_TYPE
            ] = get_sub_sub_type_for_param(i, total_param)
            processed_params.extend(param_func_params)
        else:
            param[1][Constants.CATEGORY_SUB_SUB_TYPE] = get_sub_sub_type_for_param(
                i, total_param
            )
            processed_params.append(param)

    if function_type == FunctionPrefix.FUNCTION_IO_EXECUTE.value:
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
                current_substring.endswith(FunctionPrefix.FUNCTION_IO_EXECUTE.value)
                or current_substring.endswith(
                    FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value
                )
                or current_substring.endswith(
                    FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value
                )
                or current_substring.endswith(
                    FunctionPrefix.FUNCTION_IOR_REPRESENT.value
                )
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
    function_reference = function_manager.get_name_to_reference().get(function_name[2:])
    function_type = function_name[:2]
    function_return_type = get_sub_category_type(
        FunctionManager.get_function_return_type(function_reference)
    )

    return (
        function_reference,
        create_category_map(
            CategoryType.FUNCTION,
            function_return_type,
            get_func_sub_sub_type(function_type),
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


def split_string_by_space(input_string: str):
    return input_string.split()


def split_string_custom(input_string: str):
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
            or current_word.startswith(FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value)
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
