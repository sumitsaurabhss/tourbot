from typing import Optional

from pydantic import BaseModel, Field

class CompleteOrEscalate(BaseModel):
    """A tool to mark the current task as completed and/or to escalate control of the dialog to the main assistant,
    who can re-route the dialog based on the user's needs."""

    cancel: bool = True
    reason: str

    class Config:
        json_schema_extra = {
            "example": {
                "cancel": True,
                "reason": "I have insufficient information, need more information.",
            },
            "example 2": {
                "cancel": True,
                "reason": "I have fully completed the task.",
            },
            "example 3": {
                "cancel": False,
                "reason": "I need to search again for better response.",
            },
        }

class ToHotelAssistant(BaseModel):
    """Transfer work to a specialized assistant to handle hotel suggestion or recommendation."""

    city: str = Field(
        description="The city where the user wants to book a hotel."
    )
    price: float = Field(
        description="Price per night for hotel. Only use if explicitly specified by user.",
        default=0
    )
    rating: float = Field(
        description="Average user rating of hotel. Only use if explicitly specified by user.",
        default=0
    )
    request: str = Field(
        description="Any feature or amenities requested from the user regarding the hotel recommendation. Only use if explicitly specified by user.",
        default=''
    )

    class Config:
        json_schema_extra = {
            "example": {
                "city": "kochi",
                "price": 5000,
                "rating": 3,
                "request": "wifi, parking",
            }
        }

class ToItineraryAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle trip recommendation and itinerary planning.
    It can also find information about culture, cuisines, attractions, tour spots, destinations, activities or experiences."""

    location: str = Field(
        description="The location where the user wants to visit."
    )
    request: str = Field(
        description="Any additional information or requests from the user regarding the trip recommendation for itinerary."
    )

    class Config:
        json_schema_extra = {
            "example": {
                "location": "Udaipur",
                "request": "The user is interested in outdoor activities and scenic views.",
            }
        }