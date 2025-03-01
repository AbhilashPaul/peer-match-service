from pydantic import BaseModel, PositiveInt, Field
from typing import List

class AdolescentInput(BaseModel):
    """
    AdolescentInput is a data model representing the input details for an adolescent.

    Attributes:
        condition (str): The condition or diagnosis of the adolescent.
        hobbies (str): The hobbies or interests of the adolescent.
        about (str): A brief description or additional information about the adolescent.
    """
    condition: str
    hobbies: str
    about: str

class PeerSupporterProfile(BaseModel):
    profile_id: int = Field(..., description="Unique identifier for the peer supporter's profile")
    full_name: str = Field(..., description="The peer supporter's full name or chosen pseudonym")
    age: int = Field(..., ge=18, le=100, description="The age of the peer supporter (must be 18 or older)")
    gender: str = Field(..., description="Gender identity (e.g., male, female, nonbinary)")
    selected_interests: List[str] = Field(..., description="List of interests (e.g., art, sports, music)")
    mental_health_history: List[str] = Field(..., description="List of mental health challenges the supporter has experienced")
    lived_experience_narrative: str = Field(
        ..., 
        description="A free-text narrative summarizing the peer supporter's personal experiences with mental health challenges"
    )

class Match(BaseModel):
    peer_supporter_profile: PeerSupporterProfile
    reason_for_match: List[str]

class MatchesResponse(BaseModel):
    matches: List[Match]
