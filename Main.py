#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.14
# In conjunction with Tcl version 8.6
#    Jul 29, 2018 09:51:46 PM

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import pythongui_support
from update_records import writedatabase as wd
from upd_status import update_status as us

i=-1
def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    pythongui_support.set_Tk_var()
    top = New_Toplevel (root)
    pythongui_support.init(root, top)
    root.title("Intern Management System")
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    pythongui_support.set_Tk_var()
    top = New_Toplevel (w)
    pythongui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 

        top.geometry("600x450+650+150")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")



        self.Button1 = Button(top)
        self.Button1.place(relx=0.12, rely=0.11, height=33, width=116)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Update Excel''')
        self.Button1.configure(width=116)

        self.Button2 = Button(top,command=wd.readcsv)
        self.Button2.place(relx=0.12, rely=0.29, height=33, width=116)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Read Excel''')
        self.Button2.configure(width=116)

       

        self.Button4 = Button(top)
        self.Button4.place(relx=0.12, rely=0.76, height=33, width=116)
        self.Button4.configure(activebackground="#d9d9d9")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Send Mail''')
        self.Button4.configure(width=116)

       

        self.Checkbutton1 = Checkbutton(top)
        self.Checkbutton1.place(relx=0.62, rely=0.51, relheight=0.07
                , relwidth=0.12)
        self.Checkbutton1.configure(activebackground="#d9d9d9")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify=LEFT)
        self.Checkbutton1.configure(text='''Called''')
        self.Checkbutton1.configure(variable=pythongui_support.che48)

        self.Checkbutton2 = Checkbutton(top)
        self.Checkbutton2.place(relx=0.82, rely=0.51, relheight=0.07
                , relwidth=0.17)
        self.Checkbutton2.configure(activebackground="#d9d9d9")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify=LEFT)
        self.Checkbutton2.configure(text='''Confirmed''')
        self.Checkbutton2.configure(variable=pythongui_support.che49)

        self.Label1 = Label(top)
        self.Label1.place(relx=0.38, rely=0.22, height=26, width=52)
        self.Label1.configure(background="#ffffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='ID')
        self.Label1.configure(width=112)

        self.Label2 = Label(top)
        self.Label2.place(relx=0.5, rely=0.22, height=26, width=142)
        self.Label2.configure(background="#ffffff")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='Email')
        self.Label2.configure(width=142)

        

        self.Label3 = Label(top)
        self.Label3.place(relx=0.8, rely=0.22, height=26, width=114)
        self.Label3.configure(background="#ffffff")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='Pno')
        self.Label3.configure(width=142)

        self.Label4 = Label(top)
        self.Label4.place(relx=0.38, rely=0.18, height=10, width=52)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='ID')
        self.Label4.configure(width=112)

        self.Label5 = Label(top)
        self.Label5.place(relx=0.5, rely=0.18, height=10, width=142)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='Email')
        self.Label5.configure(width=142)

        

        self.Label6 = Label(top)
        self.Label6.place(relx=0.8, rely=0.18, height=10, width=114)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='Pno')
        self.Label6.configure(width=142)

        def func_next():
            global i
            m=us.next(i)
            i=m
            lis = us.upd(m)
            self.Label1.config(text=lis[0])
            self.Label2.config(text=lis[1])
            self.Label3.config(text=lis[2])
            #print(m)

        def func_prev():
            global i
            m=us.prev(i)
            i=m
            lis = us.upd(m)
            self.Label1.config(text=lis[0])
            self.Label2.config(text=lis[1])
            self.Label3.config(text=lis[2])

        def func_sub():
            global i
            t1=pythongui_support.che48.get()
            t2=pythongui_support.che49.get()
            #print(t2)
            us.sub(t2,t1,i)

        self.Button6 = Button(top,command=func_prev)
        self.Button6.place(relx=0.6, rely=0.67, height=33, width=67)
        self.Button6.configure(activebackground="#d9d9d9")
        self.Button6.configure(activeforeground="#000000")
        self.Button6.configure(background="#d9d9d9")
        self.Button6.configure(disabledforeground="#a3a3a3")
        self.Button6.configure(foreground="#000000")
        self.Button6.configure(highlightbackground="#d9d9d9")
        self.Button6.configure(highlightcolor="black")
        self.Button6.configure(pady="0")
        self.Button6.configure(text='''Previous''')

        self.Button7 = Button(top,command=func_next)
        self.Button7.place(relx=0.72, rely=0.67, height=33, width=43)
        self.Button7.configure(activebackground="#d9d9d9")
        self.Button7.configure(activeforeground="#000000")
        self.Button7.configure(background="#d9d9d9")
        self.Button7.configure(disabledforeground="#a3a3a3")
        self.Button7.configure(foreground="#000000")
        self.Button7.configure(highlightbackground="#d9d9d9")
        self.Button7.configure(highlightcolor="black")
        self.Button7.configure(pady="0")
        self.Button7.configure(text='''Next''')

        self.Button8 = Button(top,command=func_sub)
        self.Button8.place(relx=0.88, rely=0.67, height=33, width=59)
        self.Button8.configure(activebackground="#d9d9d9")
        self.Button8.configure(activeforeground="#000000")
        self.Button8.configure(background="#d9d9d9")
        self.Button8.configure(disabledforeground="#a3a3a3")
        self.Button8.configure(foreground="#000000")
        self.Button8.configure(highlightbackground="#d9d9d9")
        self.Button8.configure(highlightcolor="black")
        self.Button8.configure(pady="0")
        self.Button8.configure(text='''Submit''')

        

       

       

        self.Button3 = Button(top)
        self.Button3.place(relx=0.12, rely=0.44, height=33, width=116)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Call Interns''')
        self.Button3.configure(width=116)

        self.Button5 = Button(top)
        self.Button5.place(relx=0.12, rely=0.6, height=33, width=116)
        self.Button5.configure(activebackground="#d9d9d9")
        self.Button5.configure(activeforeground="#000000")
        self.Button5.configure(background="#d9d9d9")
        self.Button5.configure(disabledforeground="#a3a3a3")
        self.Button5.configure(foreground="#000000")
        self.Button5.configure(highlightbackground="#d9d9d9")
        self.Button5.configure(highlightcolor="black")
        self.Button5.configure(pady="0")
        self.Button5.configure(text='''Generate''')
        self.Button5.configure(width=116)






if __name__ == '__main__':
    vp_start_gui()



