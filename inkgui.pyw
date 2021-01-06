from PyQt5 import QtCore, QtGui, QtWidgets
import inkclicker
import inksprint
import inkcontrols


# Clickable Label Element
class QLabel_clickable(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

    def mouseReleaseEvent(self, ev):
        self.clicked.emit()


# Draggable Frame that drags entire window
class QFrame_drag_window(QtWidgets.QFrame):
    def __init__(self, parent=None):
        QtWidgets.QFrame.__init__(self, parent)
        self.dragPos = QtCore.QPoint()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            MainWindow.move(MainWindow.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        # frameless
        MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        MainWindow.resize(960, 700)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/ink_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setStyleSheet("QFrame{\n"
                                      "    background-color: rgb(255, 244, 235);\n"
                                      "    color: rgb(56, 63, 81);\n"
                                      "    border-radius: 10px;\n"
                                      "}")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QFrame_drag_window(self.main_frame)
        self.top_bar.setMinimumSize(QtCore.QSize(0, 51))
        self.top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ink_icon = QtWidgets.QLabel(self.top_bar)
        self.ink_icon.setMaximumSize(QtCore.QSize(60, 60))
        self.ink_icon.setText("")
        self.ink_icon.setTextFormat(QtCore.Qt.RichText)
        self.ink_icon.setPixmap(QtGui.QPixmap("assets/ink_icon.png"))
        self.ink_icon.setScaledContents(True)
        self.ink_icon.setObjectName("ink_icon")
        self.horizontalLayout_6.addWidget(self.ink_icon)
        self.title_label = QtWidgets.QLabel(self.top_bar)
        self.title_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        self.horizontalLayout_6.addWidget(self.title_label)
        self.minimize_button = QLabel_clickable(self.top_bar)
        self.minimize_button.setMaximumSize(QtCore.QSize(20, 20))
        self.minimize_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.minimize_button.setText("")
        self.minimize_button.setTextFormat(QtCore.Qt.RichText)
        self.minimize_button.setPixmap(QtGui.QPixmap("assets/yellow_circle.png"))
        self.minimize_button.setScaledContents(True)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_6.addWidget(self.minimize_button)
        self.exit_button = QLabel_clickable(self.top_bar)
        self.exit_button.setMaximumSize(QtCore.QSize(20, 20))
        self.exit_button.setText("")
        self.exit_button.setTextFormat(QtCore.Qt.RichText)
        self.exit_button.setPixmap(QtGui.QPixmap("assets/red_circle.png"))
        self.exit_button.setScaledContents(True)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_6.addWidget(self.exit_button)
        self.verticalLayout.addWidget(self.top_bar)
        self.autoclick_box = QtWidgets.QGroupBox(self.main_frame)
        self.autoclick_box.setMinimumSize(QtCore.QSize(340, 100))
        self.autoclick_box.setStyleSheet("color: rgb(255, 244, 235);\n"
                                         "background-color: rgb(56, 63, 81);\n"
                                         "border-radius: 10px;")
        self.autoclick_box.setFlat(False)
        self.autoclick_box.setObjectName("autoclick_box")
        self.gridLayout = QtWidgets.QGridLayout(self.autoclick_box)
        self.gridLayout.setObjectName("gridLayout")
        self.weapon_mode_frame = QtWidgets.QFrame(self.autoclick_box)
        self.weapon_mode_frame.setEnabled(True)
        self.weapon_mode_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.weapon_mode_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.weapon_mode_frame.setObjectName("weapon_mode_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.weapon_mode_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.axe_mode = QtWidgets.QRadioButton(self.weapon_mode_frame)
        self.axe_mode.setObjectName("axe_mode")
        self.verticalLayout_2.addWidget(self.axe_mode)
        self.sword_mode = QtWidgets.QRadioButton(self.weapon_mode_frame)
        self.sword_mode.setChecked(True)
        self.sword_mode.setObjectName("sword_mode")
        self.verticalLayout_2.addWidget(self.sword_mode)
        self.gridLayout.addWidget(self.weapon_mode_frame, 3, 2, 1, 1)
        self.autoclick_keybind_frame = QtWidgets.QFrame(self.autoclick_box)
        self.autoclick_keybind_frame.setStyleSheet("border-radius: 0px;\n"
                                                   "background-color: rgba(56, 63, 81, 0);\n"
                                                   "padding: 15px;")
        self.autoclick_keybind_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.autoclick_keybind_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.autoclick_keybind_frame.setObjectName("autoclick_keybind_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.autoclick_keybind_frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoclick_keybind_label = QtWidgets.QLabel(self.autoclick_keybind_frame)
        self.autoclick_keybind_label.setStyleSheet("color: rgb(255, 244, 235);")
        self.autoclick_keybind_label.setObjectName("autoclick_keybind_label")
        self.horizontalLayout.addWidget(self.autoclick_keybind_label)
        self.autoclick_keybind = QtWidgets.QLineEdit(self.autoclick_keybind_frame)
        self.autoclick_keybind.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "color: rgb(0, 0, 0);")
        self.autoclick_keybind.setInputMask("")
        self.autoclick_keybind.setMaxLength(1)
        self.autoclick_keybind.setPlaceholderText("")
        self.autoclick_keybind.setObjectName("autoclick_keybind")
        self.horizontalLayout.addWidget(self.autoclick_keybind)
        self.gridLayout.addWidget(self.autoclick_keybind_frame, 0, 0, 1, 2)
        self.mc_mode_frame = QtWidgets.QFrame(self.autoclick_box)
        self.mc_mode_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mc_mode_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mc_mode_frame.setObjectName("mc_mode_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.mc_mode_frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.mc_mode_18 = QtWidgets.QRadioButton(self.mc_mode_frame)
        self.mc_mode_18.setChecked(True)
        self.mc_mode_18.setObjectName("mc_mode_18")
        self.verticalLayout_3.addWidget(self.mc_mode_18)
        self.mc_mode_19 = QtWidgets.QRadioButton(self.mc_mode_frame)
        self.mc_mode_19.setMinimumSize(QtCore.QSize(74, 0))
        self.mc_mode_19.setObjectName("mc_mode_19")
        self.verticalLayout_3.addWidget(self.mc_mode_19)
        self.gridLayout.addWidget(self.mc_mode_frame, 1, 0, 1, 1)
        self.cps_frame = QtWidgets.QFrame(self.autoclick_box)
        self.cps_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cps_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cps_frame.setObjectName("cps_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.cps_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.min_cps_label = QtWidgets.QLabel(self.cps_frame)
        self.min_cps_label.setObjectName("min_cps_label")
        self.gridLayout_2.addWidget(self.min_cps_label, 0, 0, 1, 1)
        self.min_cps_slider = QtWidgets.QSlider(self.cps_frame)
        self.min_cps_slider.setMaximum(15)
        self.min_cps_slider.setPageStep(1)
        self.min_cps_slider.setProperty("value", 6)
        self.min_cps_slider.setOrientation(QtCore.Qt.Horizontal)
        self.min_cps_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.min_cps_slider.setObjectName("min_cps_slider")
        self.gridLayout_2.addWidget(self.min_cps_slider, 0, 1, 1, 1)
        self.max_cps_label = QtWidgets.QLabel(self.cps_frame)
        self.max_cps_label.setObjectName("max_cps_label")
        self.gridLayout_2.addWidget(self.max_cps_label, 1, 0, 1, 1)
        self.max_cps_slider = QtWidgets.QSlider(self.cps_frame)
        self.max_cps_slider.setMaximum(15)
        self.max_cps_slider.setPageStep(1)
        self.max_cps_slider.setProperty("value", 8)
        self.max_cps_slider.setOrientation(QtCore.Qt.Horizontal)
        self.max_cps_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.max_cps_slider.setObjectName("max_cps_slider")
        self.gridLayout_2.addWidget(self.max_cps_slider, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.cps_frame, 3, 0, 1, 1)
        self.verticalLayout.addWidget(self.autoclick_box)
        self.sprint_box = QtWidgets.QGroupBox(self.main_frame)
        self.sprint_box.setMinimumSize(QtCore.QSize(0, 50))
        self.sprint_box.setStyleSheet("color: rgb(255, 244, 235);\n"
                                      "background-color: rgb(56, 63, 81);\n"
                                      "border-radius: 10px;")
        self.sprint_box.setFlat(False)
        self.sprint_box.setObjectName("sprint_box")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.sprint_box)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.autoclick_keybind_frame_2 = QtWidgets.QFrame(self.sprint_box)
        self.autoclick_keybind_frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.autoclick_keybind_frame_2.setStyleSheet("border-radius: 0px;\n"
                                                     "background-color: rgba(56, 63, 81, 0);\n")
        self.autoclick_keybind_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.autoclick_keybind_frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.autoclick_keybind_frame_2.setObjectName("autoclick_keybind_frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.autoclick_keybind_frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.sprint_keybind_label = QtWidgets.QLabel(self.autoclick_keybind_frame_2)
        self.sprint_keybind_label.setStyleSheet("color: rgb(255, 244, 235);")
        self.sprint_keybind_label.setObjectName("sprint_keybind_label")
        self.horizontalLayout_2.addWidget(self.sprint_keybind_label)
        self.sprint_keybind = QtWidgets.QLineEdit(self.autoclick_keybind_frame_2)
        self.sprint_keybind.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.sprint_keybind.setInputMask("")
        self.sprint_keybind.setMaxLength(1)
        self.sprint_keybind.setPlaceholderText("")
        self.sprint_keybind.setObjectName("sprint_keybind")
        self.horizontalLayout_2.addWidget(self.sprint_keybind)
        self.horizontalLayout_4.addWidget(self.autoclick_keybind_frame_2)
        self.autoclick_keybind_frame_3 = QtWidgets.QFrame(self.sprint_box)
        self.autoclick_keybind_frame_3.setStyleSheet("border-radius: 0px;\n"
                                                     "background-color: rgba(0, 0, 0, 0)")
        self.autoclick_keybind_frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.autoclick_keybind_frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.autoclick_keybind_frame_3.setObjectName("autoclick_keybind_frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.autoclick_keybind_frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mc_sprint_keybind_label = QtWidgets.QLabel(self.autoclick_keybind_frame_3)
        self.mc_sprint_keybind_label.setStyleSheet("color: rgb(255, 244, 235);")
        self.mc_sprint_keybind_label.setObjectName("mc_sprint_keybind_label")
        self.horizontalLayout_3.addWidget(self.mc_sprint_keybind_label)
        self.mc_sprint_keybind = QtWidgets.QLineEdit(self.autoclick_keybind_frame_3)
        self.mc_sprint_keybind.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                             "color: rgb(0, 0, 0);")
        self.mc_sprint_keybind.setInputMask("")
        self.mc_sprint_keybind.setMaxLength(1)
        self.mc_sprint_keybind.setPlaceholderText("")
        self.mc_sprint_keybind.setObjectName("mc_sprint_keybind")
        self.horizontalLayout_3.addWidget(self.mc_sprint_keybind)
        self.horizontalLayout_4.addWidget(self.autoclick_keybind_frame_3)
        self.verticalLayout.addWidget(self.sprint_box)
        self.status_box = QtWidgets.QGroupBox(self.main_frame)
        self.status_box.setMinimumSize(QtCore.QSize(0, 60))
        self.status_box.setStyleSheet("color: rgb(255, 244, 235);\n"
                                      "background-color: rgb(56, 63, 81);\n"
                                      "border-radius: 10px;")
        self.status_box.setObjectName("status_box")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.status_box)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.start_button = QtWidgets.QPushButton(self.status_box)
        self.start_button.setStyleSheet("background-color: rgb(255, 244, 235);\n"
                                        "color: rgb(56, 63, 81);\n"
                                        "border-radius: 10px;")
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_5.addWidget(self.start_button)
        self.stop_button = QtWidgets.QPushButton(self.status_box)
        self.stop_button.setStyleSheet("background-color: rgb(255, 244, 235);\n"
                                       "color: rgb(56, 63, 81);\n"
                                       "border-radius: 10px;")
        self.stop_button.setObjectName("stop_button")
        self.horizontalLayout_5.addWidget(self.stop_button)
        self.verticalLayout.addWidget(self.status_box)
        self.verticalLayout_4.addWidget(self.main_frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # ---- Events ----

        # CPS
        self.max_cps_slider.valueChanged.connect(lambda: self.validateCPS('max'))
        self.min_cps_slider.valueChanged.connect(lambda: self.validateCPS('min'))
        # Autoclicker
        self.autoclick_keybind.textChanged.connect(lambda: self.validateKeybind('click'))
        self.mc_mode_18.clicked.connect(lambda: change_mode(18))
        self.mc_mode_19.clicked.connect(lambda: change_mode(19))
        self.axe_mode.clicked.connect(lambda: change_attack(inkclicker.clicker_settings.axe))
        self.sword_mode.clicked.connect(lambda: change_attack(inkclicker.clicker_settings.sword))
        # Sprint
        self.sprint_keybind.textChanged.connect(lambda: self.validateKeybind('sprint'))
        self.mc_sprint_keybind.textChanged.connect(lambda: self.validateKeybind('mc_sprint'))
        # Start Button - initialize autoclicker and listener
        self.start_button.pressed.connect(self.start_running)
        # Stop Button - pause listener (does not stop)
        self.stop_button.pressed.connect(self.stop_listening)
        # Exit and Minimize buttons
        self.exit_button.clicked.connect(exit_program)
        self.minimize_button.clicked.connect(minimize_program)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ink Client"))
        self.title_label.setText(_translate("MainWindow", "Ink Client"))
        self.autoclick_box.setTitle(_translate("MainWindow", "Autoclicker"))
        self.axe_mode.setText(_translate("MainWindow", "Axe"))
        self.sword_mode.setText(_translate("MainWindow", "Sword"))
        self.autoclick_keybind_label.setText(_translate("MainWindow", "Keybind"))
        self.autoclick_keybind.setText(_translate("MainWindow", "r"))
        self.mc_mode_18.setText(_translate("MainWindow", "1.8"))
        self.mc_mode_19.setText(_translate("MainWindow", "1.9+"))
        self.min_cps_label.setText(_translate("MainWindow", "Min CPS:06"))
        self.max_cps_label.setText(_translate("MainWindow", "Max CPS:08"))
        self.sprint_box.setTitle(_translate("MainWindow", "Sprint"))
        self.sprint_keybind_label.setText(_translate("MainWindow", "Keybind"))
        self.sprint_keybind.setText(_translate("MainWindow", "n"))
        self.mc_sprint_keybind_label.setText(_translate("MainWindow", "MC Keybind"))
        self.mc_sprint_keybind.setText(_translate("MainWindow", "v"))
        self.status_box.setTitle(_translate("MainWindow", "Status"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.stop_button.setText(_translate("MainWindow", "Stop"))

    def validateCPS(self, slider):
        """Update autoclicker's CPS and makes sure max > min cps."""
        min_cps = self.min_cps_slider.value()
        max_cps = self.max_cps_slider.value()
        if slider == 'max':
            if max_cps < min_cps:
                self.max_cps_slider.setValue(min_cps)
                self.max_cps_label.setText('Max CPS:{}'.format(str(min_cps).zfill(2)))
            else:
                inkclicker.clicker_settings.max_cps = max_cps
                self.max_cps_label.setText('Max CPS:{}'.format(str(max_cps).zfill(2)))
        else:
            if max_cps < min_cps:
                self.min_cps_slider.setValue(max_cps)
                self.min_cps_label.setText('Min CPS:{}'.format(str(max_cps).zfill(2)))
            else:
                inkclicker.clicker_settings.min_cps = min_cps
                self.min_cps_label.setText('Min CPS:{}'.format(str(min_cps).zfill(2)))

    def validateKeybind(self, mod):
        """Check and update new keybind input."""
        if mod == 'click':
            new_bind = self.autoclick_keybind.text()
            if new_bind.isalpha():
                inkclicker.clicker_settings.keybind = new_bind.lower()
        elif mod == 'sprint':
            new_bind = self.sprint_keybind.text()
            if new_bind.isalpha():
                inksprint.sprint_settings.keybind = new_bind.lower()
        elif mod == 'mc_sprint':
            new_bind = self.mc_sprint_keybind.text()
            if new_bind.isalpha():
                inksprint.sprint_settings.sprint_button = new_bind.lower()

    def start_running(self):
        """Initialize listeners and also toggles them."""
        inkcontrols.listening = True
        self.status_box.setTitle("Status - Running")
        if not k_listen.is_alive():
            k_listen.start()
        if not ac.is_alive():
            ac.start()
        if not m_listen.is_alive():
            m_listen.start()

    def stop_listening(self):
        """Temporarily disable listeners."""
        inkcontrols.listening = False
        self.status_box.setTitle("Status - Not Running")


def change_mode(version):
    """Change minecraft version (18, 19)."""
    inkclicker.clicker_settings.mode = version


def change_status(mod):
    """Update GUI."""
    if mod == 'click':
        ui.autoclick_box.setTitle("Autoclick - {}".format('On' if inkclicker.clicker_settings.toggled else 'Off'))
    elif mod == 'sprint':
        ui.sprint_box.setTitle("Sprint - {}".format('On' if inksprint.sprint_settings.toggled else 'Off'))


def change_attack(speed):
    """Change the attack mode for 1.9+ (Sword/Axe). Speed refers to the cooldown time of weapon."""
    inkclicker.clicker_settings.cooldown_mode = speed


def minimize_program():
    MainWindow.showMinimized()


def exit_program():
    """Stop listener threads and exit program."""
    inkclicker.clicker_settings.running = False  # ac thread stops when set to false
    if k_listen.is_alive():
        k_listen.stop()
    if m_listen.is_alive():
        m_listen.stop()
    MainWindow.close()


if __name__ == "__main__":
    import sys
    # Load GUI
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # initialize autoclicker and listeners
    inkcontrols.init_window(ui)
    ac = inkclicker.clicker()
    k_listen = inkcontrols.init_keyboard_listener()
    m_listen = inkcontrols.init_mouse_listener()
    # Show GUI
    MainWindow.show()
    sys.exit(app.exec_())
