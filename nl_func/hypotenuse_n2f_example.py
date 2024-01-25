import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_hypotenuse_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        side_a = RandomValueGenerator.generate_random_float(1.0, 10.0)
        side_b = RandomValueGenerator.generate_random_float(1.0, 10.0)
        examples.append({
            "inputStr": __random_explanation(side_a, side_b, (None if identifier is None else identifier+i)),
            "outputStr": f"##hypotenuse({side_a}, {side_b})",
        })
    return examples


def __random_explanation(f1: float, f2: float, identifier: int | None) -> str:
    explanations = [
        f"Calculate the hypotenuse for the sides {f1} and {f2}",
        f"HYPOTENUSE({f1}, {f2})",
        f"Determine the hypotenuse for the sides {f1} and {f2}",
        f"Find the hypotenuse value for the sides {f1} and {f2}",
        f"The result of calculating the hypotenuse for sides {f1} and {f2}",
        f"Performing the hypotenuse operation on the sides {f1} and {f2}",
        f"The hypotenuse for sides {f1} and {f2}",
        f"HYPOTENUSE calculation: ({f1}, {f2})",
        f"The result after calculating the hypotenuse for sides {f1} and {f2}, what is it?",
        f"The hypotenuse value of sides {f1} and {f2}, what does it give?",
        f"Let's calculate the hypotenuse for the sides {f1} and {f2}",
        f"The hypotenuse value for the sides {f1} and {f2}, result is",
        f"Calculating the hypotenuse for the sides {f1} and {f2}",
        f"The hypotenuse result after calculating the hypotenuse for sides {f1} and {f2}",
        f"The hypotenuse for sides {f1} and {f2}, what is its value?",
        f"Let's determine the hypotenuse for the sides {f1} and {f2}",
        f"The hypotenuse value for the sides {f1} and {f2}",
        f"The hypotenuse for the sides {f1} and {f2}, what is the result?",
        f"The hypotenuse for the sides {f1} and {f2}, what does it give?",
        f"The hypotenuse for the sides {f1} and {f2} and provide the result",
        f"HYPOTENUSE({f1}, {f2}), what does it yield?",
        f"The hypotenuse value for the sides {f1} and {f2}, ignoring order",
        f"The result after calculating the hypotenuse for sides {f1} and {f2}",
        f"The hypotenuse for the sides {f1} and {f2}, what is it?",
        f"Calculate the hypotenuse for the sides {f1} and {f2}, find the answer",
        f"The hypotenuse for the sides {f1} and {f2}, what does it give?",
        f"Let's find the result after calculating the hypotenuse for sides {f1} and {f2}",
        f"The hypotenuse for the sides {f1} and {f2}, what is the output?",
        f"The result after calculating the hypotenuse for sides {f1} and {f2}, what is it?",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_hypotenuse_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
