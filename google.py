import urllib.request
import execjs
import tkinter as tk
import pyautogui as pag
import win32clipboard
import win32con
import time
import os
import re
import tkinter.messagebox

from pynput.mouse import Listener
from pynput.keyboard import Key, Controller
import pyperclip
from pynput import keyboard



import multiprocessing
from multiprocessing import Value




def on_move(x, y):
    
    
    
    # 监听鼠标移动
    #print('Pointer moved to {0}'.format((x, y)))
    if a[0]=='鼠标按下'and a[1]=='鼠标松开':
    
        a[1]=2
        a[0]=1
        
        
        
    elif a[0]=='鼠标按下' and a[1]==2:
        a[1]='鼠标移动'

def on_click(x, y, button, pressed):

    
    # 监听鼠标点击
    #print('{0} at {1}'.format('Pressed' if pressed else 'Released', (x, y)))
    #print('鼠标按下:',(x,y))
    a[0]='鼠标按下'
    
    
    if not pressed:
        
        
        if a[1]=='鼠标移动':
            #print('鼠标松开在:',(x,y))
             
                
                
                
                
            a[0]=1
            a[1]=2
            #print('鼠标松开')
        
            return False

        elif a[1]==2:
            a[1]='鼠标松开'
    
    

def on_scroll(x, y, dx, dy):
    # 监听鼠标滚轮
    print('Scrolled {0}'.format((x, y)))

a=[1,2]
def get_ci():
            a=[1,2]

            with Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
                listener.join()
                keyboard = Controller()
                
                #检测剪切版里原有的东西
                try:
                    data_first=pyperclip.paste()
                except pyperclip.PyperclipException:
                    
                    data_first=''
                

                with keyboard.pressed(Key.ctrl):
                    

                     keyboard.press('c')
                    
                     time.sleep(0.2)

                     keyboard.release('c')
                
                try:
                    data_later=pyperclip.paste()
                    
                except pyperclip.PyperclipException:
                    
                    data_later='null'
                    
                
                if data_later!='null' and data_later!='':
                    
                    pyperclip.copy(data_first)
                    
                    
                    return data_later
                else:
                    pass
class Yuguii():

    def __init__(self):
        self.ctx = execjs.compile(""" 
        function TL(a) { 
        var k = ""; 
        var b = 406644; 
        var b1 = 3293161072; 

        var jd = "."; 
        var $b = "+-a^+6"; 
        var Zb = "+-3^+b+-f"; 

        for (var e = [], f = 0, g = 0; g < a.length; g++) { 
            var m = a.charCodeAt(g); 
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), 
            e[f++] = m >> 18 | 240, 
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, 
            e[f++] = m >> 6 & 63 | 128), 
            e[f++] = m & 63 | 128) 
        } 
        a = b; 
        for (f = 0; f < e.length; f++) a += e[f], 
        a = RL(a, $b); 
        a = RL(a, Zb); 
        a ^= b1 || 0; 
        0 > a && (a = (a & 2147483647) + 2147483648); 
        a %= 1E6; 
        return a.toString() + jd + (a ^ b) 
    }; 

    function RL(a, b) { 
        var t = "a"; 
        var Yb = "+"; 
        for (var c = 0; c < b.length - 2; c += 3) { 
            var d = b.charAt(c + 2), 
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d), 
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d 
        } 
        return a 
    } 
    """)

    def getTk(self, text):
        return self.ctx.call("TL", text)





def sentence(result):
    list=[]
    list_i=[]
    
    with open('json.txt','w',encoding='utf-8') as f:
        f.write(result)

    with open('json.txt','r',encoding='utf-8') as f:
        
        f=f.readlines()
        for i in f:
            #print(i)
            s=re.search(r'"(.*?)","',i)
            #print(s)
            if s!=None:
                #print(s.group())
                list.append(s.group())
            end_str=re.search(r'\,\[null',i,re.S)
            if end_str!=None:
                break
            
    #print(list)

    for i in list:
        
        i=i.replace('"','')
        i=i.replace(',','')
        i=i.replace('\\n','')
        i=i.replace('\\r','')
        #print(i)
        list_i.append(i)


    res = ''.join(list_i)
    #print('res是',res)
    return res
    
    
