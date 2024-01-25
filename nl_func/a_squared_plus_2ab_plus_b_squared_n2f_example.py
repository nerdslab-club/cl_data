import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_a_squared_plus_2ab_plus_b_squared_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(a, b, (None if identifier is None else identifier+i)),
            "outputStr": f"##a_squared_plus_2ab_plus_b_squared({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate {a}^2 + 2({a} * {b}) + {b}^2",
        f"A_SQUARED_PLUS_2AB_PLUS_B_SQUARED({a}, {b})",
        f"Determine the result of {a}^2 + 2ab + {b}^2",
        f"Find the expression {a}^2 + 2({a} * {b}) + {b}^2",
        f"The result of calculating {a}^2 + 2ab + {b}^2",
        f"Performing the a_squared_plus_2ab_plus_b_squared operation for {a} and {b}",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2",
        f"A_SQUARED_PLUS_2AB_PLUS_B_SQUARED operation: ({a}, {b})",
        f"The result after calculating {a}^2 + 2ab + {b}^2, what is it?",
        f"Determine {a}^2 + 2ab + {b}^2",
        f"Let's calculate {a}^2 + 2ab + {b}^2",
        f"The result of {a}^2 + 2ab + {b}^2, is it true?",
        f"Calculating {a}^2 + 2ab + {b}^2",
        f"The result after calculating a_squared_plus_2ab_plus_b_squared for {a} and {b}",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2, what is its value?",
        f"Let's determine the expression {a}^2 + 2({a} * {b}) + {b}^2",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2, what is the result?",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2, what does it give?",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2 and provide the result",
        f"A_SQUARED_PLUS_2AB_PLUS_B_SQUARED({a}, {b}), what does it yield?",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2, ignoring order",
        f"The result after calculating the expression {a}^2 + 2({a} * {b}) + {b}^2",
        f"Calculate {a}^2 + 2({a} * {b}) + {b}^2, find the answer",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2, what does it give?",
        f"Let's find the result after calculating the expression {a}^2 + 2({a} * {b}) + {b}^2",
        f"The expression {a}^2 + 2({a} * {b}) + {b}^2, what is the output?",
        f"The result after calculating the expression {a}^2 + 2({a} * {b}) + {b}^2, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_a_squared_plus_2ab_plus_b_squared_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
