from tkinter import  *
import pickle
import sklearn
from sklearn.linear_model import LogisticRegression
model =  pickle.load(open("dia.pkl","rb"))


app =Tk()
app.title("Diabetes Predicter")
app.geometry("950x440")
bg = PhotoImage(file ="final1.png")
lbl = Label(app,image=bg)
lbl.place(x=0,y=0,relwidth=1,relheight=1)
ag = DoubleVar()
gl = DoubleVar()
bp = DoubleVar()
st =DoubleVar()
ins = DoubleVar()
bmi = DoubleVar()
diap = DoubleVar()

lb1 = Label(app,text="Enter the following",font=("Georgia",20),bg="#bde5f4",fg="#de6f0d")
lb1.grid(row=0,column=0,padx=230,pady=5)
    

def submit():
        ag_val = ag.get()
        gl_val = gl.get()
        bp_val= bp.get()
        st_val = st.get()
        ins_val = ins.get()
        bmi_val = bmi.get()
        diap_val = diap.get()
        result = model.predict([[ag_val,gl_val,bp_val,st_val,ins_val,bmi_val,diap_val]])
        result_percentage = model.predict_proba([[ag_val,gl_val,bp_val,st_val,ins_val,bmi_val,diap_val]])
        if result[0]==1:
                     lb9.config(text=str(round(max(result_percentage[0])*100,2))+"% the patient may have diabetes")
                     butt = Button(app, text="Tips",command=createNewWindow,font=("Bahnschrift",12),bg="#bde5f4",fg="#e28743")
                     butt.place(relx=0.75,rely=0.87,anchor="nw")
                     
                                          
        else:
                     lb9.config(text=str(round(max(result_percentage[0])*100,2))+"% the patient may not have diabetes")
                     
        
        #lb9.config(text= str(round(max(result_percentage[0])*100,2)) +"% it is "+ result[0])


#age
lb2 = Label(app,text="Age",font=("Avenir Next LT Pro Light",15),bg="#bde5f4",fg="#141313")
lb2.place(relx = 0.25,rely = 0.15,anchor = 'nw')
ent1 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=ag)
ent1.place(relx=0.5,rely=0.15,anchor="nw")
#glucose
lb3 = Label(app,text="Glucose",font=("Bahnschrift",15),bg="#bde5f4",fg="#141313")
lb3.place(relx = 0.25,rely = 0.25,anchor = 'nw')
ent2 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=gl)
ent2.place(relx=0.5,rely=0.25,anchor="nw")
#BP
lb4 = Label(app,text="Blood Pressure",font=("Bahnschrift",15),bg="#bde5f4",fg="#141313")
lb4.place(relx = 0.25,rely = 0.35,anchor = 'nw')
ent3 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=bp)
ent3.place(relx=0.5,rely=0.35,anchor="nw")
#skin thick
lb5 = Label(app,text="Skin Thickness",font=("Bahnschrift",15),bg="#bde5f4",fg="#141313")
lb5.place(relx = 0.25,rely = 0.45,anchor = 'nw')
ent4 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=st)
ent4.place(relx=0.5,rely=0.45,anchor="nw")
#insulin
lb6 = Label(app,text="Insulin",font=("Bahnschrift",15),bg="#bde5f4",fg="#141313")
lb6.place(relx = 0.25,rely = 0.55,anchor = 'nw')
ent5 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=ins)
ent5.place(relx=0.5,rely=0.55,anchor="nw")
#BMI
lb7 = Label(app,text="BMI",font=("Bahnschrift",15),bg="#bde5f4",fg="#141313")
lb7.place(relx = 0.25,rely = 0.65,anchor = 'nw')
ent6 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=bmi)
ent6.place(relx=0.5,rely=0.65,anchor="nw")
#Diabetes predigree func
lb8 = Label(app,text="Diabetes pedigree func",font=("Bahnschrift",15),bg="#bde5f4",fg="#141313")
lb8.place(relx = 0.25,rely = 0.75,anchor = 'nw')
ent7 = Entry(app,font =("Bahnschrift",15),bg="#bde5f4",fg="#e28743",textvariable=diap)
ent7.place(relx=0.5,rely=0.75,anchor="nw")

lb9 = Label(app,text="   ",width=40,height=2,font=("Bahnschrift",13))#bg="#bde5f4",fg="#e28743")
lb9.place(relx=0.35,rely=0.85,anchor="nw")

bg1 = PhotoImage(file="tips.png")
def createNewWindow():
    newWindow = Toplevel(app)
    newWindow.title("Diabetes patient tips")
    newWindow.geometry("890x590")
    Label(newWindow,image=bg1).place(x=0,y=0,relwidth=1,relheight=1)
    #lb9 = Label(newWindow,text="   ",width=40,height=2,font=("Bahnschrift",13))#bg="#bde5f4",fg="#e28743")
    #lb9.place(relx=0.5,rely=0.35,anchor="nw")
    #btnl =Button(newWindow,text ="Results:",command=submit,font=("Bahnschrift",15),bg="#bde5f4",fg="#e28743").place(relx=0.5,rely=0.25,anchor="nw")



buttonExample = Button(app, text="Result",command=submit,font=("Bahnschrift",15),bg="#e28743",fg="white",activebackground="red",activeforeground="yellow")#bg="#bde5f4",fg="#e28743")
buttonExample.place(relx=0.26,rely=0.86,anchor="nw")

 

 

app.mainloop()

