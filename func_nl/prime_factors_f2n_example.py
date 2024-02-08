import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_f2n_prime_factors_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        x = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        examples.append(
            {
                "inputStr": f"##prime_factors({x})",
                "outputStr": __random_explanation_prime_factors(
                    x, (None if identifier is None else identifier+i)
                ),
            }
        )
    return examples


def __random_explanation_prime_factors(n: int, identifier: int | None) -> str:
    explanations = [
        f"The prime factors of {n}",
        f"The factors of {n} that are prime numbers",
        f"The prime numbers that divide {n}",
        f"The list of prime factors for {n}",
        f"The result of finding the prime factors of {n}",
        f"The prime divisors of {n}",
        f"The factors that are prime numbers for the value {n}",
        f"The prime factorization of {n}",
        f"The result of decomposing {n} into prime factors",
        f"The prime numbers that can divide {n}",
        f"The outcome of determining the prime factors of {n}",
        f"The prime factors of the integer {n}",
        f"The prime numbers that are divisors of {n}",
        f"The list of prime divisors for the value {n}",
        f"The calculated prime factors of {n} are",
        f"The prime factorization result of {n} is",
        f"The prime factor decomposition of {n} is",
        f"The prime divisors of {n} are",
        f"The prime factors for the integer {n} are",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_prime_factors_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
