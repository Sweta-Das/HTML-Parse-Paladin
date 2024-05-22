# Technical Tasks

**Task-1: Development Environment Setup**<br>
- Select and configure an open-source LLM such as LLaMA 3, BERT, Vicuna or
any other suitable alternative.
- Set up a development environment for API implementation using a framework
like Flask or FastAPI.

**Task-2: API Implementation** <br>
- Create an API endpoint that accepts an HTML block as input.
- Implement functionality within the API to utilize the chosen LLM for processing
the HTML content.

**Task-3: HTML Processing**<br>
- Using ML, parse the HTML to identify and extract meaningful attributes relevant
to e-commerce contexts (e.g., product names, prices, descriptions, images).
- Identify the CSS selectors or Xpaths for each extracted attribute to pinpoint their
location within the HTML structure.

**Task-4: Data Formatting and Output**<br>
- Format the extracted attributes and their respective selectors into a JSON
structure.
- Ensure the API returns this JSON formatted data as a response to requests.


# Solution

**API endpoint creation**<br>
- Creating an API endpoint that can accept HTML block as input using FastAPI