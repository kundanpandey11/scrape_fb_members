import requests
from read_payload import read_payload
import csv
import time 
from save_cursor import append_cursor_to_file


def save_data(cursor="AQHRJy77sIV6daeq0CdshYfV9pzIQVESvxVVU7kHE_6ya_4QxIY6Ce0bydctwr_XNkjQg9KRBplbAbhiXfb404uYZw",
              output_file="request_csv/wecomforum.csv"):
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100011944262857&__user=100011944262857&__a=1&__req=1p&__hs=19750.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=GOOD&__rev=1011069304&__s=5wd7ig%3A6jpzps%3Aidjhcb&__hsi=7329063036388484732&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUKbgS3q2ibwNw9G2Saw8i2S1DwUx60GE5O0BU2_CxS320ni48swIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UK2K364UrwFg662S269wkopg6C13whEeE4WVufxa&__csr=gaAaNqrkILOv5hROthlYIRndOdrNlNLmDOJT8DeLmiBOcZ9bRaF8HGZaJtqmHZbmDWLhzvQl2khmHm-i8GijhCiH-nVqzy39ryyAABy49CZvhGDlknDhV4hym9nVboCm9wwybqLpujh8W32cyV8ixmEtyqCxp122aF8Sexa2nz8mgKqrV84CaG5umEao8qwZwwBwlEeE_CwDwiUpwl8coixa321twKx22C4o2yxe14xy5EfU7S14w4Rw8-1EwXwIw2jo2Exy0-E36Bl2E0Dy0oOi8gC0mG03a602mO00Xl2S0_FU5l0pE1Y40dJw4Dway0m20yk1Gwf60bTx60ga9w0i680Fq01tZwUwiS0hC2u&__comet_req=15&fb_dtsg=NAcPbyOKLSQ_MjyM8ZIzoxMqRo2Z3Qqaa2vWIiisAy7l5wg8nR-LUBQ%3A47%3A1705412428&jazoest=25560&lsd=ufupMP7WF5PXbvLflAbZcW&__aaid=0&__spin_r=1011069304&__spin_b=trunk&__spin_t=1706430464&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22140964279985142%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22140964279985142%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYcFqKjj5sPEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARag-YzaDBYAABV-HEwAABYAFqD5jNoMFgAAFigA%22%2C%2295%22%3A%22HCwAABYQFtSYneENEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22r8235x%22%7D; c_user=100011944262857; usida=eyJ2ZXIiOjEsImlkIjoiQXM3eDZxZmY5ZmR4dCIsInRpbWUiOjE3MDYzNjAxNjN9; xs=47%3Av229aH3rT1tzXQ%3A2%3A1705412428%3A-1%3A8246%3A%3AAcVe_o52BVMrLtTdTQGPgv294EGqDw_3sSQ3D4Z2Tw; fr=1GclZFG0QxE84TQYX.AWXYxD5eB159-izA2qBdxFccE9Y.BltgiD.1c.AAA.0.0.BltgiD.AWU7upYb6fg; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1706430469361%2C%22v%22%3A1%7D; wd=808x945; c_user=100012100989894; fr=1J1Hp58sMwOkgERqo.AWX3DB3JqdTK_Da-hZ2lHFtZpDk.BlobMh.dH.AAA.0.0.BlobMh.AWXEyEWgsTU; xs=14%3AEJgfKs9tJ5y-7w%3A2%3A1700227820%3A-1%3A8246%3A%3AAcUIPLKDbNdmpq8-rjLK-wEQvUywB4dBjM07bEJWuKo',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/wecomforum/members',
        'sec-ch-prefers-color-scheme': 'dark',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.227", "Google Chrome";v="120.0.6099.227"',
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
        'x-fb-lsd': 'ufupMP7WF5PXbvLflAbZcW'
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
