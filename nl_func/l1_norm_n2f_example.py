import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_l1_norm_example(count: int):
    examples = []
    for _ in range(count):
        vector = RandomValueGenerator.generate_random_list(3, -10, 10)
        examples.append({
            "inputStr": __random_explanation(vector),
            "outputStr": f"##l1_norm({vector})",
        })
    return examples


def __random_explanation(vector: list) -> str:
    explanations = [
        f"Calculate the L1 norm of the vector {vector}",
        f"L1_NORM({vector})",
        f"Determine the result of the L1 norm for the vector {vector}",
        f"Find the L1 norm of the vector {vector}",
        f"The result of calculating the L1 norm of the vector {vector}",
        f"Performing the L1 norm calculation for the vector {vector}",
        f"The L1 norm of the vector {vector}",
        f"L1_NORM calculation: {vector}",
        f"The result after calculating the L1 norm of the vector {vector}, what is it?",
        f"The L1 norm of the vector {vector}, what does it give?",
        f"Let's calculate the L1 norm of the vector {vector}",
        f"The L1 norm of the vector {vector}, result is",
        f"Calculating the L1 norm of the vector {vector}",
        f"The L1 norm result after calculating L1 norm for the vector {vector}",
        f"The L1 norm of the vector {vector}, what is its value?",
        f"Let's determine the L1 norm of the vector {vector}",
        f"The L1 norm of the vector {vector}",
        f"The L1 norm of the vector {vector}, what is the result?",
        f"The L1 norm of the vector {vector}, what does it give?",
        f"The L1 norm of the vector {vector} and provide the result",
        f"L1_NORM({vector}), what does it yield?",
        f"The L1 norm of the vector {vector}, ignoring order",
        f"The result after calculating the L1 norm of the vector {vector}",
        f"The L1 norm of the vector {vector}, what is it?",
        f"Calculate the L1 norm of the vector {vector}, find the answer",
        f"The L1 norm of the vector {vector}, what does it give?",
        f"Let's find the result after calculating the L1 norm of the vector {vector}",
        f"The L1 norm of the vector {vector}, what is the output?",
        f"The result after calculating the L1 norm of the vector {vector}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_l1_norm_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
