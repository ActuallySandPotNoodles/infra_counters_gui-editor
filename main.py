# Form implementation generated from reading ui self.file 'icedit.ui'
#
# Created by: PyQt6 UI code generator 6.10.2
#
# WARNING: Any manual changes made to this self.file will be lost when pyuic6 is
# run again.  Do not edit this self.file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import json, sandstuff, vdf, os

class Ui_Form(object):
    def setupUi(self, Form):
        try:
            self.file = QtWidgets.QFileDialog.getOpenFileName(Form)[0]
            self.mapdata = json.loads(sandstuff.cat(self.file))
            self.mapkeys = list(self.mapdata)
        except: sys.exit()
        Form.setObjectName("Form")
        Form.resize(971, 576)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.repair = QtWidgets.QSpinBox(parent=Form)
        self.repair.setObjectName("repair")
        self.gridLayout.addWidget(self.repair, 3, 4, 1, 1)
        self.import_err = QtWidgets.QLabel(parent=Form)
        self.import_err.setObjectName("import_err")
        self.gridLayout.addWidget(self.import_err, 8, 3, 1, 2)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 9, 3, 1, 2)
        self.mistakes = QtWidgets.QSpinBox(parent=Form)
        self.mistakes.setObjectName("mistakes")
        self.gridLayout.addWidget(self.mistakes, 4, 4, 1, 1)
        self.remove = QtWidgets.QPushButton(parent=Form)
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 10, 2, 1, 1)
        self.apply = QtWidgets.QPushButton(parent=Form)
        self.apply.setObjectName("apply")
        self.gridLayout.addWidget(self.apply, 10, 3, 1, 2)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 3, 1, 1)
        self.save = QtWidgets.QPushButton(parent=Form)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 0, 1, 1, 1)
        self.geocaches = QtWidgets.QSpinBox(parent=Form)
        self.geocaches.setObjectName("geocaches")
        self.gridLayout.addWidget(self.geocaches, 5, 4, 1, 1)
        self.cams = QtWidgets.QSpinBox(parent=Form)
        self.cams.setObjectName("cams")
        self.gridLayout.addWidget(self.cams, 1, 4, 1, 1)
        self.add = QtWidgets.QPushButton(parent=Form)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 10, 1, 1, 1)
        self.import_2 = QtWidgets.QPushButton(parent=Form)
        self.import_2.setObjectName("import_2")
        self.gridLayout.addWidget(self.import_2, 7, 3, 1, 2)
        self.label_7 = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 3, 1, 2)
        self.label_6 = QtWidgets.QLabel(parent=Form)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 1)
        self.load = QtWidgets.QPushButton(parent=Form)
        self.load.setObjectName("load")
        self.gridLayout.addWidget(self.load, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=Form)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 3, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(parent=Form)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout.addWidget(self.treeWidget, 1, 1, 9, 2)
        self.waterflow = QtWidgets.QSpinBox(parent=Form)
        self.waterflow.setObjectName("waterflow")
        self.gridLayout.addWidget(self.waterflow, 6, 4, 1, 1)
        self.corrupt = QtWidgets.QSpinBox(parent=Form)
        self.corrupt.setObjectName("corrupt")
        self.gridLayout.addWidget(self.corrupt, 2, 4, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=Form)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 11, 1, 1, 4)
        self.init_json_to_tree()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.treeWidget.itemClicked.connect(self.item_clicked)
        self.apply.clicked.connect(self.applyf)
        self.add.clicked.connect(self.addf)
        self.remove.clicked.connect(self.removef)
        self.save.clicked.connect(self.savef)
        self.load.clicked.connect(self.loadf)
        self.import_2.clicked.connect(self.importf)

    def init_json_to_tree(self):
        self.treeWidget.headerItem().setText(0, "Map")
        for i in range(len(self.mapkeys)):
            #python is fun mate
            item = QtWidgets.QTreeWidgetItem(self.treeWidget)
            self.treeWidget.topLevelItem(i).setText(0, self.mapkeys[i])

    def importf(self):
        #mtdata_file = "lowyardeditd_metadata.txt"; ok = True
        mtdata_file, ok = QtWidgets.QFileDialog.getOpenFileName(Form, filter="*.txt")
        if mtdata_file and ok:
            try:
                fl = vdf.loads(sandstuff.cat(mtdata_file))
                c = fl['infra_metadata']
                self.cams.setValue(int(c['camera_targets']))
                self.corrupt.setValue(int(c['corruption_targets']))
                self.repair.setValue(int(c['repair_targets']))
                self.mistakes.setValue(int(c['mistake_targets']))
                self.geocaches.setValue(int(c['geocaches']))
                self.waterflow.setValue(int(c['water_flow_meter_targets']))
            except: self.import_err.setText("Failed to import file")

    def item_clicked(self, selection):
        self.index = self.treeWidget.indexOfTopLevelItem(selection)
        current = self.mapdata[self.mapkeys[self.index]]
        self.cams.setValue(current['camera_targets'])
        self.corrupt.setValue(current['corruption_targets'])
        self.repair.setValue(current['repair_targets'])
        self.mistakes.setValue(current['mistake_targets'])
        self.geocaches.setValue(current['geocaches'])
        self.waterflow.setValue(current['water_flow_meter_targets'])
        self.import_err.setText("")

        
    def applyf(self):
        lvl = self.mapkeys[self.index]
        self.mapdata[lvl]['camera_targets'] = int(self.cams.value())
        self.mapdata[lvl]['corruption_targets'] = int(self.corrupt.value())
        self.mapdata[lvl]['repair_targets'] = int(self.repair.value())
        self.mapdata[lvl]['mistake_targets'] = int(self.mistakes.value())
        self.mapdata[lvl]['geocaches'] = int(self.geocaches.value())
        self.mapdata[lvl]['water_flow_meter_targets'] = int(self.waterflow.value())
    def addf(self):
        text, ok = QtWidgets.QInputDialog.getText(Form, "Add New Map", "Enter map name:")
        if ok and text:
            self.mapdata[text] = {
    'camera_targets': 0,
    'corruption_targets': 0,
    'repair_targets': 0,
    'mistake_targets': 0,
    'geocaches': 0,
    'water_flow_meter_targets': 0
}
        self.treeWidget.clear()
        self.mapkeys = list(self.mapdata)
        self.init_json_to_tree()
    def removef(self):
        try: del self.mapdata[self.mapkeys[self.index]]
        except: pass
        self.treeWidget.clear()
        self.mapkeys = list(self.mapdata)
        self.init_json_to_tree()
    def savef(self):
        sandstuff.tee(self.file, json.dumps(self.mapdata, indent=6))

    def loadf(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(Form)[0]
        try: self.mapdata = json.loads(sandstuff.cat(self.file))
        except: pass
        self.mapkeys = list(self.mapdata)
        self.treeWidget.clear()
        self.init_json_to_tree()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "INFRA Counters Mapdata Editor"))
        self.import_err.setText(_translate("Form", ""))
        self.label.setText(_translate("Form", "Camera Targets"))
        self.label_3.setText(_translate("Form", "Repair targets"))
        self.remove.setText(_translate("Form", "Remove"))
        self.apply.setText(_translate("Form", "Apply"))
        self.label_2.setText(_translate("Form", "Corruption Targets"))
        self.save.setText(_translate("Form", "Save"))
        self.add.setText(_translate("Form", "Add"))
        self.import_2.setText(_translate("Form", "Import from metadata.txt"))
        self.label_7.setText(_translate("Form", os.path.basename(self.file)))
        self.label_6.setText(_translate("Form", "Water Flow Meters"))
        self.load.setText(_translate("Form", "Load"))
        self.label_5.setText(_translate("Form", "Geocaches"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_4.setText(_translate("Form", "Mistake Targets"))
        self.label_8.setText(_translate("Form", "INFRA Counters Mod self.mapdata Editor - Version 1.0 - Made by SandPotNoodles"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
