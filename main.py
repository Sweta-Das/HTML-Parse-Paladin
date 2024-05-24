from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.core.html_cleaning import cleaning_HTML


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
        
        return {
            "message": "HTML content has been formatted and saved.",
            "filename": filepath
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred while processing HTML block: {e}") from e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)