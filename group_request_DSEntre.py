import requests
from read_payload import read_payload
import time 
from save_cursor import append_cursor_to_file
import csv


def save_data(
        cursor="AQHRqBvueHxb3XUSGD0fvZYfZlx3T_XXLltDV2W65FKMEuJFQlnWZj-I1aHJhUbIZ7_GBwmDQ8SURkgnXezM0rbj-A", 
        output_file="request_csv/DSEntrepreneurs.csv"
        ):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100082006418590&__user=100082006418590&__a=1&__req=3o&__hs=19715.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010581623&__s=tq7ch1%3Am1vdvc%3Af7j4gz&__hsi=7316048379888715240&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81t8gxO2OU7m221FwgolzUO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W3iU8o4Wm7-2K0-poarCwLyESE6C14wwwOg2cwMwhEkxe3u364UrwFg662S269wkopg6C13whEeE4WVU-4E&__csr=gfsWT4FNcYIiDMDNr4NkD9FuDtlT999T9dMwQArCiHQGA9hTmjaOal4riiWnXhbLAWhlGFGTGGhuq4Gl34aKl9fyFAYF9vKbWXhHyCFOeWQrBgDQmuQF98WaWKFWHgkiy98tGiHG4EG8GnxmEJXyQZ289VazeUgBx2Z298ggaK6KA6WBCxum4ub-4E4HxC1Bho4i5o4e8U8EpAy-8yo4y3G5UiUgwspohw8K4UfEdFEy5E946ofbwRx6Ulwh8W36q3GU6-0iS10y80P-0i3w6bCz41elK3i0RE1IU4a0QEO3q0cGw0gBE0az803sNg1rES0r60cUwaIM3wxC5o0SS0bGU05sK02DO03uC1cwIo1PU0lHw17W04R8&__comet_req=15&fb_dtsg=NAcMeQasYVZrQ5_AyMa3F8jK33-qO2pIwXfoWfMAYRlLX0VJNu1IgZw%3A46%3A1703400250&jazoest=25368&lsd=OlnTxPSrj4Vdalp0e3Po70&__aaid=0&__spin_r=1010581623&__spin_b=trunk&__spin_t=1703400253&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22530944793683036%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22530944793683036%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=AieAZYYbKj-C5LmWLWgooBV0; datr=AieAZar-XOg3s7Sc6dMQh7sS; locale=en_GB; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYOFrDh0aYCEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARaW1JrYDBYAABV-HEwAABYAFpbUmtgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYEFsqbju4MEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%2249b4dcfb-24b4-4409-8b03-d4a4491d5cb9%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22rxxyij%22%7D; c_user=100082006418590; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703400547918%2C%22v%22%3A1%7D; xs=46%3ADuTpS1d6V0_dHQ%3A2%3A1703400250%3A-1%3A10603%3A%3AAcXjRwCig8qQDD4rYabWUz2MR_bR0vpr79qPliXDzw; fr=1JcGFrGuaKEod8s8r.AWUJBz04OaXEO_QPtM7szy-iD14.Blh_Di.2B.AAA.0.0.Blh_Di.AWXZiExY8I8; wd=584x953',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/DSEntrepreneurs/members',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.129", "Google Chrome";v="120.0.6099.129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'viewport-width': '584',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
        'x-fb-lsd': 'OlnTxPSrj4Vdalp0e3Po70'
        }

        if i%500 == 0:
            print("sleeping for 20 secs")
            time.sleep(25)
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
            append_cursor_to_file(cursor=cursor, group_name="DSEtreprenuer")
            print(e)
        if attempts == 1:
            time.sleep(200)
            print("failed once so sleeping for 200 secs")
        if attempts == 3:
            print("three failed attempts")
            break



save_data()