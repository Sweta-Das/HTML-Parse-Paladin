import json
import re

def convert_to_json(response: str):
    try:
        # Extracting output with JSON formatting
        pattern = re.compile(r'\{.*?\}', re.DOTALL)
        matches = pattern.findall(response)

        # Handling multiple json objects
        json_objs = []
        for match in matches:
            try:
                json_obj = json.loads(match)
                json_objs.append(json_obj)
            except json.JSONDecodeError:
                return "One or more extracted JSON objects are invalid."
        
        if json_objs:
            return json_objs
        else:
            return "No JSON objects found in the string"
    
    except json.JSONDecodeError as e:
        print(f"Unable to format LLM response: {e}")