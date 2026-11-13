
from spam_scoring import score_message, classify, filter_inbox, inbox_status


# Code coverage tests for score_message()
def test_plain_message_scores_zero():
    assert score_message("hello there", False, 0) == 0


def test_spam_word_increases_score():
    assert score_message("free prize", False, 0) == 4


def test_uppercase_word_increases_score():
    assert score_message("HELLO", False, 0) == 1


def test_link_count_more_than_three():
    assert score_message("hello", False, 4) == 4


def test_link_count_between_one_and_three():
    assert score_message("hello", False, 2) == 1


def test_known_sender_reduces_score():
    assert score_message("free prize", True, 0) == 1


def test_known_sender_score_does_not_go_below_zero():
    assert score_message("hello", True, 0) == 0


# Code coverage tests for classify()
def test_high_score_is_spam():
    assert classify(8) == "spam"


def test_medium_score_is_suspicious():
    assert classify(4) == "suspicious"


def test_low_score_is_clean():
    assert classify(1) == "clean"


# Code coverage tests for filter_inbox()
def test_filter_inbox_counts_messages():
    messages = [
        ("free prize", False, 0),
        ("hello", False, 2),
        ("hello", False, 0)
    ]
    assert filter_inbox(messages) == {
        "spam": 0,
        "suspicious": 1,
        "clean": 2
    }


def test_filter_inbox_empty_messages():
    assert filter_inbox([]) == {
        "spam": 0,
        "suspicious": 0,
        "clean": 0
    }


# Code coverage tests for inbox_status()
def test_empty_inbox_status():
    assert inbox_status({"spam": 0, "suspicious": 0, "clean": 0}) == "empty"


def test_flooded_inbox_status():
    assert inbox_status({"spam": 6, "suspicious": 2, "clean": 2}) == "flooded"


def test_noisy_inbox_status():
    assert inbox_status({"spam": 3, "suspicious": 4, "clean": 3}) == "noisy"


def test_healthy_inbox_status():
    assert inbox_status({"spam": 1, "suspicious": 3, "clean": 6}) == "healthy"

