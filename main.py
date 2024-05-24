from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.utils.html_cleaning import cleaning_HTML
from src.core.llm import llm_html_parsing


# Applying FastAPI for endpoint
app = FastAPI()

# Base Model
class HTMLRequest(BaseModel):
    """Class for sending HTML content."""
    html: str

# POST request
@app.post("/process_html/")
async def processing_html(html_input: str):
    """
    Endpoint for processing HTML block.
    Args: 
    - request: Request body containing HTML block
    Returns:
    - dict: JSON formatted data
    """
    try:
        # Parsing HTML with BeautifulSoup
        filepath = cleaning_HTML(html_input)

        # Get response in str
        res = llm_html_parsing(filepath)

        # Formatting respose to get JSON result

        
        return {
            "message": "HTML content has been formatted and saved.",
            "response": res
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred while processing HTML block: {e}") from e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)