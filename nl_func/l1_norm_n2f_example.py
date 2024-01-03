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
    lst_str = ", ".join(str(num) for num in vector)
    explanations = [
        f"Calculate the L1 norm of the vector {lst_str}",
        f"L1_NORM({vector})",
        f"Determine the result of the L1 norm for the vector {lst_str}",
        f"Find the L1 norm of the vector {lst_str}",
        f"The result of calculating the L1 norm of the vector {lst_str}",
        f"Performing the L1 norm calculation for the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}",
        f"L1_NORM calculation: {lst_str}",
        f"The result after calculating the L1 norm of the vector {lst_str}, what is it?",
        f"The L1 norm of the vector {lst_str}, what does it give?",
        f"Let's calculate the L1 norm of the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}, result is",
        f"Calculating the L1 norm of the vector {lst_str}",
        f"The L1 norm result after calculating L1 norm for the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}, what is its value?",
        f"Let's determine the L1 norm of the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}, what is the result?",
        f"The L1 norm of the vector {lst_str}, what does it give?",
        f"The L1 norm of the vector {lst_str} and provide the result",
        f"L1_NORM({vector}), what does it yield?",
        f"The L1 norm of the vector {lst_str}, ignoring order",
        f"The result after calculating the L1 norm of the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}, what is it?",
        f"Calculate the L1 norm of the vector {lst_str}, find the answer",
        f"The L1 norm of the vector {lst_str}, what does it give?",
        f"Let's find the result after calculating the L1 norm of the vector {lst_str}",
        f"The L1 norm of the vector {lst_str}, what is the output?",
        f"The result after calculating the L1 norm of the vector {lst_str}, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_l1_norm_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
