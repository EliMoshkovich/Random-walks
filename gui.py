from tkinter import *
from tkinter import messagebox

from Graph_from_txt import GraphFromTxt
from drive import Drive


# This is the gui class. Here we init all the gui and start the project.
class GUI:
    def __init__(self, root, D):
        self.root = root
        self.D = D
        root.title("Random Walk")
        root.resizable(width=False, height=False)
        menu = Menu(root)
        root.config(menu=menu)
        root.geometry("400x250+600+300")

        filemenu = Menu(menu, tearoff=0)
        filemenu.add_command(label='Open...', command=self.build_from_text)
        filemenu.add_separator()
        filemenu.add_command(label='Exit', command=root.quit)
        menu.add_cascade(label='File', menu=filemenu)
        helpmenu = Menu(menu, tearoff=0)
        menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About', command=self.about)

        label = Label(root, text="Choose which Graph you would like:")
        label.config(font=("Courier", 14))
        label.pack()

        l1 = Label(root, text="Nodes")
        l2 = Label(root, text="Edges (degree, for a regular graph)")
        self.e1 = Entry(root)
        self.e2 = Entry(root)
        l1.pack(fill=X)
        self.e1.pack()
        l2.pack(fill=X)
        self.e2.pack()

        self.show_graph = IntVar()
        c = Checkbutton(root, text="Show Graph", variable=self.show_graph, onvalue=1, offvalue=0)
        c.pack()

        Button(root, text='Regular Graph', command=self.build_regular).pack(fill="none", expand=True)
        Button(root, text='Random Graph', command=self.build_random).pack(fill="none", expand=True)
        Button(root, text='Tree Graph', command=self.build_tree).pack(fill="none", expand=True)

    # Here we run the random walk on the most recently built graph.
    def build_from_text(self):
        try:
            parse = GraphFromTxt()
        except FileNotFoundError:
            messagebox.showerror('Error!', 'No saved graph found. Please build a graph first.')
            return
        parse.run_random(self.show_graph.get())

    # This is the about pop up.
    def about(self):
        messagebox.showinfo('About', 'Hi and welcome to our Project!\n'
                            'In here you will find our Random Walk project and can choose in which graph you would like to run.\n'
                            'You can build a tree, a regular graph and a random graph.\n'
                            'After that just choose File-->Open and it will open your last built Graph and run random walk on it.')

    # This function builds the tree graph with the given attributes.
    def build_tree(self):
        try:
            self.D.update_v(int(self.e1.get()))
            if self.D.v < 1:
                messagebox.showerror('Error!', 'Please insert a positive number of nodes!')
                return
            self.D.tree_graph()
        except ValueError:
            messagebox.showerror('Error!', 'Please insert an integer number of nodes!')

    # This function builds the regular graph with the given attributes.
    def build_regular(self):
        try:
            self.D.update_v(int(self.e1.get()))
            self.D.update_e(int(self.e2.get()))
            if self.D.v < 1 or self.D.e < 0:
                messagebox.showerror('Error!', 'Please insert a positive number of nodes and a non-negative degree!')
            elif self.D.e * self.D.v % 2 != 0:
                messagebox.showerror('Error!', 'In a regular graph v * d must be even!')
            elif self.D.v <= self.D.e:
                messagebox.showerror('Error!', 'The degree must be smaller than the number of nodes!')
            else:
                self.D.regular_graph()
        except ValueError:
            messagebox.showerror('Error!', 'Please insert two integers!')

    # This function builds the random graph with the given attributes.
    def build_random(self):
        try:
            self.D.update_v(int(self.e1.get()))
            self.D.update_e(int(self.e2.get()))
            if self.D.v < 1 or self.D.e < 0:
                messagebox.showerror('Error!', 'Please insert a positive number of nodes and a non-negative number of edges!')
                return
            self.D.random_graph()
        except ValueError:
            messagebox.showerror('Error!', 'Please insert two integers!')


# Open the gui.
if __name__ == '__main__':
    root = Tk()
    my_gui = GUI(root, Drive())
    root.mainloop()
