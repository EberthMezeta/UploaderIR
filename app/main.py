from fastapi import FastAPI
from router.router import router

import uvicorn

app = FastAPI()
app.include_router(router)

if __name__=="__main__":
    uvicorn.run("main:app",host='localhost', port=8094, reload=True, debug=True)