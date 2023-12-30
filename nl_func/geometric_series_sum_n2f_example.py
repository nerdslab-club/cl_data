import random
from src.constants import TaskTypes
from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_n2f_geometric_series_sum_example(count: int):
    examples = []
    for _ in range(count):
        a = RandomValueGenerator.generate_random_float(1.0, 10.0)
        r = RandomValueGenerator.generate_random_float(0.1, 2.0)
        n = RandomValueGenerator.generate_random_integer(2, 10)
        examples.append({
            "inputStr": __random_explanation(a, r, n),
            "outputStr": f"##geometric_series_sum({a}, {r}, {n})",
        })
    return examples


def __random_explanation(a: float, r: float, n: int) -> str:
    explanations = [
        f"Calculate the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"GEOMETRIC_SERIES_SUM({a}, {r}, {n})",
        f"Determine the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"Find the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The result of calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"Performing the geometric series sum operation for initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"GEOMETRIC_SERIES_SUM calculation: ({a}, {r}, {n})",
        f"The result after calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what is it?",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what does it give?",
        f"Let's calculate the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, result is",
        f"Calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum result after calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what is its value?",
        f"Let's determine the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what is the result?",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what does it give?",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms and provide the result",
        f"GEOMETRIC_SERIES_SUM({a}, {r}, {n}), what does it yield?",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, ignoring order",
        f"The result after calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what is it?",
        f"Calculate the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, find the answer",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what does it give?",
        f"Let's find the result after calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms",
        f"The sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what is the output?",
        f"The result after calculating the sum of a geometric series with initial term {a}, common ratio {r}, and {n} terms, what is it?",
    ]
    return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_geometric_series_sum_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
