__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = ""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """Represents a GUI window that allows users to look up clients by
    their client number and displays client information and associated 
    bank accounts in a table.
    """

    def __init__(self):
        super().__init__()

        self.client_listing, self.accounts = load_data()

        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)
        self.filter_button.clicked.connect(self.on_filter_clicked)

    def on_lookup_client(self):
        """Handles the lookup process for a client using the client
        number entered and displays client information and populates the
        account table with associated accounts if the client is found.
        """
        
        try:
            client_number_str = self.client_number_edit.text().strip()
            client_number = int(client_number_str)
        except ValueError:
            QMessageBox.information(self, "Input Error", 
                                    "The client number must be a numeric value.")
            self.reset_display()
            return

        if client_number not in self.client_listing:
            QMessageBox.information(self, "Not Found", 
                                    f"Client number: {client_number} not found.")
            self.reset_display()
            return

        client = self.client_listing[client_number]

        self.client_info_label.setText(f"Client Name: {client.first_name} {client.last_name}")

        for account in self.accounts.values():
            if account.client_number == client_number:
                row_position = self.account_table.rowCount()
                self.account_table.insertRow(row_position)

                account_number_item = QTableWidgetItem(str(account.account_number))
                account_number_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                
                date_created_item = QTableWidgetItem(str(account._date_created))
                date_created_item.setTextAlignment(Qt.AlignCenter)

                account_type_item = QTableWidgetItem(account.__class__.__name__)
                account_type_item.setTextAlignment(Qt.AlignLeft | Qt.AlignVCenter)

                self.account_table.setItem(row_position, 0, account_number_item)
                self.account_table.setItem(row_position, 1, balance_item)
                self.account_table.setItem(row_position, 2, date_created_item)
                self.account_table.setItem(row_position, 3, account_type_item)

        self.account_table.resizeColumnsToContents() 

        self.toggle_filter(False)
    
    def on_text_changed(self):
        """Clears the account table when the client number text is
        modified.
        """

        self.account_table.setRowCount(0)

    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """
        Opens a detailed account window when a valid row is selected
        from the account table.

        Args:
            row (int): The row of the clicked cell.
            column (int): The column of the clicked cell.
        """

        account_number_item = self.account_table.item(row, 0)

        if not account_number_item or not account_number_item.text().strip():
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        account_number_str = account_number_item.text().strip()

        try:
            account_number = int(account_number_str)
        except ValueError:
            QMessageBox.information(self, "Invalid Selection", "Please select a valid record.")
            return

        if account_number not in self.accounts:
            QMessageBox.information(self, "No Bank Account", "Bank Account selected does not exist.")
            return

        account = self.accounts[account_number]
        details_window = AccountDetailsWindow(account)
        details_window.balance_updated.connect(self.update_data)
        details_window.exec()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount):
        """Updates the account's balance in the table and writes the 
        updated data to storage.

        Args:
            account (BankAccount): The updated bank account instance.
        """
        
        for row in range(self.account_table.rowCount()):
            item = self.account_table.item(row, 0)

            if not item:
                continue

            try:
                table_account_number = int(item.text())
            except ValueError:
                continue

            if table_account_number == account.account_number:
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)

                self.accounts[account.account_number] = account

                update_data(account)

                break

    @Slot()
    def on_filter_clicked(self):
        """
        Filters the account_table based on selected column and input
        value.
        """

        if self.filter_button.text() == "Apply Filter":
            column_index = self.filter_combo_box.currentIndex()
            search_text = self.filter_edit.text().strip().lower()

            for row in range(self.account_table.rowCount()):
                item = self.account_table.item(row, column_index)
                if item:
                    cell_text = item.text().strip().lower()
                    if search_text in cell_text:
                        self.account_table.setRowHidden(row, False)
                    else:
                        self.account_table.setRowHidden(row, True)

            self.toggle_filter(True)

        else:
            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.toggle_filter(False)

    def toggle_filter(self, filter_on: bool):
        """
        Toggles the visibility and behavior of filtering controls based
        on the filter state.

        Args:
            filter_on (bool): Toggles filtered view.
        """

        self.filter_button.setEnabled(True)

        if filter_on:
            self.filter_button.setText("Reset")
            self.filter_combo_box.setEnabled(False)
            self.filter_edit.setEnabled(False)
            self.filter_label.setText("Data is Currently Filtered")
        else:
            self.filter_button.setText("Apply Filter")
            self.filter_combo_box.setEnabled(True)
            self.filter_edit.setEnabled(True)
            self.filter_edit.setText("")
            self.filter_combo_box.setCurrentIndex(0)

            for row in range(self.account_table.rowCount()):
                self.account_table.setRowHidden(row, False)

            self.filter_label.setText("Data is Not Currently Filtered")

    

        