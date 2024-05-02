from PySide6.QtWidgets import QMainWindow, QFileDialog, QFileSystemModel, QWidget, QTextEdit, QGridLayout, QTabWidget, QMenu
from vscode_clone import Ui_MainWindow
from PySide6.QtCore import Qt, QSize, QPoint
from PySide6.QtGui import QAction, QKeySequence,QFont
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):

        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setupUi(self)
        self.tabWidget = QTabWidget(self.SW3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabsClosable(True)

        font = QFont()
        font.setFamilies([u"Roboto Medium"])
        font.setPointSize(12)
        font.setBold(False)
        self.tabWidget.setFont(font)

        self.closeWindow.clicked.connect(self.close_window)
        self.file_btn.setChecked(True)
        self.splitLeft_btn.setChecked(True)
        self.terminal_btn.setChecked(True)
        self.SW2.hide()

        self.file_btn.clicked.connect(self.tel)
        self.search_btn.clicked.connect(self.tel)
        self.sourceControl_btn.clicked.connect(self.tel)
        self.debug_btn.clicked.connect(self.tel)
        self.extensions_btn.clicked.connect(self.tel)
        self.testing_btn.clicked.connect(self.tel)

        self.terminal_btn.clicked.connect(self.tel1)
        self.ports_btn.clicked.connect(self.tel1)
        self.debugCpnsole_btn.clicked.connect(self.tel1)
        self.output_btn.clicked.connect(self.tel1)
        self.problems_btn.clicked.connect(self.tel1)

        self.splitLeft_btn.clicked.connect(self.splitLeftSW1)
        self.splitDoawn_btn.clicked.connect(self.splitLeftSW2)
        self.exitTerminal_btn.clicked.connect(self.hideTerminal)
        self.maximizeTerminal_btn.clicked.connect(self.maximizeTerminal)

        self.file.clicked.connect(self.fileMenu)

        self.tabWidget.tabCloseRequested.connect(self.closeTab)

        self.treeView.doubleClicked.connect(self.createTab)

        self.maximizeWindow.clicked.connect(self.resWindow)

        self.showMaximized()

    def resWindow(self,checked):
        if checked == True:
            self.showNormal()
        else:
            self.showMaximized()

    def createTab(self):
        
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")

        self.gridLayout_7 = QGridLayout(self.tab)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QTextEdit(self.tab)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_7.addWidget(self.textEdit, 0, 0, 1, 1)

        a = self.tabWidget.addTab(self.tab, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), self.treeView.currentIndex().data())

        self.tabWidget.setCurrentIndex(a)

        index = self.treeView.selectedIndexes()[0]
        info = self.treeView.model().fileInfo(index)
        
        file = open(info.absoluteFilePath())

        code = file.read()

        file.close()
        
        new = str(highlight(code, PythonLexer(), HtmlFormatter()))

        k = new.splitlines()

        new = ""

        for i in range(len(k)):
            new = new + k[i] + "<br>"

        html = '''<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
                <html>
                <head><meta name="qrichtext" content="1" /><meta charset="utf-8" />
                    <style>
                    pre { font-family: "Lucida Console", "Courier New", monospace;
                          font-size: 16px;
                          line-height: 150%; }
                    td.linenos .normal { color: red; background-color: transparent; padding-left: 5px; padding-right: 5px; }
                    span.linenos { color: red; background-color: transparent; padding-left: 5px; padding-right: 5px; }
                    td.linenos .special { color: red; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
                    span.linenos.special { color: red; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
                    .highlight .hll { background-color: #49483e }
                    .highlight { background: #0F111A; color: #f8f8f2 }
                    .highlight .c { color: #959077 } /* Comment */
                    .highlight .err { color: #ed007e; background-color: #1e0010 } /* Error */
                    .highlight .esc { color: #f8f8f2 } /* Escape */
                    .highlight .g { color: #f8f8f2 } /* Generic */
                    .highlight .k { color: #66d9ef } /* Keyword */
                    .highlight .l { color: #ae81ff } /* Literal */
                    .highlight .n { color: #f8f8f2 } /* Name */
                    .highlight .o { color: #ff4689 } /* Operator */
                    .highlight .x { color: #f8f8f2 } /* Other */
                    .highlight .p { color: #f8f8f2 } /* Punctuation */
                    .highlight .ch { color: #959077 } /* Comment.Hashbang */
                    .highlight .cm { color: #959077 } /* Comment.Multiline */
                    .highlight .cp { color: #959077 } /* Comment.Preproc */
                    .highlight .cpf { color: #959077 } /* Comment.PreprocFile */
                    .highlight .c1 { color: #959077 } /* Comment.Single */
                    .highlight .cs { color: #959077 } /* Comment.Special */
                    .highlight .gd { color: #ff4689 } /* Generic.Deleted */
                    .highlight .ge { color: #f8f8f2; font-style: italic } /* Generic.Emph */
                    .highlight .ges { color: #f8f8f2; font-weight: bold; font-style: italic } /* Generic.EmphStrong */
                    .highlight .gr { color: #f8f8f2 } /* Generic.Error */
                    .highlight .gh { color: #f8f8f2 } /* Generic.Heading */
                    .highlight .gi { color: #a6e22e } /* Generic.Inserted */
                    .highlight .go { color: #66d9ef } /* Generic.Output */
                    .highlight .gp { color: #ff4689; font-weight: bold } /* Generic.Prompt */
                    .highlight .gs { color: #f8f8f2; font-weight: bold } /* Generic.Strong */
                    .highlight .gu { color: #959077 } /* Generic.Subheading */
                    .highlight .gt { color: #f8f8f2 } /* Generic.Traceback */
                    .highlight .kc { color: #66d9ef } /* Keyword.Constant */
                    .highlight .kd { color: #66d9ef } /* Keyword.Declaration */
                    .highlight .kn { color: #ff4689 } /* Keyword.Namespace */
                    .highlight .kp { color: #66d9ef } /* Keyword.Pseudo */
                    .highlight .kr { color: #66d9ef } /* Keyword.Reserved */
                    .highlight .kt { color: #66d9ef } /* Keyword.Type */
                    .highlight .ld { color: #e6db74 } /* Literal.Date */
                    .highlight .m { color: #ae81ff } /* Literal.Number */
                    .highlight .s { color: #e6db74 } /* Literal.String */
                    .highlight .na { color: #a6e22e } /* Name.Attribute */
                    .highlight .nb { color: #f8f8f2 } /* Name.Builtin */
                    .highlight .nc { color: #a6e22e } /* Name.Class */
                    .highlight .no { color: #66d9ef } /* Name.Constant */
                    .highlight .nd { color: #a6e22e } /* Name.Decorator */
                    .highlight .ni { color: #f8f8f2 } /* Name.Entity */
                    .highlight .ne { color: #a6e22e } /* Name.Exception */
                    .highlight .nf { color: #a6e22e } /* Name.Function */
                    .highlight .nl { color: #f8f8f2 } /* Name.Label */
                    .highlight .nn { color: #f8f8f2 } /* Name.Namespace */
                    .highlight .nx { color: #a6e22e } /* Name.Other */
                    .highlight .py { color: #f8f8f2 } /* Name.Property */
                    .highlight .nt { color: #ff4689 } /* Name.Tag */
                    .highlight .nv { color: #f8f8f2 } /* Name.Variable */
                    .highlight .ow { color: #ff4689 } /* Operator.Word */
                    .highlight .pm { color: #f8f8f2 } /* Punctuation.Marker */
                    .highlight .w { color: #f8f8f2 } /* Text.Whitespace */
                    .highlight .mb { color: #ae81ff } /* Literal.Number.Bin */
                    .highlight .mf { color: #ae81ff } /* Literal.Number.Float */
                    .highlight .mh { color: #ae81ff } /* Literal.Number.Hex */
                    .highlight .mi { color: #ae81ff } /* Literal.Number.Integer */
                    .highlight .mo { color: #ae81ff } /* Literal.Number.Oct */
                    .highlight .sa { color: #e6db74 } /* Literal.String.Affix */
                    .highlight .sb { color: #e6db74 } /* Literal.String.Backtick */
                    .highlight .sc { color: #e6db74 } /* Literal.String.Char */
                    .highlight .dl { color: #e6db74 } /* Literal.String.Delimiter */
                    .highlight .sd { color: #e6db74 } /* Literal.String.Doc */
                    .highlight .s2 { color: #e6db74 } /* Literal.String.Double */
                    .highlight .se { color: #ae81ff } /* Literal.String.Escape */
                    .highlight .sh { color: #e6db74 } /* Literal.String.Heredoc */
                    .highlight .si { color: #e6db74 } /* Literal.String.Interpol */
                    .highlight .sx { color: #e6db74 } /* Literal.String.Other */
                    .highlight .sr { color: #e6db74 } /* Literal.String.Regex */
                    .highlight .s1 { color: #e6db74 } /* Literal.String.Single */
                    .highlight .ss { color: #e6db74 } /* Literal.String.Symbol */
                    .highlight .bp { color: #f8f8f2 } /* Name.Builtin.Pseudo */
                    .highlight .fm { color: #a6e22e } /* Name.Function.Magic */
                    .highlight .vc { color: #f8f8f2 } /* Name.Variable.Class */
                    .highlight .vg { color: #f8f8f2 } /* Name.Variable.Global */
                    .highlight .vi { color: #f8f8f2 } /* Name.Variable.Instance */
                    .highlight .vm { color: #f8f8f2 } /* Name.Variable.Magic */
                    .highlight .il { color: #ae81ff } /* Literal.Number.Integer.Long */
                    </style>
                </head> 
                <body>'''+new+'''
                </body>
                </html>
            '''

        self.textEdit.insertHtml(html)

    def splitLeftSW1(self):
        if self.splitLeft_btn.isChecked():
            self.SW1.show()
        else:
            self.SW1.hide()

    def splitLeftSW2(self):
        if self.splitDoawn_btn.isChecked():
            self.SW2.show()
        else:
            self.SW2.hide()

    def hideTerminal(self):
        self.splitDoawn_btn.setChecked(False)
        self.SW2.hide()

    def maximizeTerminal(self):
        if self.maximizeTerminal_btn.isChecked():
            self.SW2.setMaximumSize(QSize(16777215, 16777215))
            self.floatableWidget.hide()
            self.SW3.hide()

        else:
            self.SW2.setMaximumSize(QSize(16777215, 620))
            self.SW3.show()
            self.floatableWidget.show()

    def closeTab(self):
        self.tabWidget.removeTab(self.tabWidget.currentIndex())

    def resizeEvent(self, e):
        pos = QPoint(self.width()-105, 45)
        self.floatableWidget.move(pos)

    def close_window(self):
        self.close()

    def openFolder(self):
        file = QFileDialog.getExistingDirectory(
            None, 'Select a folder:', 'C:', QFileDialog.ShowDirsOnly)
        self.treeModel = QFileSystemModel()
        self.treeModel.setRootPath(file)
        self.treeView.setModel(self.treeModel)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.setHeaderHidden(True)
        self.treeView.setRootIndex(self.treeModel.index(file))

    def fileMenu(self):

        context = QMenu()

        button_action1 = QAction("New Text File")
        button_action1.setShortcut(QKeySequence("Ctrl+N"))

        context.addAction(button_action1)

        button_action2 = QAction("New File")
        button_action2.setShortcut(QKeySequence("Ctrl+Alt+N"))
        context.addAction(button_action2)

        button_action3 = QAction("New Window")
        button_action3.setShortcut(QKeySequence("Ctrl+Shift+N"))
        context.addAction(button_action3)

        context.addSeparator()

        button_action4 = QAction("Open File")
        button_action4.setShortcut(QKeySequence("Ctrl+O"))
        context.addAction(button_action4)

        button_action5 = QAction("Open Folder")
        button_action5.setShortcut(QKeySequence("Ctrl+K"))
        button_action5.triggered.connect(self.openFolder)
        context.addAction(button_action5)

        button_action6 = QAction("Open Workspace from File")
        context.addAction(button_action6)

        button_action7 = QAction("Open Recent")
        context.addAction(button_action7)

        context.addSeparator()

        button_action8 = QAction("Save")
        button_action8.setShortcut(QKeySequence("Ctrl+S"))
        context.addAction(button_action8)

        button_action9 = QAction("Save As")
        button_action9.setShortcut(QKeySequence("Ctrl+Shift+S"))
        context.addAction(button_action9)

        context.addSeparator()

        button_action10 = QAction("Exit")
        context.addAction(button_action10)

        pos = QPoint(self.file.pos().x()-25, self.file.pos().y()+34)

        context.exec(self.file.mapToParent(pos))

    def tel(self):
        self.SW1.show()
        self.splitLeft_btn.setChecked(True)
        if self.file_btn.isChecked():
            self.SW1.setCurrentIndex(0)
        if self.search_btn.isChecked():
            self.SW1.setCurrentIndex(1)
        if self.sourceControl_btn.isChecked():
            self.SW1.setCurrentIndex(2)
        if self.debug_btn.isChecked():
            self.SW1.setCurrentIndex(3)
        if self.extensions_btn.isChecked():
            self.SW1.setCurrentIndex(4)
        if self.testing_btn.isChecked():
            self.SW1.setCurrentIndex(5)

    def tel1(self):
        if self.terminal_btn.isChecked():
            self.terminalStackedWidget.setCurrentIndex(0)
        if self.ports_btn.isChecked():
            self.terminalStackedWidget.setCurrentIndex(4)
        if self.debugCpnsole_btn.isChecked():
            self.terminalStackedWidget.setCurrentIndex(1)
        if self.output_btn.isChecked():
            self.terminalStackedWidget.setCurrentIndex(2)
        if self.problems_btn.isChecked():
            self.terminalStackedWidget.setCurrentIndex(3)
    
    def mousePressEvent(self, event):
        self.dragPos = event.globalPosition().toPoint()


    def mouseMoveEvent(self, event):
      self.move(self.pos() + event.globalPosition().toPoint() - self.dragPos )
      self.dragPos = event.globalPosition().toPoint()
      event.accept()
