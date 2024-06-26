import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_x_squared_plus_a_plus_b_times_x_plus_ab_example(count: int):
    examples = []
    for _ in range(count):
        x = RandomValueGenerator.generate_random_integer(1, 20)
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(x, a, b),
            "outputStr": f"##x_squared_plus_a_plus_b_times_x_plus_ab({x}, {a}, {b})",
        })
    return examples


def __random_explanation(x: int, a: int, b: int) -> str:
    explanations = [
        f"Calculate {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"X_SQUARED_PLUS_A_PLUS_B_TIMES_X_PLUS_AB({x}, {a}, {b})",
        f"Determine the result of {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"Find the expression {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"The result of calculating {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"Performing the x_squared_plus_a_plus_b_times_x_plus_ab operation for {x}, {a}, and {b}",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"X_SQUARED_PLUS_A_PLUS_B_TIMES_X_PLUS_AB operation: ({x}, {a}, {b})",
        f"The result after calculating {x}^2 + ({a} + {b}) * ({x} + {a * b}), what is it?",
        f"Determine {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"Let's calculate {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"The result of {x}^2 + ({a} + {b}) * ({x} + {a * b}), is it true?",
        f"Calculating {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"The result after calculating x_squared_plus_a_plus_b_times_x_plus_ab for {x}, {a}, and {b}",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), what is its value?",
        f"Let's determine the expression {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), what is the result?",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), what does it give?",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}) and provide the result",
        f"X_SQUARED_PLUS_A_PLUS_B_TIMES_X_PLUS_AB({x}, {a}, {b}), what does it yield?",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), ignoring order",
        f"The result after calculating the expression {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"Calculate {x}^2 + ({a} + {b}) * ({x} + {a * b}), find the answer",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), what does it give?",
        f"Let's find the result after calculating the expression {x}^2 + ({a} + {b}) * ({x} + {a * b})",
        f"The expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), what is the output?",
        f"The result after calculating the expression {x}^2 + ({a} + {b}) * ({x} + {a * b}), what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_x_squared_plus_a_plus_b_times_x_plus_ab_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
