import requests
from utils.read_payload import read_payload
import csv
import time 
from utils.save_cursor import append_cursor_to_file


def save_data(cursor="AQHRXun0VAnY1yg8O7gT-yTPhKNHS8kQoNIdKPV7nnWHGTfn_wBjNbRSExaU087lGbZdnTycyqxEgmxqnL_TAr19ow",
              output_file="request_csv/realestate.csv"):
    attempts = 0
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100011944262857&__aaid=0&__user=100011944262857&__a=1&__req=s&__hs=19774.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1011539662&__s=dpp3km%3Anpcvxf%3Avhrug4&__hsi=7337916743515745712&__dyn=7AzHK4HwkEng5K8G6EjBAg2owIxu13wFG14yUKewSwAyUco5S3O2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswMwto886C11xmfz83WwtohwGxu782lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2G1jxS6FobrwKxm5o7G4-5pUfEe88o4Wm7-2K0-poarCwLyESE6C14wwwOg2cwMwhEkxebwHwNxe6Uak0zU8oC1Hg6C13whEeE4WVU-4Edo&__csr=gVb1949_SGcwIx7f9Oq5lfdfR9R9dl8G9kBIiiZli9WqumjvCR8B9iaBlAmQFdUBv-jgyFehF5hKdHCxuKA8WjGUGESlBy4qVBAGaBx3jhpVFu2Oazax5eE89Umoc8lJ1-F8Su1qxeEKqbwlUhCBwLyU9E-5pE6by88-m2yewZwrUbogxi4ogyE985636782tDwey3d0tE-3u17Cwe20w81IE9U1Do1AU5l2U1Ko1iE07ey00Tao3uwaO0kG0nm0rm021C0gK0sJ02wo0Q6aw1n-04SC3B0f102D80aa805nla0YAE3Aw&__comet_req=15&fb_dtsg=NAcMKwF11Cc8zJMHaYrVjq-ADcTkEH2csNds6w1HnBdBjz-5_hBIwyA%3A47%3A1705412428&jazoest=25361&lsd=AqNV5G48NeYvYJiPDRaUQL&__spin_r=1011539662&__spin_b=trunk&__spin_t=1708491878&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%223574355042621326%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%223574355042621326%22%7D&server_timestamps=true&doc_id=7524923467527191'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYcFqKjj5sPEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARag-YzaDBYAABV-HEwAABYAFqD5jNoMFgAAFigA%22%2C%2295%22%3A%22HCwAABYQFtSYneENEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22r8235x%22%7D; c_user=100011944262857; ps_n=0; ps_l=0; usida=eyJ2ZXIiOjEsImlkIjoiQXM5NXRvbWdzcnpncyIsInRpbWUiOjE3MDg0NDEyMjJ9; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1708491881902%2C%22v%22%3A1%7D; wd=345x827; xs=47%3Av229aH3rT1tzXQ%3A2%3A1705412428%3A-1%3A8246%3A%3AAcVdXNyuZlDsHzBHA8B1RCfvkKHVj7w-rsn6IJ-K3xw; fr=1V8LPPCJKABOepx3a.AWX8NqQCGV_Pv9KzSgIdhoJBRFg.Bl1YR7.1c.AAA.0.0.Bl1YR7.AWV4N5nFTRI; c_user=100011944262857; fr=1fFuiS0RT5yn6KwFJ.AWXOeJOpkSo6pYKpS4P-WuaX6xM.BltqP8.1c.AAA.0.0.BltqP8.AWURw2JN2uk; xs=47%3Av229aH3rT1tzXQ%3A2%3A1705412428%3A-1%3A8246%3A%3AAcVoHoZHOeuCfRN98xSQe4sr2jG_k3o7oksKh7qhSA',
        'dpr': '2',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/3574355042621326/members',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-full-version-list': '"Not A(Brand";v="99.0.0.0", "Google Chrome";v="121.0.6167.185", "Chromium";v="121.0.6167.185"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-model': '"Nexus 5"',
        'sec-ch-ua-platform': '"Android"',
        'sec-ch-ua-platform-version': '"6.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36',
        'viewport-width': '345',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
        'x-fb-lsd': 'AqNV5G48NeYvYJiPDRaUQL'
        }
        if i%500 == 1:
                print("sleeping for 20 secs >> ", i)
                time.sleep(20)
        try:
            # data = []
            response = requests.request("POST", url, headers=headers, data=payload)
            data, cursor, has_next_page = read_payload(payload=response.json())  
        
            with open(output_file, 'a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                for row in data:
                    csv_writer.writerow(row)
            print(i, output_file)
            attempts = 0
        except Exception as e:
            attempts += 1
            append_cursor_to_file(cursor=cursor, group_name="wecomforum")
            print(e)
        if attempts == 3:
            print("three failed attempts")
            break
        if attempts == 1:
            time.sleep(200)
            print("slept for 100 seconds")



save_data()
