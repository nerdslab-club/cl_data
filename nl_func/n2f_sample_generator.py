import random

from cl_data.nl_func.a_cubed_minus_b_cubed_n2f_example import create_n2f_a_cubed_minus_b_cubed_example
from cl_data.nl_func.a_cubed_plus_b_cubed_n2f_example import create_n2f_a_cubed_plus_b_cubed_example
from cl_data.nl_func.a_minus_b_times_a_squared_plus_ab_plus_b_squared_n2f_example import \
    create_n2f_a_minus_b_times_a_squared_plus_ab_plus_b_squared_example
from cl_data.nl_func.a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_n2f_example import \
    create_n2f_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_example
from cl_data.nl_func.a_minus_b_whole_squared_n2f_example import create_n2f_a_minus_b_whole_squared_example
from cl_data.nl_func.a_minus_b_whole_squared_plus_4ab_n2f_example import create_n2f_a_minus_b_whole_squared_plus_4ab_example
from cl_data.nl_func.a_plus_b_times_a_squared_minus_ab_plus_b_squared_n2f_example import \
    create_n2f_a_plus_b_times_a_squared_minus_ab_plus_b_squared_example
from cl_data.nl_func.a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_n2f_example import \
    create_n2f_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example
from cl_data.nl_func.a_plus_b_whole_square_n2f_example import create_n2f_a_plus_b_whole_square_example
from cl_data.nl_func.a_plus_b_whole_squared_minus_4ab_n2f_example import create_n2f_a_plus_b_whole_squared_minus_4ab_example
from cl_data.nl_func.a_squared_minus_2ab_plus_b_squared_n2f_example import create_n2f_a_squared_minus_2ab_plus_b_squared_example
from cl_data.nl_func.a_squared_plus_2ab_plus_b_squared_n2f_example import create_n2f_a_squared_plus_2ab_plus_b_squared_example
from cl_data.nl_func.a_squared_plus_b_squared_n2f_example import create_n2f_a_squared_plus_b_squared_example
from cl_data.nl_func.absolute_difference_n2f_example import create_n2f_absolute_difference_example
from cl_data.nl_func.absolute_n2f_example import create_n2f_absolute_example
from cl_data.nl_func.addition_n2f_example import create_n2f_addition_example
from cl_data.nl_func.arccosine_n2f_example import create_n2f_arccosine_example
from cl_data.nl_func.arcsine_n2f_example import create_n2f_arcsine_example
from cl_data.nl_func.arctangent_n2f_example import create_n2f_arctangent_example
from cl_data.nl_func.ascending_sort_n2f_example import create_n2f_ascending_sort_example
from cl_data.nl_func.average_n2f_example import create_n2f_average_example
from cl_data.nl_func.binary_to_decimal_n2f_example import create_n2f_binary_to_decimal_example
from cl_data.nl_func.calculate_dot_product_n2f_example import create_n2f_calculate_dot_product_example
from cl_data.nl_func.ceil_n2f_example import create_n2f_ceil_example
from cl_data.nl_func.check_same_string_n2f_example import create_n2f_check_same_string_example
from cl_data.nl_func.circle_area_n2f_example import create_n2f_circle_area_example
from cl_data.nl_func.combination_n2f_example import create_n2f_combination_example
from cl_data.nl_func.cosine_n2f_example import create_n2f_cosine_example
from cl_data.nl_func.cosine_similarity_n2f_example import create_n2f_cosine_similarity_example
from cl_data.nl_func.cube_n2f_example import create_n2f_cube_example
from cl_data.nl_func.cube_root_n2f_example import create_n2f_cube_root_example
from cl_data.nl_func.decimal_to_binary_n2f_example import create_n2f_decimal_to_binary_example
from cl_data.nl_func.degrees_to_radians_n2f_example import create_n2f_degrees_to_radians_example
from cl_data.nl_func.descending_sort_n2f_example import create_n2f_descending_sort_example
from cl_data.nl_func.division_n2f_example import create_n2f_division_example
from cl_data.nl_func.euler_totient_n2f_example import create_n2f_euler_totient_example
from cl_data.nl_func.exponentiation_n2f_example import create_n2f_exponentiation_example
from cl_data.nl_func.factorial_n2f_example import create_n2f_factorial_example
from cl_data.nl_func.float_to_int_n2f_example import create_n2f_float_to_int_example
from cl_data.nl_func.floor_division_n2f_example import create_n2f_floor_division_example
from cl_data.nl_func.floor_n2f_example import create_n2f_floor_example
from cl_data.nl_func.gcd_n2f_example import create_n2f_gcd_example
from cl_data.nl_func.geometric_mean_n2f_example import create_n2f_geometric_mean_example
from cl_data.nl_func.geometric_series_sum_n2f_example import create_n2f_geometric_series_sum_example
from cl_data.nl_func.get_e_n2f_example import create_n2f_get_e_example
from cl_data.nl_func.get_pi_n2f_example import create_n2f_get_pi_example
from cl_data.nl_func.greatest_value_n2f_example import create_n2f_greatest_value_example
from cl_data.nl_func.hyperbolic_cosine_n2f_example import create_n2f_hyperbolic_cosine_example
from cl_data.nl_func.hyperbolic_sine_n2f_example import create_n2f_hyperbolic_sine_example
from cl_data.nl_func.hyperbolic_tangent_n2f_exmaple import create_n2f_hyperbolic_tangent_example
from cl_data.nl_func.hypotenuse_n2f_example import create_n2f_hypotenuse_example
from cl_data.nl_func.int_to_float_n2f_example import create_n2f_int_to_float_example
from cl_data.nl_func.invert_number_n2f_example import create_n2f_invert_number_example
from cl_data.nl_func.is_even_n2f_example import create_n2f_is_even_example
from cl_data.nl_func.is_odd_n2f_example import create_n2f_is_odd_example
from cl_data.nl_func.is_palindrome_n2f_example import create_n2f_is_palindrome_example
from cl_data.nl_func.is_perfect_cube_n2f_example import create_n2f_is_perfect_cube_example
from cl_data.nl_func.is_perfect_square_n2f_example import create_n2f_is_perfect_square_example
from cl_data.nl_func.is_power_of_two_n2f_example import create_n2f_is_power_of_two_example
from cl_data.nl_func.is_prime_n2f_example import create_n2f_is_prime_example
from cl_data.nl_func.isqrt_n2f_example import create_n2f_isqrt_example
from cl_data.nl_func.l1_norm_n2f_example import create_n2f_l1_norm_example
from cl_data.nl_func.l2_norm_n2f_example import create_n2f_l2_norm_example
from cl_data.nl_func.lcm_n2f_example import create_n2f_lcm_example
from cl_data.nl_func.length_n2f_example import create_n2f_length_example
from cl_data.nl_func.logarithm_base_10_n2f_example import create_n2f_logarithm_base_10_example
from cl_data.nl_func.logarithm_base_2_n2f_example import create_n2f_logarithm_base_2_example
from cl_data.nl_func.logarithm_n2f_example import create_n2f_logarithm_example
from cl_data.nl_func.max_value_n2f_example import create_n2f_max_value_example
from cl_data.nl_func.mean_n2f_example import create_n2f_mean_example
from cl_data.nl_func.median_n2f_example import create_n2f_median_example
from cl_data.nl_func.min_value_n2f_example import create_n2f_min_value_example
from cl_data.nl_func.modulus_n2f_example import create_n2f_modulus_example
from cl_data.nl_func.multiplication_n2f_example import create_n2f_multiplication_example
from cl_data.nl_func.negative_2ab_n2f_example import create_n2f_negative_2ab_example
from cl_data.nl_func.nth_root_n2f_example import create_n2f_nth_root_example
from cl_data.nl_func.permutation_n2f_example import create_n2f_permutation_example
from cl_data.nl_func.positive_2ab_n2f_example import create_n2f_positive_2ab_example
from cl_data.nl_func.pow_mod_n2f_example import create_n2f_pow_mod_example
from cl_data.nl_func.power_of_ten_n2f_example import create_n2f_power_of_ten_example
from cl_data.nl_func.prime_factors_n2f_example import create_n2f_prime_factors_example
from cl_data.nl_func.product_n2f_example import create_n2f_product_example
from cl_data.nl_func.radians_to_degrees_n2f_example import create_n2f_radians_to_degrees_example
from cl_data.nl_func.relu_n2f_example import create_n2f_relu_example
from cl_data.nl_func.reverse_string_n2f_example import create_n2f_reverse_string_example
from cl_data.nl_func.round_n2f_example import create_n2f_round_example
from cl_data.nl_func.sigmoid_n2f_example import create_n2f_sigmoid_example
from cl_data.nl_func.sine_n2f_example import create_n2f_sine_example
from cl_data.nl_func.smallest_value_n2f_example import create_n2f_smallest_value_example
from cl_data.nl_func.square_int_n2f_example import create_n2f_square_int_example
from cl_data.nl_func.square_n2f_example import create_n2f_square_example
from cl_data.nl_func.square_root_n2f_example import create_n2f_square_root_example
from cl_data.nl_func.subtraction_n2f_example import create_n2f_subtraction_example
from cl_data.nl_func.sum_n2f_example import create_n2f_sum_example
from cl_data.nl_func.sum_of_digits_n2f_example import create_n2f_sum_of_digits_example
from cl_data.nl_func.trangent_n2f_example import create_n2f_tangent_example
from cl_data.nl_func.x_plus_a_times_x_plus_b_n2f_example import create_n2f_x_plus_a_times_x_plus_b_example
from cl_data.nl_func.x_squared_plus_a_plus_b_times_x_plus_ab_n2f_example import \
    create_n2f_x_squared_plus_a_plus_b_times_x_plus_ab_example
