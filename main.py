from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from bs4 import BeautifulSoup
import httpx

app = FastAPI()

class URLRequest(BaseModel):
    """Class for sending request to the target URL."""
    url: HttpUrl

@app.post("/process_html/")
async def processing_html(request: URLRequest):
    """
    Endpoint for processing HTML block.
    Args: 
    - url: URL of the webpage containing HTML
    Returns:
    - dict: JSON formatted data
    """
    try:
        # Fetching HTML content from URL
        async with httpx.AsyncClient() as client:
            response = await client.get(str(request.url))
            response.raise_for_status()

            # Parsing HTML with BeautifulSoup
            soup = BeautifulSoup(response.text, "html.parser")
            num_elements = len(soup.find_all("div", class_="hb_parent"))

            return {
                "url": request.url,
                "status_code": response.status_code,
                "no_of_elements": num_elements
            }

    except httpx.RequestError as e:
        raise HTTPException(status_code=400, detail=f'An error occurred while requesting the URL: {e}') from e
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=f"Error response {e.response.status_code} while requesting the URL") from e

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)