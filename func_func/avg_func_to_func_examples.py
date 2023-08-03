from git_submodules.function_representation import MathFunctions
from io_parser.category_parser_utility import create_category_map
from ..src.constants import CategoryType, CategorySubType, CategorySubSubType
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
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    [1, 2, 3, 4],
                    create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
            ],
            [
                (
                    MathFunctions.average,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.FLOAT,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    create_category_map(
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
                    [1, 2, 3, 4],
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
                    [1, 2, 3, 4],
                    create_category_map(
                        CategoryType.LIST,
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
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
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
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    create_category_map(
                        CategoryType.LIST,
                        CategorySubType.DEFAULT,
                        CategorySubSubType.PARAM_LAST,
                    ),
                ),
            ],
        ]
