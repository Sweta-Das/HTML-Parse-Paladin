# Introduction

This project is designed to extract meaningful attributes from an HTML block of E-commerce websites using LLM. On extraction, the response from the LLM is formatted in JSON and produced as result.
The detailed description of tasks performed by LLM HTML Parser is given below: 

# Technical Tasks

**Task-1: Development Environment Setup**<br>
- The LLM chosen to perform the parsing is Mixtral 8x7B (open-source) through Hugging Face Endpoint.
- The framework selected for API implementation is FastAPI. 
- Streamlit has been used to provide a clean and interactive web application at the frontend.

**Task-2: API Implementation** <br>
- The API endpoint that accepts HTML input is `/parse_html/`
- The endpoint accepts the html block (code snippet) as string, which is then cleaned and processed using LLM to extract meaningful attributes.

**Task-3: HTML Processing**<br>
- The HTML blocks may contain about products, their prices, names, images associated with them along with some description.
- LLM extracts all of these information (if present) from the block and their associated CSS selectors.

**Task-4: Data Formatting and Output**<br>
- The response provided by LLM is in string format, which is further processed to extract only JSON outputs present within the braces `{}`.
- To prevent errors, HTML blocks are to be fed in considerable size so that it won't raise 'max input token' issue. Also, sometimes the LLM may respond, but there may be error in streamlit due to incorrect JSON formatting. 