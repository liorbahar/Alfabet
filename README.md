# weather-task

create a web application showing weather data per time & saved locations

weather data per time point & location is avaialble with this api:
https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,relativehumidity_2m,rain,windspeed_10m,temperature_80m,soil_moisture_1_to_3cm

see documentation here: https://open-meteo.com/en/docs

## TASK:

![image](https://github.com/definity-ai-public/weather-task/assets/129408348/cba56757-2fdb-4dec-a0b8-f8c2c2fcc893)

create a web application with a backend server, a database of your choice and a frontend with the following functionality:

1. the top of the screen has a dropdown list allowing the user to choose from saved locations, and a button to add new saved locations.
2. A saved location has 3 values: "name" - displayed to the user in the drop down, "latitude" + "longitude" - locations coordinates.
3. When the user adds a location it is saved by the backend server to the database to be available for future sessions.

below location selection there are 2 display components:

 1. a table with each row is a single weather variable showing: name, max, min, avg, units allowing the user to select a single row.
 2. a chart showing the selected variable values across the last week on a daily basis. 

* every time the user selects a different varibale the chart updates accordingly.
* every time the user selects a different saved location, the table and the chart updates accordingly.


### Clone, solve the task and PR your solution back to this repo.
### Please include instructions for how to install & run your solution.

* need to create db sql server named: weather_task
* and then follow the steps (The tables will be created automatically)

2 ways:
without venv:
1. install: python -m pip install -r requirements.txt
2. run: python run.py

with venv:
1. create venv folder inside the project: mkdir venv
2. run the command: python -m venv venv
3. navigate to folder Scripts: cd venv\Scripts
4. run the file: activate
5. navigate back to the main folder: cd .. and then cd ..
6. run the command: pip install -r requirements.txt
7. run the file run.py: python run.py



