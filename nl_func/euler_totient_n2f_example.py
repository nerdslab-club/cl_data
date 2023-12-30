import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_euler_totient_example(count: int):
    examples = []
    for _ in range(count):
        n = RandomValueGenerator.generate_random_integer(2, 100)
        examples.append({
            "inputStr": __random_explanation(n),
            "outputStr": f"##euler_totient({n})",
        })
    return examples


def __random_explanation(n: int) -> str:
    explanations = [
        f"Calculate the Euler's totient function value for {n}",
        f"EULER_TOTIENT({n})",
        f"Determine the result of Euler's totient function for {n}",
        f"Find the Euler's totient value for {n}",
        f"The result of applying Euler's totient function to {n}",
        f"Performing Euler's totient function operation for {n}",
        f"The Euler's totient value for {n}",
        f"EULER_TOTIENT calculation: {n}",
        f"The result after applying Euler's totient function to {n}, what is it?",
        f"The Euler's totient value for {n}, what does it give?",
        f"Let's calculate the Euler's totient value for {n}",
        f"The Euler's totient value for {n}, result is",
        f"Calculating the Euler's totient value for {n}",
        f"The Euler's totient result after applying Euler's totient function to {n}",
        f"The Euler's totient value for {n}, what is its value?",
        f"Let's determine the Euler's totient value for {n}",
        f"The Euler's totient value for {n}",
        f"The Euler's totient value for {n}, what is the result?",
        f"The Euler's totient value for {n}, what does it give?",
        f"The Euler's totient value for {n} and provide the result",
        f"EULER_TOTIENT({n}), what does it yield?",
        f"The Euler's totient value for {n}, ignoring order",
        f"The result after applying Euler's totient function to {n}",
        f"The Euler's totient value for {n}, what is it?",
        f"Calculate the Euler's totient value for {n}, find the answer",
        f"The Euler's totient value for {n}, what does it give?",
        f"Let's find the result after applying Euler's totient function to {n}",
        f"The Euler's totient value for {n}, what is the output?",
        f"The result after applying Euler's totient function to {n}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_euler_totient_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
