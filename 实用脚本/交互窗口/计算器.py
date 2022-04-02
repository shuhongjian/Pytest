import tkinter  # 使用Tkinter前需要先导入
import tkinter.messagebox
window = tkinter.Tk()
window.title('计算器')
window.geometry('500x300')

# 上下窗口
frame_index = tkinter.Frame(window).pack()
frame_top = tkinter.Frame(frame_index).pack(side='top')
frame_bottom = tkinter.Frame(frame_index).pack(side='bottom')




#定义了两个输入框
lab_1 = tkinter.Label(window,text = "输入数字1",bg = "green").place(x=50, y=50)
lab_2 = tkinter.Label(window,text = "输入数字2",bg = "yellow").place(x=50, y=100)

var_1 = tkinter.StringVar()
ent = tkinter.Entry(window,show=None,textvariable = var_1)
ent.place(x=140, y=50)
var_2 = tkinter.StringVar()
ent1 = tkinter.Entry(window,show=None,textvariable = var_2)
ent1.place(x=140, y=100)

# 加法函数
def add_fa():
    try:
        zhi_1 = int(ent.get())
        zhi_2 = int(ent1.get())
        add_zhi = zhi_1+zhi_2
        print(type(add_zhi))
        text_1.insert('insert',str(add_zhi))
    except:
        tkinter.messagebox.showinfo(title='警告', message='输入非法字符')
def subtraction():
    try:
        zhi_1 = int(ent.get())
        zhi_2 = int(ent1.get())
        sub_zhi = zhi_1-zhi_2
        text_1.insert('insert',str(sub_zhi))
    except:
        tkinter.messagebox.showinfo(title='警告', message='输入非法字符')
def multiply():
    try:
        zhi_1 = int(ent.get())
        zhi_2 = int(ent1.get())
        mul_zhi = zhi_1*zhi_2
        text_1.insert('insert',str(mul_zhi))
    except:
        tkinter.messagebox.showinfo(title='警告', message='输入非法字符')
def division():
    try:
        zhi_1 = int(ent.get())
        zhi_2 = int(ent1.get())
        if zhi_1 != 0:
            div_zhi = zhi_1/zhi_2
            text_1.insert('insert',str(div_zhi))
        else:
            tkinter.messagebox.showinfo(title='警告', message='输入非法字符')
    except:
        tkinter.messagebox.showinfo(title='警告', message='输入非法字符')

# 清空按钮
def empty():
    var_1.set('')
    var_2.set('')

    text_1.delete('1.0','end')
# 定义加减乘除四个按钮，和清空按钮
btn_1 = tkinter.Button(window,text = "加",command = add_fa).place(x=50,y= 150)
btn_2 = tkinter.Button(window,text = "减",command = subtraction).place(x=100,y= 150)
btn_3 = tkinter.Button(window,text = "乘",command = multiply).place(x=150,y= 150)
btn_4 = tkinter.Button(window,text = "除",command = division).place(x=200,y= 150)
btn_5 = tkinter.Button(window,text = "清空",bg = 'red',command = empty).place(x=300,y= 150)

# 定义输出结果
lab_3 = tkinter.Label(window,text = "输出结果").place(x = 50, y=200)
var_3 = tkinter.StringVar()
text_1 = tkinter.Text(window,height=1,width = 10)
text_1.place(x = 100,y = 200)

# 第5步，主窗口循环显示
window.mainloop()