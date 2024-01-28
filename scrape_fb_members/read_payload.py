import json 

# payload = json.loads(open("sample2.json", "r", encoding="utf-8").read())
# print(payload)

def read_payload(payload, sample="sample 1"):
    edges = payload["data"]["node"]["new_members"]["edges"]
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

    cursor = payload["data"]["node"]["new_members"]['page_info']['end_cursor']
    return (data, cursor)

# if __name__ == "__main__":
#     read_payload(payload=payload)