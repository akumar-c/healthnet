# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


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


# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import pyTigerGraph as tg



################# TigerGraph Initialization ######################""
conn = tg.TigerGraphConnection(host="https://healthnet.i.tgcloud.io", password="tigergraph", gsqlVersion="3.0.5", useCert=True)
conn.graphname = "healthnet"
conn.apiToken = conn.getToken(conn.createSecret())
#######################################"

class GetDieasesForSymptoms(Action):

    def name(self) -> Text:
        return "get_disease_symptoms"   

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        print(tracker.latest_message)
        result = tracker.latest_message['entities'][0]['value']
        if result:
            query_response = conn.runInstalledQuery("viewConditionSymptoms",{"p": result})
            recommendations = query_response[0]
            symptoms = recommendations["symptoms"]
            dispatcher.utter_message("Here are the symptoms for the condition:")
            dispatcher.utter_message(result)
            dispatcher.utter_message("*********************************************")
            for i in range(len(symptoms)):
                dispatcher.utter_message(symptoms[i]["name"])
                dispatcher.utter_message("========================")

        return []


