import requests
from datetime import datetime


import tkinter as tk 

root = tk.Tk()
root.title("Weather_Details")
root.iconbitmap('weather.png')

canvas1 = tk.Canvas(root, width = 700, height = 400)
canvas1.pack()











#*****************************************************************************************












def values(): 

	api_key = 'Write_Your_API_Key'


	location = str(x.get())

	api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key

	api_link1 = requests.get(api_link)
	api_data = api_link1.json()




	if api_data['cod'] == '404':
		canvas1.delete('dt')
		error = tk.Label(root, text = 'Invalid City, Please Check Your City Name!!', bg='orange' , width = 40, height=5, font=("Helvetica", 20), bd=0)
		canvas1.create_window(350, 250, window=error, tags = 'e')
		

	else:
		canvas1.delete('e')
		canvas1.delete('ww')
		date_time = datetime.now().strftime(" %d %b %Y  |  %I:%M:%S %p ")
		temp = ((api_data['main']['temp']) - 273.15)
		temp = round(temp,4)
		main = (api_data['weather'][0]['main'])
		pressure = (api_data['main']['pressure'])
		humidity = (api_data['main']['humidity']) 
		speed = (api_data['wind']['speed']) 
		country = (api_data['sys']['country'])





		Temprature = tk.Label(root, text='Temprature : ')
		canvas1.create_window(110, 200, window=Temprature)

		pressure2 = tk.Label(root, text='pressure : ')
		canvas1.create_window(100, 250, window=pressure2)

		humidity1 = tk.Label(root, text='Humidity : ')
		canvas1.create_window(105, 300, window=humidity1)

		main1 = tk.Label(root, text='Climate : ')
		canvas1.create_window(410, 300, window=main1)


		speed1 = tk.Label(root, text='Speed : ')
		canvas1.create_window(410, 200, window=speed1)

		country1 = tk.Label(root, text='Country : ')
		canvas1.create_window(410, 250, window=country1)






		
		temp1 = tk.Label(root, text = temp, bg='orange')
		canvas1.create_window(170, 200, window=temp1)

		pressure1 = tk.Label(root, text = pressure, bg='orange')
		canvas1.create_window(170, 250, window=pressure1)

		humidity2 = tk.Label(root, text = humidity, bg='orange')
		canvas1.create_window(170, 300, window=humidity2)

		main2 = tk.Label(root, text = main, bg='orange')
		canvas1.create_window(470, 300, window=main2)

		speed2 = tk.Label(root, text = speed, bg='orange')
		canvas1.create_window(470, 200, window=speed2)

		country2 = tk.Label(root, text = country, bg='orange')
		canvas1.create_window(470, 250, window=country2)

		date_time1 = location.upper() + '   | ' + date_time
		time = tk.Label(root, text = date_time1, bg='orange')
		canvas1.create_window(530, 50, window=time, tags = 'dt')












#*****************************************************************************************















			
Enter_Location = tk.Label(root, text='Enter Location  : ')
canvas1.create_window(270, 100, window=Enter_Location)

x = tk.Entry (root) 
canvas1.create_window(390, 100, window=x)

button1 = tk.Button (root, text='Show_Details', command=values,bg='orange') 
canvas1.create_window(380, 150, window=button1)


weather_window = tk.Label(root, text = '!!    WEATHER REPORT    !!', bg='orange' , width = 40, height=5, font=("Helvetica", 20), bd=0)
canvas1.create_window(350, 250, window=weather_window, tags = 'ww')






root.mainloop()

#*****************************************************************************************