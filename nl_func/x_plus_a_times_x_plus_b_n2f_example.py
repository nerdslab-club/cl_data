import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_x_plus_a_times_x_plus_b_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_integer()
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(x, a, b, (None if identifier is None else identifier+i)),
            "outputStr": f"##x_plus_a_times_x_plus_b({x}, {a}, {b})",
        })
    return examples


def __random_explanation(x: int, a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Performing the x_plus_a_times_x_plus_b operation for {x}, {a}, and {b}",
        f"Calculate ({x} + {a}) * ({x} + {b})",
        f"Determine the result of ({x} + {a}) * ({x} + {b})",
        f"Find the expression ({x} + {a}) * ({x} + {b})",
        f"The result of calculating ({x} + {a}) * ({x} + {b})",
        f"The expression ({x} + {a}) * ({x} + {b})",
        f"The result after calculating ({x} + {a}) * ({x} + {b}), what is it",
        f"Determine ({x} + {a}) * ({x} + {b})",
        f"Let's calculate ({x} + {a}) * ({x} + {b})",
        f"The result of ({x} + {a}) * ({x} + {b}), is it true",
        f"Calculating ({x} + {a}) * ({x} + {b})",
        f"The result after calculating x_plus_a_times_x_plus_b for {x}, {a}, and {b}",
        f"The expression ({x} + {a}) * ({x} + {b}), what is its value",
        f"Let's determine the expression ({x} + {a}) * ({x} + {b})",
        f"The expression ({x} + {a}) * ({x} + {b}), what is the result",
        f"The expression ({x} + {a}) * ({x} + {b}), ignoring order",
        f"The result after calculating the expression ({x} + {a}) * ({x} + {b})",
        f"Calculate ({x} + {a}) * ({x} + {b}), find the answer",
        f"The expression ({x} + {a}) * ({x} + {b}), what does it give",
        f"Let's find the result after calculating the expression ({x} + {a}) * ({x} + {b})",
        f"The expression ({x} + {a}) * ({x} + {b}), what is the output",
        f"The result after calculating the expression ({x} + {a}) * ({x} + {b}), what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_x_plus_a_times_x_plus_b_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
