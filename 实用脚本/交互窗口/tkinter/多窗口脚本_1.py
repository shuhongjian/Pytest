from re import A
from tkinter import *
import time
import tkinter.ttk
import logging
from func_timeout import func_set_timeout
import threading

class Application(Frame):
    def __init__(self,master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        # ! 调用函数去创建菜单
        self.Menu_test1()
    
    def Menu_test1(self):

        notebook = tkinter.ttk.Notebook(self.master)
        fr1 = Frame()
        fr2 = Frame()

        notebook.add(fr1,text = '时间戳脚本')
        notebook.add(fr2,text = '格式化脚本')
        notebook.pack(padx = 10,pady=5,fill = tkinter.BOTH,expand = True)

        time_jiaoben(fr1)
        string_format(fr2)
class time_jiaoben():
    timevar_1 = 1
    timevar_2 = 1
    
    def __init__(self,fr1):
        super().__init__()
        # 存放所有组件
        var_1 = tkinter.StringVar()
        var_2 = tkinter.StringVar()
        var_3 = tkinter.StringVar()
        tkinter.Label(fr1,text = "现在的时间戳：").place(x=250,y=10)
        tkinter.Label(fr1,text = "时间戳").place(x=50,y=40)
        text_1 = tkinter.Entry(fr1,show=None,textvariable = var_2)
        text_1.place(x=110,y=43)
        
        def newtime():
            var_1.set(int(time.time()))
            lab_3 = tkinter.Label(fr1, textvariable = var_1)
            lab_3.place(x=340, y=10)
            # 相当于反复重跑当前函数，使lable标签反复更新，但又不影响主进程
            lab_3.after(1000, newtime)
        newtime()
        def timeHandoff_1():
            global timevar_1
            if self.timevar_1 == 1:
                self.timevar_1 = 2
                btn_1['text']= '10位秒级'
            else:
                self.timevar_1 = 1
                btn_1['text'] = '13位毫秒级'
            fr1.update()
        def time_conersion():
            var_3.set('')
            time_var = var_2.get()
            try:
                time_var = int(time_var)
                a = len(str(time_var))
                print("输入的值：",a)
                if a == 10 or a == 13:
                    if self.timevar_1 == 1:
                        heure = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_var/1000))
                        ent_2.insert('end',heure)
                    else:
                        heure1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_var))
                        ent_2.insert('end',heure1)
                else:
                    print("输入的字符长度错误")
            except:
                print("输入了非整数字符")
        
        btn_1 = tkinter.Button(fr1,text = "13位毫秒级",command = timeHandoff_1,width = 9)
        btn_1.place(x=50,y=70)

        tkinter.Button(fr1,text = "转换",command = time_conersion,width = 5,height = 1).place(x=50,y=110)
        ent_2 = tkinter.Entry(fr1,textvariable = var_3)
        ent_2.place(x=110,y=115)
        
        right_var1 = tkinter.StringVar()
        right_var2 = tkinter.StringVar()
        # 定义右边->时间转换为时间戳
        # 给个默认的北京时间
        def oldtime():
            rigth_old_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            right_var1.set(rigth_old_time)
        
        def timeHandoff_2():
            global timevar_2
            if self.timevar_2 == 1:
                self.timevar_2 = 2
                right_btn_1['text']= '10位秒级'
            else:
                self.timevar_2 = 1
                right_btn_1['text'] = '13位毫秒级'
            fr1.update()

        # 开始转换时间戳
        def time_conersion_2():
            right_var2.set('')
            time_var = right_ent_1.get()
            try:
                newArray = time.strptime(time_var, "%Y-%m-%d %H:%M:%S")
                if self.timevar_2 == 1:
                    newStamp = int(time.mktime(newArray))*1000
                    right_ent_2.insert('end',newStamp)
                else:
                    newStamp = int(time.mktime(newArray))
                    right_ent_2.insert('end', newStamp)
            except:
                print("错误时间")
            pass

        # 定义时间戳转换列
        tkinter.Label(fr1,text = "北京时间").place(x=350,y=40)
        right_ent_1 = tkinter.Entry(fr1,show=None,textvariable = right_var1)
        oldtime()
        right_ent_1.place(x=410,y=43)

        right_btn_1 = tkinter.Button(fr1,text = "13位毫秒级",command = timeHandoff_2,width = 9)
        right_btn_1.place(x=350,y=70)

        tkinter.Button(fr1,text = "转换",command = time_conersion_2,width = 5,height = 1).place(x=350,y=110)

        right_ent_2 = tkinter.Entry(fr1,textvariable = right_var2)
        right_ent_2.place(x=410,y=115)
        
        def empty():
            oldtime()
            right_var2.set('')
            var_3.set('')
            var_2.set('')
        photo = PhotoImage(file = 'D:/Pytest/实用脚本/交互窗口/tkinter/重置按钮.jpg')
        tkinter.Button(fr1,image = photo,command = empty).place(x=295,y=75)

class string_format():
    def __init__(self,fr2):
        #* 实现方法
        # ! 1.json格式化
        def format_json():
            try:
                i = 10
                j = A
                b = i+j
                Text_2.insert(b)
            except:
                Text_2.delete('1.0','end')
                Text_2.insert(INSERT,logging_1(1))
        # ! 2.json压缩

        # ! 3.英文翻译

        # ! 4.中文翻译

        # ! 5.清空文本
        def Empty_text():
            Text_1.delete('1.0','end')
            Text_2.delete('1.0','end')
            Text_2_2.get('1.0','end')
            pass
        # ! 公共方法
        def logging_1(self):
            if self == 1:
                a = logging.error('格式化错误')
                return str(a)

        #* fr2布局
        Label(fr2,text="左侧").grid(row=0,column=0)
        Text_1 = Text(fr2,width = 45,height = 30)
        Text_1.grid(row =1,column =0,rowspan =6)

        Button(fr2,text="json格式化",command = format_json).grid(row =1,column =1)
        Button(fr2,text="json压缩").grid(row =2,column =1)
        Button(fr2,text="英文翻译").grid(row =3,column =1)
        Button(fr2,text="中文翻译").grid(row =4,column =1)
        Button(fr2,text="清空文本",command =Empty_text).grid(row =5,column =1)

        Label(fr2,text="右侧").grid(row=0,column=12)
        Text_2 = Text(fr2,width = 45,height = 20)
        Text_2.grid(row =1,column =12,rowspan =3)
        
        Label(fr2,text="日志").grid(row=3,column=12,rowspan =4)
        
        Text_2_2 = Text(fr2,width = 45,height = 7)
        Text_2_2.grid(row =5,column =12,rowspan =2)


if __name__ == '__main__':
    root = Tk()
    root.geometry("730x470")
    root.title("优化脚本")
    app = Application(master = root)
    root.mainloop()