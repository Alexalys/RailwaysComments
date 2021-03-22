import connector
from pymongo import MongoClient
import sys
from PyQt5 import QtWidgets
import add_comment
import main_frame
import add_show_comments
import dialog_show_comment

client = MongoClient()


# Class of start window.
class MainWindow(QtWidgets.QMainWindow, main_frame.UiMainFrame):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)  # Design initialization
        self.pushButton.clicked.connect(self.list_sql)

    def list_sql(self):
        self.tableWidget.setRowCount(0)
        connection = connector.connect()

        city = self.lineEdit.text()
        sql_list = connector.get_cities_from_sql(connection, city)

        while sql_list.next():
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows+1)

            self.tableWidget.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(sql_list.value(0))))
            self.tableWidget.setItem(rows, 1, QtWidgets.QTableWidgetItem(sql_list.value(1).toString()))
            self.tableWidget.setItem(rows, 2, QtWidgets.QTableWidgetItem(sql_list.value(2).toString()))
            self.tableWidget.setItem(rows, 3, QtWidgets.QTableWidgetItem(sql_list.value(3)))
            self.tableWidget.setItem(rows, 4, QtWidgets.QTableWidgetItem(sql_list.value(4)))

        self.tableWidget.cellDoubleClicked.connect(self.get_row)

    def get_row(self, row):
        item = self.tableWidget.item(row, 0)

        dialog = AddAndShowComments(item.text())
        dialog.exec_()


# Choice between add and show comments.
class AddAndShowComments(QtWidgets.QDialog, add_show_comments.UiAddShowComment):
    def __init__(self, identifier):
        super().__init__()
        self.setup_ui(self)
        self.identifier = identifier
        self.ButtonSee.clicked.connect(self.see_comments)
        self.ButtonAdd.clicked.connect(self.add_comments)

    def see_comments(self):
        dialog_show_comments = TableShowComments(self.identifier)
        dialog_show_comments.exec_()

    def add_comments(self):
        dialog_add_comments = AddComment(self.identifier)
        dialog_add_comments.exec_()


# Displaying comments.
class TableShowComments(QtWidgets.QDialog, dialog_show_comment.UiShowComment):
    def __init__(self, identifier):
        super().__init__()
        self.setup_ui(self)
        self.identifier = identifier
        self.show_comments()

    def show_comments(self):
        global client
        db = client["railways"]
        collection = db["feedback"]

        results = collection.find({"identifier": self.identifier})
        for result in results:
            rows = self.tableWidget.rowCount()
            self.tableWidget.setRowCount(rows + 1)
            self.tableWidget.setItem(rows, 0, QtWidgets.QTableWidgetItem(str(result['rate'])))

            self.tableWidget.setItem(rows, 1, QtWidgets.QTableWidgetItem(result['comment']))
        self.tableWidget.cellDoubleClicked.connect(self.delete_row)

    def delete_row(self, row):
        item1 = self.tableWidget.item(row, 0)
        item2 = self.tableWidget.item(row, 1)
        print(str(item1.text()))
        print(item2.text())
        document = {'rate': int(item1.text()), 'comment': item2.text()}
        db = client["railways"]
        collection = db["feedback"]
        print(collection.delete_one(document))
        self.tableWidget.removeRow(row)


# Adding comments to Mongo.
class AddComment(QtWidgets.QDialog, add_comment.Ui_DialogAddComment):
    def __init__(self, identifier):
        super().__init__()
        self.setupUi(self)
        self.identifier = identifier
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Save).clicked.connect(self.comment_to_mongo)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Close).clicked.connect(self.close_on_click)

    def comment_to_mongo(self):
        db = client["railways"]
        collection = db["feedback"]
        document = {}
        document['identifier'] = self.identifier
        document['rate'] = self.spinBox.value()
        document['surname'] = self.surnameLine.text()
        document['comment'] = self.plainTextEdit.toPlainText()
        collection.insert_one(document)
        self.close()

    def close_on_click(self):
        self.close()


def main():
    global client
    client = MongoClient('localhost', 27017)

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()  # show window
    app.exec_()  # launch application


if __name__ == '__main__':
    main()
