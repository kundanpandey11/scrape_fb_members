import requests
from read_payload import read_payload
import csv


def save_data(cursor="AQHRx7iCOemhgNNZIYX9wChUEs-343pN0iRN2bCk514IF-VKZXJEs_xHBhAeqGDMHQWKw4fOqUfwEpoP1P8AG6s79Q", output_file="request_csv/wecomforum.csv"):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=61554793140471&__user=61554793140471&__a=1&__req=r&__hs=19712.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010553507&__s=jkctep%3A689tum%3A6tfn4v&__hsi=7314944135654057070&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwnUW3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG1Rx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwuEjUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1Hg6C13whEeE4WVU-4E&__csr=gF7hcI4ajk9sZPlllR95Wd9b98zilRRcGOiiW9lp94yK88gLy5Vd8lipSZ6gyiQvVahaCBLF4K9zqGXxajAD-QScGi22V8hBxSGzFUKmmi6pEF6HCAAxR1K3y49oJ1Cbx63q2OEiz88UpwMwgUgg5G4orwpoeEcobo5SqewZwkEox26U4R0Bxy2q14wdq1SwAAwpk681y80vHwvE0_-00l0x0dW0vm1mgiw2XXw5dxW58gw2U83ww2uK01krBg32xq02BC03re0RC0le05tU&__comet_req=15&fb_dtsg=NAcO6HDq7_vXs9OZ03FVgp2g96qPqeoJ_dnC4v-vxCCYWOWpVQ_W9hA%3A36%3A1703143059&jazoest=25373&lsd=WGKqMCyp8LgLfWTFIdvhmh&__aaid=0&__spin_r=1010553507&__spin_b=trunk&__spin_t=1703143151&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22140964279985142%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22140964279985142%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=AieAZYYbKj-C5LmWLWgooBV0; datr=AieAZar-XOg3s7Sc6dMQh7sS; locale=en_GB; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYOFrDh0aYCEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARaW1JrYDBYAABV-HEwAABYAFpbUmtgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYEFsqbju4MEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%2249b4dcfb-24b4-4409-8b03-d4a4491d5cb9%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22rxxyij%22%7D; c_user=61554793140471; xs=36%3ACKm7yGPSXRXb6A%3A2%3A1703143059%3A-1%3A-1; fr=1fxlUgWk8ABxOG2pC.AWVmNTnITDy7q8OEUoR0BE70eJY.Blg-Yo.2B.AAA.0.0.Blg-aY.AWXVpj-_MUE; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703143156436%2C%22v%22%3A1%7D; wd=584x953',
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
        'x-fb-lsd': 'WGKqMCyp8LgLfWTFIdvhmh'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        data, cursor = read_payload(payload=response.json())  
        with open(output_file, 'a', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            for row in data:
                csv_writer.writerow(row)
        print(i)
    # print(data,"\n", cursor)
    # return save_data(cursor=cursor, output_file=output_file)


save_data()
