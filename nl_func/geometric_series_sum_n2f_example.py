import random
from cl_data.src.constants import TaskTypes
from cl_data.src.random_value_generator import RandomValueGenerator
from cl_data.src.utility import Utility


def create_n2f_geometric_series_sum_example(count: int, identifier: int | None):
    examples = []
    for i in range(count):
        a = RandomValueGenerator.generate_random_float(1.0, 10.0)
        r = RandomValueGenerator.generate_random_float(0.1, 2.0)
        n = RandomValueGenerator.generate_random_integer(2, 10)
        examples.append({
            "inputStr": __random_explanation(a, r, n, (None if identifier is None else identifier+i)),
            "outputStr": f"##geometric_series_sum({a}, {r}, {n})",
        })
    return examples


def __random_explanation(f1: float, f2: float, a: int, identifier: int | None) -> str:
    explanations = [
        f"Calculate the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"Find the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The result of calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"Performing the geometric series sum operation for initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The result after calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what is it",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what does it give",
        f"Let's calculate the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, result is",
        f"Calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum result after calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what is its value",
        f"Let's determine the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what is the result",
        f"The result after calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what is it",
        f"Calculate the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, find the answer",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what does it give",
        f"Let's find the result after calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms",
        f"The sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what is the output",
        f"The result after calculating the sum of a geometric series with initial term {f1}, common ratio {f2}, and {a} terms, what is it",
    ]
    if identifier is not None:
        return explanations[identifier % len(explanations)]
    else:
        return random.choice(explanations)


if __name__ == "__main__":
    print(
        Utility.create_sample_from_example(
            create_n2f_geometric_series_sum_example(2),
            TaskTypes.NL_TO_FUNC_TRANSLATION
        )
    )
