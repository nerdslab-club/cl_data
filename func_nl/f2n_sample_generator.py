import random

from func_nl.a_cubed_minus_b_cubed_f2n_example import create_f2n_a_cubed_minus_b_cubed_example
from func_nl.a_cubed_plus_b_cubed_f2n_example import create_f2n_a_cubed_plus_b_cubed_example
from func_nl.a_minus_b_times_a_squared_plus_ab_plus_b_squared_f2n_example import \
    create_f2n_a_minus_b_times_a_squared_plus_ab_plus_b_squared_example
from func_nl.a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_f2n_example import \
    create_f2n_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_example
from func_nl.a_minus_b_whole_squared_f2n_example import create_f2n_a_minus_b_whole_squared_example
from func_nl.a_minus_b_whole_squared_plus_4ab_f2n_example import create_f2n_a_minus_b_whole_squared_plus_4ab_example
from func_nl.a_plus_b_times_a_squared_minus_ab_plus_b_squared_f2n_example import \
    create_f2n_a_plus_b_times_a_squared_minus_ab_plus_b_squared_example
from func_nl.a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_f2n_example import \
    create_f2n_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example
from func_nl.a_plus_b_whole_square_f2n_example import create_f2n_a_plus_b_whole_square_example
from func_nl.a_plus_b_whole_squared_minus_4ab_f2n_example import create_f2n_a_plus_b_whole_squared_minus_4ab_example
from func_nl.a_squared_minus_2ab_plus_b_squared_f2n_example import create_f2n_a_squared_minus_2ab_plus_b_squared_example
from func_nl.a_squared_plus_2ab_plus_b_squared_f2n_example import create_f2n_a_squared_plus_2ab_plus_b_squared_example
from func_nl.a_squared_plus_b_squared_f2n_example import create_f2n_a_squared_plus_b_squared_example
from func_nl.absolute_difference_f2n_example import create_f2n_absolute_difference_example
from func_nl.absolute_f2n_example import create_f2n_absolute_example
from func_nl.addition_f2n_example import create_f2n_addition_example
from func_nl.arccosine_f2n_example import create_f2n_arccosine_example
from func_nl.arcsine_f2n_example import create_f2n_arcsine_example
from func_nl.arctangent_f2n_example import create_f2n_arctangent_example
from func_nl.ascending_sort_f2n_example import create_f2n_ascending_sort_example
from func_nl.average_f2n_example import create_f2n_average_example
from func_nl.binary_to_decimal_f2n_example import create_f2n_binary_to_decimal_example
from func_nl.calculate_dot_product_f2n_example import create_f2n_calculate_dot_product_example
from func_nl.ceil_f2n_example import create_f2n_ceil_example
from func_nl.check_same_string_f2n_example import create_f2n_check_same_string_example
from func_nl.circle_area_f2n_example import create_f2n_circle_area_example
from func_nl.combination_f2n_example import create_f2n_combination_example
from func_nl.cosine_f2n_example import create_f2n_cosine_example
from func_nl.cosine_similarity_f2n_example import create_f2n_cosine_similarity_example
from func_nl.cube_f2n_example import create_f2n_cube_example
from func_nl.cube_root_f2n_example import create_f2n_cube_root_example
from func_nl.decimal_to_binary_f2n_example import create_f2n_decimal_to_binary_example
from func_nl.degrees_to_radians_f2n_example import create_f2n_degrees_to_radians_example
from func_nl.descending_sort_f2n_example import create_f2n_descending_sort_example
from func_nl.division_f2n_example import create_f2n_division_example
from func_nl.euler_totient_f2n_example import create_f2n_euler_totient_example
from func_nl.exponentiation_f2n_example import create_f2n_exponentiation_example
from func_nl.factorial_f2n_example import create_f2n_factorial_example
from func_nl.float_to_int_f2n_example import create_f2n_float_to_int_example
from func_nl.floor_division_f2n_example import create_f2n_floor_division_example
from func_nl.floor_f2n_example import create_f2n_floor_example
from func_nl.gcd_f2n_example import create_f2n_gcd_example
from func_nl.geometric_mean_f2n_example import create_f2n_geometric_mean_example
from func_nl.geometric_series_sum_f2n_example import create_f2n_geometric_series_sum_example
from func_nl.get_e_f2n_example import create_f2n_get_e_example
from func_nl.get_pi_f2n_example import create_f2n_get_pi_example
from func_nl.greatest_value_f2n_example import create_f2n_greatest_value_example
from func_nl.hyperbolic_cosine_f2n_example import create_f2n_hyperbolic_cosine_example
from func_nl.hyperbolic_sine_f2n_example import create_f2n_hyperbolic_sine_example
from func_nl.hyperbolic_tangent_f2n_example import create_f2n_hyperbolic_tangent_example
from func_nl.hypotenuse_f2n_example import create_f2n_hypotenuse_example
from func_nl.int_to_float_f2n_example import create_f2n_int_to_float_example
from func_nl.invert_number_f2n_example import create_f2n_invert_number_example
from func_nl.is_even_f2n_example import create_f2n_is_even_example
from func_nl.is_odd_f2n_example import create_f2n_is_odd_example
from func_nl.is_palindrome_f2n_example import create_f2n_is_palindrome_example
from func_nl.is_perfect_cube_f2n_example import create_f2n_is_perfect_cube_example
from func_nl.is_perfect_square_f2n_example import create_f2n_is_perfect_square_example
from func_nl.is_power_of_two_f2n_example import create_f2n_is_power_of_two_example
from func_nl.is_prime_f2n_example import create_f2n_is_prime_example
from func_nl.isqrt_f2n_example import create_f2n_isqrt_example
from func_nl.l1_norm_f2n_example import create_f2n_l1_norm_example
from func_nl.l2_norm_f2n_example import create_f2n_l2_norm_example
from func_nl.lcm_f2n_example import create_f2n_lcm_example
from func_nl.length_f2n_example import create_f2n_length_example
from func_nl.logarithm_base_10_f2n_example import create_f2n_logarithm_base_10_example
from func_nl.logarithm_base_2_f2n_example import create_f2n_logarithm_base_2_example
from func_nl.logarithm_f2n_example import create_f2n_logarithm_example
from func_nl.max_value_f2n_example import create_f2n_max_value_example
from func_nl.mean_f2n_example import create_f2n_mean_example
from func_nl.median_f2n_example import create_f2n_median_example
from func_nl.min_value_f2n_example import create_f2n_min_value_example
from func_nl.modulus_f2n_example import create_f2n_modulus_example
from func_nl.multiplication_f2n_example import create_f2n_multiplication_example
from func_nl.negative_2ab_f2n_example import create_f2n_negative_2ab_example
from func_nl.nth_root_f2n_example import create_f2n_nth_root_example
from func_nl.permutation_f2n_example import create_f2n_permutation_example
from func_nl.positive_2ab_f2n_example import create_f2n_positive_2ab_example
from func_nl.pow_mod_f2n_example import create_f2n_pow_mod_example
from func_nl.power_of_ten_f2n_example import create_f2n_power_of_ten_example
from func_nl.prime_factors_f2n_example import create_f2n_prime_factors_example
from func_nl.product_f2n_example import create_f2n_product_example
from func_nl.radians_to_degrees_f2n_example import create_f2n_radians_to_degrees_example
from func_nl.relu_f2n_example import create_f2n_relu_example
from func_nl.reverse_string_f2n_example import create_f2n_reverse_string_example
from func_nl.round_f2n_example import create_f2n_round_example
from func_nl.sigmoid_f2n_example import create_f2n_sigmoid_example
from func_nl.sine_f2n_example import create_f2n_sine_example
from func_nl.smallest_value_f2n_example import create_f2n_smallest_value_example
from func_nl.square_f2n_example import create_f2n_square_example
from func_nl.square_int_f2n_example import create_f2n_square_int_example
from func_nl.square_root_f2n_example import create_f2n_square_root_example
from func_nl.subtraction_f2n_example import create_f2n_subtraction_example
from func_nl.sum_f2n_example import create_f2n_sum_example
from func_nl.sum_of_digits_f2n_example import create_f2n_sum_of_digits_example
from func_nl.tangent_f2n_example import create_f2n_tangent_example
from func_nl.x_plus_a_times_x_plus_b_f2n_example import create_f2n_x_plus_a_times_x_plus_b_example
from func_nl.x_squared_plus_a_plus_b_times_x_plus_ab_f2n_example import \
    create_f2n_x_squared_plus_a_plus_b_times_x_plus_ab_example
