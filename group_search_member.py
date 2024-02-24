import requests
import time 
import csv
import json
from utils.read_payload import read_payload
from utils.save_cursor import append_cursor_to_file



# def save_data(cursor="AbovMXFTsHhyy3n3yPf8IgObijLdP11_tXOecjClFTloWyNMMKdOBFiF1kQ50DLdfsxWPMCYYrq1OB_CIBQhNCdZODYqXiKw7fCAHathhwkLqKz8Wf-GWzk4yJqXLkU6PLNlpeo_2M7je9bIQBvLODU5nytPEYYzHWEPkmY4UjF2wHfF7WFJJDTFwpZsBfnRm0hKiBoyXi1dsLFKhuqWBaHvjWn5nczFkb34ZbOby1x23XInmALr0YqhhWyxSn7gNXrTwwVibRffe2HStx0HU_6ENCW6GmeV3q7UEAwUvdLLJWR8FLAMFDhemx9WFg_pDcudH6OS9FpdgsvinYhE3cPfqX870Dxf1Bx6dnempx-G4q-u5dNbGEAN34QJKILShtWSQDXvgK0XgfOGjtbUWQdxwfIVShE46T81bdP9rAZYFhQNqVhm1EAoyVpTRQRQ_lnJ0eSim7pGy7hyzvbXUYEi_W1PIqmpzeTF3lTrNGE7Dto5Ivv40WxkRc-Tx-RBGNseuw9itN44W87dcNVgh76isGT92wVtLRSEMIwmv8vL08uaXm71PUtlo8uEpWIuzRZ8qjZyAVC2fYVMXkGb3cxXJyFfVT1S8OUMFJDcjeGaarLbCrQS0G7jqkh9KH9h0ZJEVeaTsposBFpQsEm9VEwqHsykVycp-eriCNyxjyYS-RJzOznElJBsOOYie5qTWxGgvg9oHJplTeThaBhuBmrhvVR6YAFlN6H0duW14FR3jKC2FpJC97AlSVPINEP4EYwFnpP4Aj9pfax1W3cA2Cl7g-2ZVyT45nNGFa6MuBQReFhT83GOAB4SD3olB9sKaHwcYu1btqivmrM3xCig7vjuS-SdZsAJOeYmLo515-WGNnGY7pCuvjf60JlsjTrLgFhW0tLV0ApRjU2v68fX5igtSLaP5IV715HooPpa_6n_FZ4ASFsdciTclq5rtWgqPStIB2yIXi-tC1ZL7XMncQCm0kBIhdKSzro5XoFNgMPiBqKydJWDgih695fg3kOTJTRNmBifO1VgIsMODYJfvQ4TwiOa4MCpWE6JaZBfhagiaa0nMD32y57z-amJU41xEWo4Gg_3uhB050sL-nfyg2O6q4cqF9dfYVAji6P0RB0pPQDXhe-KwlEfWqL89VnF2WV1SmoRzuuZm32VxERKTzcjMp22E4avPfBOo52LlrBuBaoJR5_Q5bdkvR0jU3HPTS6cfDJtBeY6UV8sOBpwd3YbWk0kDDRk7VCC3-g9uhKCqVH9ztzGYofM11VrUf7b0gClAcTjbN5KvW_crhCjhMvT25s2nbbThIw1YCeuixmGwCy0Kh1TDupkmGRaN6c_PYOSrLwh1SItMTEXyIY2_kw_hVhIe78_w01U00q9NrhGlQioyVG4fE1D-MLxqA_FyiYqIRGz3XS4UeiaTsNAt7fqjnMt84y0xW-9oEx8Oh-yOcrppI2Rya4AtGhyiFjWPJs6c2YOQp7Ji3mY1OZy8TrI0x1fSFYjFHx4487vfazfK7sxqxv4H_c2lnXH4oDbsWyxCAcrw4lZmSS80bRxCe03BARZEbToG-sQMBLEXOfYCA",
def save_data(cursor="null",          
              output_file="request_csv/wecomforum_search_starting_ad.csv", query="ab"):
    attempts = 0
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100092382603298&__user=100092382603298&__a=1&__req=11&__hs=19751.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1011081070&__s=oktoex%3Ass7twq%3A0ozqcs&__hsi=7329627409174591141&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwhUngS3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG12wOx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UK2K364UrwFg662S269wkopg6C13whEeE4WVufxa&__csr=gbO4Mjb5tYZ89EeJ8luNmBibN3N6Hq9RGhnTF8Bp5XFHF5qGWpbhdvGJcOXuKjGuZ7_GlbBAz5aqqaqhqmuECAlam4-fXmjyGVF99eUC8XDm9JWihnrytkV8O6rAK8yQaBCAzUqG9Ax2EW5VkaxybxmdgV3EK4pFUCudykfwYwAG9wHwopUSaG223a5Earg8E5p1eUbE47whU46qawk8aoaE4XxC2a2e8wzwIwpU4-10wfO0UEbU4W2-260j60j-04tE3xwiE0UC00zKo0c7E020JxO0fGwq81eU4swdodS0mx01P60fRw1420gLw10a0fOw64g27g023Lxa586e0iW0GE&__comet_req=15&fb_dtsg=NAcPEajgOlgr2wlum3Dh1VD4xYqQ5Q6SZJ2FPZYv5sGCA4ncOgTlcdQ%3A23%3A1706561715&jazoest=25439&lsd=uxhy-rfIBlTpmbq7PqOfZH&__aaid=0&__spin_r=1011081070&__spin_b=trunk&__spin_t=1706561867&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=useGroupsCometMemberSearchResultsRefetchQuery&variables=%7B%22count%22%3A20%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22140964279985142%22%2C%22query%22%3A%22{query}%22%2C%22scale%22%3A1%2C%22id%22%3A%22140964279985142%22%7D&server_timestamps=true&doc_id=7106655662730162'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'datr=FnneZH4QF8GVoC99zxyP-v3N; sb=HHneZBPXs7riQpnxPzb8jjso; ps_n=0; ps_l=0; c_user=100092382603298; xs=23%3A4aXV1WEukl1rMg%3A2%3A1706561715%3A-1%3A-1; fr=1nToUMkq3QlLQErPd.AWV7du8P2p1cYLpyIpzEidmr5B4.BluBAf.Jt.AAA.0.0.BluBDd.AWV6QaIEJFI; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1706561871370%2C%22v%22%3A1%7D; wd=1149x945; c_user=100011944262857; fr=1fFuiS0RT5yn6KwFJ.AWXOeJOpkSo6pYKpS4P-WuaX6xM.BltqP8.1c.AAA.0.0.BltqP8.AWURw2JN2uk; xs=47%3Av229aH3rT1tzXQ%3A2%3A1705412428%3A-1%3A8246%3A%3AAcVoHoZHOeuCfRN98xSQe4sr2jG_k3o7oksKh7qhSA',
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
        'viewport-width': '1149',
        'x-asbd-id': '129477',
        'x-fb-friendly-name': 'useGroupsCometMemberSearchResultsRefetchQuery',
        'x-fb-lsd': 'uxhy-rfIBlTpmbq7PqOfZH'
        }
        if i%500 == 0:
                print("sleeping for 5 secs")
                time.sleep(5)
        try:
            # data = []
            response = requests.request("POST", url, headers=headers, data=payload)
            data, cursor, has_next_page = read_payload(payload=response.json(), payload_type="search_results")  

            with open(output_file, 'a', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                for row in data:
                    csv_writer.writerow(row)
            
            print(i, output_file, has_next_page)
            attempts = 0
            if has_next_page == False:
                break
        except Exception as e:
            print("error \n\n\n")
            print(response.json())
            print("\\n")
            print(payload)
            attempts += 1
            append_cursor_to_file(cursor=cursor, group_name="wecomforum")
            print(e)
        if attempts == 3:
            print("three failed attempts")
            break
        if attempts == 1:
            time.sleep(200)
            print("slept for 100 seconds")



# save_data()




if __name__ == "__main__":
    with open("alphabet.json", "r", encoding="utf-8") as query_file:
        queries = json.loads(query_file.read())
        for query in queries[3:]:
            q = query['value']
            ind = query['index']
            print(q,ind)
            save_data(query=q)