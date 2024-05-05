import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_prime_factors_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        examples.append({
            "inputStr": __random_explanation(num, (None if identifier is None else identifier+i)),
            "outputStr": f"##prime_factors({num})",
        })
    return examples


def __random_explanation(x: int, identifier: int | None) -> str:
    explanations = [
        f"The list of prime numbers that divide {x}",
        f"The prime factors of {x}",
        f"Find the prime factors of {x}",
        f"Calculate the prime factors of {x}",
        f"Finding prime factors for {x}",
        f"prime factors calculation: {x}",
        f"Let's find the prime factors of {x}",
        f"Find the prime factors for {x}",
        f"The prime factors of {x}, result is",
        f"Calculating the prime factors of {x}",
        f"Let's determine the prime factors of {x}",
        f"{x}, what are its prime factors",
        f"Finding the prime factors of {x}",
        f"Find the prime factors of {x} and provide the result",
        f"The prime factors of {x}, ignoring order",
        f"Calculate the prime factors of {x}, find the answer",
        f"Let's find the list of prime numbers that divide {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_prime_factors_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
