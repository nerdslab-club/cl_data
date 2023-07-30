from src.constants import TaskTypes


class FuncToFuncSamples:
    TASK_TYPE = TaskTypes.FUNC_TO_FUNC_TRANSLATION.value

    def __init__(self):
        self.func_to_func_samples = []
        self.__set_func_to_func_samples()
        pass

    def __set_func_to_func_samples(self):
        pass

    def __add_to_func_to_func_samples(self, sample: dict):
        self.func_to_func_samples.append(sample)

    def get_func_to_func_samples(self):
        return self.func_to_func_samples

    @staticmethod
    def create_func_to_func_sample_from_data(
        input_map: dict, output_map: dict, task_type=TASK_TYPE
    ) -> dict:
        return {"inputMap": input_map, "outputMap": output_map, "taskType": task_type}

    @staticmethod
    def create_input_array_from_data(
        token,
        category: dict,
    ) -> list:
        pass

    @staticmethod
    def create_output_array_from_data():
        pass
