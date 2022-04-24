from typing import (
    Any,
    Dict,
    TypeVar,
    Hashable,
)

from pydantic import BaseModel

Model = TypeVar("Model", bound=BaseModel)
DEFAULT_EXCLUDE = ("cls", "self", "__class__")


def filter_dictionary_none_values(dictionary: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Pop NoneType values and convert everything to str, designed?for=params
    :param dictionary: source dict
    :return: filtered dict
    """
    return {k: str(v) for k, v in dictionary.items() if v is not None}


def make_payload(**kwargs: Any) -> Dict[Hashable, Any]:
    exclude_list = kwargs.pop("exclude", ())
    return {
        key: value
        for key, value in kwargs.items()
        if key not in DEFAULT_EXCLUDE + exclude_list and value is not None
    }
