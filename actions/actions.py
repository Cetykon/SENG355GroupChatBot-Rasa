# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pyowm



class ActionTellTemperature(Action):
    # Name Method
    def name(self) -> Text:
        return "action_tell_temperature"

    
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        current_place = next(tracker.get_latest_entity_values("place"), None)
        
        owm = pyowm.OWM('3701e9245325560b2e1eb9a37bcdfce7')
        weather_mgr = owm.weather_manager()
        place = str(current_place) + ', US'
        observation = weather_mgr.weather_at_place(place)
        temperature = observation.weather.temperature("celsius")["temp"]
        
        if not current_place:
            msg = f"Can you give me a place."
            dispatcher.utter_message(text=msg)
            return[]
        
        msg = f"The Temperature is {temperature} in " + str(current_place) + " now."
        dispatcher.utter_message(text=msg)
        return []