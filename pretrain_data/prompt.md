### Story generation

"""
Write me a mathematics  story with lots of calculation in it use the following operations, 
write the story in such a way so that it coherent and lots of math operation

relu(x: float)
ascending_sort(lst: list[int])
descending_sort(lst: list[int])
square_int(x: int)
square(x: float)
absolute(x: float)
power_of_ten(x: float)
cube(x: float)
cube_root(x: float)
is_even(x: int)
is_odd(x: int)

For the param of the functions use random number, let say we have the following variables in python
random_list = Utility.remove_spaces(str(RandomValueGenerator.generate_random_list()))
random_int_one = RandomValueGenerator.generate_random_integer()
random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
random_int_four = RandomValueGenerator.generate_random_integer()
random_float = RandomValueGenerator.generate_random_float()
random_bool = RandomValueGenerator.generate_random_boolean()

whenever there is a calculation, for example:
f"The cube root of 729 is 9" change it with f"The cube root of 729 is ##square_root({random_int_one}})"
Here you are supposed to use ## before function call like ##function_name(), and add the appropriate params like ##function_name(param_one, param_two), function_name can be addition, subtraction, multiplication ...
if recursive function call is needed use like -> f"##subtraction(##exponentiation({random_int_one},{random_int_two}),{random_int_three})"
Do the similar for other calculations wherever possible. 
Please try to use only calculations that use the given functions in your story.
Please also don't use space in between params of functions like: ##exponentiation({random_int_one},{random_int_four})
don't use ## after function call and for showing variable outside function call write it like {random_int_one}.

Now write a python code with the story string as the first item of an array, use python formatted string literals.
"""


### Function names

addition(x: int, y: int)
subtraction(x: int, y: int)
multiplication(x: float, y: float)
division(x: float, y: float)
exponentiation(x: float, y: float)
square_root(x: float)
floor_division(x: int, y: int)
modulus(x: int, y: int)
logarithm(x: float, base: float)
sine(x: float)

cosine(x: float)
tangent(x: float)
arcsine(x: float)
arccosine(x: float)
arctangent(x: float)
hyperbolic_sine(x: float)
hyperbolic_cosine(x: float)
hyperbolic_tangent(x: float)
logarithm_base_10(x: float)
logarithm_base_2(x: float)

degrees_to_radians(x: float)
radians_to_degrees(x: float)
gcd(x: int, y: int)
lcm(x: int, y: int)
isqrt(x: int)
pow_mod(x: int, y: int, mod: int)
ceil(x: float)
floor(x: float)
round(x: float)
absolute_difference(x: float, y: float)

greatest_value(x: float, y: float)
smallest_value(x: float, y: float)
product(numbers: list)
factorial(x: int)
is_prime(x: int)
prime_factors(x: int)
is_perfect_square(x: int)
is_perfect_cube(x: int)
mean(numbers: list)
median(numbers: list)

relu(x: float)
ascending_sort(lst: list[int])
descending_sort(lst: list[int])
square_int(x: int)
square(x: float)
absolute(x: float)
power_of_ten(x: float)
cube(x: float)
cube_root(x: float)
is_even(x: int)
is_odd(x: int)

max_value(lst: list[int])
min_value(lst: list[int])
nth_root(x: float, n: int)
geometric_mean(lst: list[float])
is_power_of_two(x: int)
binary_to_decimal(binary)
decimal_to_binary(decimal)
is_palindrome(x: str)
sum_of_digits(x: int)
hypotenuse(a: float, b: float)

circle_area(radius: float)
permutation(n: int, r: int)
combination(n: int, r: int)
invert_number(number: float)
float_to_int(value: float)
int_to_float(value: int)
geometric_series_sum(a: float, r: float, n: int)
sigmoid(x: float)
cosine_similarity(vector1: list, vector2: list)
euler_totient(n: int)

l1_norm(vector: list)
l2_norm(vector: list)
average(numbers: list)
sum(numbers: list)
length(numbers: list)
check_same_string(str1: str, str2: str)
reverse_string(input_str: str)
get_pi()
get_e()
calculate_dot_product(vector1: list, vector2: list)

a_plus_b_whole_square(a: int, b: int)
a_squared_plus_2ab_plus_b_squared(a: int, b: int)
a_minus_b_whole_squared_plus_4ab(a: int, b: int)
a_minus_b_whole_squared(a: int, b: int)
a_squared_minus_2ab_plus_b_squared(a: int, b: int)
a_plus_b_whole_squared_minus_4ab(a: int, b: int)
a_squared_plus_b_squared(a: int, b: int)

negative_2ab(a: int, b: int)
positive_2ab(a: int, b: int)
x_plus_a_times_x_plus_b(x: int, a: int, b: int)
x_squared_plus_a_plus_b_times_x_plus_ab(x: int, a: int, b: int)
a_cubed_plus_b_cubed(a: int, b: int)
a_plus_b_whole_cubed_minus_3ab_times_a_plus_b(a: int, b: int)
a_plus_b_times_a_squared_minus_ab_plus_b_squared(a: int, b: int)
a_cubed_minus_b_cubed(a: int, b: int)
a_minus_b_whole_cubed_plus_3ab_times_a_minus_b(a: int, b: int)
a_minus_b_times_a_squared_plus_ab_plus_b_squared(a: int, b: int)

