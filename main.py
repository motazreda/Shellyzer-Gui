import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from mainview import Ui_MainView
from capstone import *
import binascii
import string

class Shellcode_Analyze(QMainWindow):
	def __init__(self, parent=None):
		super(Shellcode_Analyze, self).__init__(parent)
		self.ui = Ui_MainView()
		self.ui.setupUi(self)
		self.ui.pushButton.clicked.connect(self.gotshellcode)


	def gotshellcode(self):
		self.shellcode = unicode(self.ui.lineEdit.text())
		print self.shellcode
		md = Cs(CS_ARCH_X86, CS_MODE_32)
		model = QStandardItemModel(self.ui.listView)
		for i in md.disasm(self.shellcode.decode('string-escape'), 0):
			if "0x" in i.op_str and "[" not in i.op_str:
				try:					
					opstr = i.op_str.replace("0x", "")
					info = binascii.unhexlify(opstr)
					print str(info)
					linear_disas = "0x%08x:\t\t%s\t%s\t\t" % (i.address, i.mnemonic, i.op_str)
					linear_disas = linear_disas + "String : " + str(info) + "\n"
					item = QStandardItem(linear_disas)
					item.setEditable(False)
					model.appendRow(item)
					self.ui.listView.setModel(model)
				except:
					# pass
					linear_disas = "0x%08x:\t\t%s\t%s\n"%(i.address, i.mnemonic, i.op_str)					
					item = QStandardItem(linear_disas)
					item.setFont(QFont('Sans Serif'))
					item.setEditable(False)
					model.appendRow(item)
					self.ui.listView.setModel(model)
			else:
				linear_disas = "0x%08x:\t\t%s\t%s\n"%(i.address, i.mnemonic, i.op_str)					
				item = QStandardItem(linear_disas)
				item.setFont(QFont('Sans Serif'))
				item.setEditable(False)
				model.appendRow(item)
				self.ui.listView.setModel(model)	


		# here dumping strings in listWidget
		self.item = ''
		for strs in self.shellcode.decode('string-escape'):
			if strs in string.printable:
				self.item += strs
				continue
			self.strings = QListWidgetItem(self.item)
			self.ui.listWidget.addItem(self.strings)


app = QApplication(sys.argv)
mainscreen = Shellcode_Analyze()
mainscreen.show()
sys.exit(app.exec_())
