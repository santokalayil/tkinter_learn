from tkinter import Tk, PhotoImage, Menu
import os
from settings.window_settings import *
from settings.locations import *




window = Tk()
window.geometry(INITIAL_GEOMETRY)
window.title(APP_TITLE)
# window.config(background="#aaaaaa")


app_icon = PhotoImage(file=os.path.join(eccl_folder, 'ecl_ico_round.png'))
window.iconphoto(True, app_icon)

# executing menu code from gui/menu.py file
with open(os.path.join('gui', 'menu.py'), 'r') as py_file:
    menu_code = py_file.read()
exec(menu_code)

with open(os.path.join('gui', 'title_section.py'), 'r') as py_file:
    title_image_code = py_file.read()
exec(title_image_code)



with open(os.path.join('gui', 'family_table_frame.py'), 'r') as py_file:
    family_table_frame_code = py_file.read()
exec(family_table_frame_code)


window.mainloop()
