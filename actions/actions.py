import yaml
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

class AskSuretoSkip(Action):
    def name(self) -> Text:
        return "action_are_you_sure_skip"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        print(tracker.get_slot("requested_slot"))
        dispatcher.utter_message("Are you sure you want to skip this step?")
        return []
    
class SkipCurrentSlot(Action):
    def name(self) -> Text:
        return "action_skip_current_slot"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        current_slot = tracker.get_slot("requested_slot")
        dispatcher.utter_message("Okey, let's go to the next step")
        return [SlotSet(str(current_slot), "hold")]

# TOOLS FORM ACTIONS ----------------------
class ValidateToolsForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_tools_form"
    def validate_CitrixDoors(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        if slot_value in ["hold","progress","done"]:
            dispatcher.utter_message("Okey! Let's get to it")
            return {"CitrixDoors": slot_value}
        else:
            return {"CitrixDoors": None}
    def validate_GIT(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        if slot_value in ["hold","progress","done"]:
            dispatcher.utter_message("Great! Let's move on to the next one")
            return {"GIT": slot_value}
        else:
            return {"GIT": None}
    def validate_ScreenPresso(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        if slot_value in ["hold","progress","done"]:
            dispatcher.utter_message("Great! Let's move on to the next one")
            return {"ScreenPresso": slot_value}
        else:
            return {"ScreenPresso": None}

class AskForCitrixDoorsAction(Action):
    def name(self) -> Text:
        return "action_ask_tools_form_CitrixDoors"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        ask_slot_data('CitrixDoors',dispatcher=dispatcher)
        return []
    
class AskForGITAction(Action):
    def name(self) -> Text:
        return "action_ask_tools_form_GIT"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        ask_slot_data('GIT',dispatcher=dispatcher)
        return []
    
class AskForScreenPressoAction(Action):
    def name(self) -> Text:
        return "action_ask_tools_form_ScreenPresso"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        ask_slot_data('ScreenPresso',dispatcher=dispatcher)
        return []
    
def ask_slot_data(slot,dispatcher):
    with open('slots.yml','r') as file:
        data = yaml.safe_load(file)
    if slot in data:
        slot_data = data.get(slot)
        text = slot_data.get('text')
        link = slot_data.get('link')
        button = state_buttons()
        if "]" in text:
            index = text.find("]")
            message = text[:index+1] + "(" + link + ")" + text[index+1:]
        else: 
            message = text
        dispatcher.utter_message(message)
        dispatcher.utter_message(buttons=button)
        dispatcher.utter_message(text="Let me know when you're done😉")
        return text, link
    else:
        print("Slot Not Found")
        return '',''

def state_buttons():
    buttons = [{"title": "Completed✔️" , "payload": '/completed'},
               {"title": "In Progress🔄","payload": '/inprogress'},
               {"title": "Skip Step❌" , "payload": '/skip'}]
    return buttons