import git_submodules.function_representation.src.math_functions


class AvgFuncToFuncExamples:
    def __init__(self):
        self.input_tuple_arrays = []
        self.output_tuple_arrays = []
        self.__set_input_tuple_arrays()
        self.__set_output_tuple_arrays()

    def __set_input_tuple_arrays(self):
        self.input_tuple_arrays = [
            [
                (
                    "dfijs",
                    "sdfuuhsd",
                    {
                        "type": 1,
                        "subType": 2,
                        "subSubType": 2,
                    },
                ),
                (
                    [1, 2, 3, 4],
                    {
                        "type": 1,
                        "subType": 2,
                        "subSubType": 2,
                    },
                ),
                (
                    "dfijs",
                    "sdfuuhsd",
                    {
                        "sfj": 1,
                        "sdfds": 2,
                    },
                ),
            ],
            [
                (
                    "dfijs",
                    "sdfuuhsd",
                    {
                        "type": 1,
                        "subType": 2,
                        "subSubType": 2,
                    },
                ),
            ],
        ]

    def __set_output_tuple_arrays(self):
        self.output_tuple_arrays = [
            [
                (
                    "dfijs",
                    "sdfuuhsd",
                    {
                        "type": 1,
                        "subType": 2,
                        "subSubType": 2,
                    },
                ),
            ],
            [
                (
                    "dfijs",
                    "sdfuuhsd",
                    {
                        "type": 1,
                        "subType": 2,
                        "subSubType": 2,
                    },
                ),
            ],
        ]
