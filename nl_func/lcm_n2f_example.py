import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_lcm_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        num1 = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i))
        num2 = RandomValueGenerator.generate_random_integer(seed=(None if identifier is None else identifier+i+1))
        examples.append({
            "inputStr": __random_explanation(num1, num2, (None if identifier is None else identifier+i)),
            "outputStr": f"##lcm({num1}, {num2})",
        })
    return examples


def __random_explanation(a: int, b: int, identifier: int | None) -> str:
    explanations = [
        f"The least common multiple of {a} and {b}",
        f"LCM of {a} and {b}",
        f"Find the least common multiple of {a} and {b}",
        f"Calculate the least common multiple of {a} and {b}",
        f"Finding LCM for {a} and {b}",
        f"{a} and {b}, what is their least common multiple",
        f"The smallest number that is a multiple of both {a} and {b}",
        f"The LCM for {a} and {b}",
        f"Let's find the least common multiple of {a} and {b}",
        f"Find the LCM for {a} and {b}",
        f"{a} and {b}, their LCM",
        f"The least common multiple when you have {a} and {b}",
        f"Common multiple of {a} and {b}",
        f"The multiple common to {a} and {b}",
        f"LCM of {a} and {b}, find the answer",
        f"The smallest number that is divisible by both {a} and {b}",
        f"Let's determine the LCM of {a} and {b}",
        f"{a} and {b}, what is their common multiple",
        f"LCM calculation for {a} and {b}",
        f"The least common multiple of numbers {a} and {b}",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_lcm_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
