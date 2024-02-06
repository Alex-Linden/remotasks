from tkinter import *
import tkinter as tk
from tkinter import ttk


class Node:
    def __init__(self, data, top, down, left, right):
        self.data = data
        self.top = top
        self.down = down
        self.left = left
        self.right = right


class SkipList:
    def __init__(self):
        self.levels = []

    # insert operations core-most operation
    def insert(self, data):
        # checking if the data is already in the list, if so, throw the error
        for node in self.levels:
            if node.data == data:
                raise ValueError("Value already in the list, cannot insert again")

        # reading the levels
        for I in range(len(self.levels)):
            if self.levels[I] == None:
                new_node = Node(data, -1, 1, I,
                                self.levels[(I-1) if I!=0 else 0].data)
                self.levels[I] = new_node
                break
            if self.levels[I].data > data:
                new_node = Node(data, self.levels[I].data, 1, I,
                                self.levels[(I-1) if I!=0 else 0].data)
                self.levels[I:0] = [new_node]
                for k in range(I-2, -1, -1):
                    self.levels[k] = Node(self.levels[k+1].data, self.levels[k+2].data, 1, k,
                                          self.levels[(k - 1) if k != 0 else 0].data)
                self.align_list()
                return

        self.align_list()

    # remove function of the list operations
    def remove(self, data):
        None

    # Seaching function that searches for provided number
    def search(self, data):
        for I in range(len(self.levels)):
            if self.levels[I].data == data:
                return True, I
            if self.levels[I].data > data:
                return False, I
        return False, I

    # Aligns the created skip list
    def align_list(self):
        elements_list = []
        for I in range(len(self.levels)):
            str1 = []
            for j in range(len(self.levels)):
                str1.append(self.levels[j].data)
            elements_list.append(str1)

        #travels the each leaf and appar any none values with correct number
        for I in range(len(elements_list)):
            for j in range(len(elements_list[I])):
                if elements_list[I][j] is None:
                    for k in range(len(elements_list) - 1, I - 1, -1):
                        if elements_list[k][j] < elements_list[k + 1][j]:
                            elements_list[k][j] = elements_list[k + 1][j]
                        if elements_list[k][j] == elements_list[k + 1][j]:
                            break

    def print_complete_list(self):
        elements_list = []
        for I in range(len(self.levels)):
            str1 = []
            for j in range(len(self.levels)):
                str1.append(self.levels[j].data)
            elements_list.append(str1)
        return elements_list

class SkipListGUIApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.skplist = SkipList()
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, InsertData):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#10ff73")
        tk.Frame(self, height=5, width=550, bg='#10ff73', relief='ridge').pack(side=tk.TOP, expand=True, fill=tk.BOTH)
        lbltext = 'Skip List visualization'
        lblfont = ('Arial', 25, 'bold')
        lbl = tk.Label(self, text=lbltext, fg='black', bg='#10ff73', font=lblfont)
        lbl.pack()
    def invoke_info():
        cont.show_frame(InsertData)
class InsertData(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent, bg="#00a015")

        def skplistinsert():

            text = textBox.get("1.0", "end-1c")
            textBox.delete("1.0", "end")
            if text == '':
                showerror("Message", 'Please insert a list of numbers')
            values = text.split()
            if len(values) < 1:
                showerror("Message", 'Please insert a list of numbers')
            else:
                if values[0] == '':
                    showerror("Message", 'Please insert a list of numbers')
                else:
                    for value in values:
                        try:
                             if int(value.replace(' ','')) < 0:
                                 showerror("Validation", "Please insert positive numbers")
                                 textBox.delete("1.0", "end")
                        except ValueError:
                            showerror("Validation", "Please insert positive numbers")
                            textBox.delete("1.0", "end")
                            return
                    if len(values) != 1:
                        showerror("Warning", 'No Scale Error. Insertion unique invalid')
            controller.skplist.insert(values)
            controller.show_frame(SkipListTitle)

        topFrame = tk.Frame(self, height = 5, width = 580 , relief = 'solid')
        middleFrame = tk.Frame(self, height = 580 , width = 650 , relief = 'solid')
        bottomFrame = tk.Frame(self, height = 5 , width = 580 , relief = 'solid')

        topFrame.pack(side = 'top', expand=True, fill=tk.BOTH)
        middleFrame.pack(side='top', expand=True, fill=tk.BOTH)
        bottomFrame.pack(side='top', expand=True, fill=tk.BOTH)

        tk.Button(topFrame, text = 'Insert Data').pack()

        button = tk.Button(middleFrame, text = 'Confirm', width = 25, height = 1, bd=10, disabledbackground = '#00cc15', command = skplistinsert())
        button.pack()

        textBox = tk.Text(middleFrame, height=4, width=60)
        textBox.pack(anchor=tk.CENTER)

class SkipListTitle(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tk.Frame(self, height = 5 , width = 650 , relief = 'solid').pack(side=tk.TOP, expand=True, fill=tk.BOTH)

        lbltext = 'The creation of a node in a skip list is same as Linked List.'
        lblfont = ('Arial', 25, 'bold')
        lbl = tk.Label(self, text = 'Skip List Visualization, its Creation and Insertion in Python', fg ='black', bg='#ffb536', font = lblfont)
        lbl.pack()
if __name__ == '__main__':
    app = SampleApp()
    app.mainloop()
