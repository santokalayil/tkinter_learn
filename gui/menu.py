from settings.locations import menu_icon_folder, eccl_folder
from gui.functions import *

# menu bar
open_icon = PhotoImage(file=os.path.join(menu_icon_folder, 'open.png'))
save_icon = PhotoImage(file=os.path.join(menu_icon_folder, 'save.png'))
exit_icon = PhotoImage(file=os.path.join(menu_icon_folder, 'exit.png'))
about_icon = PhotoImage(file=os.path.join(menu_icon_folder, 'about.png'))
help_icon = PhotoImage(file=os.path.join(menu_icon_folder, 'help.png'))
license_icon = PhotoImage(file=os.path.join(menu_icon_folder, 'license.png'))
about_ecclesistica_icon = PhotoImage(file=os.path.join(eccl_folder, 'ecl_ico_round_smallest.png'))

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)  # , font=("Segoe MDL2 Assets", 10)
# tearoff is to get rid of lines above menu
file_menu.add_command(label='Open', command=open_file, image=open_icon, compound='left')
file_menu.add_command(label='Save', command=save_file, image=save_icon, compound='left')
file_menu.add_separator()
file_menu.add_command(label='Exit', command=quit, image=exit_icon, compound='left')  # quit function is prebuilt

menu_bar.add_cascade(label='File', menu=file_menu)

about_menu = Menu(menu_bar, tearoff=0)  # tearoff is to get rid of lines above menu
about_menu.add_command(label='Help', command=None, image=help_icon, compound='left')
about_menu.add_command(label='License', command=None, image=license_icon, compound='left')
about_menu.add_separator()
about_menu.add_command(label='About Author', command=None, image=about_icon, compound='left')  # quit function is prebuilt
about_menu.add_command(label='Ecclesiastica', command=None, image=about_ecclesistica_icon, compound='left')

menu_bar.add_cascade(label='About', menu=about_menu)