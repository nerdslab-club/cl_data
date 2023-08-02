from git_submodules.function_representation import MathFunctions
from ..src.constants import CategoryType, CategorySubType, CategorySubSubType
from ..src.utility import Utility
from ..src.random_value_generator import RandomValueGenerator


class AvgFuncToFuncExamples:
    def __init__(self):
        self.input_tuple_arrays = []
        self.output_tuple_arrays = []
        self.__set_input_tuple_arrays()
        self.__set_output_tuple_arrays()

    def __set_input_tuple_arrays(self):
        self.input_tuple_arrays = [
            [
                (
                    MathFunctions.average,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    [1, 2, 3, 4],
                    Utility.create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
            ],
            [
                (
                    MathFunctions.average,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    Utility.create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
            ],
        ]

    def __set_output_tuple_arrays(self):
        self.output_tuple_arrays = [
            [
                (
                    MathFunctions.division,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    MathFunctions.sum,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
                (
                    [1, 2, 3, 4],
                    Utility.create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
                (
                    MathFunctions.length,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.INTEGER,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
                (
                    [1, 2, 3, 4],
                    Utility.create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
            ],
            [
                (
                    MathFunctions.division,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    MathFunctions.sum,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
                (
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    Utility.create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
                (
                    MathFunctions.length,
                    Utility.create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.INTEGER,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
                (
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    Utility.create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
            ],
        ]
