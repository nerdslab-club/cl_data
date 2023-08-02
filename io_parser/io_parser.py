from git_submodules.function_representation import MathFunctions
import re


class IoParser:
    def __init__(self):
        pass

    @staticmethod
    def parseInputString(input_str: str) -> list:
        result = []
        words = input_str.split()
        for word in words:
            try:
                num = int(word)
                result.append(num)
            except ValueError:
                try:
                    num = float(word)
                    result.append(num)
                except ValueError:
                    result.append(word)
        return result

    @staticmethod
    def extract_function_params(input_func_str: str):
        # Use regular expression to find the function name and parameters
        pattern = r"([\$\#@]+[a-zA-Z_][a-zA-Z0-9_]*)\(([^)]*)\)"
        matches = re.findall(pattern, input_func_str)

        if not matches:
            return []

        function_name, param_str = matches[0]
        params = [p.strip() for p in param_str.split(",")]
        internal_array = []

        # Convert parameters to appropriate data types
        processed_params = []
        for param in params:
            param = param.strip()
            if len(internal_array) != 0 and not param.endswith("]"):
                internal_array.append(str(param))
            elif param.lower() == "true":
                processed_params.append(True)
            elif param.lower() == "false":
                processed_params.append(False)
            elif param.isdigit():
                processed_params.append(int(param))
            elif re.match(r"^[+-]?([0-9]*[.])?[0-9]+$", param):
                processed_params.append(float(param))
            elif param.startswith("["):
                internal_array.append(str(param[1:]))
            elif param.endswith("]"):
                internal_array.append(str(param[:-1]))
                processed_params.append(internal_array)
                internal_array = []
            else:
                processed_params.append(IoParser.remove_quotes(param))

        return [function_name] + processed_params

    @staticmethod
    def remove_quotes(input_string: str):
        if input_string.startswith("'") and input_string.endswith("'"):
            return input_string[1:-1]
        elif input_string.startswith('"') and input_string.endswith('"'):
            return input_string[1:-1]
        else:
            return input_string

    @staticmethod
    def addCategoryMap(output_array: list) -> list:
        """Create category Map foreach token and associate that with the token.

        :param output_array:
        :return: list of tuple(token, category_map)
        """
        pass

    @staticmethod
    def getExampleInputArrays():
        return [
            "$$addition(3,4)",
            "##addition(3,4)",
            "##division(##sum([2,3,4]), ##length([2,3,4]))",
            "function for averaging list of number",
            "adding 3 plus 2",
            "@@average(@list)" "3 + 2 = 5",
            "3 + 2 = ##addition(3,2)",
        ]

    @staticmethod
    def getExampleOutputArrays():
        return [
            [
                7,
            ],
            [
                MathFunctions.addition,
                3,
                4,
            ],
            [
                MathFunctions.division,
                MathFunctions.sum,
                [2, 3, 4],
                MathFunctions.length,
                [2, 3, 4],
            ],
            [
                "function",
                "for",
                "averaging",
                "list",
                "of",
                "number",
            ],
            [
                "adding",
                3,
                "plus",
                2,
            ],
            [
                MathFunctions.average,
                "@list",
            ],
            [
                3,
                "+",
                2,
                "=",
                5,
            ],
            [
                3,
                "+",
                2,
                "=",
                MathFunctions.addition,
                3,
                2,
            ],
        ]


if __name__ == "__main__":
    # Test the function with different input strings
    input_strings = [
        "$$addition(3, 50.0)",
        "##division(4.5, 2)",
        "@@average(1.5, 2.5, 3.5)",
        "$$combination([1,2,3], 'hello', True, 2.5)",
    ]

    for input_string in input_strings:
        output_list = IoParser.extract_function_params(input_string)
        print(output_list)


# additional functionality
# batch parse
# tuple creating
