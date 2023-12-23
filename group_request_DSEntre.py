import requests
from read_payload import read_payload
import csv


def save_data(
        cursor="AQHRaWuCUfiY2z-IfC3QrECiB3zEPAZWOhxjbJuchIvm6C_fPSKRrs7LUz6xK7w6YDSxrJsr8jVZozY9BKDdUHyUVw", 
        output_file="request_csv/DSEntrepreneurs.csv"
        ):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=61554862379223&__user=61554862379223&__a=1&__req=11&__hs=19711.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010538080&__s=r2zru7%3Aywrotc%3A4q3fbj&__hsi=7314783820907553994&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81t8gxO2OU7m221FwgolzUO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiE567Udo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W3y261eBx_wHwfCm2CVEbUGdG1Fwh888cA0z8c84q58jwTwNxe6Uak1xwJwxyo566k1FwgU4q3G1eKnzUiw&__csr=gaYjk9N5nddkRR9TTtlGyONYjtPFTJ9eGZPIBtL8F5vZddnmGGBWQqZ4illTQiuoyBhp9ay9bHTJqBKvlyGF29FVFAdhkdJrooBAy_CF5hDWALmquA-cBGm8xu9AyFQ2_Gl38KbByGwMxK9xmaAzUKRz8hAx2ax2bzEoyEeKuu5EFoS4bDwKxSu585G2y6obo4Wmu2W3W78dawQBUjwNx-261dws86q8K12wibwRxO2iQ0ia0y8iwp8qxWdw5ZG5qxCA260r60jC15w5Uw2hYE061i02Qe00M1A0scwnwjQ0eWwvE0idwUw8-1ew20E0J-0-oixe2m0hOE464A580BC02NB1a0s6010dw0M_o14Ulw9W06nE&__comet_req=15&fb_dtsg=NAcM8KDywStACw6qnWACP3RkJogOfy6_he0YTJ0bM-6vBP07fhwirvA%3A33%3A1703105753&jazoest=25409&lsd=LmKI_pZZlki1sIRBri1uM2&__aaid=0&__spin_r=1010538080&__spin_b=trunk&__spin_t=1703105825&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22530944793683036%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22530944793683036%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=AieAZYYbKj-C5LmWLWgooBV0; datr=AieAZar-XOg3s7Sc6dMQh7sS; locale=en_GB; c_user=61554862379223; xs=33%3A01cdaTVW9vBF8w%3A2%3A1703105753%3A-1%3A-1; fr=1IyTsjuo2NhxuEJP0.AWU5EUZjl7JtIT9eKWlXGt9n8tM.Blgz-q.2B.AAA.0.0.Blg1T_.AWUB_wxhS10; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703105828119%2C%22v%22%3A1%7D; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYOFrDh0aYCEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARaW1JrYDBYAABV-HEwAABYAFpbUmtgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYEFsqbju4MEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%2249b4dcfb-24b4-4409-8b03-d4a4491d5cb9%22%2C%22s%22%3A%221%22%2C%22u%22%3A%22ujqrz7%22%7D; wd=584x953',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/DSEntrepreneurs/members',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.110", "Google Chrome";v="120.0.6099.110"',
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
        'x-fb-lsd': 'LmKI_pZZlki1sIRBri1uM2'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data, cursor = read_payload(payload=response.json())  

        with open(output_file, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)
        print(output_file, i)



save_data()