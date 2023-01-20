import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from Util import Util
from create_from_single_meta import Create_from_single_meta as cfcm
from create_from_folder import Create_from_folder as cff
__version__ = "3.0"
username = os.path.expanduser("~")
appPath = os.path.join(username, "Documents", "LuaCreator")

app_bg = "#1a1a1a"
button_bg = "#4d4d4d"
entry_bg = "#000000"
info_bg = "#808080"
entry_fg = "#ffffff"
fg = "#e6e6e6"

canvasRow = 3
formNum = 1

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("vehicles.lua creator " + __version__)
        self.geometry("375x300")
        self.resizable(False, False)
        self.config(bg="#1a1a1a")
        icon = "./cmp.ico"
        self.wm_iconbitmap(icon)
        CFF = cff()
        U = Util()
        #create menubar help menu and about option, and move window menu to it own menu on menu bar
        menubar = tk.Menu(self, bg=app_bg, fg=fg)
        #main menu
        window_menu = tk.Menu(menubar, tearoff=0, bg=app_bg, fg=fg)
        menubar.add_cascade(label="Menu", menu=window_menu)
        window_menu.add_command(label="Reset App", command=lambda: reset_all())
        window_menu.add_command(label="Minimize", command=lambda: self.iconify())
        window_menu.add_command(label="Close", command=lambda: self.destroy())
        
        #help menu
        self.config(menu=menubar)
        help_menu = tk.Menu(menubar, tearoff=0, bg=app_bg, fg=fg)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.about_callback)

        #create start screen
        self.start_frame = tk.Frame(self)
        self.start_frame.config(bg=app_bg)
        self.start_frame.place(relx=.5, rely=.5, anchor="center")
        welcome_label = tk.Label(self.start_frame, text="Welcome in the vehicles.lua creator!\n", justify=tk.CENTER, bg=app_bg, fg=fg)
        welcome_label.grid(column=0, row=0, columnspan=2)
        welcome_label.config(font=("Roboto", 12, "bold"))
        single_label_text = tk.Label(self.start_frame, text="Do you have a single meta file ", justify=tk.CENTER, bg=app_bg, fg=fg)
        single_label_text.grid(column=0, row=1, columnspan=2)
        single_label_text.config(font=("Roboto", 12))
        tk.Button(self.start_frame, text="Single meta file", command=self.single_file, width=20, bg=button_bg, fg=fg).grid(column=0, row=2, columnspan=2)
        folder_label_text = tk.Label(self.start_frame, text="Or folder structure\n with a structure of: \nCollection/brands/models/vehicles.meta", bg=app_bg, fg=fg)
        folder_label_text.grid(column=0, row=3, columnspan=2)
        folder_label_text.config(font=("Roboto", 12))
        tk.Button(self.start_frame, text="folder structure", command=self.folder_structure, width=20, bg=button_bg, fg=fg).grid(column=0, row=4, columnspan=2)
        
        #create single meta file selection screen
        self.single_frame = tk.Frame(self)
        self.single_frame.config(bg=app_bg)
        self.single_frame.place(relx=.5, rely=.5, anchor="center")
        single_label_text = tk.Label(self.single_frame, text="Press the select file button to select your meta file", justify=tk.CENTER, bg=app_bg, fg=fg)
        single_label_text.grid(column=0, row=0, columnspan=2)
        single_label_text.config(font=("Roboto", 10, "bold"))
        tk.Button(self.single_frame, text="Select meta file", command=lambda: select_meta_file(), width=20, bg=button_bg, fg=fg).grid(column=0, row=1)
        path_single = tk.Label(self.single_frame, text="", justify=tk.CENTER, width=45, pady=5, bd=2, relief="solid", bg=info_bg, fg=fg)
        path_single.grid(column=0, row=2, columnspan=2)
        tk.Button(self.single_frame, text="generate new date", command=lambda: generateDateSingle(), width=20, bg=button_bg, fg=fg).grid(column=0, row=3)
        prefix_single_input = tk.Entry(self.single_frame, width=20, justify=tk.CENTER, bg=entry_bg, fg=entry_fg)
        prefix_single_input.grid(column=1, row=3)
        tk.Label(self.single_frame, text="Shop:", bg=app_bg, fg=fg).grid(column=0, row=4)
        shop_single_entry = tk.Entry(self.single_frame, width=20, justify=tk.CENTER, bg=entry_bg, fg=entry_fg)
        shop_single_entry.grid(column=1, row=4)
        shop_single_entry.delete(0, tk.END)
        shop_single_entry.insert(0, 'pdm')
        tk.Label(self.single_frame, text="Price:", bg=app_bg, fg=fg).grid(column=0, row=5)
        price_single_entry = tk.Entry(self.single_frame, width=20, justify=tk.CENTER, bg=entry_bg, fg=entry_fg)
        price_single_entry.grid(column=1, row=5)
        price_single_entry.delete(0, tk.END)
        price_single_entry.insert(0, "4000")
        #mutliple choice for lua creation file
        tk.Label(self.single_frame, bg=app_bg, fg=fg, text="select lua type").grid(column=0, row=6)
        single_combo = ttk.Combobox(self.single_frame, values=["normal lua", "esx list", "qubus list"], state="readonly", background=app_bg, foreground=fg)
        single_combo.current(0)
        single_combo.grid(column=1, row=6)
        tk.Button(self.single_frame, text="create lua file", command=lambda: create_lua_file(), width=20, bg=button_bg, fg=fg).grid(column=0, row=7)
        msg_single = tk.Label(self.single_frame, text="", justify=tk.CENTER, width=45, pady=5, bd=2, relief="solid", bg=info_bg, fg=fg)
        msg_single.grid(column=0, row=8, columnspan=2)
        tk.Button(self.single_frame, text="Reset screen", command=lambda: resetSingle(), width=20, bg=button_bg, fg=fg).grid(column=0, row=9)
        tk.Button(self.single_frame, text="back to main screen", command=self.back, width=20, bg=button_bg, fg=fg).grid(column=1, row=9)
        self.single_frame.place_forget()

        def resetSingle():
            path_single.config(text="")
            prefix_single_input.delete(0, tk.END)
            shop_single_entry.delete(0, tk.END)
            shop_single_entry.insert(0, "pdm")
            price_single_entry.delete(0, tk.END)
            price_single_entry.insert(0, "4000")
            msg_single.config(text="")

        def generateDateSingle():
            prefix_single_input.delete(0, tk.END)
            prefix_single_input.insert(0, U.getDateNow())

        def select_meta_file():
            filename = filedialog.askopenfilename(filetypes=[("META files", "*.meta")])
            if filename:
                path_single.config(text=filename)

        def create_lua_file():
            if os.path.exists(path_single.cget('text')) and os.path.isfile(path_single.cget('text')):
                cfcm.create_lua_from_single_meta(path_single.cget('text'), "\\" + prefix_single_input.get(), shop_single_entry.get(), price_single_entry.get(), single_combo.get())
                msg_single.config(text="Lua file creation succesfull")
            else: 
                U.errorHandling(path_single.cget('text'), "not-found", prefix_single_input.get()) 
                msg_single.config(text="Failed to create lua file")
            

        #creeer folder selection screen
        self.folder_frame = tk.Frame(self)
        self.folder_frame.config(bg=app_bg)
        self.folder_frame.place(relx=.5, rely=.5, anchor="center")
        folder_label_text = tk.Label(self.folder_frame, text="Press the select folder button to select your \ncars collection folder", justify=tk.CENTER, bg=app_bg, fg=fg)
        folder_label_text.grid(column=0, row=0, columnspan=2)
        folder_label_text.config(font=("roboto", 10, "bold"))
        tk.Button(self.folder_frame, text="Select folder", command=lambda: select_folder(), width=20, bg=button_bg, fg=fg).grid(column=0, row=1)
        path_folder = tk.Label(self.folder_frame, text="", justify=tk.CENTER, width=45, pady=5, bd=2, relief="solid", bg=info_bg, fg=fg)
        path_folder.grid(column=0, row=2, columnspan=2)
        tk.Button(self.folder_frame, text="generate new date", command=lambda: generateDateFolder(), width=20, bg=button_bg, fg=fg).grid(column=0, row=3)
        prefix_folder_input = tk.Entry(self.folder_frame, width=20, justify=tk.CENTER, bg=entry_bg, fg=entry_fg)
        prefix_folder_input.grid(column=1, row=3)
        tk.Label(self.folder_frame, text="Shop:", bg=app_bg, fg=fg).grid(column=0, row=4)
        shop_folder_entry = tk.Entry(self.folder_frame, width=20, justify=tk.CENTER, bg=entry_bg, fg=entry_fg)
        shop_folder_entry.grid(column=1, row=4)
        shop_folder_entry.delete(0, tk.END)
        shop_folder_entry.insert(0, 'pdm')
        tk.Label(self.folder_frame, text="Price:", bg=app_bg, fg=fg).grid(column=0, row=5)
        price_folder_entry = tk.Entry(self.folder_frame, width=20, justify=tk.CENTER, bg=entry_bg, fg=entry_fg)
        price_folder_entry.grid(column=1, row=5)
        price_folder_entry.delete(0, tk.END)
        price_folder_entry.insert(0, '4000')
        tk.Label(self.folder_frame, bg=app_bg, fg=fg, text="select lua type").grid(column=0, row=6)
        folder_combo = ttk.Combobox(self.folder_frame, values=["normal lua", "esx list", "qubus list"], state="readonly", background=app_bg, foreground=fg)
        folder_combo.current(0)
        folder_combo.grid(column=1, row=6)
        tk.Button(self.folder_frame, text="Create lua file", command=lambda: create_lua_file_from_collection(), width=20, bg=button_bg, fg=fg).grid(column=0, row=7)
        msg_folder = tk.Label(self.folder_frame, text="", justify=tk.CENTER, width=45, pady=5, bd=2, relief="solid", bg=info_bg, fg=fg)
        msg_folder.grid(column=0, row=8, columnspan=2)
        tk.Button(self.folder_frame, text="Reset screen", command=lambda: resetFolder(), width=20, bg=button_bg, fg=fg).grid(column=0, row=9)
        tk.Button(self.folder_frame, text="back to main screen", command=self.back, width=20, bg=button_bg, fg=fg).grid(column=1, row=9)
        self.folder_frame.place_forget()

        def resetFolder():
            path_folder.config(text="")
            prefix_folder_input.delete(0, tk.END)
            shop_folder_entry.delete(0, tk.END)
            shop_folder_entry.insert(0, "pdm")
            price_folder_entry.delete(0, tk.END)
            price_folder_entry.insert(0, "4000")
            msg_folder.config(text="")

        def reset_all():
            path_folder.config(text="")
            prefix_folder_input.delete(0, tk.END)
            shop_folder_entry.delete(0, tk.END)
            shop_folder_entry.insert(0, "pdm")
            price_folder_entry.delete(0, tk.END)
            price_folder_entry.insert(0, "4000")
            msg_folder.config(text="")
            path_single.config(text="")
            prefix_single_input.delete(0, tk.END)
            shop_single_entry.delete(0, tk.END)
            shop_single_entry.insert(0, "pdm")
            price_single_entry.delete(0, tk.END)
            price_single_entry.insert(0, "4000")
            msg_single.config(text="")

        def generateDateFolder():
            prefix_folder_input.delete(0, tk.END)
            prefix_folder_input.insert(0, U.getDateNow())

        def select_folder():
            filename = filedialog.askdirectory()
            if filename:
                path_folder.config(text=filename + "/")


        def create_lua_file_from_collection():
            path = path_folder.cget('text')
            prefix = "\\" + prefix_folder_input.get()
            shop = shop_folder_entry.get()
            price = price_folder_entry.get()
            CFF.create_lua_from_folder_collection(path, prefix, shop, price, folder_combo.get())
            msg_folder.config(text="Lua file creation succesfull")
        
        # self.canvas = tk.Canvas(self)
        # self.canvas.pack(fill="both", expand=True)
        # self.advanced_mode_frame = tk.Frame(self.canvas)
        # self.canvas.create_window((0,0), window=self.advanced_mode_frame, anchor="nw")
        # v_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.canvas.yview)
        # v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        # self.canvas.config(yscrollcommand=v_scrollbar.set)
        # self.advanced_mode_frame.config(bg=app_bg)
        # self.advanced_mode_frame.pack(fill="both", expand=True)
        # tk.Label(self.advanced_mode_frame, text="Add new form part for job function", bg=app_bg, fg=fg).grid(column=0, row=0, columnspan=2)
        # tk.Button(self.advanced_mode_frame, text="back to main screen", command=self.back, width=20, bg=button_bg, fg=fg).grid(column=0, row=1)
        # tk.Button(self.advanced_mode_frame, bg=button_bg, fg=fg, width=20, text="Add function from meta", command=lambda: add_function_meta_form()).grid(column=0, row=2)
        # tk.Button(self.advanced_mode_frame, bg=button_bg, fg=fg, width=20, text="Add function from folder", command=lambda: add_function_folder_form()).grid(column=1, row=2)
        # self.canvas.pack_forget()
        
        # def add_function_meta_form():
        #     global canvasRow
        #     setattr(self, f"add_meta_btn{formNum}", tk.Button(self.advanced_mode_frame, text='Select meta file', command=lambda: select_meta_file_advanced(formNum), width=20, bg=button_bg, fg=fg))
        #     getattr(self, f"add_meta_btn{formNum}").grid(column=0, row=canvasRow)
        #     canvasRow += 1 
        #     setattr(self, f"meta_path{formNum}", tk.Label(self.advanced_mode_frame, text='', justify=tk.CENTER, width=45, pady=5, bd=2, relief='solid', bg=info_bg, fg=fg))
        #     getattr(self, f"meta_path{formNum}").grid(column=0, row=canvasRow, columnspan=2)
        #     canvasRow += 1


        # def add_function_folder_form():
        #     return

        # def select_meta_file_advanced(formNum):
        #     return

    def single_file(self):
        self.start_frame.place_forget()
        self.single_frame.place(relx=.5, rely=.5, anchor="center")
    
    def folder_structure(self):
        self.start_frame.place_forget()
        self.folder_frame.place(relx=.5, rely=.5, anchor="center")
    
    def advanced_mode(self):
        self.start_frame.place_forget()
        # self.canvas.pack()
    
    def back(self):
        self.folder_frame.place_forget()
        self.single_frame.place_forget()
        # self.canvas.pack_forget()
        self.start_frame.place(relx=.5, rely=.5, anchor="center")

    def about_callback(self):
        messagebox.showinfo(
            "About",
            f"""This program was made by Crazymontana, for my buddy TroublesomeJon.\n
The purpose of this program is to convert xml data from gtaV carpacks to lua scripts ready for use in FiveM.\n
All generated files will be saved in:\n'{appPath}'.\n
The version of this program is: {__version__}"""
        )
if __name__ == "__main__":
    app = GUI()
    app.mainloop()