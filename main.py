# Creating FastAPI endpoints
from fastapi import FastAPI, Body
from bs4 import BeautifulSoup

app = FastAPI()

@app.post("/process_html")
def processing_html(html: str = Body(..., title="HTML Content")):
    """
    Endpoint for processing HTML block.
    Args: 
    - html: HTML content as string
    Returns:
    - dict: JSON formatted data
    """

    response = f"No. of elements in HTML: {len}"