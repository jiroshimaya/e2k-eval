"""Common schema definitions for the project."""
from pydantic import BaseModel, Field


class WordPair(BaseModel):
    english: str = Field(..., description="The English word.")
    kana: str = Field(..., description="The Kana representation of the word.")