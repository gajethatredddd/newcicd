from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from app.services.message_service import MessageService
from app.tasks.celery_tasks import send_email_task
from app.api.schemas.messages import SendMessageRequest, SendMessageResponse
from app.core.di import get_message_service

router = APIRouter()

MessageServiceDep = Annotated[MessageService, Depends(get_message_service)]

@router.post(
    "/send_message_to_email",
    response_model=SendMessageResponse,
    tags =["Отправка письма"],
    summary = ["Основная ручка отправки"]
)
async def send_message(
    request: SendMessageRequest,
    service: MessageServiceDep
):
    try:
        send_email_task.delay(request.to_email, request.image_id)
        return SendMessageResponse(
            status="ок",
            message="таска запущена"
        )
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))
