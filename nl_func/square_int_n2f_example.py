import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_square_int_example(count: int):
    examples = []
    for _ in range(count):
        num = RandomValueGenerator.generate_random_integer(1, 10)
        examples.append({
            "inputStr": __random_explanation(num),
            "outputStr": f"##square_int({num})",
        })
    return examples


def __random_explanation(x: int) -> str:
    explanations = [
        f"Calculate the square of the integer {x}",
        f"SQUARE_INT({x})",
        f"Find the square value for the integer {x}",
        f"The result of squaring the integer {x}",
        f"Perform the square operation on the integer {x}",
        f"Squaring the integer {x}",
        f"The square of the integer {x}",
        f"SQUARE_INT calculation: {x}",
        f"The result after squaring the integer {x}, what is it?",
        f"The square value of the integer {x}, what does it give?",
        f"Let's square the integer {x}",
        f"Square the integer {x}, result is",
        f"Calculating the square for the integer {x}",
        f"The squared result after squaring the integer {x}",
        f"The square of the integer {x}, what is its value?",
        f"Let's determine the square of the integer {x}",
        f"The square value of the integer {x}",
        f"Square {x}, what is the result?",
        f"The square of the integer {x}, what does it give?",
        f"Square {x} and provide the result",
        f"SQUARE_INT({x}), what does it yield?",
        f"The square value of the integer {x}, ignoring order",
        f"The result after squaring the integer {x}",
        f"The square of the integer {x}, what is it?",
        f"Calculate the square for the integer {x}, find the answer",
        f"The square value of the integer {x}, what does it give?",
        f"Let's find the result after squaring the integer {x}",
        f"Square {x}, what is the output?",
        f"The squared result after squaring the integer {x}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_square_int_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
