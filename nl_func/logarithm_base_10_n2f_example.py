import random
import math  # Import the math module for logarithm base 10 function

from src.constants import TaskTypes
from src.utility import Utility


def create_n2f_logarithm_base_10_example(count: int):
    examples = []
    for _ in range(count):
        value = round(random.uniform(0.1, 1000), 2)  # Random positive value in a suitable range
        examples.append(
            {
                "inputStr": __random_explanation_logarithm_base_10(value),
                "outputStr": f"##logarithm_base_10({value})",
            }
        )
    return examples


def __random_explanation_logarithm_base_10(value: float) -> str:
    result = math.log10(value)
    explanations = [
        f"Logarithm base 10 of {value}",
        f"log10({value})",
        f"The logarithm base 10 value for {value}",
        f"Calculate logarithm base 10 for {value}",
        f"Logarithm base 10 function applied to {value}",
        f"log10({value}), what is it?",
        f"The result of log10({value})",
        f"Find the logarithm base 10 of {value}",
        f"Logarithm base 10 value when input is {value}",
        f"Input: {value}, logarithm base 10?",
        f"Logarithm base 10 of {value}, tell me",
        f"log10({value}), the answer?",
        f"Calculate log10({value})",
        f"The logarithm base 10 for input {value}",
        f"What is log10({value})?",
        f"Logarithm base 10 of {value}, result?",
        f"log10({value}), find the value",
        f"The logarithm base 10 value for input {value}",
        f"Logarithm base 10 of input {value}, what does it give?",
        f"Find log10({value})",
        f"Logarithm base 10 function for input {value}",
        f"Logarithm base 10 of {value}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_logarithm_base_10_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
