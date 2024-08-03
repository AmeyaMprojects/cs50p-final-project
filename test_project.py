import pytest
from project import get_season, get_gender, get_fit

def test_get_season():
    assert get_season() == "summer"
    assert get_season() == "winter"
    with pytest.raises(ValueError):
        get_season() == "spring"

def test_get_gender():
    assert get_gender() == "male"
    assert get_gender() == "female"
    with pytest.raises(ValueError):
        get_gender() == "other"

def test_get_fit():
    assert get_fit("summer", "male") == "T-shirt, shorts, and sandals" or "polo shirt, chinos, and loafers" or "tank top, jeans, and sneakers" or "linen shirt, shorts, and sandals"

