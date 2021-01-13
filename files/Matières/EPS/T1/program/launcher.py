from p2x800 import *
#from Tableau_vers_ligne_de_commande import*
#from Main_shower import Main_Board
#from tkinter import*
#from re_redesining_fontselector_aspect import*
#from dumbfontpicker import *
#import os

class none():
    class shoo:
        def sho():
            gui = Tk()
            gui.geometry("250x70")
            Framemain = Frame(gui, borderwidth=0, relief=GROOVE)
            Framemain.pack(side=BOTTOM, padx=0, pady=0)
            Frame1 = Frame(Framemain, borderwidth=0, relief=GROOVE)
            Frame1.pack(side=BOTTOM, padx=0, pady=0)
            Frame2 = Frame(Frame1, borderwidth=0, relief=GROOVE)
            Frame2.pack(side=TOP, padx=0, pady=0)
            Frame3 = Frame(Frame1, borderwidth=0, relief=GROOVE)
            Frame3.pack(side=TOP, padx=0, pady=0)
            ST=Label(Framemain, text="Veuillez entrer votre prénom.")
            ST.pack(fill=X,pady=0,side=TOP)
            def getEntry():
                res = myEntry.get()
                print(res)
            myEntry = Entry(Frame2, width=40)
            myEntry.pack(pady=0)
            btn = Button(Frame3, height=1, width=10, text="Lire", command=getEntry)
            btn.pack(side=BOTTOM)
            gui.mainloop()
    class Caler:
        def get_date():
            import tkinter as tk
            from tkinter import ttk
            from tkcalendar import Calendar, DateEntry

        def cal_done():
            top.withdraw()
            root.quit()

            root = tk.Tk()
            root.withdraw() # keep the root window from appearing

            top = tk.Toplevel(root)

            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand1")
            cal.pack(fill="both", expand=True)
            ttk.Button(top, text="ok", command=cal_done).pack()

            selected_date = None
            root.mainloop()
            return cal.selection_get()

            selection = get_date()
            print(selection)

        try:
            import tkinter as tk
            from tkinter import ttk
        except ImportError:
            import Tkinter as tk
            import ttk
        try:
            from tkcalendar import Calendar, DateEntry
        except:
            try:
               print(" -m pip install tkcalendar")
            except:
                os.system("py -m pip install tkcalendar")
                
        def example1():
            def print_sel():
                print(cal.selection_get())

            top = tk.Toplevel(root)

            cal = Calendar(top,
                           font="Arial 14", selectmode='day',
                           cursor="hand1", year=2018, month=2, day=5)
            cal.pack(fill="both", expand=True)
            ttk.Button(top, text="ok", command=print_sel).pack()

        def example2():
            top = tk.Toplevel(root)

            ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

            cal = DateEntry(top, width=12, background='darkblue',
                            foreground='white', borderwidth=2)
            cal.pack(padx=10, pady=10)

        def CCCAAALLLEEERRR():
            root = Tk()
            s = ttk.Style(root)
            s.theme_use('clam')

            ttk.Button(root, text='Calendar', command=Caler.example1).pack(padx=10, pady=10)
            ttk.Button(root, text='DateEntry', command=Caler.example2).pack(padx=10, pady=10)

            root.mainloop()
    #shoo.sho()
    #Caler.get_date()
    #Caler.cal_done()
    #Caler.CCCAAALLLEEERRR()
    def Lianch():
        try:
            Main_Board.Shower(Main_Board())
            show_history=True
            if show_history==True:
                Main_Board.HistoryShower(Main_Board())
        except:
            print("Main_Board File not found, or not imported")

