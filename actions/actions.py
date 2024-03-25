# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

# Importing weather-related libraries
import pyowm  # pip install pyowm
from geopy.geocoders import Nominatim  # pip install geopy
from datetime import datetime   



# Custom action to get the current temperature of a place
class ActionTellTemperature(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_temperature"

    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # Extracting location entity from the user's input
        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        # If location entity is not provided by the user
        if not current_place:
            msg = f"Can you give me a place."
            dispatcher.utter_message(text=msg)
            return[]
        
        try:  
            # Initializing OpenWeatherMap API
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            weather_mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = weather_mgr.weather_at_place(place)
            temperature = observation.weather.temperature("fahrenheit")["temp"]
        except:
            print("Weather API Failed")
            msg = f"You may have misspell the Location can you give me the location again."
            dispatcher.utter_message(text=msg)
            return []
        
        # Constructing the response message
        msg = f"The Temperature is {temperature} fahrenheit in " + str(current_place) + " now."
        dispatcher.utter_message(text=msg)
        return []
    
    
class ActionTellWeatherCondition(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_weather_condition"

    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        if not current_place:
            msg = f"Can you give me a place?"
            dispatcher.utter_message(text=msg)
            return[]
        
        try:   
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            weather_mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = weather_mgr.weather_at_place(place)
            weatherCondition = observation.weather.detailed_status
            
        except:
            print("Weather API Failed")
            msg = f"You may have misspell the Location can you give me the location again."
            dispatcher.utter_message(text=msg)
            return []
            
        
        msg = f"The weather condition is {weatherCondition} in " + str(current_place) + " now."
        dispatcher.utter_message(text=msg)
        return []
    

class ActionTellWindSpeed(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_wind_speed"

    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        if not current_place:
            msg = f"Can you give me a place."
            dispatcher.utter_message(text=msg)
            return[]
        
        try: 
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            weather_mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = weather_mgr.weather_at_place(place)
            wind_speed = observation.weather.wind()["speed"]
        
        except:
            print("Weather API Failed")
            msg = f"You may have misspell the Location can you give me the location again."
            dispatcher.utter_message(text=msg)
            return []
            
        msg = f"The wind speed is {wind_speed} m/s in " + str(current_place) + " now."
        dispatcher.utter_message(text=msg)
        return []
    
    
class ActionTellWindSpeedInDetail(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_wind_speed_in_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        if not current_place:
            msg = f"Can you give me a place?"
            dispatcher.utter_message(text=msg)
            return[]
        
        try:   
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            weather_mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = weather_mgr.weather_at_place(place)
            wind_dict_in_meters_per_sec = observation.weather.wind()
            wind_speed = wind_dict_in_meters_per_sec['speed']
            wind_direction = wind_dict_in_meters_per_sec['deg']
            wind_gust = wind_dict_in_meters_per_sec['gust']
            
            
        except Exception as e:  
            print(f"Weather API Failed: {e}")
            msg = f"You may have misspell the Location can you give me the location again."
            dispatcher.utter_message(text=msg)
            return []
            
        
        msg = f"The wind speed is {wind_speed} m/s. The wind direction is {wind_direction} degrees. The wind gust is {wind_gust} meters/sec in " + str(current_place) + " now."
        dispatcher.utter_message(text=msg)
        return []
    
    
class ActionTellMinAndMaxTemp(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_min_and_max_temp"

    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        if not current_place:
            msg = f"Can you give me a place?"
            dispatcher.utter_message(text=msg)
            return[]
        
        try:   
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            weather_mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = weather_mgr.weather_at_place(place)
            temp_dict_kelvin = observation.weather.temperature()
            temp_dict_kelvin['temp_min']
            temp_dict_kelvin['temp_max']
            
            fahrenheit_min = int((temp_dict_kelvin['temp_min'] - 273.15) * 9 / 5 + 32)
            fahrenheit_max = int((temp_dict_kelvin['temp_max'] - 273.15) * 9 / 5 + 32)
            
        except Exception as e:  
            print(f"Weather API Failed: {e}")
            msg = f"You may have misspell the Location can you give me the location again."
            dispatcher.utter_message(text=msg)
            return []
            
        
        msg = f"The minimum temperature is {fahrenheit_min} fahrenheit and the max Temperature {fahrenheit_max} fahrenheit"
        dispatcher.utter_message(text=msg)
        return []
    
    
class ActionGetAirQuality(Action):
    def name(self):
        return "action_get_air_quality"

    def run(self, dispatcher, tracker, domain):

        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        if not current_place:
            msg = f"Can you give me a place?"
            dispatcher.utter_message(text=msg)
            return[]

        try:  
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            mgr = owm.airpollution_manager()
            
            # Initialize Nominatim API
            geolocator = Nominatim(user_agent="MyApp")
            location = geolocator.geocode(current_place)
            
            aq_data = mgr.air_quality_at_coords(location.latitude, location.longitude)
            aqi = aq_data.aqi
            
        except Exception as e:  
            print(f"Weather API Failed: {e}")
            msg = f"You may have misspell the Location can you give me the location again."
            dispatcher.utter_message(text=msg)
            return []
        
        if aqi <= 50:
            response = "The air quality is good with an AQI of {}. It's safe to go outside.".format(aqi)
        elif aqi <= 100:
            response = "The air quality is moderate with an AQI of {}. Sensitive individuals should consider limiting outdoor activities.".format(aqi)
        else:
            response = "The air quality is poor with an AQI of {}. It's advisable to stay indoors if possible.".format(aqi)

        dispatcher.utter_message(text=response)

        return []
    

class ActionTellHumidity(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_humidity"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_place = next(tracker.get_latest_entity_values("place"), None)

        if not current_place:
            msg = f"Can you give me a place."
            dispatcher.utter_message(text=msg)
            return[]

        try: 
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            weather_mgr = owm.weather_manager()
            
            # Initialize Nominatim API
            geolocator = Nominatim(user_agent="MyApp")
            location = geolocator.geocode(current_place)
            
            observation = weather_mgr.one_call(lat=location.latitude, lon=location.longitude)
            humidity  = observation.current.humidity

        except Exception as e:  
            print(f"Weather API Failed: {e}")
            msg = f"You may have misspelled the location. Can you give me the location again?"
            dispatcher.utter_message(text=msg)
            return []

        msg = f"The humidity is {humidity} in " + str(current_place) + "now."
        dispatcher.utter_message(text=msg)
        return []


class ActionTellSunrise(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_sunrise"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_place = next(tracker.get_latest_entity_values("place"), None)

        if not current_place:
            msg = f"Can you give me a place."
            dispatcher.utter_message(text=msg)
            return[]

        try: 
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = mgr.weather_at_place(place)
            sunrise = observation.weather.sunrise_time(timeformat='date')
            
            user_friendly_sunrise = sunrise.strftime("%I:%M %p on %B %d, %Y")
            
        except Exception as e:  
            print(f"Weather API Failed: {e}")
            msg = f"You may have misspelled the location. Can you give me the location again?"
            dispatcher.utter_message(text=msg)
            return []

        msg = f"The sunrise will be at {user_friendly_sunrise} in {current_place}."

        dispatcher.utter_message(text=msg)
        return []


class ActionTellSunset(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_sunset"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        current_place = next(tracker.get_latest_entity_values("place"), None)

        if not current_place:
            msg = f"Can you give me a place."
            dispatcher.utter_message(text=msg)
            return[]

        try: 
            owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
            mgr = owm.weather_manager()
            place = str(current_place) + ', US'
            observation = mgr.weather_at_place(place)
            sunset = observation.weather.sunset_time(timeformat='date')
            
            user_friendly_sunset = sunset.strftime("%I:%M %p on %B %d, %Y")

        except Exception as e:  
            print(f"Weather API Failed: {e}")
            msg = f"You may have misspelled the location. Can you give me the location again?"
            dispatcher.utter_message(text=msg)
            return []

        msg = f"The sunset will be at {user_friendly_sunset} in {current_place}."

        dispatcher.utter_message(text=msg)
        return []