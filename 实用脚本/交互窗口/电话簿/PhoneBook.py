import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as tkmsg
import sqlite3
import logging
from turtle import width

PROGRAM_NAME= 'PhoneBook'
VERSION = '1.0'
AUTHOR = '*.*.'

logging.basicConfig(filename='SQLCommand.log',level=logging.INFO)

class PhoneBook():
    db_filenmae = ''

    def __init__(self,root):
        self.root = root
        self.root.title(PROGRAM_NAME+' | V' + VERSION)
        self.root.iconbitmap('D:/Pytest/实用脚本/交互窗口/电话簿/图1.ico') # 图标
        self.root.resizable(0,0)
        self.create_gui()

    def create_gui(self):
        self.create_left_icon()
        self.create_top_right_lableframe()
        self.create_message_area()
        self.create_records_treeview()
        self.create_bottom_frame()
        self.create_bottom_buttons()

    def create_left_icon(self):
        photo = tkinter.PhotoImage(file='D:/Pytest/实用脚本/交互窗口/电话簿/图2.ico')
        icon_photo_label = tkinter.Label(self.root,image=photo)
        icon_photo_label.image = photo
        icon_photo_label.grid(row=0,column=0,padx=10,pady=12)
    def create_top_right_lableframe(self):
        add_record_labelframe = tkinter.LabelFrame(self.root,text = '新增记录',width = 400)
        add_record_labelframe.grid(row=0,column=1,sticky='ew',padx=8,pady=8)

        tkinter.Label(add_record_labelframe,text = '姓名').grid(row=1,column=1,sticky='w',padx=8,pady=8)
        self.namefield = tkinter.Entry(add_record_labelframe)
        self.namefield.grid(row=1,column=2,sticky='w',padx=5,pady=2)

        tkinter.Label(add_record_labelframe,text = '电话').grid(row=2,column=1,sticky='w',padx=8,pady=8)
        self.namefield1 = tkinter.Entry(add_record_labelframe)
        self.namefield1.grid(row=2,column=2,sticky='w',padx=5,pady=2)

        tkinter.Button(add_record_labelframe,text = '新增').grid(row=3,column=2,sticky='w',padx=8,pady=8)

    def create_message_area(self):
        self.message_label = tkinter.Label(text = ' : -->',fg='red')
        self.message_label.grid(row=3,column=2,sticky='w')

    def create_records_treeview(self):
        treeview_columns = ['序号','姓名','电话号码']
        self.record_treeview = ttk.Treeview(self.root,show = 'headings',height = 5 ,columns = treeview_columns)
        self.record_treeview.grid(row=4,column=0,columnspan = 3)

        self.record_treeview.heading('序号',text = '序号',anchor = 'center')
        self.record_treeview.heading('姓名',text = '姓名',anchor = 'center')
        self.record_treeview.heading('电话号码',text = '电话号码',anchor = 'center')

        self.record_treeview.column('序号',width =50,anchor = 'center')
        self.record_treeview.column('姓名',width =120,anchor = 'center')
        self.record_treeview.column('电话号码',width =220,anchor = 'center')

    def create_bottom_frame(self):
        self.bottom_frame = tkinter.Frame(self.root,height = 30,background = 'yellow')
        self.bottom_frame.grid(row=5,column = 0,columnspan =3,sticky = 'w')

    def create_bottom_buttons(self):
        ttk.Button(self.bottom_frame,text='删除选中').pack(side="left")
        ttk.Button(self.bottom_frame,text='修改选中').pack(side="left")

        self.search_entry = ttk.Entry(self.bottom_frame,width = 18)
        self.search_entry.pack(side="left")
        ttk.Button(self.bottom_frame,text = '查询').pack(side="right")



if __name__ == '__main__':
    root = tkinter.Tk()
    app = PhoneBook(root)
    root.mainloop()