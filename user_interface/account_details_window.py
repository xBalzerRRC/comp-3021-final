__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """Represents a GUI window for viewing and performing transactions
    on a single bank account.
    """

    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Initializes a new instance of the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        
        super().__init__()

        if isinstance(account, BankAccount):
            self.account = copy.copy(account)

            self.account_number_label.setText(str(self.account.account_number))
            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.deposit_button.clicked.connect(self.on_apply_transaction)
            self.withdraw_button.clicked.connect(self.on_apply_transaction)
            self.exit_button.clicked.connect(self.on_exit)

        else:
            self.reject()

    
    def on_apply_transaction(self):
        """
        Handles deposit or withdrawal transactions based on user input.
        Validates input, updates the balance, and emits a signal with
        the updated account.
        """

        try:
            amount_str = self.transaction_amount_edit.text().strip()
            amount = float(amount_str)
        except ValueError:
            QMessageBox.information(self, "Invalid Data", "Amount must be numeric.")
            self.transaction_amount_edit.setFocus()
            return

        try:
            sender = self.sender()
            transaction_type = ""

            if sender == self.deposit_button:
                transaction_type = "Deposit"
                self.account.deposit(amount)

            elif sender == self.withdraw_button:
                transaction_type = "Withdraw"
                self.account.withdraw(amount)

            self.balance_label.setText(f"${self.account.balance:,.2f}")

            self.balance_updated.emit(self.account)

            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()

        except Exception as e:
            QMessageBox.information(
                self,
                f"{transaction_type} failed",
                str(e)
            )
            self.transaction_amount_edit.setText("")
            self.transaction_amount_edit.setFocus()


    def on_exit(self):
        """Closes the account details window."""

        self.close()

    def render_account_html(self, user_note: str) -> str:
        """Render account info as HTML - VULNERABLE TO XSS."""
        return f"<html><body><h1>Account: {self.account.account_number}</h1><p>Note: {user_note}</p></body></html>"