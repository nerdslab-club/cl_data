import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_nth_root_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num = RandomValueGenerator.generate_random_float(seed=(None if identifier is None else identifier+i))
        root = RandomValueGenerator.generate_random_integer(2, 5, seed=(None if identifier is None else identifier+i+1))
        examples.append({
            "inputStr": __random_explanation(num, root, (None if identifier is None else identifier+i)),
            "outputStr": f"##nth_root({num}, {root})",
        })
    return examples


def __random_explanation(x: float, n: int, identifier: int | None) -> str:
    explanations = [
        f"taking the {n} -th root of {x}",
        f"{n} -th root value of {x}",
        f"Calculate the {n} -th root of the number {x}",
        f"Find the {n} -th root value for the number {x}",
        f"The result of taking the {n} -th root of {x}",
        f"Performing the {n} -th root operation on the number {x}",
        f"The {n} -th root of the number {x}",
        f"NTH_ROOT calculation: {x}, {n}",
        f"{n} -th root of {x}, result is",
        f"Calculating the {n} -th root for the number {x}",
        f"The {n} -th root result after taking the {n} -th root of {x}",
        f"Let's determine the {n} -th root of the number {x}",
        f"The {n} -th root value of {x}",
        f"{n} -th root {x} and provide the result",
        f"NTH_ROOT({x}, {n}), what does it yield",
        f"The {n} -th root value of {x}, ignoring order",
        f"Calculate the {n} -th root of {x}, find the answer",
        f"Let's find the result after taking the {n} -th root of {x}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_nth_root_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
