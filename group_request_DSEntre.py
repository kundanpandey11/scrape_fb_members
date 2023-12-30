import requests
from read_payload import read_payload
import time 
from save_cursor import append_cursor_to_file
import csv


def save_data(
        cursor="AQHRQraYzq7D45N9pDIf6aKqfvSQxUQ3c1CNTUfznrz4TerIalCa5NyI3vOEpdsKSCWDzU7f5ui8l_ycuEpWACdCaw", 
        output_file="request_csv/DSEntrepreneurs.csv"
        ):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100082006418590&__user=100082006418590&__a=1&__req=1u&__hs=19718.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010598376&__s=irar0w%3Aoc6gi1%3Assl8pr&__hsi=7317388620480996243&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320om78bbwto886C11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEdbwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo4e16wWwjHDzUiw&__csr=g9JY4AvTkRheZfp79T9PlkgzlNJPZRb5HvQBkDdJTcFdQGDjiq9h6SJAjhuGAhl-RimLXGFGCSFeARKExDyu9x2aiGvRBnh5XogGFkKkwyURpHBh4iElylAK9gVAzJ4zVpizHx7zXyUoxmozV8Km9wwhGyE8o-9y8ZouK69ByoybzoG5e6oycAUfo4G2a48621nxWewxwKWwxwSAxumEK4o7ufxa2ubDxm3G0wUbU9U-Fpo9EhG2x0nE2hw43yUf8f8C0Boa80Gi0acw0wjw6cw0oFU03tIU1dodQ0WE3Ew11G3Wbxa2q1xw2lYMfA0qa0quq01kswaVwqE0b580dqE14U3Jw1CG09vw2181J46E&__comet_req=15&fb_dtsg=NAcPd6L1tvRepesn2dyZGCcNvH2TJN-lmGh_8Toj5xErUSvaQQbzl8g%3A27%3A1703712300&jazoest=25610&lsd=TBaTnRQh-FCnOsTeiR4WcD&__aaid=0&__spin_r=1010598376&__spin_b=trunk&__spin_t=1703712302&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22530944793683036%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22530944793683036%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; usida=eyJ2ZXIiOjEsImlkIjoiQXM1eXNwNnB1Z3dscCIsInRpbWUiOjE3MDMwNzYxNDB9; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYSFoKOzsIPEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARay27rYDBYAABV-HEwAABYAFrLbutgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYIFuCW45YBEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%2227hfvj%22%7D; c_user=100082006418590; xs=27%3AhGilK86Qxn6qaQ%3A2%3A1703712300%3A-1%3A10603; fr=1okShaus4ToFlYzA0.AWWGoLnlRl999IOcVrVx6BazzyA.BljJX3.1c.AAA.0.0.BljJYu.AWVY9KI8F10; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703712307430%2C%22v%22%3A1%7D; wd=717x945; c_user=100012100989894; fr=1R9M41gN6EiZttrxZ.AWV2sp7DscmtQatBLktn5LOG9nc.BlhqBz.dg.AAA.0.0.BlhqBz.AWVjz9LljRU; xs=14%3AEJgfKs9tJ5y-7w%3A2%3A1700227820%3A-1%3A8246%3A%3AAcUyYJOmHcFsqZFzMVrQGOfuB2M1voHyciiArtLgUt0',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/DSEntrepreneurs/members',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.130", "Google Chrome";v="120.0.6099.130"',
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
        'x-fb-lsd': 'TBaTnRQh-FCnOsTeiR4WcD'
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