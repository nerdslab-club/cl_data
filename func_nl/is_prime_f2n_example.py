import random
import sympy

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_is_prime_example(count: int):
    examples = []
    for _ in range(count):
        x = random.randint(1, 100)
        is_prime_result = sympy.isprime(x)
        examples.append(
            {
                "inputStr": f"##is_prime({x})",
                "outputStr": __random_explanation_is_prime(x, is_prime_result),
            }
        )
    return examples


def __random_explanation_is_prime(x: int, is_prime_result: bool) -> str:
    prime_str = "prime" if is_prime_result else "not prime"
    explanations = [
        f"Whether {x} is a prime number",
        f"is_prime({x})",
        f"Checking if {x} is a prime number",
        f"Calculation: is_prime({x})",
        f"Whether {x} is prime or not",
        f"Whether the integer {x} is a prime",
        f"Determining if {x} is a prime number",
        f"Checking if the number {x} is prime",
        f"Finding if {x} is a prime number",
        f"The result of evaluating is_prime({x})",
        f"Verifying if the number {x} is prime",
        f"Whether {x} is a {prime_str} number",
        f"Whether {x} is prime or composite",
        f"Checking if the integer {x} is prime",
        f"Checking if the value {x} is prime",
        f"Finding whether {x} is a {prime_str} number",
        f"Whether the number {x} is {prime_str}",
        f"Whether the value {x} is a prime number",
        f"Determining whether {x} is prime",
        f"The outcome of evaluating is_prime({x}) is",
        f"Verifying whether {x} is a {prime_str} number",
        f"The result of checking if {x} is a prime number is",
        f"The boolean value indicating if {x} is a {prime_str} number",
        f"The outcome of the is_prime({x}) calculation is",
        f"Checking if {x} is a prime number is",
        f"The boolean result of is_prime({x}) is",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_is_prime_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
