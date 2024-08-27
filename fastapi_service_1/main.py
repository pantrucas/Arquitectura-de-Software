from fastapi import FastAPI
import logging
import sys

app = FastAPI()

#logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)

@app.get("/")
async def root():
    logging.info("Service 1: Handling root endpoint")
    #logger.info("Service 1: Handling root endpoint")
    return {"message": "Hello from Service 1"}