import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from backend.app.api.main import api_router

app = FastAPI(
    title="Lorenzo Pacitto's personal website",
    description="This is the personale website of Lorenzo Pacitto, showcasing his portfolio, blog, and contact information.",
    version="1.0",
    debug=True
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:8000",
    "https://your-production-domain.com",  # Add your production domain if applicable
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows all origins, adjust as needed
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods, adjust as needed
    allow_headers=["*"],  # Allows all headers, adjust as needed
)

app.include_router(api_router)
@app.get("/")
async def root():
    return {"message": "Welcome to Lorenzo Pacitto's personal website!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info", reload=True)
