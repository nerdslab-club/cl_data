import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_a_cubed_plus_b_cubed_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(a, b, (None if identifier is None else identifier+i)),
            "outputStr": f"##a_cubed_plus_b_cubed({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Performing the a_cubed_plus_b_cubed operation for {a} and {b}",
        f"Calculate {a}^3 + {b}^3",
        f"Determine the result of {a}^3 + {b}^3",
        f"Find the expression {a}^3 + {b}^3",
        f"The result of calculating {a}^3 + {b}^3",
        f"The expression {a}^3 + {b}^3",
        f"The result after calculating {a}^3 + {b}^3, what is it",
        f"Determine {a}^3 + {b}^3",
        f"Let's calculate {a}^3 + {b}^3",
        f"The result of {a}^3 + {b}^3, is it true",
        f"Calculating {a}^3 + {b}^3",
        f"The result after calculating a_cubed_plus_b_cubed for {a} and {b}",
        f"The expression {a}^3 + {b}^3, what is its value",
        f"Let's determine the expression {a}^3 + {b}^3",
        f"The expression {a}^3 + {b}^3, what is the result",
        f"The result after calculating the expression {a}^3 + {b}^3",
        f"Calculate {a}^3 + {b}^3, find the answer",
        f"The expression {a}^3 + {b}^3, what does it give",
        f"Let's find the result after calculating the expression {a}^3 + {b}^3",
        f"The expression {a}^3 + {b}^3, what is the output",
        f"The result after calculating the expression {a}^3 + {b}^3, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_cubed_plus_b_cubed_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
