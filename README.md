# alfabet


## TASK:

* Need to create db sql server named: alfabet
* Then follow the steps (The tables will be created automatically)
* The server will run on port 1112

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

## Reminder
To start the event reminder run 'python event_reminder.py'

## Doc
* POST - create new event - /event
    * request
    ```json
        {
         "location": "tel jjjaviv",
          "venue": "tel jjjjaviv",
          "date": "2022-12-12T00:09:00Z",
          "participantsNumber": 9999
        }
    ```
    * response
    ```json  
        {
        "creationTime": "2023-11-26 00:07:13.450000+00:00",
        "date": "2022-12-12 00:09:00+00:00",
        "id": "e86c84f2-a089-4129-8f18-ad6a8318f856",
        "location": "tel jjjaviv",
        "participantsNumber": 9999,
        "venue": "tel jjjjaviv"
        }
    ```
    
* PUT - update event details -  /event/<evnet_id>
    * request
    ```json
        {
         "location": "tel jjjaviv",
          "venue": "tel jjjjaviv",
          "date": "2022-12-12T00:09:00Z",
          "participantsNumber": 9999
        }
    ```
    * response
    ```json  
        {
        "creationTime": "2023-11-26 00:07:13.450000+00:00",
        "date": "2022-12-12 00:09:00+00:00",
        "id": "e86c84f2-a089-4129-8f18-ad6a8318f856",
        "location": "tel jjjaviv",
        "participantsNumber": 9999,
        "venue": "tel jjjjaviv"
        }
    ```
        

* GET - get specific event details - /event/<event_id>
    * response
     ```json  
    {
        "creationTime": "2023-11-26 00:07:13.450000+00:00",
        "date": "2022-12-12 00:09:00+00:00",
        "id": "e86c84f2-a089-4129-8f18-ad6a8318f856",
        "location": "tel jjjaviv",
        "participantsNumber": 9999,
        "venue": "tel jjjjaviv"
    }
    ```
        
* DELETE - delete specific event - /event/<event_id>
    * response
    ```json  
    {
        "message": "Event with uuid: e86c84f2-a089-4129-8f18-ad6a8318f856 delete successfully"
    }
    ```
            
* GET - /events?location=<location_name>&venue=<venue_name>&sortOption=<date|participants|creationTime>
    * this route can retrieve events by some filters
    * the query params are optional, we can get all the events by send request to /event
    * we can add filters by query params: location, venue, sortOption
    * response
    ```json
        {
        "events": [
            {
                "id": "a79eb893-b40c-4925-8f41-3917ffe71d75",
                "location": "tel jjjaviv",
                "venue": "tel jjjjaviv",
                "date": "2023-11-21 02:10:00+00:00",
                "participantsNumber": 11,
                "creationTime": "2023-11-20 22:15:45.603333+00:00"
            },
            {
                "id": "913b2179-e37e-4dda-a7e6-bfa6e00cad01",
                "location": "tel jjjaviv",
                "venue": "tel jjjjaviv",
                "date": "2023-11-21 02:10:00+00:00",
                "participantsNumber": 9999,
                "creationTime": "2023-11-21 00:36:10.270000+00:00"
            },
            {
                "id": "575d9100-a39b-45b3-b655-99403e053499",
                "location": "tel jjjaviv",
                "venue": "tel jjjjaviv",
                "date": "2023-11-21 02:10:00+00:00",
                "participantsNumber": 9999,
                "creationTime": "2023-11-21 00:41:56.216666+00:00"
            }
        ]
      }
    ```
    
# Reminder:
To start the reminder run the command: 'python event_reminder.py'
        




