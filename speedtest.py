from tkinter import *
import speedtest

root=Tk()
root.geometry("400x400")
root.title("Speedtest")
root.config(bg="#dbdb00")

label=Label(root, text="Internet Speedcheck", font=("Gill Sans MT", 20, "bold"), fg="#000000", bg="#dbdb00")
label.place(relx=0.5, rely=0.2, anchor=CENTER)
label1=Label(root, text="Download Speed ↓", font=("Gill Sans MT Condensed", 18), fg="#000000", bg="#dbdb00")
label1.place(relx=0.2, rely=0.5,anchor=CENTER)
label2=Label(root, text="Upload Speed ↑", font=("Gill Sans MT Condensed", 18), fg="#000000", bg="#dbdb00")
label2.place(relx=0.8, rely=0.5,anchor=CENTER)
labeldwn=Label(root, text="", font=("Gill Sans MT", 18, "bold"), fg="#003cff", bg="#dbdb00")
labeldwn.place(relx=0.2, rely=0.6, anchor=CENTER)
labelup=Label(root, text="", font=("Gill Sans MT", 18, "bold"), fg="#003cff", bg="#dbdb00")
labelup.place(relx=0.8, rely=0.6, anchor=CENTER)

def speedcheck():
    st=speedtest.Speedtest()
    download_speed=round(st.download()/1000000,2)
    labeldwn["text"]=str(download_speed)+"mbps"
    upload_speed=round(st.upload()/1000000,2)
    labelup["text"]=str(upload_speed)+"mbps"

btn=Button(root, text="Check Speed", command=speedcheck)
btn.place(relx=0.5, rely=0.7, anchor=CENTER)






























root.mainloop()