#!/usr/bin/python
# -*- coding: UTF-8 -*-

import Tkinter
import info
import qiangke
import time


root = Tkinter.Tk()
# 进入消息循环
root.title('说实话我也不信这玩意能正常帮你抢课')
root.geometry('600x550')
root.resizable(width=False, height=True) #宽不可变, 高可变,默认为True


frm = Tkinter.Frame(root)



frm_1 = Tkinter.Frame(frm)
Tkinter.Label(frm_1, text='学号:', font=('Arial', 15)).pack(side=Tkinter.LEFT)

var1 = Tkinter.StringVar()
e1 = Tkinter.Entry(frm_1, textvariable = var1)
var1.set("16126193")
e1.pack(side=Tkinter.RIGHT)

frm_1.pack(side=Tkinter.TOP)
#2
frm_2 = Tkinter.Frame(frm)
Tkinter.Label(frm_2, text='密码:', font=('Arial', 15)).pack(side=Tkinter.LEFT)
var2 = Tkinter.StringVar()
e2 = Tkinter.Entry(frm_2, textvariable = var2)
var2.set("153019")
e2.pack(side=Tkinter.RIGHT)

frm_2.pack(side=Tkinter.TOP)

#3
frm_3 = Tkinter.Frame(frm)
Tkinter.Label(frm_3, text='最多重复:', font=('Arial', 15)).pack(side=Tkinter.LEFT)
var3 = Tkinter.StringVar()
e3 = Tkinter.Entry(frm_3, textvariable = var3)
var3.set("2")
e3.pack(side=Tkinter.LEFT)
Tkinter.Label(frm_3, text='次停止', font=('Arial', 15)).pack(side=Tkinter.LEFT)
frm_3.pack(side=Tkinter.TOP)

#3—2
frm_3_2 = Tkinter.Frame(frm)
Tkinter.Label(frm_3_2, text='每次重复间隔:', font=('Arial', 15)).pack(side=Tkinter.LEFT)
var3_2 = Tkinter.StringVar()
e3_2 = Tkinter.Entry(frm_3_2, textvariable = var3_2)
var3_2.set("2")
e3_2.pack(side=Tkinter.LEFT)
Tkinter.Label(frm_3_2, text='秒', font=('Arial', 15)).pack(side=Tkinter.LEFT)
frm_3_2.pack(side=Tkinter.TOP)


#4
frm_4 = Tkinter.Frame(frm)
Tkinter.Label(frm_4, text='课程value值:', font=('Arial', 15)).pack(side=Tkinter.LEFT)
var4 = Tkinter.StringVar()
e4 = Tkinter.Entry(frm_4, textvariable = var4)
var4.set("19559")
e4.pack(side=Tkinter.LEFT)
Tkinter.Label(frm_4, text='(不是课程编号！目前得从浏览器源代码查看)', font=('Arial', 15)).pack(side=Tkinter.LEFT)
frm_4.pack(side=Tkinter.TOP)


frm.pack()

t = Tkinter.Text()
t.pack()

def run():
    user = e1.get()
    #t.insert(Tkinter.END, 'user:' + user+'\n')
    password = e2.get()
    #t.insert(Tkinter.END,'password:' + password+'\n')
    times = e3.get()
    #t.insert(Tkinter.END, 'time:' + time3 + '\n')
    coursevalue = e4.get()
    #t.insert(Tkinter.END, 'coursevalue:' + coursevalue + '\n')
    times =  int(times)
    #更改用户名和密码
    interval = e3_2.get()
    interval = int(interval)
    im = info.PersonalInfo()
    im.set_info(user,password)
    #设置选课字典
    dict1 = {'checkbox':coursevalue}


    for i in range(times):
        str = qiangke.qiang(dict1)
        t.insert(Tkinter.END, '第%i次结果:' % (i + 1) + str + '\n')
        t.update()
        if str == '验证码错误！':
            t.insert(Tkinter.END, '验证码识别好难，让我再试一次=。=' + '\n')
            t.update()
            time.sleep(interval)
        elif str == '课程重复！':
            t.insert(Tkinter.END, '最终结果：这课程都重复了，你都自己选好了还尼玛让我帮你选？！'+ '\n')
            t.update()
            break
        elif str == '选课成功！':
            t.insert(Tkinter.END, '接种结果：成功啦~快去瞅一眼有没有选上！' + '\n')
            t.update()
            break

        if i == times-1:
            t.insert(Tkinter.END, '已经结束了貌似还是没有选成功，你多设置点次数好不好' + '\n')
            t.update()

    #dic2 = t.get()
def clear():
    t.delete(1.0, Tkinter.END)



frm5 = Tkinter.Frame(root)
Tkinter.Button(frm5, text="开始", command = run).pack(side=Tkinter.LEFT)
Tkinter.Button(frm5, text="清空", command = clear).pack()
frm5.pack(side=Tkinter.BOTTOM)


root.mainloop()