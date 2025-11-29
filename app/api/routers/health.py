from fastapi import APIRouter

router = APIRouter()

@router.get("/health",tags =["Здоровье"],summary = ["Проверить жив ли сервис"],include_in_schema=True)
async def health_check():
    return {"status": "active"}

@router.get("/test/division-by-zero",tags =["ОШИБКИ"],summary = ["Деление на ноль"])
async def division_by_zero():
    result = 1 / 0
    return {"result": result}

