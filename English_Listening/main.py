import time

from PIL import Image

import cv2

import pytesseract

import win32gui

import win32api

import win32ui 

import win32con

import difflib

import os

print("started")

def comparison(texts,word):
    print('hhh')
    
    
def window_capture(filename):
    # hwnd = 0 # 窗口的编号，0号表示当前活跃窗口
    hwnd = win32gui.FindWindow(None, "逍遥模拟器 - Android 7.1")
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, -120), (w, h-100), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
    
def click(pos):
    win32api.SetCursorPos(pos)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    
path = os.getcwd()
file=open(path+'\keywords_list.txt')
text=file.read()
list_answer=text.split(' ')
if len(list_answer)!=20:
    print(list_answer)
    print(len(list_answer))
    print("the format of answer is false")
    exit()
for i in range(len(list_answer)):#转换大小写
    if i<9:
        list_answer[i]=list_answer[i][2:].lower()
    else:
        list_answer[i]=list_answer[i][3:].lower()
print("list_answer",list_answer)
#处理答案txt

clock=time.time()
final=time.time()+1

selected=[[str(i+1)] for i in range(20)]#初始化选项list

flag=[False for i in range(20)]
ptr=0

while final-clock < 1500 :
    time.sleep(1)
    beg = time.time()
    for i in range(10):
        window_capture("C:/Users/陈柏诚大帅B/Desktop/English Listening/photo/2.jpg")
    end = time.time()
    print('running time:',end - beg)

    #读取截图中的文本
    data = pytesseract.image_to_data(Image.open(path+'\photo\2.jpg'), output_type=pytesseract.Output.DICT,lang='eng')
    text = pytesseract.image_to_string(Image.open(path+'\photo\2.jpg'),lang='eng')
    list1=text.split('\n')

    print("list1",list1)
    for i in list1:
        if len(i)<=5:#去除杂乱信息
            continue
        if (('0'<=i[0]<='9') and i[1]=='.') or (i[0]=='1' and ('0'<=i[1]<='9') and i[2]=='.'):
            #去除题目的序号
            if ('0'<=i[0]<='9') and i[1]=='.':
                num=int(i[0])-1
            elif (i[0]=='1' and ('0'<=i[1]<='9') and i[2]=='.'):
                num=int(i[0:2])-1
        if 'A'<=i[0]<='C' and i[1]=='.' and len(selected[num])<=4:
            #将每个题目的选项加入list(selected)
            selected[num].append(i)
    print("selected",selected)
    for i in range(len(selected)-1,-1,-1):
        if len(selected[i])<4:
            continue
        else:
            ptr=i
            break
    
    print("ptr:",ptr+1)#ptr+1即为题号
    que_ans=list_answer[ptr]
    print(que_ans)
    
    ptr_position=0
    data["text"].append('')
    for i in range(len(data["text"])):
        if que_ans in data["text"][i].lower():
            ptr_position=i
    print("ptr_position",ptr_position)
    
    hwnd = win32gui.FindWindow(None, "逍遥模拟器 - Android 7.1")
    rect=win32gui.GetWindowRect(hwnd)#获取窗口坐标
    pos=[data["left"][ptr_position]+rect[0],data["top"][ptr_position]+rect[1]+120]#获取答案在文本中的坐标
    win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
    click(pos)
    
    flag[ptr] = True
    time.sleep(1)
    print(ptr)#(ptr+1)-1即为上一个题号
    que_ans=list_answer[ptr-1]
    print(que_ans)
    
    ptr_position=0
    for i in range(len(data["text"])):
        if que_ans in data["text"][i].lower():
            ptr_position=i
    pos=[data["left"][ptr_position]+rect[0],data["top"][ptr_position]+rect[1]+120]
    print(pos)
    click(pos)
    #-------------------------------------------------------
    if flag[17]==True:
        que_ans=list_answer[18]
        print(que_ans)

        ptr_position=0
        for i in range(len(data["text"])):
            if que_ans in data["text"][i].lower():
                ptr_position=i
        pos=[data["left"][ptr_position]+rect[0],data["top"][ptr_position]+rect[1]+120]
        print(pos)
        click(pos)
        
        que_ans=list_answer[19]
        print(que_ans)

        ptr_position=0
        for i in range(len(data["text"])):
            if que_ans in data["text"][i].lower():
                ptr_position=i
        pos=[data["left"][ptr_position]+rect[0],data["top"][ptr_position]+rect[1]+120]
        print(pos)
        click(pos)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-1)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL,0,0,-1)
        que_ans=list_answer[19]
        print(que_ans)


#最后交卷
hwnd = win32gui.FindWindow(None, "逍遥模拟器 - Android 7.1")
rect=win32gui.GetWindowRect(hwnd)#获取窗口坐标
pos=[data["left"][ptr_position]+rect[0],data["top"][ptr_position]+rect[1]+120]#获取答案在文本中的坐标
win32api.SetCursorPos(rect[0]+500,rect[1]+1000)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)