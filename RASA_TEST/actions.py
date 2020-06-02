# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import UserUtteranceReverted, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from weather import Weather
from stock import stockrate

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_city"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global name1
        cityname=tracker.latest_message['entities']
        print(cityname)

        for e in cityname:
            if e['entity'] == 'city':
                name1 = e['value']
        temp = int(Weather(name1)['temp'] - 273)
        dispatcher.utter_template("utter_temp", tracker, temp=temp)
        return []



    class ActionTset(Action):

        def name(self) -> Text:
            return "action_weather"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            dispatcher.utter_message(text="Chennai weather is high")
            return []

    class AllSlotsReset(Action):
        def name(self):
            return 'action_slot_reset'

        def run(self, dispatcher, tracker, domain):
            return [AllSlotsReset()]

    class ActionStock(Action):

        def name(self) -> Text:
            return "action_stock_market"

        def run(self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            stock_name = tracker.latest_message['entities']
            print(stock_name)
            for e in stock_name:
                if e['entity'] == 'rate':
                    name = e['value']
                    temp = float(stockrate(name))
                    dispatcher.utter_template("utter_stock", tracker, temp=temp)
 #                   message="{} stock price is 740".format(name)
 #                   dispatcher.utter_message(text=message)
                return []

