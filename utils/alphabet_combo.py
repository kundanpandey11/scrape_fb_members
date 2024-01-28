import json

def generate_alphabet_combinations():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    combinations = []
    index = 1

    for char1 in alphabet:
        for char2 in alphabet:
            combination = char1 + char2
            combinations.append({"value": combination, "index": index})
            index += 1

    return combinations


if __name__ == "__main__":
    with open("alphabet.json", "w", encoding="utf-8") as json_file:
        
        # Generate alphabet combinations
        result = generate_alphabet_combinations()

        # Convert the result to JSON
        json_result = json.dumps(result, indent=2)
        json_file.write(json_result)


        # Print or use the JSON result as needed
        print(json_result)