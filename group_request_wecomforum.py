import requests
from read_payload import read_payload
import csv
import time 
from save_cursor import append_cursor_to_file


def save_data(cursor="AQHRKQ19UKie7wIXr2gT5bvuV_3KPdnOnpyllkzu2ltGmvI0iBGje1v42WHOSZILCcVgoY3Y0EYg1PRJuBDDCtViRw",
              output_file="request_csv/wecomforum.csv"):
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100082006418590&__user=100082006418590&__a=1&__req=2h&__hs=19734.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010801113&__s=mua66j%3Agtj22m%3A0xtmzz&__hsi=7323312981916039201&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320ni48swIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo4e16wWwjHDzUiw&__csr=gmOgx3kj1dkL4N4ALsgBOijaBblh5nb9aIABdiEZRcBbkhdHlEIYyREVtEy9aLpaQVlX-J8zmGJeWjZLAAJkWZ4jVoJvAXjXJ2A_yGF99qKicmAnJ5humeleK_BBGaHEwjQGKQcgS9yGgKu9yooKiHhempy9eGJa78DCih8ybLzFUK8Dx6i6opAzE8kEOimEnghzVH-bwExx2EgwgomizEO3m68aErwxDzUnyod8C6F8C4p4fxW4azU9p8sx23K2W2O3a5EfU7d0vESVEdqgfEhwBwwwg-3q5ob8cU0jYDwn62i1KwqA0aDwbeckw9o0LSU5u7bw2MpE30J0pUyU1K808AU04oi00Rz40gV05EwKw7Xw3fo462u2Ceo7C6E7-0c0w2M8C01qfw0BpwmU0dDU6G0Im0h-02wu&__comet_req=15&fb_dtsg=NAcPz-tLLV2rnyIPrm0kV7UR9gUbQ_wfbbJtEpC4739wOQIAUC2MWeg%3A1%3A1705091673&jazoest=25337&lsd=LTE-BOIgGQBt9ETj_nyByz&__aaid=0&__spin_r=1010801113&__spin_b=trunk&__spin_t=1705091675&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22140964279985142%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22140964279985142%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; usida=eyJ2ZXIiOjEsImlkIjoiQXM2bjMwdDE3ajJxeSIsInRpbWUiOjE3MDQyMDc2Mjl9; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYcFqKjj5sPEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARag-YzaDBYAABV-HEwAABYAFqD5jNoMFgAAFigA%22%2C%2295%22%3A%22HCwAABYQFtSYneENEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22r8235x%22%7D; c_user=100082006418590; xs=1%3AZ0ATrh1ECeqavg%3A2%3A1705091673%3A-1%3A10603; fr=1hGYsIhHXpYLs3pQx.AWX-OwtyGV1Fmh9VMRTBp-sweUE.BloZ3p.1c.AAA.0.0.BloaJb.AWUDiYSIjTA; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1705091679191%2C%22v%22%3A1%7D; wd=808x945; c_user=100011944262857; fr=1VDsZMe2TT5NWWrfj.AWW2c09cf5VZ94Namgxvw-Ub40w.Blju4F.1c.AAA.0.0.Blju4F.AWVr9fWVCzg; xs=17%3AYvfqa29jxTLFDw%3A2%3A1703863786%3A-1%3A8222%3A%3AAcVi4TB8R78xsSAv2xoB9MYRpIna31fZXLxdGfVU5g',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/wecomforum/members',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.217", "Google Chrome";v="120.0.6099.217"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'viewport-width': '808',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
        'x-fb-lsd': 'LTE-BOIgGQBt9ETj_nyByz'
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
