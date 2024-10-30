import sys
from typing import Dict, Union

# Inicializar mappings globales
distances_true: Dict[int, int] = {}
distances_false: Dict[int, int] = {}


def update_maps(condition_num: int, d_true: int, d_false: int):
    global distances_true, distances_false

    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(
            distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(
            distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false


def clear_maps():
    global distances_true, distances_false
    distances_true.clear()
    distances_false.clear()


def get_true_distance(condition_num: int) -> Union[int, None]:
    global distances_true
    if condition_num in distances_true.keys():
        return distances_true[condition_num]
    else:
        return None


def get_false_distance(condition_num: int) -> Union[int, None]:
    global distances_false
    if condition_num in distances_false.keys():
        return distances_false[condition_num]
    else:
        return None


def has_reached_condition(condition_num: int) -> bool:
    global distances_true, distances_false
    return condition_num in distances_true.keys() or condition_num in distances_false.keys()


def evaluate_condition(condition_num: int, op: str, lhs: Union[str, Dict], rhs: Union[str, Dict]) -> bool:
    if isinstance(lhs, int) and isinstance(rhs, int):
        if op == "Eq":
            if lhs == rhs:
                update_maps(condition_num, 0, 1)
                return True
            else:
                update_maps(condition_num, abs(rhs-lhs),0)
                return False
        if op == "Ne":
            if lhs != rhs:
                update_maps(condition_num, 0, abs(rhs - lhs))
                return True
            else:
                update_maps(condition_num, 1, 0)
                return False
        if op == "Lt":
            if lhs < rhs:
                update_maps(condition_num, 0, rhs - lhs)
                return True
            else:
                update_maps(condition_num, lhs - rhs + 1, 0)
                return False
        if op == "Gt":
            if lhs > rhs:
                update_maps(condition_num, 0, lhs - rhs)
                return True
            else:
                update_maps(condition_num, rhs - lhs + 1, 0)
                return False
        if op == "Le":
            if lhs <= rhs:
                update_maps(condition_num, 0, rhs - lhs + 1)
                return True
            else:
                update_maps(condition_num, lhs - rhs, 0)
                return False
        if op == "Ge":
            if lhs >= rhs:
                update_maps(condition_num, 0, lhs - rhs + 1)
                return True
            else:
                update_maps(condition_num, rhs - lhs, 0)
                return False
    if isinstance(lhs, str) and len(lhs) == 1 and isinstance(rhs, str) and len(rhs) == 1:
        if op == "Eq":
            if ord(lhs) == ord(rhs):
                update_maps(condition_num, 0, 1)
                return True
            else:
                update_maps(condition_num, abs(ord(rhs)-ord(lhs)),0)
                return False
        if op == "Ne":
            if ord(lhs) != ord(rhs):
                update_maps(condition_num, 0, abs(ord(rhs) - ord(lhs)))
                return True
            else:
                update_maps(condition_num, 1, 0)
                return False
        if op == "Lt":
            if ord(lhs) < ord(rhs):
                update_maps(condition_num, 0, ord(rhs) - ord(lhs))
                return True
            else:
                update_maps(condition_num, ord(lhs) - ord(rhs) + 1, 0)
                return False
        if op == "Gt":
            if ord(lhs) > ord(rhs):
                update_maps(condition_num, 0, ord(lhs) - ord(rhs))
                return True
            else:
                update_maps(condition_num, ord(rhs) - ord(lhs) + 1, 0)
                return False
        if op == "Le":
            if ord(lhs) <= ord(rhs):
                update_maps(condition_num, 0, ord(rhs) - ord(lhs) + 1)
                return True
            else:
                update_maps(condition_num, ord(lhs) - ord(rhs), 0)
                return False
        if op == "Ge":
            if ord(lhs) >= ord(rhs):
                update_maps(condition_num, 0, ord(lhs) - ord(rhs) + 1)
                return True
            else:
                update_maps(condition_num, ord(rhs) - ord(lhs), 0)
                return False
    if isinstance(lhs, str) and len(lhs) == 1 and isinstance(rhs, dict):
        if op == "In":
            if lhs in rhs.keys():
                update_maps(condition_num, 0, 1)
                return True
            else:
                update_maps(condition_num, min(abs(ord(lhs) - ord(k)) for k in rhs.keys()), 0)
                return False
    raise ValueError()
