import requests
from read_payload import read_payload
from utils.save_cursor import append_cursor_to_file
import csv
import time 


def save_data(cursor="AQHRSdIc-XrAb6t0-VBZRUx1JFHiSAVp6ru8WsgteoaW7hxzs7qHM-Pf9DaHrcXysRx0d3nSoouERwRM0GdHBOt68g", output_file="request_csv/eeCAB.csv"):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100011944262857&__user=100011944262857&__a=1&__req=y&__hs=19735.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=GOOD&__rev=1010817478&__s=206vfv%3Afvhew4%3A6f4ns7&__hsi=7323722670878523053&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320ni48swIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo4e16wWwjHBU-4E&__csr=ggMtE5sI9NcOZZQN4ZhJl7JlqkR_tmDuIz4l8L4ZiZnvFRrWARV9bCZ5Z_44OaFBFylO6LQjVfVHqnAz4uh5iCyaVp8KQdZAJ2G-HBJ2o-aCALyrWJ6zaG2OBhe9z8G9VEBppER5gjz4ha6UpK2le8Ve8xvyoK49Fe69agymUak3m6Ub8jzEW7rxa7EiVGCy8lyEO1ixm1iBxO5FoWQqi4UdE9UyF82fw9S5U6y6UgUgDwCw_w_w9-9wsU13u0ajzEnw6cw6bg1E80hLwbS1txDacw2EozG8w3kU28w0qIU0a0E02Nag3GwVw50w6Jg7a0dgw4jx61Dw6HwgQ1Xw4vw4se5o4O0Xu01fzwnE2yBg3qw0E1wno0eiE7Bweu3i&__comet_req=15&fb_dtsg=NAcNwJENqpxUfB-jJyr8X-wal2kSiZBmx1a3B04b6M0RGXTcsx0gHUA%3A26%3A1705152511&jazoest=25361&lsd=MVW78Wf8tXu5BeacYwXIeC&__aaid=0&__spin_r=1010817478&__spin_b=trunk&__spin_t=1705187063&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22867105006641269%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22867105006641269%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; usida=eyJ2ZXIiOjEsImlkIjoiQXM2bjMwdDE3ajJxeSIsInRpbWUiOjE3MDQyMDc2Mjl9; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYcFqKjj5sPEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARag-YzaDBYAABV-HEwAABYAFqD5jNoMFgAAFigA%22%2C%2295%22%3A%22HCwAABYQFtSYneENEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22r8235x%22%7D; c_user=100011944262857; xs=26%3APvIqnSXvlpQ65w%3A2%3A1705152511%3A-1%3A8222%3A%3AAcVCJ6eLC_IlgsrM7BBoVLDsG70lz_g0Ehc8GNOEeA; fr=17cELfEs0WTEKdRtX.AWXXK_nBNn3ZNrsEPiOBlrYJRUQ.BloxEK.1c.AAA.0.0.BloxZW.AWV0h3k0Kto; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1705187070328%2C%22v%22%3A1%7D; wd=808x945; c_user=100012100989894; fr=1J1Hp58sMwOkgERqo.AWX3DB3JqdTK_Da-hZ2lHFtZpDk.BlobMh.dH.AAA.0.0.BlobMh.AWXEyEWgsTU; xs=14%3AEJgfKs9tJ5y-7w%3A2%3A1700227820%3A-1%3A8246%3A%3AAcUIPLKDbNdmpq8-rjLK-wEQvUywB4dBjM07bEJWuKo',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/eeCAB/members',
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
        'x-fb-lsd': 'MVW78Wf8tXu5BeacYwXIeC'
        }

        if i%1000 == 0:
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