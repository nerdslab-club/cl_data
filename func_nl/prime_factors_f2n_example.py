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


def __random_explanation_prime_factors(x: int, prime_factors_result: dict) -> str:
    prime_factors_str = ", ".join(
        [f"{factor}^{exponent}" for factor, exponent in prime_factors_result.items()]
    )
    explanations = [
        f"The prime factors of {x}",
        f"prime_factors({x})",
        f"The factors of {x} that are prime numbers",
        f"Calculation: prime_factors({x})",
        f"The prime numbers that divide {x}",
        f"The list of prime factors for {x}",
        f"The result of finding the prime factors of {x}",
        f"The prime divisors of {x}",
        f"The factors that are prime numbers for the value {x}",
        f"The prime factorization of {x}",
        f"The result of decomposing {x} into prime factors",
        f"The prime numbers that can divide {x}",
        f"The outcome of determining the prime factors of {x}",
        f"The prime factors of the number {x} are",
        f"The prime factors of the integer {x}",
        f"The prime factors of {x} are represented as {prime_factors_str}",
        f"The prime numbers that are divisors of {x}",
        f"The list of prime divisors for the value {x}",
        f"The calculated prime factors of {x} are",
        f"The prime factorization result of {x} is",
        f"The prime factors of {x} are given by {prime_factors_str}",
        f"The prime factor decomposition of {x} is",
        f"The prime divisors of {x} are",
        f"The prime factors for the integer {x} are",
        f"The prime factors of {x} are determined as {prime_factors_str}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_prime_factors_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
