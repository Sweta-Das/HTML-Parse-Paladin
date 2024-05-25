import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Union, List, Dict
from src.utils.html_cleaning import cleaning_HTML
from src.core.llm import llm_html_parsing
from src.utils.formatter import convert_to_json


# Applying FastAPI for endpoint
app = FastAPI()

# Input Model Class
class HTMLContent(BaseModel):
    """HTML Block Input"""
    content: str

# Output Model Class
class JSONResponse(BaseModel):
    """JSON Response of HTML block"""
    message: str
    response: Union[Dict[str, str], List[Dict[str, str]]]

    model_config = {
        "json_schema_extra": {
            "examples" : [
                {
                    "message": "Result of HTML Parsing using LLM",
                    "response": [
                        {
                            "product": "Coffee",
                            "product_tag": ".productTitle",
                            "price": "$ 20",
                            "price_tag": ".regualarPrice",
                            "desc": "Get refreshed and energized",
                            "desc_tag": ".description > a",
                            "img": "https://www.example.com/Coffee.jpg",
                            "img_tag": ".titleImage"
                        }
                    ]
                }
            ]
        }
    }


# POST request
@app.post("/parse_html/", response_model=JSONResponse)
async def parsing_html(html_input: HTMLContent):
    """
    Endpoint for processing HTML block.

    Args: 
    - html_input: HTML block or code snippet

    Returns:
    - dict: JSON formatted data
    """
    try:
        
        # Cleaning HTML with BeautifulSoup
        filepath = cleaning_HTML(html_input.content)

        # Get response in str
        res = llm_html_parsing(filepath)
        
        # Formatting respose to get JSON result
        frmt_res = convert_to_json(res)

        # Removing the temporarily created file
        # os.remove(filepath)
        
        if "list" in frmt_res:
            response = [frmt_res]
        else:
            response = frmt_res

        return JSONResponse(
            message="Result of HTML Parsing using LLM",
            response=response
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"An error occurred while processing HTML block: {e}") from e

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)