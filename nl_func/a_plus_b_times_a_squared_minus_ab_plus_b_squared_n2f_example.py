import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_a_plus_b_times_a_squared_minus_ab_plus_b_squared_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(a, b, (None if identifier is None else identifier+i)),
            "outputStr": f"##a_plus_b_times_a_squared_minus_ab_plus_b_squared({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"Determine the result of ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"Find the expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"The result of calculating ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"Performing the a_plus_b_times_a_squared_minus_ab_plus_b_squared operation for {a} and {b}",
        f"The expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"The result after calculating ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), what is it",
        f"Determine ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"Let's calculate ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"The result of ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), is it true",
        f"Calculating ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"The result after calculating a_plus_b_times_a_squared_minus_ab_plus_b_squared for {a} and {b}",
        f"The expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), what is its value",
        f"Let's determine the expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"The expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), what is the result",
        f"The result after calculating the expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"Calculate ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), find the answer",
        f"The expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), what does it give",
        f"Let's find the result after calculating the expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2)",
        f"The expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), what is the output",
        f"The result after calculating the expression ({a} + {b}) * ({a}^2 - {a * b} + {b}^2), what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_plus_b_times_a_squared_minus_ab_plus_b_squared_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
