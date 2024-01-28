import json
from datetime import datetime

def append_cursor_to_file(cursor: str, group_name: str) -> str:
    # Create dictionary with required information
    cursor_dict = {
        "cursor": cursor,
        "datetime": str(datetime.now()),
        "group_name": group_name
    }
    # Convert dictionary to JSON string
    cursor_json = json.dumps(cursor_dict)
    # Open the file in append mode and write the JSON string
    file_path = "cursor.txt" 
    with open(file_path, "a") as file:
        file.write(cursor_json + "\n")
    return group_name

# Example usage:

if __name__== "__main__":
    cursor_value = "AQHRX3QbqXPS9avMkron7BehZOhtaQJZzoHvo73kB_K6Oqt2jMyrtuKxP1GNBPFkSN_rN1HtSPgfXz50Cfpon8yaew"
    group_name_value = "wecomforum"
    appended_group_name = append_cursor_to_file(cursor_value, group_name_value)

    print(f"Group name '{appended_group_name}' appended to file.")