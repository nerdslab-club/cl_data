import random

from src.random_value_generator import RandomValueGenerator
from src.utility import Utility


def create_nlf2nlf_batch_one_example(count: int):
    examples = []
    for _ in range(count):
        example = __get_batch_one_example_pair()
        examples.append({
            "inputStr": example[0],
            "outputStr": example[1]
        })
    return examples


def __get_batch_one_example_pair():
    random_list = Utility.remove_spaces(str(RandomValueGenerator.generate_random_list()))
    random_int_one = RandomValueGenerator.generate_random_integer()
    random_int_two = random_int_one + RandomValueGenerator.generate_random_integer()
    random_int_three = random_int_two + RandomValueGenerator.generate_random_integer()
    random_int_four = RandomValueGenerator.generate_random_integer()
    random_float = RandomValueGenerator.generate_random_float()
    random_bool = RandomValueGenerator.generate_random_boolean()

    examples = [
        (
            f"{random_int_one}*{random_int_four}",
            f"The result of multiplying {random_int_one} by {random_int_four} is ##multiplication({random_int_one},{random_int_four})",
        ),
        (
            f"{random_int_two}+{random_int_three}",
            f"The result of adding {random_int_two} and {random_int_three} is ##addition({random_int_two},{random_int_three})",
        ),
        (
            f"{random_int_three}-{random_int_one}",
            f"The result of subtracting {random_int_three} from {random_int_one} is ##subtraction({random_int_one},{random_int_three})",
        ),
        (
            f"{random_int_two}/{random_int_one}",
            f"The result of dividing {random_int_two} by {random_int_one} is ##division({random_int_two},{random_int_one})",
        ),
        (
            f"What's the total when you add {random_int_two} and {random_int_three}?",
            f"The answer is ##addition({random_int_two},{random_int_three})"
        ),
        (
            f"If you have {random_int_one} cookies and you eat {random_int_four} of them, how many are left?",
            f"You have ##subtraction({random_int_one},{random_int_four}) cookies remaining."
        ),
        (
            f"Imagine you want to split {random_int_three} candies among {random_int_one} children. How many candies will each child receive?",
            f"Each children will receive ##division({random_int_three},{random_int_one}) candies"
        ),
        (
            f"You have {random_int_two} boxes, and each box holds {random_int_four} pencils. How many pencils do you have in total?",
            f"Calculating the total. You have ##multiplication({random_int_two},{random_int_four}) pencils in total"
        ),
        (
            f"If you add {random_float} to {random_int_three}, what's the resulting value?",
            f"The result of adding {random_float} to {random_int_three} is ##addition({random_float},{random_int_three})."
        ),
        (
            f"When you take away {random_int_one} from {random_int_three}, what's the outcome?",
            f"The outcome of subtracting {random_int_one} from {random_int_three} is ##subtraction({random_int_three},{random_int_one})."
        ),
        (
            f"If you divide {random_int_two} by {random_int_four}, what's the quotient?",
            f"The quotient of dividing {random_int_two} by {random_int_four} is ##division({random_int_two},{random_int_four})."
        ),
        (
            f"Suppose you have {random_int_one} groups, and each group consists of {random_int_three} students. How many students are there in total?",
            f"In total, there are ##multiplication({random_int_one},{random_int_three}) students."
        ),
        (
            f"If you add {random_int_two} to {random_float}, what's the sum?",
            f"The sum of {random_int_two} and {random_float} is ##addition({random_int_two},{random_float})."
        ),
        (
            f"When you subtract {random_int_four} from {random_int_three}, what's the result?",
            f"The result of subtracting {random_int_four} from {random_int_three} is ##subtraction({random_int_three},{random_int_four})."
        ),
        (
            f"If you distribute {random_int_three} candies evenly among {random_int_one} kids, how many candies does each child get?",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies."
        ),
        (
            f"What's the total of {random_int_two} and {random_int_three}?",
            f"The sum is ##addition({random_int_two},{random_int_three})"
        ),
        (
            f"If you start with {random_int_one} apples and consume {random_int_four}, how many do you have left?",
            f"You are left with ##subtraction({random_int_one},{random_int_four}) apples."
        ),
        (
            f"If you need to distribute {random_int_three} candies among {random_int_one} children, how many candies will each child get?",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies."
        ),
        (
            f"You have {random_int_two} boxes, and each box contains {random_int_four} pencils. How many pencils are there in total?",
            f"The total number of pencils is ##multiplication({random_int_two},{random_int_four})."
        ),
        (
            f"If you increase {random_float} by {random_int_three}, what's the result?",
            f"The result after increasing {random_float} by {random_int_three} is ##addition({random_float},{random_int_three})."
        ),
        (
            f"When you remove {random_int_one} from {random_int_three}, what's left?",
            f"The remaining value after subtracting {random_int_one} from {random_int_three} is ##subtraction({random_int_three},{random_int_one})."
        ),
        (
            f"If you split {random_int_two} equally among {random_int_four} people, how much does each person get?",
            f"Each person receives ##division({random_int_two},{random_int_four})."
        ),
        (
            f"Imagine you have {random_int_one} teams, and each team consists of {random_int_three} players. How many players are there in total?",
            f"The total number of players is ##multiplication({random_int_one},{random_int_three})."
        ),
        (
            f"If you add {random_int_two} to {random_float}, what's the outcome?",
            f"The outcome of adding {random_int_two} and {random_float} is ##addition({random_int_two},{random_float})."
        ),
        (
            f"When you subtract {random_int_four} from {random_int_three}, what's the answer?",
            f"The answer after subtracting {random_int_four} from {random_int_three} is ##subtraction({random_int_three},{random_int_four})."
        ),
        (
            f"If you distribute {random_int_three} candies evenly among {random_int_one} children, how many candies will each child receive?",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies."
        ),
        (
            f"What's the result when you add {random_int_one} to {random_int_four}?",
            f"The result is ##addition({random_int_one},{random_int_four})."
        ),
        (
            f"If you take {random_int_three} and divide it by {random_int_one}, what's the quotient?",
            f"The quotient after dividing {random_int_three} by {random_int_one} is ##division({random_int_three},{random_int_one})."
        ),
        (
            f"If you have {random_int_two} bags, and each bag contains {random_int_four} marbles, how many marbles are there in total?",
            f"The total number of marbles is ##multiplication({random_int_two},{random_int_four})."
        ),
        (
            f"What's the result of adding {random_int_one} to {random_float}?",
            f"The result is ##addition({random_int_one},{random_float})."
        ),
        (
            f"If you subtract {random_int_four} from {random_int_three}, what's the remaining value?",
            f"The remaining value after subtracting {random_int_four} from {random_int_three} is ##subtraction({random_int_three},{random_int_four})."
        ),
        (
            f"If you divide {random_int_three} by {random_int_one}, what's the outcome?",
            f"The outcome of dividing {random_int_three} by {random_int_one} is ##division({random_int_three},{random_int_one})."
        ),
        (
            f"How many do you get when you add {random_int_two} to {random_int_three}?",
            f"The sum is ##addition({random_int_two},{random_int_three})."
        ),
        (
            f"If you consume {random_int_four} out of {random_int_one} cookies, how many cookies do you have left?",
            f"You have ##subtraction({random_int_one},{random_int_four}) cookies remaining."
        ),
        (
            f"If you evenly distribute {random_int_three} candies among {random_int_one} children, how many candies does each child receive?",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies."
        ),
        (
            f"If you have {random_int_two} boxes, and each box holds {random_int_four} chocolates, how many chocolates do you have in total?",
            f"The total number of chocolates is ##multiplication({random_int_two},{random_int_four})."
        ),
        (
            f"When you increase {random_float} by {random_int_three}, what's the new value?",
            f"The new value after increasing {random_float} by {random_int_three} is ##addition({random_float},{random_int_three})."
        ),
        (
            f"If you remove {random_int_one} from {random_int_three}, what's the result?",
            f"The result after subtracting {random_int_one} from {random_int_three} is ##subtraction({random_int_three},{random_int_one})."
        ),
        (
            f"If you divide {random_int_two} by {random_int_four}, what's the quotient?",
            f"The quotient after dividing {random_int_two} by {random_int_four} is ##division({random_int_two},{random_int_four})."
        ),
        (
            f"Suppose you have {random_int_one} teams, and each team has {random_int_three} members. How many members are there in total?",
            f"The total number of members is ##multiplication({random_int_one},{random_int_three})."
        ),
        (
            f"If you add {random_int_two} to {random_float}, what's the sum?",
            f"The sum of {random_int_two} and {random_float} is ##addition({random_int_two},{random_float})."
        ),
        (
            f"When you subtract {random_int_four} from {random_int_three}, what's the outcome?",
            f"The outcome after subtracting {random_int_four} from {random_int_three} is ##subtraction({random_int_three},{random_int_four})."
        ),
        (
            f"If you distribute {random_int_three} candies evenly among {random_int_one} children, how many candies does each child get?",
            f"Each child will receive ##division({random_int_three},{random_int_one}) candies."
        ),
        (
            f"What do you get when you add {random_int_one} to {random_int_four}?",
            f"The result is ##addition({random_int_one},{random_int_four})."
        ),
        (
            f"If you divide {random_int_three} by {random_int_one}, what's the quotient?",
            f"The quotient after dividing {random_int_three} by {random_int_one} is ##division({random_int_three},{random_int_one})."
        ),
        (
            f"If you have {random_int_two} boxes, and each box contains {random_int_four} pencils, how many pencils are there in total?",
            f"The total number of pencils is ##multiplication({random_int_two},{random_int_four})."
        ),
    ]
    return random.choice(examples)


if __name__ == "__main__":
    __get_batch_one_example_pair()
    pass
