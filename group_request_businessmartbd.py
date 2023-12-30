import requests
from read_payload import read_payload
import csv
import time 
from save_cursor import append_cursor_to_file


def save_data(
      cursor="AQHRjRJBwNmuuYQftNesjeaxcT7kKPDcW_SF0JXZJMtOTMvTDqftmewrAm6CBIBQ7Iw1Kh98oV46srVAXkVLtYSBIQ", 
      output_file="request_csv/businessmartbd.csv"):
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100011944262857&__user=100011944262857&__a=1&__req=t&__hs=19720.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=GOOD&__rev=1010611268&__s=ytl1cb%3Anvbnl7%3Agn2lgm&__hsi=7318120361550295563&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwnUW3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG1Rx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwuEjUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1Hg6C13whEeE4WVU-4E&__csr=gX3sl3WkkG4PkJZdRkaQkI88ynaOYBRluB8zaGaOfH99inAvuPG-_AXJ2HjAhp4mVpvmupauF8W8-UWQ98A4rGEydxeuFp8O68Z3eax6vBy8oUmzV8vAyoF6y9oScwhopG2a17xq6oC2C3l4zUcU42dDw9W78d9o9E-16Dx678C0y822yo5B0qQ0M8S3e1awvUe8cob82pw15G00nf10be0Bo1044U0Q63W0G889UOu0r609mwAw2F-01hPwdep1202OK03ta2Fw5iw1Iu&__comet_req=15&fb_dtsg=NAcPZlItZumbqND9KwnFdSeLPd5ZXZWKfXx59LPXfEQ0Mw2nHSbia9w%3A17%3A1703863786&jazoest=25536&lsd=DDCyKRJ1OipA5Sd-z4oGLk&__aaid=0&__spin_r=1010611268&__spin_b=trunk&__spin_t=1703882674&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22194476664258288%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22194476664258288%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; usida=eyJ2ZXIiOjEsImlkIjoiQXM1eXNwNnB1Z3dscCIsInRpbWUiOjE3MDMwNzYxNDB9; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYWFubfzZUKEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARbSz-7YDBYAABV-HEwAABYAFtLP7tgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYMFsKV_vgGEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22i264iz%22%7D; dpr=1.25; c_user=100011944262857; xs=17%3AYvfqa29jxTLFDw%3A2%3A1703863786%3A-1%3A8222%3A%3AAcXBw7dL831xksOQvI_fgEeEKXa5WoLybS256nm4yg; fr=1AxwQDuw6Ih0lkGaQ.AWW2Ud2BxjSM5o4VNUU0s6qV-Zc.Bljy76.1c.AAA.0.0.Bljy76.AWXQEzIGvyE; wd=972x945; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703882679256%2C%22v%22%3A1%7D; c_user=100011944262857; fr=1VDsZMe2TT5NWWrfj.AWW2c09cf5VZ94Namgxvw-Ub40w.Blju4F.1c.AAA.0.0.Blju4F.AWVr9fWVCzg; xs=17%3AYvfqa29jxTLFDw%3A2%3A1703863786%3A-1%3A8222%3A%3AAcVi4TB8R78xsSAv2xoB9MYRpIna31fZXLxdGfVU5g',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/info.businessmartbd/members',
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
        'viewport-width': '972',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
        'x-fb-lsd': 'DDCyKRJ1OipA5Sd-z4oGLk'
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
