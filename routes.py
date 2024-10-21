from states import State
from typing import Literal
from langgraph.prebuilt import tools_condition
from langgraph.graph import END
from models import CompleteOrEscalate, ToHotelAssistant, ToItineraryAssistant

def route_hotel(
    state: State,
) -> Literal[
    "primary_assistant", "hotel_tools", "__end__"
]:
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "primary_assistant"
    return "hotel_tools"


def route_itinerary(
    state: State,
) -> Literal[
    "itinerary_tools",
    "primary_assistant",
    "__end__",
]:
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    did_cancel = any(tc["name"] == CompleteOrEscalate.__name__ for tc in tool_calls)
    if did_cancel:
        return "primary_assistant"
    return "itinerary_tools"


def route_primary_assistant(
    state: State,
) -> Literal[
    "primary_assistant_tools",
    "hotel",
    "itinerary",
    "__end__",
]:
    route = tools_condition(state)
    if route == END:
        return END
    tool_calls = state["messages"][-1].tool_calls
    if tool_calls:
        if tool_calls[0]["name"] == ToHotelAssistant.__name__:
            return "hotel"
        elif tool_calls[0]["name"] == ToItineraryAssistant.__name__:
            return "itinerary"
        return "primary_assistant_tools"
    raise ValueError("Invalid route")