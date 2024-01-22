import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_a_plus_b_whole_square_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(a, b),
            "outputStr": f"##a_plus_b_whole_square({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Calculate the square of the sum of {a} and {b}",
        f"A_PLUS_B_WHOLE_SQUARE({a}, {b})",
        f"Determine the result of ({a} + {b})^2",
        f"Find the square of the sum of {a} and {b}",
        f"The result of calculating ({a} + {b})^2",
        f"Performing the a_plus_b_whole_square operation for {a} and {b}",
        f"The square of the sum of {a} and {b}",
        f"A_PLUS_B_WHOLE_SQUARE operation: ({a}, {b})",
        f"The result after calculating ({a} + {b})^2, what is it?",
        f"Determine ({a} + {b})^2",
        f"Let's calculate ({a} + {b})^2",
        f"The result of ({a} + {b})^2, is it true?",
        f"Calculating ({a} + {b})^2",
        f"The result after calculating a_plus_b_whole_square for {a} and {b}",
        f"The square of the sum of {a} and {b}, what is its value?",
        f"Let's determine the square of the sum of {a} and {b}",
        f"The square of the sum of {a} and {b}",
        f"The square of the sum of {a} and {b}, what is the result?",
        f"The square of the sum of {a} and {b}, what does it give?",
        f"The square of the sum of {a} and {b} and provide the result",
        f"A_PLUS_B_WHOLE_SQUARE({a}, {b}), what does it yield?",
        f"The square of the sum of {a} and {b}, ignoring order",
        f"The result after calculating the square of the sum of {a} and {b}",
        f"Calculate the square of the sum of {a} and {b}, find the answer",
        f"The square of the sum of {a} and {b}, what does it give?",
        f"Let's find the result after calculating the square of the sum of {a} and {b}",
        f"The square of the sum of {a} and {b}, what is the output?",
        f"The result after calculating the square of the sum of {a} and {b}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_plus_b_whole_square_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
