from git_submodules.function_representation import MathFunctions
from enum import Enum


class TaskTypes(Enum):
    FUNC_TO_FUNC_TRANSLATION = "func_to_func_translation"
    FUNC_TO_NL_TRANSLATION = "func_to_nl_translation"
    NL_TO_FUNC_TRANSLATION = "nl_to_func_translation"
    NL_TO_NL_TRANSLATION = "nl_to_nl_translation"


class CategoryType(Enum):
    FUNCTION = "function"
    NATURAL_LANGUAGE = "natural_language"  # This is string as well
    INTEGER = "integer"
    FLOATING_POINT = "floating_point"
    LIST = "list"
    BOOL = "bool"


class CategorySubType(Enum):
    EXECUTE = "execute"
    REPRESENT = "represent"
    WORD = "word"
    PARAM = "param"
    NONE = "none"


class CategorySubSubType(Enum):
    PARAM_ONE = "param_one"
    PARAM_TWO = "param_two"
    PARAM_THREE = "param_three"
    PARAM_FOUR = "param_four"
    PARAM_FIVE = "param_five"
    NONE = "none"


class Constants:
    FUNCTION_DEFAULT_VALUE = MathFunctions.average
    NATURAL_LANGUAGE_DEFAULT_VALUE = str("String")
    INTEGER_DEFAULT_VALUE = int(25)
    FLOATING_POINT_DEFAULT_VALUE = float(25.0)
    LIST_DEFAULT_VALUE = list([2, 3, 4, 5, 6])
