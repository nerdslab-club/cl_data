import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_float_to_int_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        value = RandomValueGenerator.generate_random_float(1.0, 100.0)
        examples.append({
            "inputStr": __random_explanation(value, (None if identifier is None else identifier+i)),
            "outputStr": f"##float_to_int({value})",
        })
    return examples


def __random_explanation(f1: float, identifier: int | None) -> str:
    explanations = [
        f"Convert the float value {f1} to an integer",
        f"FLOAT_TO_INT({f1})",
        f"Change the float value {f1} to an integer",
        f"Find the integer equivalent of the float value {f1}",
        f"The result of converting the float value {f1} to an integer",
        f"Performing the float to integer conversion on the value {f1}",
        f"The integer equivalent of the float value {f1}",
        f"FLOAT_TO_INT calculation: {f1}",
        f"The result after converting the float value {f1} to an integer, what is it?",
        f"The integer equivalent of {f1}, what does it give?",
        f"Let's convert the float value {f1} to an integer",
        f"The integer equivalent of the float value {f1}, result is",
        f"Converting the float value {f1} to an integer",
        f"The conversion result after converting the float value {f1} to an integer",
        f"The integer equivalent of the float value {f1}, what is its value?",
        f"Let's determine the integer equivalent of the float value {f1}",
        f"The integer equivalent of the float value {f1}",
        f"The integer equivalent of the float value {f1}, what is the result?",
        f"The integer equivalent of the float value {f1}, what does it give?",
        f"The integer equivalent of the float value {f1} and provide the result",
        f"FLOAT_TO_INT({f1}), what does it yield?",
        f"The integer equivalent of the float value {f1}, ignoring order",
        f"The result after converting the float value {f1} to an integer",
        f"The integer equivalent of the float value {f1}, what is it?",
        f"Convert the float value {f1} to an integer, find the answer",
        f"The integer equivalent of the float value {f1}, what does it give?",
        f"Let's find the result after converting the float value {f1}",
        f"The integer equivalent of the float value {f1}, what is the output?",
        f"The result after converting the float value {f1} to an integer, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_float_to_int_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
