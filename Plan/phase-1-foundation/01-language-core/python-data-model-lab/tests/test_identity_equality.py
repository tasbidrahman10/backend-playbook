"""Tests for identity and equality behavior."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


def _load_exercise_module():
    exercise_path = (
        Path(__file__).resolve().parents[1]
        / "exercises"
        / "01_identity_vs_equality.py"
    )
    spec = spec_from_file_location("exercise_01_identity", exercise_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load exercise module")
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_identity_and_equality_behavior() -> None:
    module = _load_exercise_module()
    task_a, same_reference, same_id_new_instance, different_id = module.build_demo_tasks()

    assert task_a is same_reference
    assert task_a is not same_id_new_instance

    assert task_a == same_reference
    assert task_a == same_id_new_instance
    assert task_a != different_id
