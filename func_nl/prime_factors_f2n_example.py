import random
import sympy

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_prime_factors_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(2, 100)
        prime_factors_result = sympy.factorint(x)
        examples.append(
            {
                "inputStr": f"##prime_factors({x})",
                "outputStr": __random_explanation_prime_factors(
                    x, prime_factors_result
                ),
            }
        )
    return examples


def __random_explanation_prime_factors(n: int, prime_factors_result: dict) -> str:
    explanations = [
        f"The prime factors of {n}",
        f"prime_factors({n})",
        f"The factors of {n} that are prime numbers",
        f"Calculation: prime_factors({n})",
        f"The prime numbers that divide {n}",
        f"The list of prime factors for {n}",
        f"The result of finding the prime factors of {n}",
        f"The prime divisors of {n}",
        f"The factors that are prime numbers for the value {n}",
        f"The prime factorization of {n}",
        f"The result of decomposing {n} into prime factors",
        f"The prime numbers that can divide {n}",
        f"The outcome of determining the prime factors of {n}",
        f"The prime factors of the number {n} are",
        f"The prime factors of the integer {n}",
        f"The prime numbers that are divisors of {n}",
        f"The list of prime divisors for the value {n}",
        f"The calculated prime factors of {n} are",
        f"The prime factorization result of {n} is",
        f"The prime factor decomposition of {n} is",
        f"The prime divisors of {n} are",
        f"The prime factors for the integer {n} are",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_prime_factors_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
