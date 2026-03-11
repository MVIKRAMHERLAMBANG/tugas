import unittest
from bank import BankAccount 

class TestBankAccount(unittest.TestCase):

    def test_deposit(self):

        akun = BankAccount("kramm", 5000)
        akun.deposit(3000)

        self.assertEqual(akun.get_balance(), 8000)

    def test_depositerror(self):

        akun = BankAccount("kramm", 3000)

        with self.assertRaises(ValueError):
            akun.deposit(-100)

    def test_withdraw(self):

        akun = BankAccount("kramm", 6000)
        akun.withdraw(2000)

        self.assertEqual(akun.get_balance(), 4000)

    def test_withdrawerror(self):

        akun = BankAccount("kramm", 5000)

        with self.assertRaises(ValueError):
            akun.withdraw(7000)

    def test_get_balance(self):
        akun = BankAccount("kramm", 8000)

        self.assertEqual(akun.get_balance(), 8000)            

if __name__ == "__main__":
    unittest.main()