"""Lesson 4 homework: baseline tasks.

Replace each `raise NotImplementedError` with your implementation.
You may use AI, as long as you can explain every line.
"""


import json


def count_selected(media_ids: list[str]) -> int:
    return len(set(media_ids));


def group_by_gallery(media: list[dict]) -> dict[str, list[str]]:
    """Group media items {"gallery_id": ..., "id": ...} by gallery.

    Return a dict: gallery id -> list of media ids, in input order.
    """
    grouped = {}
    for item in media:
        gallery_id = item["gallery_id"]
        media_id = item["id"]
        grouped.setdefault(gallery_id, []).append(media_id)
    return grouped


def total_price(prices_minor: list[int | None]) -> int:
    return sum(p for p in prices_minor if p is not None)


def first_missing(required: list[str], present: list[str]) -> str | None:
    return next((x for x in required if x not in present), None)


def load_events(path) -> list[dict]:
    with open(path,  encoding="utf-8") as f:
        return json.load(f)
