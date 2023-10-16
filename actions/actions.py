def links():
    webUrl = "https://www.facebook.com"
    return webUrl

def state_buttons():
    buttons = [{"title": "Completed✔️" , "payload": '/completed'},
               {"title": "In Progress🔄","payload": '/inprogress'},
               {"title": "Skip Step❌" , "payload": '/skip'}]
    return buttons

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict

class SelectMainSteps(Action):
    def name(self) -> Text:
        return "action_select_main_steps"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        buttons =  [{"title": "Basic Tools Installation🟩","payload": '/start_tools'},
                    {"title": "Basic Induction Topics🔲","payload": '/start_tools'},
                    {"title": "Advanced Induction Topics🔲","payload": '/start_tools'}]
        dispatcher.utter_message("Select main step: ")
        dispatcher.utter_message(buttons=buttons)
        return []

class AskSuretoSkip(Action):
    def name(self) -> Text:
        return "action_are_you_sure_skip"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        print(tracker.get_slot("requested_slot"))
        dispatcher.utter_message("Are you sure you want to skip this step")
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
        print(slot_value)
        return {"CitrixDoors": slot_value}
    def validate_GIT(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        print(slot_value)
        return {"GIT": slot_value}
    def validate_ScreenPresso(self,slot_value: Any,dispatcher: CollectingDispatcher,tracker: Tracker,domain: DomainDict,) -> Dict[Text, Any]:
        print(slot_value)
        return {"ScreenPresso": slot_value}
    
class AskForCitrixDoorsAction(Action):
    def name(self) -> Text:
        return "action_ask_tools_form_CitrixDoors"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        webUrl = links()
        button = state_buttons()
        dispatcher.utter_message(text="Here's the link to the documentation about CitrixDoors")
        #dispatcher.utter_message(template="utter_link",link=webUrl)
        dispatcher.utter_message(buttons=button)
        dispatcher.utter_message(text="Let me know when you are done")
        return []
    
class AskForGITAction(Action):
    def name(self) -> Text:
        return "action_ask_tools_form_GIT"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        webUrl = links()
        button = state_buttons()
        dispatcher.utter_message(text="Here's the link to the documentation about GIT")
        #dispatcher.utter_message(template="utter_link",link=webUrl)
        dispatcher.utter_message(buttons=button)
        dispatcher.utter_message(text="Let me know when you are done")
        return []
    
class AskForScreenPressoAction(Action):
    def name(self) -> Text:
        return "action_ask_tools_form_ScreenPresso"
    def run( self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        webUrl = links()
        button = state_buttons()
        dispatcher.utter_message(text="Here's the link to the documentation about ScreenPresso")
        #dispatcher.utter_message(template="utter_link",link=webUrl)
        dispatcher.utter_message(buttons=button)
        dispatcher.utter_message(text="Let me know when you are done")
        return []