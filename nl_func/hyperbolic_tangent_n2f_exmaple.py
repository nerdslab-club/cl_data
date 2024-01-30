import random

from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_hyperbolic_tangent_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_float()
        examples.append(
            {
                "inputStr": __random_explanation_hyperbolic_tangent(value, (None if identifier is None else identifier+i)),
                "outputStr": f"##hyperbolic_tangent({value})",
            }
        )
    return examples


def __random_explanation_hyperbolic_tangent(value: float, identifier: int | None) -> str:
    explanations = [
        f"Hyperbolic tangent of {value}",
        f"The hyperbolic tangent value for {value}",
        f"Calculate hyperbolic tangent for {value}",
        f"Hyperbolic tangent function applied to {value}",
        f"Tanh({value}), what is it",
        f"The result of tanh({value})",
        f"Find the hyperbolic tangent of {value}",
        f"Hyperbolic tangent value when input is {value}",
        f"Input: {value}, hyperbolic tangent",
        f"Hyperbolic tangent of {value}, tell me",
        f"Tanh({value}), the answer",
        f"Calculate tanh({value})",
        f"The hyperbolic tangent for input {value}",
        f"What is tanh({value})",
        f"Hyperbolic tangent of {value}, result",
        f"Tanh({value}), find the value",
        f"The hyperbolic tangent value for input {value}",
        f"Hyperbolic tangent of input {value}, what does it give",
        f"Find tanh({value})",
        f"Hyperbolic tangent function for input {value}",
        f"Hyperbolic tangent of {value}, what is the result",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_hyperbolic_tangent_example(2), TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
