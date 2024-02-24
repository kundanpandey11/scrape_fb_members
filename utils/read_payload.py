import json 

# payload = json.loads(open("sample2.json", "r", encoding="utf-8").read())
# print(payload)

def read_payload(payload, payload_type="new_members"):
    edges = payload["data"]["node"][payload_type]["edges"]
    data = []
    for pld in edges:
        try:
            joined = pld["join_status_text"]["text"]
        except Exception as e:
            print(e)
            joined = ""
        try:
            name = pld['node']["name"]
            # print(name)
            url = pld['node']['url']
        except Exception as e:
            print(e)
            name = url = ""
        try:
            work = pld['node']["bio_text"]
            work_at = work['text'] if work != None else ""
        except Exception as e:
            print(e)
            work_at = ""
        data.append([name, url, joined, work_at])

    cursor = payload["data"]["node"][payload_type]['page_info']['end_cursor']
    next_page = payload["data"]["node"][payload_type]['page_info']['has_next_page']
    has_next_page = True if next_page == True or next_page == "true" else False
    
    # print(data)
    # print(has_next_page)
    # print(cursor)
    return (data, cursor, has_next_page)



if __name__ == "__main__":
    with open("test.json", "r", encoding="utf-8") as json_file:
        payload = json.loads(json_file.read())
        # read_payload(payload=payload, payload_type="search_results")
        read_payload(payload=payload, )
        