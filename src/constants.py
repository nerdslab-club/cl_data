from cl_data.function_representation import MathFunctions
from enum import Enum


class TaskTypes(Enum):
    FUNC_TO_FUNC_TRANSLATION = "func_to_func_translation"
    FUNC_TO_NL_TRANSLATION = "func_to_nl_translation"
    NL_TO_FUNC_TRANSLATION = "nl_to_func_translation"
    NL_TO_NL_TRANSLATION = "nl_to_nl_translation"


class CategoryType(Enum):
    FUNCTION = "function"
    WORD = "word"  # This is string as well
    INTEGER = "integer"
    FLOAT = "float"
    LIST = "list"
    BOOL = "bool"
    SPECIAL = "special"


class CategorySubType(Enum):
    DEFAULT = "default"
    PLACEHOLDER = "placeholder"
    RETURN_VALUE = "return_value"
    WORD = "word"  # This is string as well
    INTEGER = "integer"
    FLOAT = "float"
    LIST = "list"
    BOOL = "bool"


class CategorySubSubType(Enum):
    PARAM_ONE = "param_one"
    PARAM_TWO = "param_two"
    PARAM_THREE = "param_three"
    PARAM_FOUR = "param_four"
    PARAM_FIVE = "param_five"
    PARAM_LAST = "param_last"
    NONE = "none"
    PLACEHOLDER = "placeholder"
    EXECUTE = "execute"
    REPRESENT = "represent"


class PlaceholderTokenType(Enum):
    FUNCTION = "@function"
    WORD = "@word"
    INTEGER = "@integer"
    FLOAT = "@float"
    LIST = "@list"
    BOOL = "@bool"


class FunctionPrefix(Enum):
    FUNCTION_IO_EXECUTE = "$$"
    FUNCTION_IO_REPRESENT_R_EXECUTE = "##"
    FUNCTION_IOR_REPRESENT = "&&"
    FUNCTION_IOR_PLACEHOLDER = "@@"


class PretrainTasks(Enum):
    MASKED_TOKEN_PREDICTION = "masked_token_prediction"
    NEXT_TOKEN_PREDICTION = "next_token_prediction"


class SpecialTokens(Enum):
    MASK_TOKEN = "<MASK>"
    SEPARATOR_TOKEN = "<SEP>"
    BEGINNING = "<BOS>"
    ENDING = "<EOS>"
    PADDING = "<PAD>"


class Constants:
    FUNCTION_DEFAULT_VALUE = MathFunctions.average
    WORD_DEFAULT_VALUE = str("word")
    INTEGER_DEFAULT_VALUE = int(25)
    FLOAT_DEFAULT_VALUE = float(25.0)
    LIST_DEFAULT_VALUE = list([2, 3, 4, 5, 6])
    BOOL_DEFAULT_VALUE = bool(True)
    WORD_PLACEHOLDER_VALUE = "@str"
    INTEGER_PLACEHOLDER_VALUE = "@int"
    FLOAT_PLACEHOLDER_VALUE = "@float"
    LIST_PLACEHOLDER_VALUE = "@list"
    BOOL_PLACEHOLDER_VALUE = "@bool"
    PARAM_PLACEHOLDER_PRIOR = "@"
    CATEGORY_TYPE = "type"
    CATEGORY_SUB_TYPE = "subType"
    CATEGORY_SUB_SUB_TYPE = "subSubType"
    TOKEN = "token"
    CATEGORY = "category"
    POSITION = "position"
    NOT_MY_TOKEN = "nOtMyToKeN"
    NOT_MY_TOKEN_INDEX = 0
    TASK_TYPE = "taskType"
    INPUT_TOKEN_COUNT = "inputTokenCount"
    INITIAL_TOKEN_COUNT = "initialTokenCount"
    IO_PARSER_OUTPUT = "ioParserOutput"
    SENTENCE = "sentence"
    INPUT_STR = "inputStr"
    OUTPUT_STR = "outputStr"

