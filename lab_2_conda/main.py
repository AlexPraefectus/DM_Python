from tkinter import Tk, Menu, Button, messagebox, END
from webbrowser import open_new
from gui.window_2 import Window2 as Win2
from gui.window_3 import Window3 as Win3
from gui.window_4 import Window4 as Win4
from logic.graph import GraphDrawer
from data import male_objects, female_objects
from itertools import chain
from random import choice
from logic.genders import Male, Female

a = set()
b = set()
graph = GraphDrawer(set(), set())


def go_to_main():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.withdraw()


def go_to_win_2():
    win_2.win.deiconify()
    win_3.win.withdraw()
    win_4.win.withdraw()


def go_to_win_3():
    win_2.win.withdraw()
    win_3.win.deiconify()
    win_4.win.withdraw()


def go_to_win_4():
    win_2.win.withdraw()
    win_3.win.withdraw()
    win_4.win.deiconify()


def default_graph(event):
    global a, b, graph
    a = {choice(list(chain(male_objects, female_objects))) for i in range(10)}
    b = {choice(list(chain(male_objects, female_objects))) for i in range(10)}
    graph = GraphDrawer(a, b)
    graph.draw_graph_mother()
    graph.draw_graph_mother_in_law()


class NavMenu:
    def __init__(self):
        self.navmenu = Menu()
        self.navmenu.add_command(label='Main Window', font=16, command=go_to_main)
        self.navmenu.add_command(label='Window 2', font=16, command=go_to_win_2)
        self.navmenu.add_command(label='Window 3', font=16, command=go_to_win_3)
        self.navmenu.add_command(label='Window 4', font=16, command=go_to_win_4)
        self.menu = Menu()
        self.menu.add_cascade(label='Navigation', font=16, menu=self.navmenu)
        self.menu.add_command(label='GitHub', font=16,
                              command=lambda: open_new('https://github.com/AlexPraefectus/DM_Python'))
        self.menu.add_command(label='Info', font=16,
                              command=lambda: messagebox.showinfo('Info', 'Oleksandr Korienev, IV-7210\nVariant №23'))


def input_parser(event):
    tmp = win_2.textbox.get(1.0, END).split('&')
    global a, b, graph
    a.update([Male(i) for i in tmp[0].split()])
    a.update([Female(i) for i in tmp[1].split()])
    b.update([Male(i) for i in tmp[2].split()])
    b.update([Female(i) for i in tmp[3].split()])
    graph = GraphDrawer(a, b)
    print(a, b)


def show_a(event):
    win_3.a_set_list.delete(1, END)
    for i in a:
        win_3.a_set_list.insert(END, i.name)


def show_b(event):
    win_3.b_set_list.delete(1, END)
    for i in b:
        win_3.b_set_list.insert(END, i.name)


root = Tk()
root_menu = NavMenu()
root.config(menu=root_menu.menu)
default_graph_button = Button(root, text='draw \ndefault\n graphs', font=20, width=15, height=10)
default_graph_button.bind('<Button-1>', default_graph)
default_graph_button.pack()
root.geometry('600x600')

win_2 = Win2(root)
win_2.win.config(menu=NavMenu().menu)
win_2.collect.bind('<Button-1>', input_parser)


win_3 = Win3(root)
win_3_menu = NavMenu()
win_3.win.config(menu=win_3_menu.menu)
win_3.a_show_but.bind('<Button-1>', show_a)
win_3.b_show_but.bind('<Button-1>', show_b)
win_3.draw_s.bind('<Button-1>', lambda event: GraphDrawer(a, b).draw_graph_mother())
win_3.draw_r.bind('<Button-1>', lambda event: GraphDrawer(a, b).draw_graph_mother_in_law())

win_4 = Win4(root)
win_4.win.config(menu=NavMenu().menu)
win_4.but_intersection.bind('<Button-1>',
                            lambda event: graph.draw_graph_operation(graph.relation_maker.relation_intersection()))
win_4.but_union.bind('<Button-1>',
                     lambda event: graph.draw_graph_operation(graph.relation_maker.relation_union()))
win_4.but_dif1.bind('<Button-1>',
                    lambda event: graph.draw_graph_operation(graph.relation_maker.relation_difference()))
win_4.but_dif2.bind('<Button-1>',
                    lambda event: graph.draw_graph_operation(graph.relation_maker.relation_difference_with_u()))
win_4.but_reversed.bind('<Button-1>',
                    lambda event: graph.draw_graph_operation(graph.relation_maker.reversed_r_relation()))

root.mainloop()
