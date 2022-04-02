import tkinter
import tkinter.messagebox
import json
# 写一个登录窗口
window = tkinter.Tk()
window.title("登录界面")
window.geometry("500x300")

# 定义账号
user_1 = [
    {"username":"admin","password":"admin"}
]
# 声明全局变量
def varuser():
    global zhi_1, zhi_2, variable
    zhi_1 = ent.get()  # key
    zhi_2 = ent1.get()  # vale
    variable = -1
    print("打印zhi_1: ",zhi_1)

# 先实现简单的场景，输入账号密码后，点击注册，可以把账号密码加入账号
def zhuce():
    new_user = {}
    zhi_1 = ent.get()
    zhi_2 = ent1.get()
    new_user["username"] = zhi_1
    new_user["password"] = zhi_2
    user_1.append(new_user)
    tkinter.messagebox.showinfo(title="提示",message='注册成功')
    var_1.set('')
    var_2.set('')
    #print(user_1)

# 判断输入的账号密码是否在数据库中
def judgement():
    varuser()
    for i in user_1:
        if zhi_1 == i["username"]:
            variable = i
            break
        else:
            variable = -1
    return variable

# 实现登录场景
def login():
    var_user1 = judgement()
    varuser()
    print("返回的变量为：",var_user1)
    if var_user1 == -1:
        tkinter.messagebox.showinfo(title='警告', message='账号错误')
    else:
        if zhi_2 == var_user1["password"]:
            tkinter.messagebox.showinfo(title='提示', message='登录成功')
        else:
            tkinter.messagebox.showinfo(title='告警', message='密码错误')

# 定义两个账号、密码输入框
lab_1 = tkinter.Label(window,text = "账号",bg = "green").place(x=50, y=50)
lab_2 = tkinter.Label(window,text = "密码",bg = "yellow").place(x=50, y=100)
var_1 = tkinter.StringVar()
ent = tkinter.Entry(window,show=None,textvariable = var_1)
ent.place(x=140, y=50)
var_2 = tkinter.StringVar()
ent1 = tkinter.Entry(window,show=None,textvariable = var_2)
ent1.place(x=140, y=100)

# 定义登录按钮
btn_1 = tkinter.Button(window,text = "登录",width = 10,command = login).place(x=150,y= 150)
btn_2 = tkinter.Button(window,text = "注册",width = 10,command = zhuce).place(x=150,y= 200)

window.mainloop()