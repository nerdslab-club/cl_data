import random
import math  # Import the math module for logarithm base 2 function

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_logarithm_base_2_example(count: int):
    examples = []
    for _ in range(count):
        value = round(random.uniform(0.1, 1000), 2)  # Random positive value in a suitable range
        examples.append(
            {
                "inputStr": __random_explanation_logarithm_base_2(value),
                "outputStr": f"##logarithm_base_2({value})",
            }
        )
    return examples


def __random_explanation_logarithm_base_2(f1: float) -> str:
    explanations = [
        f"Logarithm base 2 of {f1}",
        f"log2({f1})",
        f"The logarithm base 2 value for {f1}",
        f"Calculate logarithm base 2 for {f1}",
        f"Logarithm base 2 function applied to {f1}",
        f"log2({f1}), what is it?",
        f"The result of log2({f1})",
        f"Find the logarithm base 2 of {f1}",
        f"Logarithm base 2 value when input is {f1}",
        f"Input: {f1}, logarithm base 2?",
        f"Logarithm base 2 of {f1}, tell me",
        f"log2({f1}), the answer?",
        f"Calculate log2({f1})",
        f"The logarithm base 2 for input {f1}",
        f"What is log2({f1})?",
        f"Logarithm base 2 of {f1}, result?",
        f"log2({f1}), find the value",
        f"The logarithm base 2 value for input {f1}",
        f"Logarithm base 2 of input {f1}, what does it give?",
        f"Find log2({f1})",
        f"Logarithm base 2 function for input {f1}",
        f"Logarithm base 2 of {f1}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_logarithm_base_2_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
