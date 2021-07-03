#It's khoji <a.khoji@gmail.com>

#pip install requests,pillow
import tkinter as tk
from tkinter import font
from PIL import Image,ImageTk
import requests
#api from https://openweathermap.org/current
def weather(city):
    try:
        key = '2986b1a66e55309d909652df6c9cec2d'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'appid': key,'q':city,'units':'metric'}
        res = requests.get(url,params=params)
        json = res.json()
        name = json['name']
        country = json['sys']['country']
        temp = json['main']['temp']
        desc = json['weather'][0]['description']
        show = (f'{str(name)}\n{str(country)}\n{str(temp)}\n{str(desc)}\n')
    except:
        show = 'there is no city with this name'
    labels['text'] = show
    return show
#main frame
root = tk.Tk()
canvas = tk.Canvas(root,height = 500,width=600)
canvas.pack()
#background image
img = Image.open("C:\\Users\\persian\\Pictures\\wllpp.jpg")
photo = ImageTk.PhotoImage(img.resize((600,500)))
label = tk.Label(root, image=photo)
label.image = photo
label.place(relwidth=1, relheight=1)
#frame for entry
frame = tk.Frame(root,bg = 'blue',bd =5)
frame.place(relheight = 0.1,relwidth=0.8,relx = 0.5,rely = 0.1,anchor = 'n')
entry = tk.Entry(frame,font=('Estrangelo Edessa',18))
butten = tk.Button(frame,text = 'Get Weather',font=('Estrangelo Edessa',12),command = lambda : weather(entry.get()))
butten.place(relx = 0.75 , rely = 0,relwidth= 0.25,relheight=1)
entry.place(relwidth= 0.70,relheight=1)
#frame for showing data
lower_f = tk.Frame(root,bg = 'blue', bd =10)
lower_f.place(relx = 0.5 , rely = 0.25 , anchor = 'n',relwidth = 0.8,relheight = 0.6)
labels = tk.Label(lower_f ,font=('Estrangelo Edessa',18),anchor = 'nw',justify = 'left',bd= 5)
labels.place(relwidth=1,relheight =1)
root.mainloop()