from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility

from cl_data.src.constants import Constants


class N2FSamples:
    TASK_TYPE = TaskTypes.NL_TO_FUNC_TRANSLATION

    def __init__(self):
        self.n2f_example_generators = {}
        self.__set_n2f_example_generators()
        self.n2f_samples = []

    def get_length_of_sample_generators(self):
        return len(self.n2f_example_generators)

    def get_next_random_sample(self, batch_size: int, generator_index: int | None, identifier: int | None):
        if generator_index is not None:
            random_generator_index = generator_index
        else:
            random_generator_index = random.randint(0, len(self.n2f_example_generators) - 1)
        selected_generator = list(self.n2f_example_generators.values())[
            random_generator_index
        ]
        list_of_samples = selected_generator(batch_size, identifier)
        for my_dict in list_of_samples:
            my_dict[Constants.TASK_TYPE] = N2FSamples.TASK_TYPE.value
        return list_of_samples

    def get_n2f_samples(self, each_example_count: int):
        self.__set_n2f_samples(each_example_count)
        return self.n2f_samples

    def __set_n2f_samples(self, each_example_count: int):
        for key, generator in self.n2f_example_generators.items():
            self.n2f_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), N2FSamples.TASK_TYPE
                ),
            )

    def __set_n2f_example_generators(self):
        self.n2f_example_generators = {
            "addition": create_n2f_addition_example,
            "subtraction": create_n2f_subtraction_example,
            "multiplication": create_n2f_multiplication_example,
            "division": create_n2f_division_example,
            "exponentiation": create_n2f_exponentiation_example,
            "square_root": create_n2f_square_root_example,
            "floor_division": create_n2f_floor_division_example,
            "modulus": create_n2f_modulus_example,
            "logarithm": create_n2f_logarithm_example,
            "sine": create_n2f_sine_example,
            "cosine": create_n2f_cosine_example,
            "tangent": create_n2f_tangent_example,
            "gcd": create_n2f_gcd_example,
            "lcm": create_n2f_lcm_example,
            "absolute_difference": create_n2f_absolute_difference_example,
            "greatest_value": create_n2f_greatest_value_example,
            "smallest_value": create_n2f_smallest_value_example,
            "product": create_n2f_product_example,
            "factorial": create_n2f_factorial_example,
            "ascending_sort": create_n2f_ascending_sort_example,
            "descending_sort": create_n2f_descending_sort_example,
            "circle_area": create_n2f_circle_area_example,
            "permutation": create_n2f_permutation_example,
            "combination": create_n2f_combination_example,
            "average": create_n2f_average_example,
            "sum": create_n2f_sum_example,
            "length": create_n2f_length_example,
            "mean": create_n2f_mean_example,
            "median": create_n2f_median_example,
            "cube": create_n2f_cube_example,
            "cube_root": create_n2f_cube_root_example,
            "square": create_n2f_square_example,
            "nth_root": create_n2f_nth_root_example,
            "pow_mod": create_n2f_pow_mod_example,
            "ceil": create_n2f_ceil_example,
            "floor": create_n2f_floor_example,
            "round": create_n2f_round_example,
            "prime_factors": create_n2f_prime_factors_example,
            "absolute": create_n2f_absolute_example,
            "invert_number": create_n2f_invert_number_example,
            "degrees_to_radians": create_n2f_degrees_to_radians_example,
            "radians_to_degrees": create_n2f_radians_to_degrees_example,
            "isqrt": create_n2f_isqrt_example,

            "arcsine": create_n2f_arcsine_example,
            "arccosine": create_n2f_arccosine_example,
            "arctangent": create_n2f_arctangent_example,
            "hyperbolic_sine": create_n2f_hyperbolic_sine_example,
            "hyperbolic_cosine": create_n2f_hyperbolic_cosine_example,
            "hyperbolic_tangent": create_n2f_hyperbolic_tangent_example,
            "logarithm_base_10": create_n2f_logarithm_base_10_example,
            "logarithm_base_2": create_n2f_logarithm_base_2_example,
            "is_prime": create_n2f_is_prime_example,
            "is_perfect_square": create_n2f_is_perfect_square_example,
            "is_perfect_cube": create_n2f_is_perfect_cube_example,
            "relu": create_n2f_relu_example,
            "square_int": create_n2f_square_int_example,
            "power_of_ten": create_n2f_power_of_ten_example,
            "is_even": create_n2f_is_even_example,
            "is_odd": create_n2f_is_odd_example,
            "max_value": create_n2f_max_value_example,
            "min_value": create_n2f_min_value_example,
            "geometric_mean": create_n2f_geometric_mean_example,
            "is_power_of_two": create_n2f_is_power_of_two_example,
            "binary_to_decimal": create_n2f_binary_to_decimal_example,
            "decimal_to_binary": create_n2f_decimal_to_binary_example,
            "is_palindrome": create_n2f_is_palindrome_example,
            "sum_of_digits": create_n2f_sum_of_digits_example,
            "hypotenuse": create_n2f_hypotenuse_example,
            "float_to_int": create_n2f_float_to_int_example,
            "int_to_float": create_n2f_int_to_float_example,
            "geometric_series_sum": create_n2f_geometric_series_sum_example,
            "sigmoid": create_n2f_sigmoid_example,
            "cosine_similarity": create_n2f_cosine_similarity_example,
            "euler_totient": create_n2f_euler_totient_example,
            "l1_norm": create_n2f_l1_norm_example,
            "l2_norm": create_n2f_l2_norm_example,
            "check_same_string": create_n2f_check_same_string_example,
            "reverse_string": create_n2f_reverse_string_example,
            "get_pi": create_n2f_get_pi_example,
            "get_e": create_n2f_get_e_example,
            "calculate_dot_product": create_n2f_calculate_dot_product_example,
            "a_plus_b_whole_square": create_n2f_a_plus_b_whole_square_example,
            "a_squared_plus_2ab_plus_b_squared": create_n2f_a_squared_plus_2ab_plus_b_squared_example,
            "a_minus_b_whole_squared_plus_4ab": create_n2f_a_minus_b_whole_squared_plus_4ab_example,
            "a_minus_b_whole_squared": create_n2f_a_minus_b_whole_squared_example,
            "a_squared_minus_2ab_plus_b_squared": create_n2f_a_squared_minus_2ab_plus_b_squared_example,
            "a_plus_b_whole_squared_minus_4ab": create_n2f_a_plus_b_whole_squared_minus_4ab_example,
            "a_squared_plus_b_squared": create_n2f_a_squared_plus_b_squared_example,
            "negative_2ab": create_n2f_negative_2ab_example,
            "positive_2ab": create_n2f_positive_2ab_example,
            "x_plus_a_times_x_plus_b": create_n2f_x_plus_a_times_x_plus_b_example,
            "x_squared_plus_a_plus_b_times_x_plus_ab": create_n2f_x_squared_plus_a_plus_b_times_x_plus_ab_example,
            "a_cubed_plus_b_cubed": create_n2f_a_cubed_plus_b_cubed_example,
            "a_plus_b_whole_cubed_minus_3ab_times_a_plus_b": create_n2f_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example,
            "a_plus_b_times_a_squared_minus_ab_plus_b_squared": create_n2f_a_plus_b_times_a_squared_minus_ab_plus_b_squared_example,
            "a_cubed_minus_b_cubed": create_n2f_a_cubed_minus_b_cubed_example,
            "a_minus_b_whole_cubed_plus_3ab_times_a_minus_b": create_n2f_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_example,
            "a_minus_b_times_a_squared_plus_ab_plus_b_squared": create_n2f_a_minus_b_times_a_squared_plus_ab_plus_b_squared_example,
        }