def word(result):
    list=[]
    list_i=[]
    with open('json.txt','w',encoding='utf-8') as f:
        f.write(result)
    with open('json.txt','r',encoding='utf-8') as f:
    
        f=f.readlines()
        count=0
        for i in f:
            #print(i)
            #print(i)
            if count==0:
        
                s=re.search(r'"(.*?)",',i)
       
                if s!=None:
                    #print(s.group())
                    list.append(s.group())
                    count=1
            
            s1=re.search(r'词",\[',i,re.S)

            if s1!=None:
                
                
                list.append(i)
                
            end_str=re.search(r'词",\[(.*?)[a-zA-Z]',i,re.S)
            if end_str!=None:
                #print(end_str.group())
                list.pop()
                break
       
        # end_str=re.search(r',\[\["',i,re.S)
        # print(end_str)
        # if end_str!=None:
            # s=re.findall(r'"(.*?)",',i)
            # list.append(s)
            # break
        

    #print(list)
    

    for i in list:
        
        i=i.replace('"',' ')
        i=i.replace(',','')
        i=i.replace('[','')
        i=i.replace(']','')
        i=i.replace('\\n','')
        
        s=re.sub('[a-zA-Z]+','',i)
        
        if s!=None:
            list_i.append(s)
        else:
            list_i.append(i)
    #print(list_i)


    res = ''.join(list_i)
    #print('res是',res)
    return res

#界面


    
    
    


        
    #右键菜单
def popupmenu1(event):
        menu1.post(event.x_root,event.y_root)
def popupmenu2(event):
        menu2.post(event.x_root,event.y_root)
def onPaste1():
    try:
        text = root.clipboard_get()
        
    except:

        pass
    try:
        if root.clipboard_get()!='':
            t1.insert('insert',str(text))
    except:
        pass
        
def onCopy1():
    global cpoy_is_set
    if t1.get('0.0','end').replace('\n','')!='':
        try:
            text = t1.get('1.0','end')
            root.clipboard_clear()
            root.clipboard_append(text)
            cpoy_is_set=True
        except:
            pass
def onPaste2():
    try:
        text = root.clipboard_get()
        
    except:
       
        pass
    try:
        if root.clipboard_get()!='':
            t2.insert('insert',str(text))
    except:
        pass
def onCopy2():
    global cpoy_is_set
    if t2.get('0.0','end').replace('\n','')!='':

        try:
            text = t2.get('1.0','end')
            root.clipboard_clear()
            root.clipboard_append(text)
            cpoy_is_set=True
        except:
            pass
#复制鼠标选中内容
def onselcopy2():
    global cpoy_is_set
    if t2.get('0.0','end').replace('\n','')!='':
        text2=t2.get('sel.first','sel.last')
        #print(text2)
        root.clipboard_clear()
        root.clipboard_append(text2)
        cpoy_is_set=True
        #print('zaizhe',cpoy_is_set)
        root.update()
        time.sleep(0.2)
        root.update()
def onselcopy1():
    global cpoy_is_set
    if t1.get('0.0','end').replace('\n','')!='':
        #print(t1.get('0.0','end'))
        text1=t1.get('sel.first','sel.last')
        #print(text1)
        root.clipboard_clear()
        root.clipboard_append(txet1)
        cpoy_is_set=True
        root.update()
        time.sleep(0.2)
        root.update()
    
    
