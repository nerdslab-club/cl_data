import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_power_of_ten_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        exponent = RandomValueGenerator.generate_random_integer(-5, 5)
        examples.append({
            "inputStr": __random_explanation(exponent, (None if identifier is None else identifier+i)),
            "outputStr": f"##power_of_ten({exponent})",
        })
    return examples


def __random_explanation(x: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate 10 raised to the power of {x}",
        f"POWER_OF_TEN({x})",
        f"Find the result of 10 to the power of {x}",
        f"The result of raising 10 to the power of {x}",
        f"Performing the power of ten operation with exponent {x}",
        f"10 raised to the power of {x}",
        f"POWER_OF_TEN calculation: {x}",
        f"The result after raising 10 to the power of {x}, what is it?",
        f"10 to the power of {x}, what does it give?",
        f"Let's find 10 to the power of {x}",
        f"10 to the power of {x}, result is",
        f"Calculating 10 raised to the power of {x}",
        f"The result after raising 10 to the power of {x}",
        f"10 raised to the power of {x}, what is its value?",
        f"Let's determine 10 to the power of {x}",
        f"10 raised to the power of {x}",
        f"10 to the power of {x}, what is the result?",
        f"10 to the power of {x}, what does it give?",
        f"10 to the power of {x} and provide the result",
        f"POWER_OF_TEN({x}), what does it yield?",
        f"The result of 10 to the power of {x}, ignoring order",
        f"The result after raising 10 to the power of {x}",
        f"10 raised to the power of {x}, what is it?",
        f"Calculate 10 raised to the power of {x}, find the answer",
        f"The result of 10 to the power of {x}, what does it give?",
        f"Let's find the result after raising 10 to the power of {x}",
        f"10 to the power of {x}, what is the output?",
        f"The result after raising 10 to the power of {x}, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_power_of_ten_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
