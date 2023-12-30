import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_decimal_to_binary_example(count: int):
    examples = []
    for _ in range(count):
        decimal_num = RandomValueGenerator.generate_random_integer(1, 1000)
        examples.append({
            "inputStr": __random_explanation(decimal_num),
            "outputStr": f"##decimal_to_binary({decimal_num})",
        })
    return examples


def __random_explanation(decimal_num: int) -> str:
    explanations = [
        f"Convert the decimal number {decimal_num} to binary",
        f"DECIMAL_TO_BINARY({decimal_num})",
        f"Translate the decimal number {decimal_num} to binary representation",
        f"Convert the decimal number {decimal_num} to its binary equivalent",
        f"The binary representation corresponding to the decimal number {decimal_num}",
        f"Converting the decimal number {decimal_num} to binary",
        f"DECIMAL_TO_BINARY calculation: {decimal_num}",
        f"The result after converting the decimal number {decimal_num} to binary, what is it?",
        f"The binary representation of the decimal number {decimal_num}, what does it give?",
        f"Let's convert the decimal number {decimal_num} to binary",
        f"The binary representation of the decimal number {decimal_num}, result is",
        f"Translating the decimal number {decimal_num} to binary representation",
        f"The binary result after converting the decimal number {decimal_num}",
        f"The binary representation of the decimal number {decimal_num}, what is its value?",
        f"Let's determine the binary representation of the decimal number {decimal_num}",
        f"The binary representation of the decimal number {decimal_num}",
        f"The binary representation of the decimal number {decimal_num}, what is the result?",
        f"The binary representation of the decimal number {decimal_num}, what does it give?",
        f"The binary representation of the decimal number {decimal_num} and provide the result",
        f"DECIMAL_TO_BINARY({decimal_num}), what does it yield?",
        f"The binary representation of the decimal number {decimal_num}, ignoring order",
        f"The result after converting the decimal number {decimal_num} to binary",
        f"The binary representation of the decimal number {decimal_num}, what is it?",
        f"Calculate the binary representation of the decimal number {decimal_num}, find the answer",
        f"The binary representation of the decimal number {decimal_num}, what does it give?",
        f"Let's find the result after converting the decimal number {decimal_num} to binary",
        f"The binary representation of the decimal number {decimal_num}, what is the output?",
        f"The result after converting the decimal number {decimal_num} to binary, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_decimal_to_binary_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
