from git_submodules.function_representation import MathFunctions
from io_parser.category_parser_utility import create_category_map
from ..src.constants import CategoryType, CategorySubType, CategorySubSubType
from ..src.random_value_generator import RandomValueGenerator


class CombinationFuncToFuncExamples:
    def __init__(self):
        self.input_tuple_arrays = []
        self.output_tuple_arrays = []
        self.__set_input_tuple_arrays()
        self.__set_output_tuple_arrays()

    def __set_input_tuple_arrays(self):
        self.input_tuple_arrays = [
            [
                (
                    MathFunctions.combination,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.INTEGER,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    10,
                    create_category_map(
                        CategoryType.INTEGER,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
                (
                    4,
                    create_category_map(
                        CategoryType.INTEGER,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_TWO,
                    ),
                ),
            ],
            [
                (
                    MathFunctions.combination,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.EXECUTE,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    22,
                    create_category_map(
                        CategoryType.INTEGER,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
                (
                    9,
                    create_category_map(
                        CategoryType.INTEGER,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_TWO,
                    ),
                ),
            ],
        ]

    MathFunctions.floor_division(
        MathFunctions.permutation(10, 4), MathFunctions.factorial(4)
    )

    def __set_output_tuple_arrays(self):
        self.output_tuple_arrays = [
            [
                (
                    MathFunctions.floor_division,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.EXECUTE,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    MathFunctions.permutation,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.EXECUTE,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    10,
                    create_category_map(
                        CategoryType.INTEGER,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
                (
                    4,
                    create_category_map(
                        CategoryType.INTEGER,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_TWO,
                    ),
                ),
                (
                    [1, 2, 3, 4],
                    create_category_map(
                        CategoryType.LIST,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
            ],
            [
                (
                    MathFunctions.division,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.EXECUTE,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    MathFunctions.sum,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.EXECUTE,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    create_category_map(
                        CategoryType.LIST,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
                (
                    MathFunctions.length,
                    create_category_map(
                        CategoryType.FUNCTION,
                        CategorySubType.EXECUTE,
                        CategorySubSubType.NONE,
                    ),
                ),
                (
                    RandomValueGenerator.generate_random_list(5, 1, 100, 32),
                    create_category_map(
                        CategoryType.LIST,
                        CategorySubType.PARAM,
                        CategorySubSubType.PARAM_ONE,
                    ),
                ),
            ],
        ]
