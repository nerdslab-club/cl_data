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


def __random_explanation_logarithm_base_2(value: float) -> str:
    result = math.log2(value)
    explanations = [
        f"Logarithm base 2 of {value}",
        f"log2({value})",
        f"The logarithm base 2 value for {value}",
        f"Calculate logarithm base 2 for {value}",
        f"Logarithm base 2 function applied to {value}",
        f"log2({value}), what is it?",
        f"The result of log2({value})",
        f"Find the logarithm base 2 of {value}",
        f"Logarithm base 2 value when input is {value}",
        f"Input: {value}, logarithm base 2?",
        f"Logarithm base 2 of {value}, tell me",
        f"log2({value}), the answer?",
        f"Calculate log2({value})",
        f"The logarithm base 2 for input {value}",
        f"What is log2({value})?",
        f"Logarithm base 2 of {value}, result?",
        f"log2({value}), find the value",
        f"The logarithm base 2 value for input {value}",
        f"Logarithm base 2 of input {value}, what does it give?",
        f"Find log2({value})",
        f"Logarithm base 2 function for input {value}",
        f"Logarithm base 2 of {value}, what is the result?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_logarithm_base_2_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
