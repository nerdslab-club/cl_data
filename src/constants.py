from git_submodules.function_representation import MathFunctions
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


class CategorySubType(Enum):
    DEFAULT = "default"
    PLACEHOLDER = "placeholder"
    RETURN_VALE = "return_value"
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


class PlaceholderTokenType(Enum):
    FUNCTION = "@function"
    WORD = "@word"
    INTEGER = "@integer"
    FLOAT = "@float"
    LIST = "@list"
    BOOL = "@bool"


class Constants:
    FUNCTION_DEFAULT_VALUE = MathFunctions.average
    WORD_DEFAULT_VALUE = str("word")
    INTEGER_DEFAULT_VALUE = int(25)
    FLOAT_DEFAULT_VALUE = float(25.0)
    LIST_DEFAULT_VALUE = list([2, 3, 4, 5, 6])
    BOOL_DEFAULT_VALUE = bool(True)