from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, START
from llms import langsmith_trace
from states import State
from assistant import Assistant
from runnables import primary_runnable, hotel_runnable, itinerary_runnable
from tool_nodes import create_tool_node_with_fallback
from runnables import primary_assistant_tools, hotel_tools, itinerary_tools
from routes import route_hotel, route_itinerary, route_primary_assistant

def setup_graph():
    langsmith_trace()
    builder = StateGraph(State)

    builder.add_node("primary_assistant", Assistant(primary_runnable()))
    builder.add_edge(START, "primary_assistant")
    builder.add_node("primary_assistant_tools", create_tool_node_with_fallback(primary_assistant_tools))
    builder.add_conditional_edges(
        "primary_assistant",
        route_primary_assistant,
        {
            "hotel": "hotel",
            "itinerary": "itinerary",
            "primary_assistant_tools": "primary_assistant_tools",
            END: END,
        },
    )
    builder.add_edge("primary_assistant_tools", "primary_assistant")

    builder.add_node("hotel", Assistant(hotel_runnable()))
    builder.add_node("hotel_tools", create_tool_node_with_fallback(hotel_tools))
    builder.add_edge("hotel_tools", "hotel")
    builder.add_conditional_edges("hotel", route_hotel)

    builder.add_node("itinerary", Assistant(itinerary_runnable()))
    builder.add_node("itinerary_tools", create_tool_node_with_fallback(itinerary_tools))
    builder.add_edge("itinerary_tools", "itinerary")
    builder.add_conditional_edges("itinerary", route_itinerary)

    memory = MemorySaver()
    return builder.compile(checkpointer=memory)