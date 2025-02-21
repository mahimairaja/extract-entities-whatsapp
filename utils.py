import getpass
import os
from typing import Literal
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")


from langchain.chat_models import init_chat_model
from typing import Optional
from pydantic import BaseModel, Field


class FoodOrder(BaseModel):
    """Food order details."""

    food_name: str = Field(description="The name of the food item")
    quantity: int = Field(description="The quantity of food ordered")
    when_needed: Optional[Literal["breakfast", "lunch", "dinner"]] = Field(
        description="When the food is needed (breakfast, lunch, or dinner) if applicable. brekfast for morning, lunch for afternoon, and dinner for evening."
    )

def extract_food_order(text: str) -> Optional[FoodOrder]:
    """Extract food order details from the given text."""
    chat_model = init_chat_model("gpt-4o-mini", model_provider="openai")
    structured_llm = chat_model.with_structured_output(FoodOrder)
    return structured_llm.invoke(text)

