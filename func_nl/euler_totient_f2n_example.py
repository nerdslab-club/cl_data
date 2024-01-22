import random

from cl_data.src.constants import TaskTypes
from cl_data.src.utility import Utility


def create_f2n_euler_totient_example(count: int):
    examples = []
    for _ in range(count):
        n = random.randint(1, 50)
        examples.append(
            {
                "inputStr": f"##euler_totient({n})",
                "outputStr": __random_explanation_euler_totient(n),
            }
        )
    return examples


def __random_explanation_euler_totient(n: int) -> str:
    explanations = [
        f"The Euler's totient function value for the integer {n}",
        f"euler_totient({n})",
        f"The result of calculating Euler's totient function for the integer {n}",
        f"Calculation: euler_totient({n})",
        f"The value of Euler's totient function for the number {n}",
        f"The outcome of finding the value of Euler's totient function for the integer {n}",
        f"The phi value of the integer {n} using Euler's totient function",
        f"The result of determining Euler's totient function value for the integer {n}",
        f"The computed result of calculating Euler's totient function for the integer {n}",
        f"The Euler's totient coefficient for the integer {n}",
        f"The outcome of evaluating euler_totient({n})",
        f"The value obtained by calculating Euler's totient function for the integer {n}",
        f"The result of evaluating euler_totient({n})",
        f"The totient value of the integer {n} using Euler's totient function",
        f"The computed Euler's totient function value of the integer {n}",
        f"The Euler's totient coefficient of the integer {n}",
        f"The calculated result of determining Euler's totient function value for the integer {n}",
        f"The phi coefficient of the integer {n} using Euler's totient function",
        f"The result obtained from calculating Euler's totient function for the integer {n}",
        f"The computed value of Euler's totient function for the integer {n}",
        f"The Euler's totient value for the number {n} is",
        f"The result derived from calculating Euler's totient function for the integer {n}",
        f"The computed phi value of the integer {n} using Euler's totient function",
        f"The Euler's totient value obtained by evaluating euler_totient({n})",
        f"The calculated outcome of evaluating euler_totient({n})",
        f"The computed totient value of the integer {n} using Euler's totient function",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_euler_totient_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
