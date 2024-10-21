from llms import llm
from hotel_db import search_hotels
from vector_store import retriever_tool
from prompts import hotel_prompt, itinerary_prompt, primary_assistant_prompt
from models import CompleteOrEscalate, ToHotelAssistant, ToItineraryAssistant

hotel_tools = [search_hotels]

def hotel_runnable():
    runnable = hotel_prompt | llm.bind_tools(
        hotel_tools + [CompleteOrEscalate]
    )
    return runnable

itinerary_tools = [retriever_tool]

def itinerary_runnable():
    runnable = itinerary_prompt | llm.bind_tools(
        itinerary_tools + [CompleteOrEscalate]
    )
    return runnable

primary_assistant_tools = [ToHotelAssistant, ToItineraryAssistant]

def primary_runnable():
    runnable = primary_assistant_prompt | llm.bind_tools(
        primary_assistant_tools
    )
    return runnable