from src.constants import TaskTypes
from src.utility import Utility


class F2NSamples:
    TASK_TYPE = TaskTypes.FUNC_TO_NL_TRANSLATION

    def __init__(self):
        self.f2n_example_generators = {}
        self.__set_f2n_example_generators()
        self.f2n_samples = []

    def get_next_random_f2n_sample(self):
        random_generator_index = random.randint(0, len(self.f2n_example_generators) - 1)
        selected_generator = list(self.f2n_example_generators.values())[
            random_generator_index
        ]
        return Utility.create_sample_from_example(
            selected_generator(1), F2NSamples.TASK_TYPE
        )

    def get_f2n_samples(self, each_example_count: int):
        self.__set_f2n_samples(each_example_count)
        return self.f2n_samples

    def __set_f2n_samples(self, each_example_count: int):
        for key, generator in self.f2n_example_generators.items():
            self.f2n_samples.extend(
                Utility.create_sample_from_example(
                    generator(each_example_count), F2NSamples.TASK_TYPE
                ),
            )

    def __set_f2n_example_generators(self):
        self.f2n_example_generators = {
            "addition": create_f2n_addition_example,
            "subtraction": create_f2n_subtraction_example,
            "multiplication": create_f2n_multiplication_example,
            "division": create_f2n_division_example,
            "exponentiation": create_f2n_exponentiation_example,
            "square_root": create_f2n_square_root_example,
            "floor_division": create_f2n_floor_division_example,
            "modulus": create_f2n_modulus_example,
            "logarithm": create_f2n_logarithm_example,
            "sine": create_f2n_sine_example,
            "cosine": create_f2n_cosine_example,
            "tangent": create_f2n_tangent_example,
            "arcsine": create_f2n_arcsine_example,
            "arccosine": create_f2n_arccosine_example,
            "arctangent": create_f2n_arctangent_example,
            "hyperbolic_sine": create_f2n_hyperbolic_sine_example,
            "hyperbolic_cosine": create_f2n_hyperbolic_cosine_example,
            "hyperbolic_tangent": create_f2n_hyperbolic_tangent_example,
            "logarithm_base_10": create_f2n_logarithm_base_10_example,
            "logarithm_base_2": create_f2n_logarithm_base_2_example,
            "degrees_to_radians": create_f2n_degrees_to_radians_example,
            "radians_to_degrees": create_f2n_radians_to_degrees_example,
            "gcd": create_f2n_gcd_example,
            "lcm": create_f2n_lcm_example,
            "isqrt": create_f2n_isqrt_example,
            "pow_mod": create_f2n_pow_mod_example,
            "ceil": create_f2n_ceil_example,
            "floor": create_f2n_floor_example,
            "round": create_f2n_round_example,
            "absolute_difference": create_f2n_absolute_difference_example,
            "greatest_value": create_f2n_greatest_value_example,
            "smallest_value": create_f2n_smallest_value_example,
            "product": create_f2n_product_example,
            "factorial": create_f2n_factorial_example,
            "is_prime": create_f2n_is_prime_example,
            "prime_factors": create_f2n_prime_factors_example,
            "is_perfect_square": create_f2n_is_perfect_square_example,
            "is_perfect_cube": create_f2n_is_perfect_cube_example,
            "mean": create_f2n_mean_example,
            "median": create_f2n_median_example,
            "relu": create_f2n_relu_example,
            "ascending_sort": create_f2n_ascending_sort_example,
            "descending_sort": create_f2n_descending_sort_example,
            "square_int": create_f2n_square_int_example,
            "square": create_f2n_square_example,
            "absolute": create_f2n_absolute_example,
            "power_of_ten": create_f2n_power_of_ten_example,
            "cube": create_f2n_cube_example,
            "cube_root": create_f2n_cube_root_example,
            "is_even": create_f2n_is_even_example,
            "is_odd": create_f2n_is_odd_example,
            "max_value": create_f2n_max_value_example,
            "min_value": create_f2n_min_value_example,
            "nth_root": create_f2n_nth_root_example,
            "geometric_mean": create_f2n_geometric_mean_example,
            "is_power_of_two": create_f2n_is_power_of_two_example,
            "binary_to_decimal": create_f2n_binary_to_decimal_example,
            "decimal_to_binary": create_f2n_decimal_to_binary_example,
            "is_palindrome": create_f2n_is_palindrome_example,
            "sum_of_digits": create_f2n_sum_of_digits_example,
            "hypotenuse": create_f2n_hypotenuse_example,
            "circle_area": create_f2n_circle_area_example,
            "permutation": create_f2n_permutation_example,
            "combination": create_f2n_combination_example,
            "invert_number": create_f2n_invert_number_example,
            "float_to_int": create_f2n_float_to_int_example,
            "int_to_float": create_f2n_int_to_float_example,
            "geometric_series_sum": create_f2n_geometric_series_sum_example,
            "sigmoid": create_f2n_sigmoid_example,
            "cosine_similarity": create_f2n_cosine_similarity_example,
            "euler_totient": create_f2n_euler_totient_example,
            "l1_norm": create_f2n_l1_norm_example,
            "l2_norm": create_f2n_l2_norm_example,
            "average": create_f2n_average_example,
            "sum": create_f2n_sum_example,
            "length": create_f2n_length_example,
            "check_same_string": create_f2n_check_same_string_example,
            "reverse_string": create_f2n_reverse_string_example,
            "get_pi": create_f2n_get_pi_example,
            "get_e": create_f2n_get_e_example,
            "calculate_dot_product": create_f2n_calculate_dot_product_example,
            "a_plus_b_whole_square": create_f2n_a_plus_b_whole_square_example,
            "a_squared_plus_2ab_plus_b_squared": create_f2n_a_squared_plus_2ab_plus_b_squared_example,
            "a_minus_b_whole_squared_plus_4ab": create_f2n_a_minus_b_whole_squared_plus_4ab_example,
            "a_minus_b_whole_squared": create_f2n_a_minus_b_whole_squared_example,
            "a_squared_minus_2ab_plus_b_squared": create_f2n_a_squared_minus_2ab_plus_b_squared_example,
            "a_plus_b_whole_squared_minus_4ab": create_f2n_a_plus_b_whole_squared_minus_4ab_example,
            "a_squared_plus_b_squared": create_f2n_a_squared_plus_b_squared_example,
            "negative_2ab": create_f2n_negative_2ab_example,
            "positive_2ab": create_f2n_positive_2ab_example,
            "x_plus_a_times_x_plus_b": create_f2n_x_plus_a_times_x_plus_b_example,
            "x_squared_plus_a_plus_b_times_x_plus_ab": create_f2n_x_squared_plus_a_plus_b_times_x_plus_ab_example,
            "a_cubed_plus_b_cubed": create_f2n_a_cubed_plus_b_cubed_example,
            "a_plus_b_whole_cubed_minus_3ab_times_a_plus_b": create_f2n_a_plus_b_whole_cubed_minus_3ab_times_a_plus_b_example,
            "a_plus_b_times_a_squared_minus_ab_plus_b_squared": create_f2n_a_plus_b_times_a_squared_minus_ab_plus_b_squared_example,
            "a_cubed_minus_b_cubed": create_f2n_a_cubed_minus_b_cubed_example,
            "a_minus_b_whole_cubed_plus_3ab_times_a_minus_b": create_f2n_a_minus_b_whole_cubed_plus_3ab_times_a_minus_b_example,
            "a_minus_b_times_a_squared_plus_ab_plus_b_squared": create_f2n_a_minus_b_times_a_squared_plus_ab_plus_b_squared_example,
        }
