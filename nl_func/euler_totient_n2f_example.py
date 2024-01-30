import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_euler_totient_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        n = RandomValueGenerator.generate_random_integer()
        examples.append({
            "inputStr": __random_explanation(n, (None if identifier is None else identifier+i)),
            "outputStr": f"##euler_totient({n})",
        })
    return examples


def __random_explanation(a: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate the Euler's totient function value for {a}",
        f"Determine the result of Euler's totient function for {a}",
        f"Find the Euler's totient value for {a}",
        f"The result of applying Euler's totient function to {a}",
        f"Performing Euler's totient function operation for {a}",
        f"The Euler's totient value for {a}",
        f"The result after applying Euler's totient function to {a}, what is it",
        f"The Euler's totient value for {a}, what does it give",
        f"Let's calculate the Euler's totient value for {a}",
        f"The Euler's totient value for {a}, result is",
        f"Calculating the Euler's totient value for {a}",
        f"The Euler's totient result after applying Euler's totient function to {a}",
        f"The Euler's totient value for {a}, what is its value",
        f"Let's determine the Euler's totient value for {a}",
        f"The Euler's totient value for {a}, what is the result",
        f"The Euler's totient value for {a}, ignoring order",
        f"The result after applying Euler's totient function to {a}",
        f"Calculate the Euler's totient value for {a}, find the answer",
        f"The Euler's totient value for {a}, what does it give",
        f"Let's find the result after applying Euler's totient function to {a}",
        f"The Euler's totient value for {a}, what is the output",
        f"The result after applying Euler's totient function to {a}, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_euler_totient_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
