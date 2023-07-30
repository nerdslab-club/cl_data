from src.constants import TaskTypes


class NlToFuncSamples:
    TASK_TYPE = TaskTypes.NL_TO_FUNC_TRANSLATION.value

    def __init__(self):
        self.nl_to_func_samples = {}
        self.__set_nl_to_func_samples()
        pass

    def __set_nl_to_func_samples(self):
        pass

    def __add_to_nl_to_func_samples(self):
        pass

    def get_nl_to_func_samples(self):
        return self.nl_to_func_samples
