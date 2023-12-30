import requests
from read_payload import read_payload
from save_cursor import append_cursor_to_file
import csv
import time 


def save_data(cursor="AQHRte4tz89jncC1tTkjDqSMqBBlfziHV0s4d-5fW0VQM6q1DPwmkPIHfZ-uKNoO00MYgxAoOx1-ezDCA4vTDNj30A", output_file="request_csv/eeCAB.csv"):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=61554862379223&__user=61554862379223&__a=1&__req=u&__hs=19717.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=GOOD&__rev=1010589214&__s=ho6l1o%3Amz2y4w%3Aavryck&__hsi=7317004305298092575&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwkUKewSwAyUco2qwJyE24wJwpUe8hwaG0Z82_CxS320ni48swIK1Rwwwqo465o-cwfG1Rx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwuEjUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1Hg6C13whEeE4WVU-4E&__csr=gmih4r7mzPPPl9RbbbqOAqq9Nftn94q4Pit-yiIy_SLtfBRUCqzkuGHAGjl5yHjVkFqnGXKczFQL_qyFRhQl1JqokUyUS8y49y8uDz4bXKcy8qKEjyBXDxmcxa5VogwgubgfpUK8yoy6Gx2ezEkyoW8x-2Cbwpo7-6o768wBU5S26361NxqdwhogwEyE6e321Dw8278hwiUswem0na1lw8a0aSwayE4pwn87m0t601Jyw0fm-4o2mwEw1lG3S0le6ogDw8u5o6K0alw2DVU05AO02520ri03ze1Mw0Iww2wUcFk&__comet_req=15&fb_dtsg=NAcNWW83eBneHU_QtOiMqSzjh52g9v9Xjn8fNjNMVruT4Zb2S9Lg8lA%3A7%3A1703368401&jazoest=25379&lsd=qTQpzFrcpB4fsedseil4ik&__aaid=0&__spin_r=1010589214&__spin_b=trunk&__spin_t=1703622821&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22867105006641269%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22867105006641269%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; usida=eyJ2ZXIiOjEsImlkIjoiQXM1eXNwNnB1Z3dscCIsInRpbWUiOjE3MDMwNzYxNDB9; c_user=61554862379223; dpr=1.25; xs=7%3A0rjFgVujdHsjOQ%3A2%3A1703368401%3A-1%3A-1%3A%3AAcWFtyYB0eXrHXsyg9O7cV9qPM_IpgzGhhHza0N4UA; fr=1hrIVxtFFPVsD1ekP.AWXktr4c9aJwORPrAYk9Pl0_iMM.BlizdP.1c.AAA.0.0.BlizdP.AWX2T69UYYQ; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYSFoKOzsIPEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARay27rYDBYAABV-HEwAABYAFrLbutgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYIFuCW45YBEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%221%22%2C%22u%22%3A%222ba9qp%22%7D; wd=717x945; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703622826382%2C%22v%22%3A1%7D; c_user=100012100989894; fr=1R9M41gN6EiZttrxZ.AWV2sp7DscmtQatBLktn5LOG9nc.BlhqBz.dg.AAA.0.0.BlhqBz.AWVjz9LljRU; xs=14%3AEJgfKs9tJ5y-7w%3A2%3A1700227820%3A-1%3A8246%3A%3AAcUyYJOmHcFsqZFzMVrQGOfuB2M1voHyciiArtLgUt0',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/eeCAB/members',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.111", "Google Chrome";v="120.0.6099.111"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'viewport-width': '717',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
        'x-fb-lsd': 'qTQpzFrcpB4fsedseil4ik'
        }
        if i%500 == 0:
            print("sleeping for 20 secs")
            time.sleep(20)
        try:
            # data = []
            response = requests.request("POST", url, headers=headers, data=payload)
            data, cursor = read_payload(payload=response.json())  
        
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