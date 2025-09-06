import tkinter as tk
from tkinter import messagebox
from tkinter import*
import math,random,os
from fpdf import FPDF
class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x780+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"

        #------variable declaring------
        #------cement------
        self.prism=IntVar()
        self.birla=IntVar()
        self.pcon=IntVar()
        self.con=IntVar()
        self.bangur=IntVar()
        self.plus=IntVar()

        #------Asbestos & Rod------
        self.a=IntVar()
        self.b=IntVar()
        self.c=IntVar()
        self.d=IntVar()
        self.e=IntVar()
        self.f=IntVar()

        #------hardware------
        self.enamel=IntVar()
        self.emulsion=IntVar()
        self.tank=IntVar()
        self.upvc=IntVar()
        self.cpvc=IntVar()
        self.swr=IntVar()

        #------Total product price & Total tax------
        self.cem_total=StringVar()
        self.aro_total=StringVar()
        self.har_total=StringVar()

        self.cem_tax=StringVar()
        self.aro_tax=StringVar()
        self.har_tax=StringVar()

        #------customer detail-----
        self.cname=StringVar()
        self.cphone=StringVar()
        self.cbill=StringVar()
        x=random.randint(1000,9999)
        self.cbill.set(str(x))
        self.search_bill=StringVar()
        


        #-------titlt frame------
        title=Label(self.root,text="Maa Vindywashini Hardware",bg=bg_color,fg="white",
                    bd=12,relief=GROOVE,font=("Rockwell",24,"bold"),pady=2).pack(fill=X)
        
        #-------customer detail frame------
        c1=LabelFrame(self.root,text="Customer Detail",fg="Gold",bg=bg_color,bd=10,relief=GROOVE,font=("times new roman",15,"bold"))
        c1.place(x=0,y=80,relwidth=1)

        cname_label=Label(c1,text="Customer Name",bg=bg_color,fg="White",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_entry=Entry(c1,width=15,font=("arial,15"),textvariable=self.cname,bd=7,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=5)

        cphone_label=Label(c1,text="Phone No.",bg=bg_color,fg="White",font=("times new roman",15,"bold")).grid(row=0,column=2,padx=20,pady=5)
        cphone_entry=Entry(c1,width=15,font=("arial,15"),textvariable=self.cphone,bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=5)

        cbill_label=Label(c1,text="Bill Number",bg=bg_color,fg="White",font=("times new roman",15,"bold")).grid(row=0,column=4,padx=20,pady=5)
        cbill_entry=Entry(c1,width=15,font=("arial,15"),textvariable=self.search_bill,bd=7,relief=SUNKEN).grid(row=0,column=5,padx=10,pady=5)

        bill_button=Button(c1,text="Search",command=self.find_bill,bd=7,font="arial 12 bold").grid(row=0,column=6,pady=10,padx=20)

        #-------cement product frame------
        cem=LabelFrame(self.root,text="Cement",fg="Gold",bg=bg_color,bd=10,relief=GROOVE,font=("times new roman",15,"bold"))
        cem.place(x=5,y=180,width=325,height=380)

        prism_label=Label(cem,text="Prism Champion",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        prism_entry=Entry(cem,width=10,bd=5,relief=SUNKEN,textvariable=self.prism,font=("arial",15)).grid(row=0,column=1,padx=10,pady=10)

        birla_label=Label(cem,text="Birla Samrat",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        birla_entry=Entry(cem,width=10,bd=5,relief=SUNKEN,textvariable=self.birla,font=("arial",15)).grid(row=1,column=1,padx=10,pady=10)

        pcon_label=Label(cem,text="All Weather",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        pcon_entry=Entry(cem,width=10,bd=5,relief=SUNKEN,textvariable=self.pcon,font=("arial",15)).grid(row=2,column=1,padx=10,pady=10)

        con_label=Label(cem,text="Perfect Plus",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        con_entry=Entry(cem,width=10,bd=5,relief=SUNKEN,textvariable=self.con,font=("arial",15)).grid(row=3,column=1,padx=10,pady=10)

        bangur_label=Label(cem,text="Bangur Cement",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        bangur_entry=Entry(cem,width=10,bd=5,relief=SUNKEN,textvariable=self.bangur,font=("arial",15)).grid(row=4,column=1,padx=10,pady=10)

        plus_label=Label(cem,text="Prism Plus",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        plus_entry=Entry(cem,width=10,bd=5,relief=SUNKEN,textvariable=self.plus,font=("arial",15)).grid(row=5,column=1,padx=10,pady=10)

        #------Asbestos and rod product frame------
        aro=LabelFrame(self.root,text="Asbestos & Rod",fg="Gold",bg=bg_color,bd=10,relief=GROOVE,font=("times new roman",15,"bold"))
        aro.place(x=340,y=180,width=325,height=380)

        a_label=Label(aro,text="12ft Asbestos",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        a_entry=Entry(aro,width=10,bd=5,relief=SUNKEN,textvariable=self.a,font=("arial",15)).grid(row=0,column=1,padx=10,pady=10)

        b_label=Label(aro,text="10ft Asbestos",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        b_entry=Entry(aro,width=10,bd=5,relief=SUNKEN,textvariable=self.b,font=("arial",15)).grid(row=1,column=1,padx=10,pady=10)

        c_label=Label(aro,text="8ft Asbestos",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        c_entry=Entry(aro,width=10,bd=5,relief=SUNKEN,textvariable=self.c,font=("arial",15)).grid(row=2,column=1,padx=10,pady=10)

        d_label=Label(aro,text="6ft Asbestos",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d_entry=Entry(aro,width=10,bd=5,relief=SUNKEN,textvariable=self.d,font=("arial",15)).grid(row=3,column=1,padx=10,pady=10)

        e_label=Label(aro,text="12&10mm Rod",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        e_entry=Entry(aro,width=10,bd=5,relief=SUNKEN,textvariable=self.e,font=("arial",15)).grid(row=4,column=1,padx=10,pady=10)

        f_label=Label(aro,text="8&6mm Rod",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        f_entry=Entry(aro,width=10,bd=5,relief=SUNKEN,textvariable=self.f,font=("arial",15)).grid(row=5,column=1,padx=10,pady=10)

        #-------hardware product frame------
        har=LabelFrame(self.root,text="Hardware Items",fg="Gold",bg=bg_color,bd=10,relief=GROOVE,font=("times new roman",15,"bold"))
        har.place(x=675,y=180,width=325,height=380)

        enamel_label=Label(har,text="Enamel",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=0,column=0,padx=10,pady=10,sticky="w")
        enamel_entry=Entry(har,width=10,bd=5,relief=SUNKEN,textvariable=self.enamel,font=("arial",15)).grid(row=0,column=1,padx=10,pady=10)

        emulsion_label=Label(har,text="Emulsion",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=1,column=0,padx=10,pady=10,sticky="w")
        emulsion_entry=Entry(har,width=10,bd=5,relief=SUNKEN,textvariable=self.emulsion,font=("arial",15)).grid(row=1,column=1,padx=10,pady=10)

        tank_label=Label(har,text="Tank",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=2,column=0,padx=10,pady=10,sticky="w")
        tank_entry=Entry(har,width=10,bd=5,relief=SUNKEN,textvariable=self.tank,font=("arial",15)).grid(row=2,column=1,padx=10,pady=10)

        upvc_label=Label(har,text="UPVC Pipe",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=3,column=0,padx=10,pady=10,sticky="w")
        upvc_entry=Entry(har,width=10,bd=5,relief=SUNKEN,textvariable=self.upvc,font=("arial",15)).grid(row=3,column=1,padx=10,pady=10)

        cpvc_label=Label(har,text="CPVC Pipe",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=4,column=0,padx=10,pady=10,sticky="w")
        cpvc_entry=Entry(har,width=10,bd=5,relief=SUNKEN,textvariable=self.cpvc,font=("arial",15)).grid(row=4,column=1,padx=10,pady=10)

        swr_label=Label(har,text="SWR Pipe",bg=bg_color,fg="white",font=("times new roman",15,"bold")).grid(row=5,column=0,padx=10,pady=10,sticky="w")
        swr_entry=Entry(har,width=10,bd=5,relief=SUNKEN,textvariable=self.swr,font=("arial",15)).grid(row=5,column=1,padx=10,pady=10)

        #------bill area------
        bill_area=Label(self.root,bd=10,relief=GROOVE)
        bill_area.place(x=1010,y=180,width=360,height=380)

        bill_title=Label(bill_area,text="Bill Area",font=("Ariall",15,"bold"),bd=7,relief=GROOVE).pack(fill=X)
        scroll_y=Scrollbar(bill_area,orient=VERTICAL)
        self.txtarea=Text(bill_area,yscrollcommand=scroll_y.set)
        scroll_y.pack(side="right",fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #------button frame------
        but=LabelFrame(self.root,text="Bill Menu",fg="Gold",bg=bg_color,bd=10,relief=GROOVE,
                      font=("times new roman",15,"bold"))
        but.place(x=0,y=560,relwidth=1,height=140)

        #------totla taxable amount------
        cem_total=Label(but,text="Total Cement Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=0,padx=10,pady=1,sticky="W")
        cem_entry=Entry(but,width=18,textvariable=self.cem_total,font=("Arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=1,padx=1)

        aro_total=Label(but,text="Total Rod Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=0,padx=10,pady=1,sticky="W")
        aro_entry=Entry(but,width=18,textvariable=self.aro_total,font=("Arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=1,padx=1)

        har_total=Label(but,text="Total Hardware Price",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=0,padx=10,pady=1,sticky="W")
        har_entry=Entry(but,width=18,textvariable=self.har_total,font=("Arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=1,padx=1)

        #------total tax amount------
        cem_tax=Label(but,text="Total Cement Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=0,column=2,padx=10,pady=1,sticky="W")
        cemt_entry=Entry(but,width=18,textvariable=self.cem_tax,font=("Arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=0,column=3,padx=1)

        arot_tax=Label(but,text="Total Rod Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=1,column=2,padx=10,pady=1,sticky="W")
        arot_entry=Entry(but,width=18,textvariable=self.aro_tax,font=("Arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=1,column=3,padx=1)

        har_tax=Label(but,text="Total Hardware Tax",bg=bg_color,fg="white",font=("times new roman",14,"bold")).grid(row=2,column=2,padx=10,pady=1,sticky="W")
        hart_entry=Entry(but,width=18,textvariable=self.har_tax,font=("Arial",10,"bold"),bd=7,relief=SUNKEN).grid(row=2,column=3,padx=1)

        #------button frame------
        b1_frame=Frame(but,bd=7,relief=GROOVE)
        b1_frame.place(x=750,width=580,height=105)

        total_btn=Button(b1_frame,text="Total",command=self.total,font=("Arial",13,"bold"),bd=5,bg="cadetblue",fg="white",width=11,pady=15).grid(row=0,column=0,padx=5,pady=5)
        Gbill_btn=Button(b1_frame,text="Generate Bill",command=self.bill_area,font=("Arial",13,"bold"),bd=5,bg="cadetblue",fg="white",width=11,pady=15).grid(row=0,column=1,padx=5,pady=5)
        clear_btn=Button(b1_frame,text="Clear",command=self.clear_data,font=("Arial",13,"bold"),bd=5,bg="cadetblue",fg="white",width=11,pady=15).grid(row=0,column=2,padx=5,pady=5)
        exit_btn=Button(b1_frame,text="Exit",command=self.exit,font=("Arial",13,"bold"),bd=5,bg="cadetblue",fg="white",width=11,pady=15).grid(row=0,column=3,padx=5,pady=5)
        self.welcome_bill()
    #------making total price function------
    def total(self):
        self.c_pr_p=(self.prism.get()*285)
        self.c_bi_p=(self.birla.get()*280)
        self.c_pcon_p=(self.pcon.get()*305)
        self.c_con_p=(self.con.get()*290)
        self.c_ba_p=(self.bangur.get()*275)
        self.c_pl_p=(self.plus.get()*295)
        self.total_cement_price=float(
                          self.c_pr_p+
                          self.c_bi_p+
                          self.c_pcon_p+
                          self.c_con_p+
                          self.c_ba_p+
                          self.c_pl_p
        )
        self.cem_total.set("Rs. "+str(self.total_cement_price))
        self.c_tax=round((self.total_cement_price*0.28),2)
        self.cem_tax.set("Rs. "+str(self.c_tax))

        self.ar_a_p=(self.a.get()*678)
        self.ar_b_p=(self.b.get()*525)
        self.ar_c_p=(self.c.get()*440)
        self.ar_d_p=(self.d.get()*322)
        self.ar_e_p=(self.e.get()*50)
        self.ar_f_p=(self.f.get()*52)
        self.total_asbrod_price=float(
                           self.ar_a_p+
                           self.ar_b_p+
                           self.ar_c_p+
                           self.ar_d_p+
                           self.ar_e_p+
                           self.ar_f_p
        )
        self.aro_total.set("Rs. "+str(self.total_asbrod_price))
        self.ar_tax=round((self.total_asbrod_price*0.18),2)
        self.aro_tax.set("Rs. "+str(self.ar_tax))

        self.h_en_p=(self.enamel.get()*322)
        self.h_em_p=(self.emulsion.get()*1186)
        self.h_t_p=(self.tank.get()*3390)
        self.h_up_p=(self.upvc.get()*220)
        self.h_cp_p=(self.cpvc.get()*300)
        self.h_sw_p=(self.swr.get()*466)
        self.total_hardware_price=float(
                            self.h_en_p+
                            self.h_em_p+
                            self.h_t_p+
                            self.h_up_p+
                            self.h_cp_p+
                            self.h_sw_p
        )
        self.har_total.set("Rs. "+str(self.total_hardware_price))
        self.h_tax=round((self.total_hardware_price*0.18),2)
        self.har_tax.set("Rs. "+str(self.h_tax))

        self.total_price=float(self.total_cement_price+
                               self.total_asbrod_price+
                               self.total_hardware_price+
                               self.c_tax+
                               self.ar_tax+
                               self.h_tax
        )
    
    #------defining function for bill heading------
    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\tMaa Vindywashini Hardware\n")
        self.txtarea.insert(END,"\t   Number : 6200411069\n")
        self.txtarea.insert(END,f"\n Bill Number : {self.cbill.get()}")
        self.txtarea.insert(END,f"\n Customer Name : {self.cname.get()}")
        self.txtarea.insert(END,f"\n Customer Number : {self.cphone.get()}")
        self.txtarea.insert(END,"\n=======================================")
        self.txtarea.insert(END,"\n Products\t\t  QTY\t\tPrice")
        self.txtarea.insert(END,"\n=======================================")

    #------defining function for bill arae------
    def bill_area(self):
        if self.cname.get()=="" or self.cphone.get()=="":
            messagebox.showerror("Error","Customber detail not found")
        elif self.cem_total.get()=="Rs. 0.0" and self.aro_total.get()=="Rs. 0.0" and self.har_total.get()=="Rs. 0.0":
            messagebox.showerror("Error","No product purchased")
        else:
            self.welcome_bill()

            #------Cements-------
            if self.prism.get() != 0:
                self.txtarea.insert(END,f"\n Prism Champion\t\t {self.prism.get()}\t\t{self.c_pr_p}")
            if self.birla.get() != 0:
                self.txtarea.insert(END,f"\n Birla Samrat\t\t  {self.birla.get()}\t\t{self.c_bi_p}")
            if self.pcon.get() != 0:
                self.txtarea.insert(END,f"\n All Weather\t\t  {self.pcon.get()}\t\t{self.c_pcon_p}")
            if self.con.get() != 0:
                self.txtarea.insert(END,f"\n Perfect Plus\t\t  {self.con.get()}\t\t{self.c_con_p}")
            if self.bangur.get() != 0:
                self.txtarea.insert(END,f"\n Bangur Cement\t\t  {self.bangur.get()}\t\t{self.c_ba_p}")
            if self.plus.get() != 0:
                self.txtarea.insert(END,f"\n Prism Plus\t\t  {self.plus.get()}\t\t{self.c_pl_p}")

            #------Asbestos & Rod------
            if self.a.get() != 0:
                self.txtarea.insert(END,f"\n 12ft Asbestos\t\t  {self.a.get()}\t\t{self.ar_a_p}")
            if self.b.get() != 0:
                self.txtarea.insert(END,f"\n 10ft Asbestos\t\t  {self.b.get()}\t\t{self.ar_b_p}")
            if self.c.get() != 0:
                self.txtarea.insert(END,f"\n 8ft Asbestos\t\t  {self.c.get()}\t\t{self.ar_c_p}")
            if self.d.get() != 0:
                self.txtarea.insert(END,f"\n 6ft Asbestos\t\t  {self.d.get()}\t\t{self.ar_d_p}")
            if self.e.get() != 0:
                self.txtarea.insert(END,f"\n 12&10mm Rod\t\t  {self.e.get()}\t\t{self.ar_e_p}")
            if self.f.get() != 0:
                self.txtarea.insert(END,f"\n 8&6mm Rod\t\t  {self.f.get()}\t\t{self.ar_f_p}")

            #------Hardware Items------
            if self.enamel.get() != 0:
                self.txtarea.insert(END,f"\n Enamel\t\t  {self.enamel.get()}\t\t{self.h_en_p}")
            if self.emulsion.get() != 0:
                self.txtarea.insert(END,f"\n Emulsion\t\t  {self.emulsion.get()}\t\t{self.h_em_p}")
            if self.tank.get() != 0:
                self.txtarea.insert(END,f"\n Tank\t\t  {self.tank.get()}\t\t{self.h_t_p}")
            if self.upvc.get() != 0:
                self.txtarea.insert(END,f"\n UPVC Pipe\t\t  {self.upvc.get()}\t\t{self.h_up_p}")
            if self.cpvc.get() != 0:
                self.txtarea.insert(END,f"\n CPVC Pipe\t\t  {self.cpvc.get()}\t\t{self.h_cp_p}")
            if self.swr.get() != 0:
               self.txtarea.insert(END,f"\n SWR Pipe\t\t  {self.swr.get()}\t\t{self.h_sw_p}")
        
            self.txtarea.insert(END,"\n---------------------------------------")
            if self.cem_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Cement Tax\t\t\t {self.cem_tax.get()}")
            if self.aro_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Asbestos & Rod Tax\t\t\t {self.aro_tax.get()}")
            if self.har_tax.get() != "Rs. 0.0":
                self.txtarea.insert(END,f"\n Hardware Tax\t\t\t {self.har_tax.get()}")
            self.txtarea.insert(END,"\n---------------------------------------")
            self.txtarea.insert(END,"\n---------------------------------------")
            self.txtarea.insert(END,f"\n Total Bill : \t\t\t Rs. {self.total_price}") 
            self.txtarea.insert(END,"\n=======================================")
            self.save_bill()

    #------saving the bill------
    def save_bill(self):
        op=messagebox.askyesno("Save Bill","Do you want to save the bill?")
        if op>0:
            self.bill_data=self.txtarea.get("1.0",END)
            f1=open("bills/"+str(self.cbill.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved",f"Bill no: {self.cbill.get()}  saved successfully")
        else:
            return

    #------finding the bill------  
    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill Number")
    
    #------clearing the data------
    def clear_data(self):
        op=messagebox.askyesno("Clear","Do you want to clear data?")
        if op>0:
            self.prism.set(0)
            self.birla.set(0)
            self.pcon.set(0)
            self.con.set(0)
            self.bangur.set(0)
            self.plus.set(0)

            self.a.set(0)
            self.b.set(0)
            self.c.set(0)
            self.d.set(0)
            self.e.set(0)
            self.f.set(0)

            self.enamel.set(0)
            self.emulsion.set(0)
            self.tank.set(0)
            self.upvc.set(0)
            self.cpvc.set(0)
            self.swr.set(0)

            self.cem_total.set("")
            self.aro_total.set("")
            self.har_total.set("")

            self.cem_tax.set("")
            self.aro_tax.set("")
            self.har_tax.set("")

            self.cname.set("")
            self.cphone.set("")
            self.search_bill.set("")
            x=random.randint(1000,9999)
            self.cbill.set(str(x))

            self.welcome_bill()
 
    #------exit the software------
    def exit(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op>0:
            self.root.destroy()
    

root=tk.Tk()
obj=Bill_App(root)
root.mainloop()