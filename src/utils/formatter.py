import json
import re

def convert_to_json(response: dict):
    try:
        # Extracting output with JSON formatting
        # pattern = re.compile(r'\{.*?\}', re.DOTALL)
        # matches = pattern.findall(response)

        # Handling multiple json objects
        # for match in matches:
        #     try:
        #         json_obj = json.loads(match)
        #         print(f"json obj: {json_obj}")

        #     except json.JSONDecodeError:
        #         return "One or more extracted JSON objects are invalid."
        
        # if json_obj:
        #     return json_obj
        # else:
        #     return "No JSON objects found in the string"
        if response:
            try:
                json_obj = json.dumps(response)
                print(f"json_obj: {json_obj}, type = {type(json_obj)}")
                return json_obj

            except json.JSONDecodeError:
                return "JSON objects cannot be formatted"
    
    except json.JSONDecodeError as e:
        print(f"Unable to format LLM response: {e}")