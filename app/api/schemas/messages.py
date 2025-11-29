from pydantic import BaseModel, EmailStr

class SendMessageRequest(BaseModel):
    to_email: EmailStr
    image_id: int

class SendMessageResponse(BaseModel):
    status: str
    message: str
