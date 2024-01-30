import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_positive_2ab_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_integer()
        b = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(a, b, (None if identifier is None else identifier+i)),
            "outputStr": f"##positive_2ab({a}, {b})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate 2({a} * {b})",
        f"Find the expression 2({a} * {b})",
        f"Performing the positive_2ab operation for {a} and {b}",
        f"The expression 2({a} * {b})",
        f"The result after calculating positive_2ab for {a} and {b}",
        f"The expression 2({a} * {b}), what is its value?",
        f"Let's determine the expression 2({a} * {b})",
        f"The expression 2({a} * {b}), what is the result?",
        f"POSITIVE_2AB({a}, {b}), what does it yield?",
        f"The result after calculating the expression 2({a} * {b})",
        f"Calculate 2({a} * {b}), find the answer",
        f"The expression 2({a} * {b}), what does it give?",
        f"Let's find the result after calculating the expression 2({a} * {b})",
        f"The expression 2({a} * {b}), what is the output?",
        f"The result after calculating the expression 2({a} * {b}), what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_positive_2ab_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
