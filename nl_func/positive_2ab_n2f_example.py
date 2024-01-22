import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_positive_2ab_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_integer(1, 20)
        b = RandomValueGenerator.generate_random_integer(1, 20)
        examples.append({
            "inputStr": __random_explanation(a, b),
            "outputStr": f"##positive_2ab({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int) -> str:
    explanations = [
        f"Calculate 2({a} * {b})",
        f"POSITIVE_2AB({a}, {b})",
        f"Determine the result of 2ab",
        f"Find the expression 2({a} * {b})",
        f"The result of calculating 2ab",
        f"Performing the positive_2ab operation for {a} and {b}",
        f"The expression 2({a} * {b})",
        f"POSITIVE_2AB operation: ({a}, {b})",
        f"The result after calculating 2ab, what is it?",
        f"Determine 2ab",
        f"Let's calculate 2ab",
        f"The result of 2ab, is it true?",
        f"Calculating 2ab",
        f"The result after calculating positive_2ab for {a} and {b}",
        f"The expression 2({a} * {b}), what is its value?",
        f"Let's determine the expression 2({a} * {b})",
        f"The expression 2({a} * {b})",
        f"The expression 2({a} * {b}), what is the result?",
        f"The expression 2({a} * {b}), what does it give?",
        f"The expression 2({a} * {b}) and provide the result",
        f"POSITIVE_2AB({a}, {b}), what does it yield?",
        f"The expression 2({a} * {b}), ignoring order",
        f"The result after calculating the expression 2({a} * {b})",
        f"Calculate 2({a} * {b}), find the answer",
        f"The expression 2({a} * {b}), what does it give?",
        f"Let's find the result after calculating the expression 2({a} * {b})",
        f"The expression 2({a} * {b}), what is the output?",
        f"The result after calculating the expression 2({a} * {b}), what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_positive_2ab_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
