from .constants import CategoryType, CategorySubType, CategorySubSubType


class Utility:
    def __init__(self):
        pass

    @staticmethod
    def create_category_map(
        category_type: CategoryType,
        category_sub_type: CategorySubType,
        category_sub_sub_type: CategorySubSubType,
    ) -> dict:
        return {
            "type": category_type.value,
            "subType": category_sub_type.value,
            "subSubType": category_sub_sub_type.value,
        }
