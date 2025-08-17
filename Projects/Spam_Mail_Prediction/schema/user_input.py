from pydantic import BaseModel, Field
from typing import Annotated

class Message(BaseModel):
    message: Annotated[str, Field(..., description= "Enter the email message content only: ")]