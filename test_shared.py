def test_funded_account_deposit(funded_account):
    funded_account.deposit(200)
    assert funded_account.balance == 1200


def test_funded_account_withdraw(funded_account):
    funded_account.withdraw(300)
    assert funded_account.balance == 700