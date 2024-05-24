import json

def convert_to_json(response: str):
    try:
        # Cleaning up the LLM response string
        cleaned_res = response.replace('\n', '').replace('\\', '')

        # Converting cleaned string to dictionary (JSON obj.)
        json_res = json.loads(cleaned_res)

        return json_res
    
    except json.JSONDecodeError as e:
        print(f"Unable to format LLM response: {e}")