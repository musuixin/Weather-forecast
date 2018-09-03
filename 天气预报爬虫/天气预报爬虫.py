import requests
from bs4 import BeautifulSoup
import re
from tkinter import *
from xpinyin import Pinyin
def data():
    dizhi=Pinyin().get_pinyin(v1.get(),'')#默认分割符为-
    print(dizhi)
    url='https://www.tianqi.com/'+dizhi+'/'
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    html=requests.get(url,headers=head)
    html=html.text
    soup=BeautifulSoup(html,'lxml')
    data=soup.find(class_="raweather760")
    data=re.findall(r'title=\".*?℃\"',str(data))
    text1.delete('1.0','end')
    for i in data:
        i=i.split('"')
        i=i[1]+'\n'
        text1.insert(INSERT,i)
#创建窗口
root=Tk()
root.geometry('420x400+200+300')

#添加标题
root.title('天气预报by慕随心')

#添加标签(label)
#tupian=PhotoImage(file='1.gif')
label1=Label(root,font='楷体',text="请输入要查询天气城市的拼音:").grid(row=0)
#添加输入框(entry)
v1=StringVar()
e1=Entry(root,textvariable=v1).grid(row=0,column=1)
#添加文本框
text1=Text(root,width=40,height=50)
text1.grid(row=2)
#添加按钮(button)
button1=Button(root,font='楷体',text='查询',command=data).grid(row=1,column=0)
button2=Button(root,font='楷体',text='退出',command=root.quit).grid(row=1,column=1)
#显示窗口
root.mainloop()
