from typing import Union

list1: list[Union[str, int]] = [1, 2, "aaa"]
dict1: dict[str, Union[str, int]] = {"name": "jack", "age": 18}


def func1(data: Union[str, int]) -> Union[str, int]:
    pass
