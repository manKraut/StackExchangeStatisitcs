import pytest
from stackstats import utils


def test_convert_string_to_epoch_fail():
    inpt = "20200602 10:00:00"
    expected = 123456789
    assert utils.convert_string_to_epoch(inpt) != expected


def test_convert_string_to_epoch_succeeded():
    inpt = "20200602 10:00:00"
    expected = 1591081200
    assert utils.convert_string_to_epoch(inpt) == expected


def test_flatten_json_succeed():
    inpt = {'top_ten_answers_comment_count': {62147743: 0,
                                       62148304: 10}}

    expected = {
            'top_ten_answers_comment_count/62147743': 0,
            'top_ten_answers_comment_count/62148304': 10
            }

    assert utils.flatten_json(inpt) == expected


def test_flatten_json_throws_key_error():
    inpt = {'random_key': 'random_value'}

    with pytest.raises(KeyError) as err:
        utils.flatten_json(inpt)