def callback():
        
        
        #print(clipboard_get())
        #data=clipboard_get(root)
        
        #flag=later_clipboard(data)
        #print(ss)
        
        
        
        
        
        # if os.path.isfile("C:/data.dat")==True:
            # try:
                # with open('C:/data.dat','r',encoding='utf-8') as w:
                    # w=w.readlines()
                    # w=''.join(w)
                        
                    # print(w)
                    # if w !='':
                        # flag='change'

            # except UnicodeDecodeError:
                # pass
                    
        flag=ss['flag']
        data=ss['data']
        if flag=='change'and data!='none':
            #print('change')
            
            content=data
            js = Yuguii()
            tk1 = js.getTk(content)
            
            translate(content, tk1)
            t1.delete('0.0','end')
            t1.insert('0.0',content)
            t2.delete('0.0','end')
            t2.insert('0.0',res)
            
            ss['flag']='nochange'
            ss['data']='none'
           
            
            # with open('C:/data.dat','w',encoding='utf-8') as w:
                # w.write('')
                # flag='nochange'
        else:
            pass
        root.after(1000, callback)
def tran():
    if t1.get('0.0','end').replace('\n','')!='':
        
        content =t1.get('0.0','end')
        js = Yuguii()
        tk1 = js.getTk(content)
        
        translate(content, tk1)
        t1.delete('0.0','end')
        t1.insert('0.0',content)
        t2.delete('0.0','end')
        t2.insert('0.0',res)
        
    elif t1.get('0.0','end')=='':
        pass
        
def clear():
    t1.delete('0.0','end')
    t2.delete('0.0','end')
def StartMove(event):
    
    global x,y
    x = event.x

    y = event.y



def StopMove(event):
    global x,y
    x = None

    y = None

def OnMotion(event):
    global x,y

    deltax = event.x - x

    deltay = event.y - y

    X = root.winfo_x() + deltax

    Y = root.winfo_y() + deltay

    root.geometry("+%s+%s" % (X,Y))

def updata():
    global num,p2
    
    ck=chVarDis.get()
    
    if ck==1:
        tk.messagebox.showinfo('提示','取词打开')
        #print(num.value)
        num.value=1
        start()
        
    if ck==0:
        tk.messagebox.showinfo('提示','宝贝还能取一次词哦')
        
        num.value=0
        
        

        



def open_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        req = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(req)
       
        data = response.read().decode('utf-8')
        return data
    except urllib.error.URLError:
        tk.messagebox.showinfo('提示','网络请求错误')
        data='null'
        return data

def translate(content, tk):
    global res
    
    if len(content) > 4891:
        #print("翻译文本超过限制！")
        return
    if len(content)>0:
        chinese=re.findall(r'[\u4e00-\u9fa5]+',content)
        chinese=''.join(chinese)
        english=re.findall(r'[a-zA-Z]+',content)
        english=''.join(english)
        if len(chinese)>len(english):
            chinese=True
        else:
            chinese=False
    
    
    
    
    s=content
    content = urllib.parse.quote(content)

    url = "https://translate.google.cn/translate_a/single?client=webapp&sl=auto&tl=zh-CN&hl=zh-CN&" \
          "dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&clearbtn=1&otf=1&pc=1&ssel=0" \
          "&tsel=0&kc=3&tk=%s&q=%s" % (tk, content)
    url2 = 'https://translate.google.cn/translate_a/single?client=webapp&sl=zh-CN&tl=en&hl=zh-CN&'\
          'dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&otf=2&ssel=0'\
          '&tsel=0&kc=1&tk=%s&q=%s'% (tk, content)
          
          
    

    if chinese==True:
        result = open_url(url2)
        res=sentence(result)
        
    else:
        result = open_url(url)
    
        if ' 'in s and len(s)>18:
            res=sentence(result)
        else:
            res=word(result)
#if __name__=='__main__':





def start2(num,ss):
    # global is_start
    # is_start=False
    
    while 1:
        
        
        
        #print('进入取词')
        
       
        
        #print(num.value)
        if num.value==0:
            break
            
        data=get_ci()
        #传回来东西
        
        if data!=None :#and data!=data_first:
        
            # with open('C:/data.dat','w',encoding='utf-8') as d:
                # d.write(data)
            
            
            
            
            
            print('取词到的',data)
            ss['data']=data
            ss['flag']='change'
            
            
            
        
        

    
