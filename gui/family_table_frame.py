from tkinter import LabelFrame, Label, Entry, Button
from tkinter import StringVar
from tkinter import LEFT
from db.connect import get
from tkinter.ttk import Treeview


def update_table_view(rows, clear=False):
    # global table_wrapper
    global tree_view
    if clear:
        tree_view.delete(*tree_view.get_children())
        # for column, column_name in zip(columns, columns):
        #     tree_view.heading(column, text=column_name)
    for row in rows:
        tree_view.insert('', 'end', values=row)


table_wrapper = LabelFrame(window, text='Family List')
search_wrapper = LabelFrame(window, text='Search')
data_wrapper = LabelFrame(window, text='Family Data')


table_wrapper.pack(fill='both', expand='yes', padx=20, pady=10)
search_wrapper.pack(fill='both', expand='yes', padx=20, pady=10)
data_wrapper.pack(fill='both', expand='yes', padx=20, pady=10)

# TABLE VIEW SECTION
# query = '''select famid, email, "where" from families;'''
query = '''select * from families;'''
# maps = ["Family ID", "Email", "Location"]
columns, rows = get(query)
tree_view = Treeview(table_wrapper, columns=columns, show='headings', height='6')
tree_view.pack()
for column, column_name in zip(columns, columns):
    tree_view.heading(column, text=column_name)
update_table_view(rows)


# SEARCH SECTION
qry = StringVar()


def search_cmd():
    global qry
    global search_wrapper
    query_text = qry.get()
    q = f'''SELECT * FROM families WHERE email LIKE '%{query_text}%' OR "where" LIKE '%{query_text}%' OR famid = '{query_text}';'''
    columns, rows = get(q)
    update_table_view(rows, clear=True)


def search_cmd_keyboard(event):  # event is needed for keyboard triggered callback function to work
    search_cmd()


def clear_cmd():
    q = f'''SELECT * FROM families;'''
    _, rws = get(q)
    update_table_view(rws, clear=True)


def clear_cmd_keyboard(event):  # event is needed for keyboard triggered callback function to work
    clear_cmd()


search_label = Label(search_wrapper, text="Search")
search_label.pack(side=LEFT, padx=10)
search_entry = Entry(search_wrapper, textvariable=qry)
search_entry.bind("<Return>", search_cmd_keyboard)
search_entry.pack(side=LEFT, padx=6)
search_button = Button(search_wrapper, text="Search", command=search_cmd)
search_button.pack(side=LEFT, padx=6)
clear_button = Button(search_wrapper, text="Clear", command=clear_cmd)
search_entry.bind("<Escape>", clear_cmd_keyboard)
clear_button.pack(side=LEFT, padx=6)





