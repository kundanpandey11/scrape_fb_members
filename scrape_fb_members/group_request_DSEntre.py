import requests
from read_payload import read_payload
import time 
from save_cursor import append_cursor_to_file
import csv


def save_data(
        cursor="AQHRK_8CZ_xEiWdUYspa_aLgipZe6L-64ay03j9JjCpnFvhov_bCj3RMU-TOAp7ij9Aue_ZO1RnAV2P65SdmQu4NGQ", 
        output_file="request_csv/DSEntrepreneurs.csv"
        ):
  
    for i in range(100000):
        url = "https://www.facebook.com/api/graphql/"

        payload = f'av=100011944262857&__user=100011944262857&__a=1&__req=u&__hs=19733.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010778471&__s=g9nq00%3Ar0wbne%3A2tvy87&__hsi=7322969989708376962&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFG14xt3odE98K361twYwJyE24wJwpUe8hwaG0Z82_CxS320om78bbwto886C11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61awkovwRwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe8sAwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1hxB0qo4e16wWwjHBU-4E&__csr=gea2YTsy4lRN4GNsYBihSLiR9bcB2nqi8hTfFiQmKyGyr4vsKOfHhepaAZfZeWpdnRaWhaK8LGQ494QtkQ8heuXm8xTCS8Ax534FRyWpVUKVrAyFaJqgHzF-dxe8DBl1ScyEgh9FFVHyp9k3K4Kfh8gx26U-cACyrGmm789ouVay89UK3y788k8xvxy2laEgUpwHxamidxuu221yx-UrDwlU8Gg2uK3u1vyUoWCw8Kbx22u2K0gW0mG3i0ZGwmKE2Ow3uE1d80Fy0vkE0KC48gw0kWU03MBg1nA0pO0w83vw3rE460P8-0h20AUeU0y-1dwbhG4A5e0oTw0jM81Fo0a3o1680dao6Kbo1KU&__comet_req=15&fb_dtsg=NAcNyD4k5CYKqyLsdfp4hgwIzWO5uWLocLCuQibUXhf-C9v-Na3BNGQ%3A17%3A1703863786&jazoest=25499&lsd=DQ6iSIReCXzBFz0SERe5Vy&__aaid=0&__spin_r=1010778471&__spin_b=trunk&__spin_t=1705011816&qpl_active_flow_ids=431626709&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22530944793683036%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22530944793683036%22%7D&server_timestamps=true&doc_id=6621621524622624'
        headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=zKtkZSyW7dPcVakLiZkL3tRb; datr=zKtkZTBkFK_CO0d80Z55MIl1; m_ls=%7B%22c%22%3A%7B%221%22%3A%22HCwAABYWFubfzZUKEwUWrsOmu_v-GwA%22%2C%222%22%3A%22GSwVQBxMAAAWARbSz-7YDBYAABV-HEwAABYAFtLP7tgMFgAAFigA%22%2C%2295%22%3A%22HCwAABYMFsKV_vgGEwUWrsOmu_v-GwA%22%7D%2C%22d%22%3A%228e2662a6-ff72-49f9-9e03-0d442a41c5a6%22%2C%22s%22%3A%220%22%2C%22u%22%3A%22i264iz%22%7D; c_user=100011944262857; usida=eyJ2ZXIiOjEsImlkIjoiQXM2bjMwdDE3ajJxeSIsInRpbWUiOjE3MDQyMDc2Mjl9; dpr=1; xs=17%3AYvfqa29jxTLFDw%3A2%3A1703863786%3A-1%3A8222%3A%3AAcW00L0bGMpfa_Z6h9S6iisIOlg1PSKzVznQXodr4Hc; fr=1J5TFa5s51lDwxnRc.AWUm7_zVjDzxXen5jAsk10KSOYo.BloGpr.1c.AAA.0.0.BloGpr.AWV0kJwSwuo; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1705011823389%2C%22v%22%3A1%7D; wd=808x945; c_user=100011944262857; fr=1VDsZMe2TT5NWWrfj.AWW2c09cf5VZ94Namgxvw-Ub40w.Blju4F.1c.AAA.0.0.Blju4F.AWVr9fWVCzg; xs=17%3AYvfqa29jxTLFDw%3A2%3A1703863786%3A-1%3A8222%3A%3AAcVi4TB8R78xsSAv2xoB9MYRpIna31fZXLxdGfVU5g',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/DSEntrepreneurs/members',
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
        'x-fb-lsd': 'DQ6iSIReCXzBFz0SERe5Vy'
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