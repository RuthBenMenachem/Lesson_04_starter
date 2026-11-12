import pytest

import baseline.tasks as tasks

@pytest.mark.req("BASELINE-04")
def test_first_missing_returns_first_misssing():
    required = ["med_1", "med_2", "med_3"]
    present = ["med_1", "med_3"]
    assert tasks.first_missing(required, present) == "med_2"
