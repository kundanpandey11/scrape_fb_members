import requests
from read_payload import read_payload
import csv


def save_data(
      cursor="AQHR46l9wPK6whd3mR7jyywBXNoiYNc6fJFOPPkTJkzeaDQFFfNBT1FlAvIQBO_cUSKpYasG110ik04i3Agx8nJI8g", 
      output_file="request_csv/businessmartbd.csv"):
    for i in range(100000):
      url = "https://www.facebook.com/api/graphql/"
      payload = f'av=100082006418590&__user=100082006418590&__a=1&__req=r&__hs=19711.HYP%3Acomet_pkg.2.1..2.1&dpr=1&__ccg=EXCELLENT&__rev=1010534526&__s=4qd2i2%3Ah1psef%3Ac97ok2&__hsi=7314760237251056949&__dyn=7AzHK4HwkEng5K8G6EjBAo2nDwAxu13wFwnUW3q2ibwNw9G2Saw8i2S1DwUx60GE3Qwb-q7oc81xoswIK1Rwwwqo465o-cwfG1Rx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwuEjUlDw-wUwxwjFovUaU3VBwFKq2-azqwqo4i223908O3216xi4UdUcojxK2B0oobo8oC1Hg6C13whEeE4WVU-4E&__csr=gjhsYbjFPsojsjikD8D5cGdkmybdbnjkAAL9ATFqWtp4hjCCWlkGRSgPQEKjmKunWCiDK4BxSteVppTUOhecG9zpvgeaxSml2u8Gudgy-QEnCBAwKzEyfLxOE4Ci5ohVoixeUC6A5EcUkxO6orwnErwIxi0CUeFobUy1nK5o524FE5a78uzES9zojK0Bo2QwMwiUPwSx20BE3Jw2ME09_V806CXw0dHC09SxG0rsg0dVxa0b_w1il1S780Au0jm08qw15N6Dw6dw2Uo4N1a0xE08Do1ho0hqw0WqwJo1Eo09Oo&__comet_req=15&fb_dtsg=NAcP6GMNpxw9bQZwKQ5JFusTGsHmnmml9NnVj5s8yO7Er_DfYHZIxIA%3A46%3A1702897433&jazoest=25562&lsd=wjPhohgGt-D-3P-TF0tfQh&__aaid=0&__spin_r=1010534526&__spin_b=trunk&__spin_t=1703100334&__jssesw=1&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22194476664258288%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22194476664258288%22%7D&server_timestamps=true&doc_id=6621621524622624'
      headers = {
        'authority': 'www.facebook.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'sb=AieAZYYbKj-C5LmWLWgooBV0; datr=AieAZar-XOg3s7Sc6dMQh7sS; c_user=100082006418590; xs=46%3AFdW5wPuvCi9_Gg%3A2%3A1702897433%3A-1%3A10603%3A%3AAcX4Xs0XxMOBWuS3V3SGymtWb60VHv6yrY7N5q73eg; fr=1IyTsjuo2NhxuEJP0.AWUlfHbwJyFQ5nKdcgWtgn0739I.Blgz-q.2B.AAA.0.0.Blgz-q.AWUpVSaxti4; wd=584x953; presence=C%7B%22t3%22%3A%5B%5D%2C%22utc3%22%3A1703100338920%2C%22v%22%3A1%7D',
        'dpr': '1',
        'origin': 'https://www.facebook.com',
        'referer': 'https://www.facebook.com/groups/info.businessmartbd/members',
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
        'x-fb-lsd': 'wjPhohgGt-D-3P-TF0tfQh'
      }
      response = requests.request("POST", url, headers=headers, data=payload)
      data, cursor = read_payload(payload=response.json())  

      with open(output_file, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in data:
            csv_writer.writerow(row)
      print(output_file, i)
    # print(data,"\n", cursor)
    # return save_data(cursor=cursor, output_file=output_file)


save_data()
