from tkinter import*
import qrcode
from PIL import Image,ImageTk

from resizeimage import resizeimage
class Qr_Generator:
    def __init__(self,root):
        self.root=root

        self.root.geometry('1000x600')
        self.root.title("QR_Generator")
        self.root.resizable(False,False)
        title=Label(self.root,text='  QR Code Generator',font=("times new roman",40),bg="#053246",fg='white',anchor='w').place(x=0,y=0,relwidth=1)


        #all details window
        #=====variables===
        self.var_ssid_code=StringVar()
        self.var_password_code=StringVar()
        self.var_upi_id_code=StringVar()
        self.var_fname_code=StringVar()
        self.var_lname_code=StringVar()







        wifi_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        wifi_Frame.place(x=50,y=100,width=500,height=380)


        wifi_title = Label(wifi_Frame, text='  Provide all Details', font=("goudy old style", 20), bg="#043256", fg='white').place(x=0, y=0, relwidth=1)


        lbl_ssid_code = Label(wifi_Frame, text='SSID', font=("times new roman", 15,'bold'), bg="white").place(x=20, y=60)
        lbl_password_code = Label(wifi_Frame, text='PASSWORD', font=("times new roman", 15,'bold'), bg="white").place(x=20, y=100)
        lbl_upi_id_code = Label(wifi_Frame, text='UPI_ID', font=("times new roman", 15,'bold'), bg="white").place(x=20, y=140)
        lbl_fname_code = Label(wifi_Frame, text='FNAME', font=("times new roman", 15,'bold'), bg="white").place(x=20, y=180)
        lbl_lname_code = Label(wifi_Frame, text='LNAME', font=("times new roman", 15,'bold'), bg="white").place(x=20, y=220)




        txt_ssid_code = Entry(wifi_Frame, font=("times new roman", 15),textvariable=self.var_ssid_code, bg="lightyellow").place(x=200,y=60)
        txt_password_code = Entry(wifi_Frame,  font=("times new roman", 15),textvariable=self.var_password_code, bg="lightyellow").place(x=200, y=100)
        txt_upi_id_code = Entry(wifi_Frame,  font=("times new roman", 15),textvariable=self.var_upi_id_code, bg="lightyellow").place(x=200, y=140)
        txt_fname_code = Entry(wifi_Frame,  font=("times new roman", 15),textvariable=self.var_fname_code, bg="lightyellow").place(x=200, y=180)
        txt_lname_code = Entry(wifi_Frame,  font=("times new roman", 15),textvariable=self.var_lname_code, bg="lightyellow").place(x=200, y=220)





        btn_generate = Button(wifi_Frame, text='Generate', command=self.generate,font=("times new roman", 18,'bold'), bg="#2196f3", fg='white').place(x=90, y=250,width=180,height=30)
        btn_clear = Button(wifi_Frame, text='Clear',command=self.clear,font=("times new roman", 18,'bold'), bg="#607d8b", fg='white').place(x=282, y=250,width=120,height=30)


        self.msg=''
        self.lbl_msg=Label(wifi_Frame, text=self.msg, font=("times new roman", 20), bg="white",fg='green')
        self.lbl_msg.place(x=0,y=310,relwidth=1)


        # wifi QRCODE window
        qr_Frame = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Frame.place(x=600, y=100, width=250, height=380)

        wifi_title = Label(qr_Frame, text='  Combined QR CODE', font=("goudy old style", 20), bg="#043256",fg='white').place(x=0, y=0, relwidth=1)
        self.qr_code=Label(qr_Frame,text='No QR\nAvailable',font=('times new roman',15),bg='#3f51b5',fg='white',bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_ssid_code.set('')
        self.var_password_code.set('')
        self.var_upi_id_code.set('')
        self.var_fname_code.set('')
        self.var_lname_code.set('')
        self.msg = ""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')

    def generate(self):
        if self.var_password_code.get() == "" or self.var_ssid_code.get() == "" or self.var_upi_id_code.get() == "" or self.var_fname_code.get() == "" or self.var_lname_code.get() == "":

            self.msg="All fields are required!!!"
            self.lbl_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"{upi}{self.var_upi_id_code.get()}{a}{self.var_fname_code.get()}{n}{self.var_lname_code.get()}{c};{WIFI};P:{self.var_password_code.get()};S:{self.var_ssid_code.get()};{H}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("project1"+str(self.var_ssid_code.get())+'.png')
            #======QR CODE Image updating=======
            self.im=ImageTk.PhotoImage(file="project1"+str(self.var_ssid_code.get())+'.png')
            self.qr_code.config(image=self.im)

            #======updating Notification=====
            self.msg='QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg, fg='green')



root=Tk()
WIFI = "WIFI:T:WPA"
H = "H:false"
upi="upi://pay?pa="
a="&amp;pn="
n="%20"
c="&amp;cu=INR;upi-pay1"
obj=Qr_Generator(root)
root.mainloop()
