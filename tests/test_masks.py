from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_num):
    assert get_mask_card_number(card_num) == '1234 56** **** 3456'


def test_get_mask_account(acc_number):
    assert get_mask_account(acc_number) == '**7890'
