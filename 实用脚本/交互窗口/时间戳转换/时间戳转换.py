import tkinter
import tkinter.messagebox
import time
from tkinter import *
import bs4

# 初始化窗口
window = tkinter.Tk()
window.title("时间戳转换")
window.geometry("700x300")
# 主函数
# 每秒获取当前是时间戳
var_1 = tkinter.StringVar()
var_2 = tkinter.StringVar()
var_3 = tkinter.StringVar()
# 反映当前时间戳
lab_1 = tkinter.Label(window,text = "现在的时间戳：").place(x=250,y=10)
def newtime():
    var_1.set(int(time.time()))
    lab_3 = tkinter.Label(window, textvariable = var_1)
    lab_3.place(x=340, y=10)
    # 相当于反复重跑当前函数，使lable标签反复更新，但又不影响主进程
    lab_3.after(1000, newtime)
newtime()

timevar = 1

# 切换毫秒级与秒级
def timeHandoff_1():
    global timevar
    if timevar == 1:
        timevar = 2
        btn_1['text']= '10位秒级'
    else:
        timevar = 1
        btn_1['text'] = '13位毫秒级'
    window.update()

# 时间戳转换
def time_conersion():
    var_3.set('')
    time_var = var_2.get()
    try:
        time_var = int(time_var)
        a = len(str(time_var))
        print("输入的值：",a)
        if a == 10 or a == 13:
            if timevar == 1:
                heure = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_var/1000))
                ent_2.insert('end',heure)
            else:
                heure1 = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time_var))
                ent_2.insert('end',heure1)
        else:
            print("输入的字符长度错误")
    except:
        print("输入了非整数字符")


# 定义时间戳转换列
lab_2 = tkinter.Label(window,text = "时间戳").place(x=50,y=40)
text_1 = tkinter.Entry(window,show=None,textvariable = var_2)
text_1.place(x=110,y=43)

btn_1 = tkinter.Button(window,text = "13位毫秒级",command = timeHandoff_1,width = 9)
btn_1.place(x=50,y=70)

btn_2 = tkinter.Button(window,text = "转换",command = time_conersion,width = 5,height = 1).place(x=50,y=110)

#lab_3 = tkinter.Label(window,text = "北京时间").place(x=50,y=110)
ent_2 = tkinter.Entry(window,textvariable = var_3)
ent_2.place(x=110,y=115)


right_var1 = tkinter.StringVar()
right_var2 = tkinter.StringVar()
# 定义右边->时间转换为时间戳
# 给个默认的北京时间
def oldtime():
    rigth_old_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    right_var1.set(rigth_old_time)
timevar_1 = 1
def timeHandoff_2():
    global timevar_1
    if timevar_1 == 1:
        timevar_1 = 2
        right_btn_1['text']= '10位秒级'
    else:
        timevar_1 = 1
        right_btn_1['text'] = '13位毫秒级'
    window.update()

# 开始转换时间戳
def time_conersion_2():
    right_var2.set('')
    time_var = right_ent_1.get()
    try:
        newArray = time.strptime(time_var, "%Y-%m-%d %H:%M:%S")
        if timevar_1 == 1:
            newStamp = int(time.mktime(newArray))*1000
            right_ent_2.insert('end',newStamp)
        else:
            newStamp = int(time.mktime(newArray))
            right_ent_2.insert('end', newStamp)
    except:
        print("错误时间")
    pass

# 定义时间戳转换列
right_lab_2 = tkinter.Label(window,text = "北京时间").place(x=350,y=40)
right_ent_1 = tkinter.Entry(window,show=None,textvariable = right_var1)
oldtime()
right_ent_1.place(x=410,y=43)

right_btn_1 = tkinter.Button(window,text = "13位毫秒级",command = timeHandoff_2,width = 9)
right_btn_1.place(x=350,y=70)

right_btn_2 = tkinter.Button(window,text = "转换",command = time_conersion_2,width = 5,height = 1).place(x=350,y=110)

right_ent_2 = tkinter.Entry(window,textvariable = right_var2)
right_ent_2.place(x=410,y=115)


# 重置所有按钮
def empty():
    oldtime()
    right_var2.set('')
    var_3.set('')
    var_2.set('')

photo = PhotoImage(file = "D:/Pytest/实用脚本/交互窗口/时间戳转换/重置按钮.jpg")
btn_all = tkinter.Button(window,image = photo,command = empty).place(x=295,y=75)

#窗口持久化
window.mainloop()