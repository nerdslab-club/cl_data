from git_submodules.function_representation import MathFunctions
from src.constants import Constants, CategoryType, CategorySubType, CategorySubSubType, FunctionPrefix


def create_category_map(
        category_type: CategoryType,
        category_sub_type: CategorySubType,
        category_sub_sub_type: CategorySubSubType,
) -> dict:
    return {
        Constants.CATEGORY_TYPE: category_type.value,
        Constants.CATEGORY_SUB_TYPE: category_sub_type.value,
        Constants.CATEGORY_SUB_SUB_TYPE: category_sub_sub_type.value,
    }


def get_sub_sub_type_for_param(param_order: int, total_param: int):
    if (param_order + 1) == total_param:
        return CategorySubSubType.PARAM_LAST.value
    elif param_order == 0:
        return CategorySubSubType.PARAM_ONE.value
    elif param_order == 1:
        return CategorySubSubType.PARAM_TWO.value
    elif param_order == 2:
        return CategorySubSubType.PARAM_THREE.value
    elif param_order == 3:
        return CategorySubSubType.PARAM_FOUR.value
    elif param_order == 4:
        return CategorySubSubType.PARAM_FIVE.value
    else:
        return CategorySubSubType.NONE.value


def get_func_sub_sub_type(function_type: str):
    if function_type == FunctionPrefix.FUNCTION_IOR_PLACEHOLDER.value:
        return CategorySubSubType.PLACEHOLDER
    elif function_type == FunctionPrefix.FUNCTION_IO_REPRESENT_R_EXECUTE.value:
        return CategorySubSubType.EXECUTE
    else:
        return CategorySubSubType.REPRESENT


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


def get_example_value_list():
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


def get_example_value_list_with_category():
    return [
        [
            (
                7,
                create_category_map(
                    CategoryType.INTEGER,
                    CategorySubType.RETURN_VALUE,
                    CategorySubSubType.NONE,
                ),
            )
        ],
        [
            (
                MathFunctions.addition,
                create_category_map(
                    CategoryType.FUNCTION,
                    CategorySubType.INTEGER,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                3,
                create_category_map(
                    CategoryType.INTEGER,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.PARAM_ONE,
                ),
            ),
            (
                4,
                create_category_map(
                    CategoryType.INTEGER,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.PARAM_LAST,
                ),
            ),
        ],
        [
            (
                MathFunctions.division,
                create_category_map(
                    CategoryType.FUNCTION,
                    CategorySubType.FLOAT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                MathFunctions.sum,
                create_category_map(
                    CategoryType.FUNCTION,
                    CategorySubType.FLOAT,
                    CategorySubSubType.PARAM_ONE,
                ),
            ),
            (
                [2, 3, 4],
                create_category_map(
                    CategoryType.LIST,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.PARAM_LAST,
                ),
            ),
            (
                MathFunctions.length,
                create_category_map(
                    CategoryType.FUNCTION,
                    CategorySubType.INTEGER,
                    CategorySubSubType.PARAM_LAST,
                ),
            ),
            (
                [2, 3, 4],
                create_category_map(
                    CategoryType.LIST,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.PARAM_LAST,
                ),
            ),
        ],
        [
            (
                "function",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                "for",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                "averaging",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                "list",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                "of",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                "number",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
        ],
        [
            (
                "adding",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                3,
                create_category_map(
                    CategoryType.INTEGER,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                "plus",
                create_category_map(
                    CategoryType.WORD,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
            (
                2,
                create_category_map(
                    CategoryType.INTEGER,
                    CategorySubType.DEFAULT,
                    CategorySubSubType.NONE,
                ),
            ),
        ],
        [
            (
                MathFunctions.average,
                create_category_map(
                    CategoryType.FUNCTION,
                    CategorySubType.FLOAT,
                    CategorySubSubType.PLACEHOLDER,
                ),
            ),
            (
                "@list",
                create_category_map(
                    CategoryType.LIST,
                    CategorySubType.PLACEHOLDER,
                    CategorySubSubType.PARAM_LAST,
                ),
            ),
        ],
    ]
