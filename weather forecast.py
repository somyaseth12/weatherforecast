from tkinter import * 
import tkinter as tk
from geopy.geocoders import Nominatim
geocoder = Nominatim(user_agent = 'your_app_name')
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests 
import pytz
root=Tk()
root.title("Weather forecast")
root.geometry("1500x700+200+100")
root.resizable(False,False)

def getweather():
    city = textfeild.get()
    geolocator=Nominatim(user_agent="geoapiExercises")
    location=geolocator.geocode(city)
    obj=TimezoneFinder()
    result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
    print(result)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)
    name.config(text="CURRENT WEATHER")

    #WEATHER
    api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=5bdda009e16039014420dee30805cbc8"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    temp = int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    
    #CONFIGURE
    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)

#SEARCH BOX
Search_image=PhotoImage(file="search box.png")
myimage=Label(image=Search_image)
myimage.place(x=20,y=320)
#TASKFEILD
textfeild=tk.Entry(root,justify="left",width=20,font=("poppins 60 bold"),bg="#404040",border=0,fg="white")
textfeild.place(x=20,y=70)
textfeild.focus()
#SEARCH ICON
Search_icon= PhotoImage(file="small search icon.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand1",bg="#404040",command=getweather)
myimage_icon.place(x=801,y=69)
#LOGO
Logo_image=PhotoImage(file="logo.png")
logo=Label(image=Logo_image)
logo.place(x=1000,y=1)
#BOTTOM BOX
# Frame_image=PhotoImage(file="search box.png")
# frame_myimage=Label(image=Frame_image)
# frame_myimage.pack(padx=5,pady=1,side=LEFT)
#TIME
name=Label(root,font="arial 20 bold")
name.place(x=70,y=200)
clock=Label(root,font="Helvetica 20")
clock.place(x=70,y=250)
#LABEL
l1=Label(root,text="Wind",font=("Helvetica 25 bold"),fg="white",bg="grey")
l1.place(x=110,y=400)

l2=Label(root,text="Humidity",font=("Helvetica 25 bold"),fg="white",bg="grey")
l2.place(x=280,y=400)

l3=Label(root,text="Description",font=("Helvetica 23 bold"),fg="white",bg="grey")
l3.place(x=500,y=400)

l4=Label(root,text="Pressure",font=("Helvetica 25 bold"),fg="white",bg="grey")
l4.place(x=750,y=400)

#ARRANGE IN ORDER
t=Label(font="arial 70 bold", fg="#ee666d")
t.place(x=410,y=170)
c=Label(font="arial 15 bold")
c.place(x=420,y=270)
w=Label(text="---",font="arial 25",bg="white")
w.place(x=110,y=500)
h=Label(text="---",font="arial 25",bg="white")
h.place(x=280,y=500)
d=Label(text=" ",font="arial 20",bg="white")
d.place(x=500,y=500)
p=Label(text="---",font="arial 25",bg="white")
p.place(x=765,y=500)
#END
root.mainloop()