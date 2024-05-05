import random

from cl_data.func_func.a_cubed_minus_b_cubed_f2f_example import create_f2f_cubed_minus_example
from cl_data.func_func.a_cubed_plus_b_cubed_f2f_example import create_f2f_cubed_plus_example
from cl_data.func_func.a_minus_b_whole_squared_f2f_example import create_f2f_square_minus_example
from cl_data.func_func.a_plus_b_whole_square_f2f_example import create_f2f_squared_plus_example
from cl_data.func_func.a_squared_plus_b_squared_f2f_example import create_f2f_a_squared_plus_b_squared_example
from cl_data.func_func.absolute_difference_f2f_example import create_f2f_absolute_difference_example
from cl_data.func_func.absolute_f2f_example import create_f2f_absolute_example
from cl_data.func_func.addition_f2f_example import create_f2f_addition_example
from cl_data.func_func.arctangent_f2f_example import create_f2f_arctangent_example
from cl_data.func_func.avg_f2f_example import create_f2f_average_example
from cl_data.func_func.binary_to_decimal_f2f_example import create_f2f_binary_to_decimal_example
from cl_data.func_func.ceil_f2f_example import create_f2f_ceil_example
from cl_data.func_func.circle_area_f2f_example import create_f2f_circle_area_example
from cl_data.func_func.combination_f2f_example import create_f2f_combination_example
from cl_data.func_func.cosine_similarity_f2f_example import create_f2f_cosine_similarity_example
from cl_data.func_func.cube_f2f_example import create_f2f_cube_example
from cl_data.func_func.cube_root_f2f_example import create_f2f_cube_root_example
from cl_data.func_func.exponentiation_f2f_example import create_f2f_exponentiation_example
from cl_data.func_func.float_to_int_f2f_example import create_f2f_float_to_int_example
from cl_data.func_func.floor_division_f2f_example import create_f2f_floor_division_example
from cl_data.func_func.floor_f2f_example import create_f2f_floor_example
from cl_data.func_func.gcd_f2f_example import create_f2f_gcd_example
from cl_data.func_func.geometric_mean_f2f_example import create_f2f_geometric_mean_example
from cl_data.func_func.greatest_value_f2f_example import create_f2f_greatest_value_example
from cl_data.func_func.hyperbolic_tangent_f2f_example import create_f2f_hyperbolic_example
from cl_data.func_func.hypotenuse_f2f_example import create_f2f_hypotenuse_example
from cl_data.func_func.is_palindrome_f2f_example import create_f2f_is_palindrome_example
from cl_data.func_func.isqrt_f2f_example import create_f2f_isqrt_example
from cl_data.func_func.lcm_f2f_example import create_f2f_lcm_example
from cl_data.func_func.logarithm_base_10_f2f_example import create_f2f_logarithm_base_10_example
from cl_data.func_func.logarithm_base_2_f2f_example import create_f2f_logarithm_base_2_example
from cl_data.func_func.modulus_f2f_example import create_f2f_modulus_example
from cl_data.func_func.multiplication_f2f_example import create_f2f_multiplication_example
from cl_data.func_func.permutation_f2f_example import create_f2f_permutation_example
from cl_data.func_func.pow_mod_f2f_example import create_f2f_pow_mod_example
from cl_data.func_func.power_of_ten_f2f_example import create_f2f_power_of_ten_example
from cl_data.func_func.product_f2f_example import create_f2f_product_example
from cl_data.func_func.relu_f2f_example import create_f2f_relu_example
from cl_data.func_func.sigmoid_f2f_example import create_f2f_sigmoid_example
from cl_data.func_func.smallest_value_f2f_example import create_f2f_smallest_value_example
from cl_data.func_func.square_f2f_example import create_f2f_square_example
from cl_data.func_func.square_root_f2f_example import create_f2f_square_root_example
from cl_data.func_func.subtraction_f2f_example import create_f2f_subtraction_example
from cl_data.func_func.sum_of_digits_f2f_example import create_f2f_sum_of_digits_example
from cl_data.func_func.tangent_f2f_example import create_f2f_trigonometry_example
from cl_data.func_func.x_plus_a_times_x_plus_b_f2f_example import create_f2f_polynomial_example
from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility

from cl_data.src.constants import Constants


class F2FSamples:
    TASK_TYPE = TaskTypes.FUNC_TO_FUNC_TRANSLATION

    def __init__(self):
        self.f2f_example_generators = {}
        self.__set_f2f_example_generators()
        self.f2f_samples = []

    def get_length_of_sample_generators(self):
        return len(self.f2f_example_generators)

    def get_next_random_sample(
            self,
            batch_size: int,
            generator_index: int | None,
            identifier: int | None,
            seed: int,
    ):
        if generator_index is not None:
            random_generator_index = generator_index
        else:
            random_generator_index = random.randint(0, len(self.f2f_example_generators) - 1)
        selected_generator = list(self.f2f_example_generators.values())[
            random_generator_index
        ]
        list_of_samples = selected_generator(batch_size, identifier, seed)
        for my_dict in list_of_samples:
            my_dict[Constants.TASK_TYPE] = F2FSamples.TASK_TYPE.value
        return list_of_samples

    def get_f2f_samples(self, each_example_count: int):
        self.__set_f2f_samples(each_example_count)
        return self.f2f_samples

    def __set_f2f_samples(self, each_example_count: int):
        for key, generator in self.f2f_example_generators.items():
            self.f2f_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), F2FSamples.TASK_TYPE
                ),
            )

    def __set_f2f_example_generators(self):
        self.f2f_example_generators = {
            "permutation": create_f2f_permutation_example,
            "combination": create_f2f_combination_example,
            "circle_area": create_f2f_circle_area_example,
            "gcd": create_f2f_gcd_example,
            "exponentiation": create_f2f_exponentiation_example,
            "lcm": create_f2f_lcm_example,
            "square_root": create_f2f_square_root_example,
            "cube": create_f2f_cube_example,
            "isqrt": create_f2f_isqrt_example,
            "square": create_f2f_square_example,

            "modulus": create_f2f_modulus_example,
            "cubed_minus": create_f2f_cubed_minus_example,
            "cubed_plus": create_f2f_cubed_plus_example,
            "square_minus": create_f2f_square_minus_example,
            "squared_plus": create_f2f_squared_plus_example,
            "polynomial": create_f2f_polynomial_example,
            "absolute_difference": create_f2f_absolute_difference_example,
            "trigonometry": create_f2f_trigonometry_example,
            "a_squared_plus_b_squared": create_f2f_a_squared_plus_b_squared_example,
            "multiplication": create_f2f_multiplication_example,

            "average": create_f2f_average_example,
            "addition": create_f2f_addition_example,
            "absolute": create_f2f_absolute_example,
            "ceil": create_f2f_ceil_example,
            "cube_root": create_f2f_cube_root_example,
            "cosine_similarity": create_f2f_cosine_similarity_example,
            "floor_division": create_f2f_floor_division_example,
            "floor": create_f2f_floor_example,
            "float_to_int": create_f2f_float_to_int_example,
            "greatest_value": create_f2f_greatest_value_example,
            "smallest_value": create_f2f_smallest_value_example,
            "subtraction": create_f2f_subtraction_example,
            "sum_of_digits": create_f2f_sum_of_digits_example,
            "geometric_mean": create_f2f_geometric_mean_example,
            "hyperbolic": create_f2f_hyperbolic_example,
            "hypotenuse": create_f2f_hypotenuse_example,
            "palindrome": create_f2f_is_palindrome_example,
            "logarithm_base_2": create_f2f_logarithm_base_2_example,
            "logarithm_base_10": create_f2f_logarithm_base_10_example,
            "pow_mod": create_f2f_pow_mod_example,
            "power_of_ten": create_f2f_power_of_ten_example,
            "product": create_f2f_product_example,
            "relu": create_f2f_relu_example,
            "sigmoid": create_f2f_sigmoid_example,
            "arctangent": create_f2f_arctangent_example,
            "binary_to_decimal": create_f2f_binary_to_decimal_example,
        }
