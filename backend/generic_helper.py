import re

def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

if __name__ == "__main__":
    print(get_str_from_food_dict({"mango lassi": 1, "pav bhaji": 1}))
    # print(extract_session_id("projects/foody-nfsb/agent/sessions/21311c6f-b2b6-3e43-c07f-a32b7f5e13d8/contexts/ongoing-order"))
