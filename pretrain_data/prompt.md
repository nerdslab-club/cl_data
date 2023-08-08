### Story generation

"""
Write me a mathematics  story with lots of calculation in it use the following operations, write the story in such a way so that it coherent and lots of math operation

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

### Tasks

For Masked Token Prediction:
For each sentence, randomly mask out a certain percentage of tokens (typically around 15%). Replace the masked tokens with a special "[MASK]" token. The goal is to predict these masked tokens during training.

For Next Token Prediction:
Create sequences of tokens with a certain length (e.g., 128 tokens). Slide a window over your tokenized text to create overlapping sequences. The last token in each sequence becomes the label that the model should predict.

### Model Archi
Decoder only model, category probability and output probability.