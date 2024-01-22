import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_reverse_string_example(count: int):
    examples = []
    for _ in range(count):
        input_str = RandomValueGenerator.generate_random_string()
        examples.append({
            "inputStr": __random_explanation(input_str),
            "outputStr": f"##reverse_string('{input_str}')",
        })
    return examples


def __random_explanation(input_str: str) -> str:
    explanations = [
        f"Reverse the string '{input_str}'",
        f"REVERSE_STRING('{input_str}')",
        f"Flip the characters in the string '{input_str}'",
        f"Invert the order of characters in '{input_str}'",
        f"The result of reversing the string '{input_str}'",
        f"Performing the reverse_string operation for '{input_str}'",
        f"The reversed form of the string '{input_str}'",
        f"REVERSE_STRING operation: '{input_str}'",
        f"The result after reversing the string '{input_str}', what is it?",
        f"Turn '{input_str}' backwards",
        f"Let's reverse the string '{input_str}'",
        f"The reversed form of '{input_str}', result is",
        f"Reversing the string '{input_str}'",
        f"The reversed string result after reversing for '{input_str}'",
        f"The reversed form of the string '{input_str}', what is its value?",
        f"Let's determine the reversed form of '{input_str}'",
        f"The reversed form of the string '{input_str}'",
        f"The reversed form of the string '{input_str}', what is the result?",
        f"The reversed form of the string '{input_str}', what does it give?",
        f"The reversed form of the string '{input_str}' and provide the result",
        f"REVERSE_STRING('{input_str}'), what does it yield?",
        f"The reversed form of the string '{input_str}', ignoring order",
        f"The result after reversing the string '{input_str}'",
        f"Reverse the string '{input_str}', find the answer",
        f"Reversing the string '{input_str}', what does it give?",
        f"Let's find the result after reversing the string '{input_str}'",
        f"The reversed form of the string '{input_str}', what is the output?",
        f"The result after reversing the string '{input_str}', what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_reverse_string_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
