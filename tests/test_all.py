import pytest
from typing import Any, assert_type, Literal
import typejson as jt


def test_all():
    def test_is_json_number(obj: str | jt.Number) -> jt.Number | Literal[False]:
        if jt.is_json_number(obj):
            assert_type(obj, jt.Number)
            return obj
        return False

    def test_is_json_scalar(obj: dict | bool | None) -> jt.Scalar | Literal[False]:
        if jt.is_json_scalar(obj):
            assert_type(obj, bool | None)
            return obj
        return False

    def test_is_json_array(obj: dict | list[str]) -> jt.ArrayOf[str] | Literal[False]:
        if jt.is_json_array(obj):
            assert_type(obj, list[str])
            return obj
        return False

    def test_is_json_object(
        obj: list | dict[str, Any],
    ) -> jt.ObjectOf[str, Any] | Literal[False]:
        if jt.is_json_object(obj):
            assert_type(obj, jt.ObjectOf[str, Any])
            return obj
        return False

    def test_is_json_document(
        obj: Any,
    ) -> jt.DocumentOf[Any, Any, Any] | Literal[False]:
        if jt.is_json_document(obj):
            return obj
        return False

    def test_is_json(obj: set | list[str]) -> jt.Scalar | list[str] | Literal[False]:
        if jt.is_json(obj):
            return obj
        return False

    # Guard (not deep)

    def test_guard_json_number(obj: Any) -> jt.Number | Literal[False]:
        if jt.guard_json_number(obj):
            return obj
        return False

    def test_guard_json_scalar(obj: dict | bool | None) -> jt.Scalar | Literal[False]:
        if jt.guard_json_scalar(obj):
            assert_type(obj, jt.Scalar)
            return obj
        return False

    def test_guard_json_array(
        obj: dict | list[set],
    ) -> jt.ArrayOf[Any] | Literal[False]:
        if jt.guard_json_array(obj):
            assert_type(obj, jt.ArrayOf[Any])
            return obj
        return False

    def test_guard_json_object(obj: Any) -> jt.ObjectOf[Any, Any] | Literal[False]:
        if jt.guard_json_object(obj):
            return obj
        return False

    def test_guard_json_document(
        obj: Any,
    ) -> jt.DocumentOf[Any, Any, Any] | Literal[False]:
        if jt.guard_json_document(obj):
            return obj
        return False

    def test_guard_json(
        obj: Any,
    ) -> jt.Scalar | jt.DocumentOf[Any, Any, Any] | Literal[False]:
        if jt.guard_json(obj):
            return obj
        return False

    # Is (deep)

    def test_is_json_array_deep(
        obj: float | list[jt.Json],
    ) -> jt.Array | Literal[False]:
        if jt.is_json_array_deep(obj):
            # Should fail if TypeGuard were used instead of TypeIs
            assert_type(obj, list[jt.Json])
            return obj
        return False

    def test_is_json_object_deep(
        obj: list | dict[int, int] | dict[str, Any],
    ) -> jt.Object | Literal[False]:
        if jt.is_json_object_deep(obj):
            # Should fail if TypeGuard were used instead of TypeIs
            assert_type(obj, jt.ObjectOf[str, Any])
            return obj
        return False

    def test_is_json_document_deep(obj: int | list) -> jt.Document | Literal[False]:
        if jt.is_json_document_deep(obj):
            assert_type(obj, jt.ArrayOf[Any])
            return obj
        return False

    def test_is_json_deep(obj: int | set) -> jt.Json | Literal[False]:
        if jt.is_json_deep(obj):
            assert_type(obj, int | bool)
            return obj
        return False

    # Guard (deep)

    def test_guard_json_array_deep(
        obj: float | list[int | float],
    ) -> jt.Array | Literal[False]:
        if jt.guard_json_array_deep(obj):
            assert_type(obj, jt.Array)
            return obj
        return False

    def test_guard_json_object_deep(
        obj: dict | dict[int, Any],
    ) -> jt.Object | Literal[False]:
        if jt.guard_json_object_deep(obj):
            assert_type(obj, jt.Object)
            return obj
        return False

    def test_guard_json_document_deep(obj: Any) -> jt.Document | Literal[False]:
        if jt.guard_json_document_deep(obj):
            return obj
        return False

    def test_guard_json_deep(obj: int | set) -> jt.Json | Literal[False]:
        if jt.guard_json_deep(obj):
            return obj
        return False

    obj: Any = 5
    test_is_json_number(obj)
    test_is_json_scalar(obj)
    test_is_json_array(obj)
    test_is_json_object(obj)
    test_is_json_document(obj)
    test_is_json(obj)

    test_guard_json_number(obj)
    test_guard_json_scalar(obj)
    test_guard_json_array(obj)
    test_guard_json_object(obj)
    test_guard_json_document(obj)
    test_guard_json(obj)

    test_is_json_array_deep(obj)
    test_is_json_object_deep(obj)
    test_is_json_document_deep(obj)
    test_is_json_deep(obj)

    test_guard_json_array_deep(obj)
    test_guard_json_object_deep(obj)
    test_guard_json_document_deep(obj)
    test_guard_json_deep(obj)

    assert test_is_json_number(True) is False
    assert test_is_json_scalar(True) is not False
    assert test_is_json_array([set()]) is not False  # type: ignore
    assert test_is_json_object({'key': set()}) is not False
    assert test_is_json_document({'key': set()}) is not False  # type: ignore
    assert test_is_json(set()) is False

    assert test_guard_json_number(True) is False
    assert test_guard_json_scalar(True) is not False
    assert test_guard_json_array([set()]) is not False  # type: ignore
    assert test_guard_json_object({'key': set()}) is not False
    assert test_guard_json_document({'key': set()}) is not False  # type: ignore
    assert test_guard_json(set()) is False

    assert test_is_json_array_deep([set()]) is False  # type: ignore
    assert test_is_json_object_deep({1: 'hi'}) is False  # type: ignore
    assert test_is_json_object_deep({'1': 'hi'}) is not False  # type: ignore
    assert test_is_json_document_deep({'key': set()}) is False  # type: ignore
    assert test_is_json_deep({'hi'}) is False

    assert test_guard_json_array_deep([set()]) is False  # type: ignore
    assert test_guard_json_object_deep({'key': set()}) is False
    assert test_guard_json_document_deep({'key': set()}) is False  # type: ignore
    assert test_guard_json_deep(set()) is False


def test_recursion_catch():
    obj = [[1, 2, 3]]
    obj[0].append(obj)  # type: ignore
    with pytest.raises(RecursionError):
        jt.is_json_deep(obj)
