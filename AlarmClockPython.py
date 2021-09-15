# Import Required Libraries
from tkinter import *
from threading import *
import datetime,time
import winsound

# Create Object
root = Tk()
# Set Window size
root.geometry("400x300")
root.title('Alarm Clock Python')

# Use Threading
def Threading():
    t1=Thread(target=alarm)
    t1.start()

# Generating numbers 00-24 & 00-60
def num_gen():  

    global num60,num24 
    num60,num24 = [],[]

    for n1 in range(61) :
        
        if n1 < 10 :
            n1 = str(0) + str(n1)
        if int(n1) <= 24 :
            num24.append(str(n1))
        num60.append(str(n1))
    
    return num60,num24

def alarm():
    # Infintite Loop
    while True:
        # Set alarm time
        
        input_time = time_var.get()

        # Disable text field when clicked set alarm 
        time_entry.configure(state='disabled')

        # one second wait time
        time.sleep(1)

        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time,input_time)

        # Validating Time Format HH:MM:SS
        try:
            time.strptime(input_time[:8], '%H:%M:%S')

        except ValueError:
            setlabel.config(text='Wrong Time Format !')  
            setlabel.config(fg='red')
            setlabel.pack()
            time.sleep(5)
            root.destroy()
        else:
            setlabel.config(text='')
            setlabel.pack()
            
            if len(input_time) != 8 :
                setlabel.config(text='Wrong Time Format !')  
                setlabel.config(fg='red')
                setlabel.pack()
                time.sleep(5)
                root.destroy() 
                
            else :
                alarm_time = input_time
                
        # Check if current time equals to alarm time
        if current_time == alarm_time:
            print("Alarm! Alarm! Alarm!")
            root.config(bg='red')
            # Playing sound
            winsound.PlaySound("alarmsound.WAV",winsound.SND_ASYNC)
            
            setlabel.config(text='Alarm! Alarm! Alarm!')
            setlabel.config(fg='red')
            setlabel.pack()

            for t in range(10) :  # Blinking Red window
                time.sleep(0.3)
                root.config(bg='#f0f0ed')
                time.sleep(0.3)
                root.config(bg='red')

            root.config(bg='#f0f0ed')

# Adding widgets
Label(root,text="Alarm Clock",font=("Cambria 20 bold"),fg="#e30909").pack(pady=10)
Label(root,text="Set Time",font=("Cambria 17 bold")).pack()
setlabel = Label(root,text="",font=("Cambria 15 bold"))

time_var = StringVar()
time_entry = Entry(root,width=50,font=("ds-digital 35 bold"),justify=CENTER,textvariable=time_var)
time_var.set('00:00:00')
time_entry.pack()

frame = Frame(root)
frame.pack()

num_gen()

Button(root,text="Set Alarm",font=("Helvetica 15"),command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
