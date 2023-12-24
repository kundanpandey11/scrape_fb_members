import requests
from read_payload import read_payload
import csv
import time 
from save_cursor import append_cursor_to_file


def save_data(cursor="AQHRX3QbqXPS9avMkron7BehZOhtaQJZzoHvo73kB_K6Oqt2jMyrtuKxP1GNBPFkSN_rN1HtSPgfXz50Cfpon8yaew", output_file="request_csv/wecomforum.csv"):
    attempts = 0
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=61554793140471&__user=61554793140471&__a=1&__req=14&__hs=19714.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010580661&__s=rb29kv%3Ao1m8x5%3Adcel3i&__hsi=7315916029288159436&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo4e16wWwjHBU-4E&__csr=gcdR2kWT4FNdOT4Fb4EhPSNcjbF9kWuRkLkADqsT694F6VuFdb8yktGraDGl6J9ahfKmXVe9haytWyRCxqF8yaKhKFoVfFe8XzpbhHyF8xK4figCUWiECeUGFkaQGzeWy-22i9xS8GnxybVoKgwc9UW2_yomwGxPG7aybxq6ELUiwiK5Gxe1rzorxu5oe8GawyxW5EC18wxwg-2i1zCyEa86a8w821cwMwFwRAz85W0wE5u2C0h-10w7Iw5rw4wU0yS0rCu0O84a0QEO3q0q-3G_w09BK00Jck0mWdw6Nw3e8fU1kopxm0nu0mq0zE1FolO1e0hnw0j2U0H-02DO03uC1cwIo1PU0lHw&__comet_req=15&fb_dtsg=NAcOZ5Wsv_9Xr2mSs8URciU8gTGOct2Vm260C3ZAlGKO4PBhiNa3UwA%3A2%3A1703143491&jazoest=25199&lsd=5dg4kTyVdL8ZIxe3UDuGpb&__aaid=0&__spin_r=1010580661&__spin_b=trunk&__spin_t=1703369438&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22140964279985142%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22140964279985142%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=AieAZYYbKj-C5LmWLWgooBV0; datr=AieAZar-XOg3s7Sc6dMQh7sS; locale=en_GB; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYOFrDh0aYCEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARaW1JrYDBYAABV-HEwAABYAFpbUmtgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYEFsqbju4MEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%2249b4dcfb-24b4-4409-8b03-d4a4491d5cb9%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22rxxyij%22%7D; c_user=61554793140471; xs=2%3AYOAx5n1aXuEjVA%3A2%3A1703143491%3A-1%3A8313%3A%3AAcU7dJJgVPxcd0MEIaOtZAVbXu1i0G_ESxAYxJaqfw; fr=1QnwXbCHztgx1xWnT.AWVWgFUHs8rfbnsFSHioqmic_Lk.Blh1kl.2B.AAA.0.0.Blh1kl.AWW05WJOJiQ; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703369440561%2C%22v%22%3A1%7D; wd=584x953',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/wecomforum/members',
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
        'x-fb-lsd': '5dg4kTyVdL8ZIxe3UDuGpb'
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



save_data()
