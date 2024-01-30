import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_logarithm_base_10_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": __random_explanation_logarithm_base_10(value, (None if identifier is None else identifier+i)),
                "outputStr": f"##logarithm_base_10({value})",
            }
        )
    return examples


def __random_explanation_logarithm_base_10(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Logarithm base 10 of {f1}",
        f"The logarithm base 10 value for {f1}",
        f"Calculate logarithm base 10 for {f1}",
        f"Logarithm base 10 function applied to {f1}",
        f"log10({f1}), what is it",
        f"The result of log10({f1})",
        f"Find the logarithm base 10 of {f1}",
        f"Logarithm base 10 value when input is {f1}",
        f"Input: {f1}, logarithm base 10",
        f"Logarithm base 10 of {f1}, tell me",
        f"log10({f1}), the answer",
        f"Calculate log10({f1})",
        f"The logarithm base 10 for input {f1}",
        f"What is log10({f1})",
        f"Logarithm base 10 of {f1}, result",
        f"log10({f1}), find the value",
        f"The logarithm base 10 value for input {f1}",
        f"Logarithm base 10 of input {f1}, what does it give",
        f"Logarithm base 10 function for input {f1}",
        f"Logarithm base 10 of {f1}, what is the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_logarithm_base_10_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
