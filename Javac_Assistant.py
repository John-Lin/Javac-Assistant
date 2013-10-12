import os
from Tkinter import *
import tkFileDialog
import tkMessageBox
import time
import platform

class GUIDemo(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()

        if platform.system() == 'Windows' or platform.system() == 'Linux':
            self.createWidgets()
        else:
            self.createWidgets_Mac()

        self.userinput = ""
        self.userload = ""
        self.file_opt = options = {}

    def createWidgets_Mac(self):
        menubar = Menu(self.master, tearoff=0)
        self.master.config(menu=menubar)
        
        fileMenu = Menu(menubar, tearoff=0)

        fileMenu.add_command(label="Open File...", command=self.askopenfilenameMethod, accelerator="Command+O")
        fileMenu.add_command(label="Exit", command=self.quitMethod, accelerator="Command+W")

        self.bind_all("<Command-o>", self.askopenfilenameMethod)
        self.bind_all("<Command-q>", self.quitMethod)
        
        menubar.add_cascade(label="File", menu=fileMenu)

        RunMenu = Menu(menubar, tearoff=0)
        
        RunMenu.add_command(label="Run...", command=self.runMethod, accelerator="Command-r")
        RunMenu.add_command(label="Compile...", command=self.compileMethod, accelerator="Command-b")
        

        self.bind_all("<Command-r>", self.runMethod)
        self.bind_all("<Command-b>", self.compileMethod)
        
        menubar.add_cascade(label="Run", menu=RunMenu)

        HelpMenu = Menu(menubar, tearoff=0)

        HelpMenu.add_command(label="About Java Builder", command=self.aboutMethod, accelerator="Command-i")


        self.bind_all("<Command-i>", self.aboutMethod)
        
        menubar.add_cascade(label="Help", menu=HelpMenu)

        self.inputText = Label(self)
        self.inputText["text"] = "Input File Name"
        self.inputText.grid(row=0, column=0)
        
        self.inputField = Entry(self)
        self.inputField["width"] = 46
        self.inputField.grid(row=0, column=1, columnspan=4)

        self.load = Button(self)
        self.load["text"] = " Load "
        self.load.grid(row=0, column=7)
        self.load["command"] = self.activeMethod
        self.bind_all("<Return>", self.activeMethod)

        self.statusText = Label(self)
        self.statusText["text"] = "Status "
        self.statusText.grid(row=1, column=0)

        self.displayText = Label(self)
        self.displayText["text"] = "Something happened"
        self.displayText.grid(row=1, column=1, columnspan=4)



        self.var = IntVar()

        self.R0 = Radiobutton(self)
        self.R0["text"] = "Use Portable JDK"
        self.R0["variable"] = self.var
        self.R0["value"] = 1
        self.R0.grid(row=2, column=1)
        

        self.R1 = Radiobutton(self)
        self.R1["text"] = "Use Build-in JDK"
        self.R1["variable"] = self.var
        self.R1["value"] = 2
        self.R1.grid(row=2, column=4)
        self.R1["command"] = self.EnvVarSet
        self.R1.select()


        self.clear = Button(self)
        self.clear["text"] = " Clear "
        self.clear.grid(row=3, column=1)
        self.clear["command"] =  self.clearMethod

        self.run = Button(self, state=DISABLED)
        self.run["text"] = " Run "
        self.run.grid(row=3, column=2)
        self.run["command"] =  self.runMethod
        
        self.exit = Button(self)
        self.exit["text"] = " Cancel "
        self.exit.grid(row=3, column=4)
        self.exit["command"] = self.quitMethod

    def createWidgets(self):

        menubar = Menu(self.master, tearoff=0)
        self.master.config(menu=menubar)
        
        fileMenu = Menu(menubar, tearoff=0)
        fileMenu.add_command(label="Open File...", command=self.askopenfilenameMethod, accelerator="Ctrl+O")
        fileMenu.add_command(label="Exit", command=self.quitMethod, accelerator="Ctrl+Q")
        

        
        self.bind_all("<Control-o>", self.askopenfilenameMethod)
        self.bind_all("<Control-q>", self.quitMethod)
        
        menubar.add_cascade(label="File", menu=fileMenu)

        RunMenu = Menu(menubar, tearoff=0)
        
        RunMenu.add_command(label="Run...", command=self.runMethod, accelerator="F6")
        RunMenu.add_command(label="Compile...", command=self.compileMethod, accelerator="F5")
        
        
        self.bind_all("<F6>", self.runMethod)
        self.bind_all("<F5>", self.compileMethod)
        

        menubar.add_cascade(label="Run", menu=RunMenu)

        HelpMenu = Menu(menubar, tearoff=0)
        HelpMenu.add_command(label="About Java Builder", command=self.aboutMethod, accelerator="F1")

        self.bind_all("<F1>", self.aboutMethod)
        

        menubar.add_cascade(label="Help", menu=HelpMenu)

        self.inputText = Label(self)
        self.inputText["text"] = "Input File Name"
        self.inputText.grid(row=0, column=0)
        
        self.inputField = Entry(self)
        self.inputField["width"] = 46
        self.inputField.grid(row=0, column=1, columnspan=4)

        self.load = Button(self)
        self.load["text"] = " Load "
        self.load.grid(row=0, column=7)
        self.load["command"] = self.activeMethod
        self.bind_all("<Return>", self.activeMethod)

        self.statusText = Label(self)
        self.statusText["text"] = "Status "
        self.statusText.grid(row=1, column=0)

        self.displayText = Label(self)
        self.displayText["text"] = "Something happened"
        self.displayText.grid(row=1, column=1, columnspan=4)



        self.var = IntVar()

        self.R0 = Radiobutton(self)
        self.R0["text"] = "Use Portable JDK"
        self.R0["variable"] = self.var
        self.R0["value"] = 1
        self.R0.grid(row=2, column=1)
        self.R0.select()

        self.R1 = Radiobutton(self)
        self.R1["text"] = "Use Build-in JDK"
        self.R1["variable"] = self.var
        self.R1["value"] = 2
        self.R1.grid(row=2, column=4)
        self.R1["command"] = self.EnvVarSet



        self.clear = Button(self)
        self.clear["text"] = " Clear "
        self.clear.grid(row=3, column=1)
        self.clear["command"] =  self.clearMethod

        self.run = Button(self, state=DISABLED)
        self.run["text"] = " Run "
        self.run.grid(row=3, column=2)
        self.run["command"] =  self.runMethod

        self.exit = Button(self)
        self.exit["text"] = " Cancel "
        self.exit.grid(row=3, column=4)
        self.exit["command"] = self.quitMethod

    def compileMethod(self, event=None):
        
        if self.inputField.get():
            self.userinput = self.inputField.get()
            self.statusText["text"] = "Status "
            
            if (self.var.get()) <= 1:
                initTime = time.time()
                os.system('JDK7u15\\bin\\javac '+ 'JavaCodes\\' + self.userinput + '.java')
                duringTime = time.time() - initTime
            else:
                initTime = time.time()
                os.system('javac ' + self.userinput + '.java')
                duringTime = time.time() - initTime

            self.displayText["text"] = self.userinput + ".java has been Compiled.\n"+"Spent " + str(round(duringTime,2)) + " seconds"
        
        else:
            self.statusText["text"] = "Status "
            
            if (self.var.get()) <=1 :
                initTime = time.time()
                os.system('JDK7u15\\bin\\javac '+ self.userload)
                duringTime = time.time() - initTime
            else:
                initTime = time.time()
                os.system('javac '+ self.userload)
                duringTime = time.time() - initTime
                #print "Spent " + str(round(duringTime,2)) + " seconds"

            self.displayText["text"] = self.userload.split('/')[-1] + " has been Compiled.\n"+"Spent " + str(round(duringTime,2)) + " seconds"

    def runMethod(self, event=None):
        
        self.compileMethod()

        if self.inputField.get():
            self.userinput = self.inputField.get()
            
            if (self.var.get()) <= 1:
                os.system('JDK7u15\\bin\\java ' + '-classpath ' + 'JavaCodes ' + self.userinput)
            else:
                if os.path.exists('JavaCodes'):
                    os.system('java '+ '-classpath ' + 'JavaCodes ' + self.userinput)
                else:
                    os.system('java ' + self.userinput)
            #self.displayText["text"] = "Run " + self.userinput
        
        else:
            if (self.var.get()) <= 1:
                os.system('JDK7u15\\bin\\java ' + '-classpath ' + 'JavaCodes ' + self.userload.split('/')[-1].split('.')[0])
            else:
                if os.path.exists('JavaCodes'):
                    os.system('java ' + '-classpath ' + 'JavaCodes ' + self.userload.split('/')[-1].split('.')[0])
                else:
                    os.system('java ' + self.userload.split('/')[-1].split('.')[0])
            #self.displayText["text"] = "Run " + self.userload.split('/')[-1].split('.')[0]      
    
    def askopenfilenameMethod(self, event=None):
        self.userload = tkFileDialog.askopenfilename(**self.file_opt)
        
        if self.userload.split('.')[-1] == "java":
            self.statusText["text"] = "Load... "
            self.run['state'] = 'active'
            self.displayText["text"] = self.userload

        elif self.userload == "":
            pass

        elif self.userload.split('.')[-1] != "java":
            tkMessageBox.showwarning("Loading Error", "Please Load Java Code!!")
    
    def clearMethod(self):
        self.userinput = ""
        self.userload = ""
        self.run['state'] = 'disable'
        self.inputField.delete(0, END)
        self.displayText["text"] = "Now Terminal has been Cleared"
        
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

    def activeMethod(self, event=None):
        if os.path.exists(self.inputField.get() + ".java"):
        #if self.inputField.get():
            self.run['state'] = 'active'
        elif self.inputField.get() == "":
            self.askopenfilenameMethod()
        else:
            tkMessageBox.showwarning(" Loading Error ","Can NOT Find " + self.inputField.get() + ".java")

    def quitMethod(self, event=None):
        root.quit()
    
    def aboutMethod(self, event=None):
        tkMessageBox.showinfo("Java Builder", "Made by John-Lin\nMy Blog : http://linton.logdown.com/\nContact Me : ireri339@gmail.com")

    def EnvVarSet(self):
        tkMessageBox.showwarning(" Warning ","JDK Environment Variables Must be Set!")

if __name__ == '__main__':
    root = Tk()
    root.wm_title("Java Builder Beta")
    app = GUIDemo(master=root)
    app.mainloop()