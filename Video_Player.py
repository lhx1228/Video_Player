import tkinter
import webbrowser
from tkinter import *
from tkinter import filedialog


jiexi_url = ''
e1 = ''

def VIP():
    global jiexi_url
    jiexi_url = 'http://api.3ewl.cc/qingfeng.php?url'

def Not_VIP():
    global jiexi_url
    jiexi_url = 'http://www.wmxz.wang/video.php?url'

def main(Video_url):
    #Video_url = sys.argv[1]

    url = '{}={}'.format(jiexi_url,Video_url)

    webbrowser.open(url)

def adjust():
    #print(e1.get())
    main(e1.get())

def Input_url():
    global e1
    frame = tkinter.Frame(master,height = 300,width = 500,bg = "#FFFFFF").pack()
    #frame.pack(side=tkinter.LEFT, fill=tkinter.Y)
    e1 = Entry(frame, bg='#FFFFFF')
    e1.place(x=140, y=100)
    Word = e1.get()
    tkinter.Label(master, text="输入", fg='#000000',
                  bg="#FFFFFF").place(x=100, y=98)
    Button(master, text='播放',command=adjust).place(x=180, y=130)
    #单选按钮
    v = IntVar()
    R_ONE=Radiobutton(master, text="VIP", variable=v, value=1,bg = "#FFFFFF",command=VIP).place(x=230,y=50)
    R_TWO=Radiobutton(master, text="Not VIP", variable=v, value=2,bg = "#FFFFFF",command=Not_VIP).place(x=140,y=50)

if __name__ == '__main__':
    master = tkinter.Tk()
    master.title('VideoPlayer')
    master.geometry("400x300+200+100")
    Input_url()
    master.mainloop()
