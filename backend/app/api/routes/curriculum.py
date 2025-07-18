from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(tags=["Curriculum"])

@router.get("/curriculum", response_class=JSONResponse)
async def get_curriculum():
    try:
        # Simulate fetching curriculum data
        curriculum_data = {
            "subjects": ["Math", "Science", "History"],
            "grades": ["A", "B", "C"],
            "credits": 30
        }
        return JSONResponse(status_code=200, content=curriculum_data)
    except Exception as e:
        print(f'ERROR - get_curriculum - Exception: {str(e)}')
        return JSONResponse(status_code=500, content={"msg": "Internal Server Error"})