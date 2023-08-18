import random

from src.constants import TaskTypes
from src.utility import Utility


def create_f2n_decimal_to_binary_example(count: int):
    examples = []
    for _ in range(count):
        decimal = random.randint(1, 1000)
        examples.append(
            {
                "inputStr": f"##decimal_to_binary({decimal})",
                "outputStr": __random_explanation_decimal_to_binary(decimal),
            }
        )
    return examples


def __random_explanation_decimal_to_binary(decimal: int) -> str:
    explanations = [
        f"The binary representation of the decimal number {decimal}",
        f"decimal_to_binary({decimal})",
        f"The result of converting the decimal number {decimal} to binary",
        f"Calculation: decimal_to_binary({decimal})",
        f"The binary number obtained by converting the decimal number {decimal}",
        f"The outcome of converting the decimal number {decimal} to its binary representation",
        f"The binary value of the decimal number {decimal}",
        f"The result of transforming the decimal number {decimal} into binary form",
        f"The computed result of converting the decimal number {decimal} to binary",
        f"The binary number obtained from the decimal number {decimal}",
        f"The outcome of evaluating decimal_to_binary({decimal})",
        f"The binary value calculated from the decimal number {decimal}",
        f"The result of evaluating decimal_to_binary({decimal})",
        f"The binary number represented by the decimal number {decimal}",
        f"The computed binary value of the decimal number {decimal}",
        f"The binary representation obtained by converting the decimal number {decimal}",
        f"The result derived from converting the decimal number {decimal} into binary",
        f"The calculated outcome of evaluating decimal_to_binary({decimal})",
        f"The binary value corresponding to the decimal number {decimal}",
        f"The computed binary result of decimal_to_binary({decimal})",
        f"The calculated binary representation of the decimal number {decimal}",
        f"The binary value calculated by converting the decimal number {decimal}",
        f"The result obtained by converting the decimal number {decimal} to binary",
        f"The computed binary equivalent of the decimal number {decimal}",
        f"The calculated binary value obtained from the decimal number {decimal}",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_f2n_decimal_to_binary_example(2), TaskTypes.FUNC_TO_NL_TRANSLATION
        )
    )