def start():
    global p2,num,ss
    
    p2 = multiprocessing.Process(target = start2,args=(num,ss))
    p2.start()

        
if __name__ == "__main__":
    multiprocessing.freeze_support()
    js = Yuguii()
    #初始化清空剪切板,
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32con.CF_UNICODETEXT,'null')
    win32clipboard.CloseClipboard()
    
    time.sleep(0.5)
    count=0
    save_data=0
    cpoy_is_set=False
    
    #共享内存
    
    
    
    num = Value('i', 1)
    ss=multiprocessing.Manager()
    ss=ss.dict({'data':'none','flag':'nochange'})
    
    p2 = multiprocessing.Process(target = start2,args=(num,ss))
    p2.start()
    
    
    width=500
    height=650
    root=tk.Tk()
    root.title('谷歌翻译')
    #屏幕居中
    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    
    
    root.maxsize(1000,650)
    root.minsize(250,325)

    root.geometry(alignstr)
    #root.resizable(width=False,height=False)
    root.wm_attributes('-topmost',1)
    
    
    
    

    canvas = tk.Canvas(root,width =width,height =height)


    
    canvas.pack(fill="both", expand=1,side=tk.TOP)
    
    canvas.bind("<ButtonPress-1>",StartMove)

    canvas.bind("<ButtonRelease-1>",StopMove)

    canvas.bind("<B1-Motion>",OnMotion)

    
    menu1 = tk.Menu(canvas, tearoff=0)
    menu1.add_command(label="全部复制", command=onCopy1)
    menu1.add_separator()
    menu1.add_command(label="复制", command=onselcopy1)
    menu1.add_separator()
    menu1.add_command(label="粘贴", command=onPaste1)
    
    
    b1=tk.Button(canvas,text='翻译',font=('宋体',12),command=tran)
    b1.place(relx = 0.3, rely = 0.446 , width=100, height=30)
    
    b2=tk.Button(canvas,text='清除',font=('宋体',12),command=clear)
    b2.place(relx =0.56, rely = 0.446 , width=100, height=30)
    
    #复选框
    chVarDis = tk.IntVar()   # 用来获取复选框是否被勾选，通过chVarDis.get()来获取其的状态,其状态值为int类型 勾选为1  未勾选为0
    check1 = tk.Checkbutton(canvas, text="取词", variable=chVarDis, state='normal',command=updata)    # text为该复选框后面显示的名称, variable将该复选框的状态赋值给一个变量，当state='disabled'时，该复选框为灰色，不能点的状态
         # 该复选框是否勾选,select为勾选, deselect为不勾选
    check1.place(relx =0.1, rely = 0.446 , width=100, height=30)
    check1.select()
    
    
    
    menu2 = tk.Menu(canvas, tearoff=0)
    menu2.add_command(label="全部复制", command=onCopy2)
    menu2.add_separator()
    menu2.add_command(label="复制", command=onselcopy2)
    menu2.add_separator()
    menu2.add_command(label="粘贴", command=onPaste2)
    
    
    
    


    t1=tk.Text(canvas,height=280,width=500,font =('新宋体',12))  #设置滚动条-不换行
    
    t1.place(x =0, y =0 , relwidth=1, relheight=0.43)
    t1.bind("<Button-3>",popupmenu1)
    
    
    # b2=tk.Button(canvas,text='清除',font=('楷体',13))
    # b2.place(x =200, y =100 , width=10, height=10)

    
    t2=tk.Text(canvas,height=300,width=500,font =('新宋体',12))
    t2.place(x =0, rely =0.50 , relwidth=1, relheight=0.49)
    t2.bind("<Button-3>",popupmenu2)
    
    
    
    
    root.after(1000, callback())
    
    
    root.mainloop()
    


