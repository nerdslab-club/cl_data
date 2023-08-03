from git_submodules.function_representation import MathFunctions
from src.constants import CategoryType, CategorySubType, CategorySubSubType
from src.utility import Utility


def add_category_map_to_value_list(value_list: list) -> list:
    pass


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
            (7, Utility.create_category_map(
                CategoryType.INTEGER,
                CategorySubType.RETURN_VALE,
                CategorySubSubType.NONE,
            ))
        ],
        [
            (MathFunctions.addition, Utility.create_category_map(
                CategoryType.FUNCTION,
                CategorySubType.INTEGER,
                CategorySubSubType.NONE,
            )),
            (3, Utility.create_category_map(
                CategoryType.INTEGER,
                CategorySubType.DEFAULT,
                CategorySubSubType.PARAM_ONE,
            )),
            (4, Utility.create_category_map(
                CategoryType.INTEGER,
                CategorySubType.DEFAULT,
                CategorySubSubType.PARAM_LAST,
            ))
        ],
        [
            (MathFunctions.division, Utility.create_category_map(
                CategoryType.FUNCTION,
                CategorySubType.FLOAT,
                CategorySubSubType.NONE,
            )),
            (MathFunctions.sum, Utility.create_category_map(
                CategoryType.FUNCTION,
                CategorySubType.FLOAT,
                CategorySubSubType.PARAM_ONE,
            )),
            ([2, 3, 4], Utility.create_category_map(
                CategoryType.LIST,
                CategorySubType.DEFAULT,
                CategorySubSubType.PARAM_LAST,
            )),
            (MathFunctions.length, Utility.create_category_map(
                CategoryType.FUNCTION,
                CategorySubType.INTEGER,
                CategorySubSubType.PARAM_LAST,
            )),
            ([2, 3, 4], Utility.create_category_map(
                CategoryType.LIST,
                CategorySubType.DEFAULT,
                CategorySubSubType.PARAM_LAST,
            ))
        ],
        [
            ("function", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            ("for", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            ("averaging", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            ("list", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            ("of", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            ("number", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
        ],
        [
            ("adding", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            (3, Utility.create_category_map(
                CategoryType.INTEGER,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            ("plus", Utility.create_category_map(
                CategoryType.WORD,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
            (2, Utility.create_category_map(
                CategoryType.INTEGER,
                CategorySubType.DEFAULT,
                CategorySubSubType.NONE,
            )),
        ],
        [
            (MathFunctions.average, Utility.create_category_map(
                CategoryType.FUNCTION,
                CategorySubType.FLOAT,
                CategorySubSubType.PLACEHOLDER,
            )),
            ("@list", Utility.create_category_map(
                CategoryType.LIST,
                CategorySubType.PLACEHOLDER,
                CategorySubSubType.PARAM_LAST,
            )),
        ]
    ]
