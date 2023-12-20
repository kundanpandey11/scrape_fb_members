import requests

url = "https://www.facebook.com/api/graphql/"
cursor = "AQHRFlfJcuy2e10ZfOilHWWe5Hr8OwpYwTP5rYKBtdYKvA5c9sHmk_xCvSC3coQGSp7Z55qeo_FBjfIxbSWpfKF8Fg"

payload = f'av=100090722153729&__user=100090722153729&__a=1&__req=n&__hs=19711.HYP%3Acomet_pkg.2.1..2.1&dpr=2&__ccg=EXCELLENT&__rev=1010531557&__s=1vik3q%3A363zvm%3Afeli6o&__hsi=7314702692377695353&__dyn=7AzHxqU5a5Q1ryUbFp60BVU98nwgUao5ebzEdEc8co2qwJw8-0Boe8hw2nVEtwMw65xO2O1Vwwwqo465o-cwfG1Rx62G5Usw9m1YwBgK7o884y0Mo4G1hx-3m1mzXw8W58jwGzEaE5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3VBwJCwLyESE2KwwwOg2cwMwhEkxe3u364UrwFg662S269wqQ1FwgU4q3G1eKu2a&__csr=glMz2JjH4hsyEJQBPn4ZHLi4lmYRRkZnWtvhdlvOowxlil5SJQujYFGyswLBKLBVuilyXCiGm9ypbCyd5yprhbDzkicLCJ9xuFLAKcVXAyERe8DxaiaK59ohAF3FeUy2ai58XxefxyFUgDhp8sg9pUx0hEGi4oC4o46fwLwEwhUaEpzE9EcEbEdE8o88mxK0wEgwCxq6A1mgfE2cwbuUaEswFw9a7U0HG1Sg2XDK0ve079o05ji00-DQ0ry1LweK2e8w3bo1647o1JU0z20aPg0sI80va0_80bKo0aU80dN8960ly06No0niw2yU&__comet_req=15&fb_dtsg=NAcN8TBuHNNDolifjvMERtG6vo7GZtXSz0mk2Y3jL0f8f5S7zeVxbJQ%3A14%3A1700227820&jazoest=25455&lsd=C2UigEVQTEBkqYLERhfrIf&__aaid=0&__spin_r=1010531557&__spin_b=trunk&__spin_t=1703086936&fb_api_caller_class=RelayModern&fb_api_req_friendly_name=GroupsCometMembersPageNewMembersSectionRefetchQuery&variables=%7B%22count%22%3A10%2C%22cursor%22%3A%22{cursor}%22%2C%22groupID%22%3A%22128983774404488%22%2C%22recruitingGroupFilterNonCompliant%22%3Afalse%2C%22scale%22%3A1%2C%22id%22%3A%22128983774404488%22%7D&server_timestamps=true&doc_id=6621621524622624'
headers = {
  'authority': 'www.facebook.com',
  'accept': '*/*',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'content-type': 'application/x-www-form-urlencoded',
  'cookie': 'sb=6WpXZbglsfnNL824gw2KoQpR; datr=6WpXZfRAnwLIEAV81QcQdBTc; c_user=100012100989894; m_page_voice=100090722153729; i_user=100090722153729; cppo=1; dpr=2; locale=en_US; fbl_cs=AhBPDQ%2FjYt6bFmSPQjRxOxBKGFJEMTE0SFZmbTRSTWZTdXRONk1SNTFDYw; fbl_ci=3409969645914346; vpd=v1%3B858x560x2; fbl_st=100730005%3BT%3A28384781; wl_cbv=v2%3Bclient_version%3A2383%3Btimestamp%3A1703086913; xs=14%3AEJgfKs9tJ5y-7w%3A2%3A1700227820%3A-1%3A8246%3A%3AAcX5xHnRKkV6vBmO_rQC6ECtsVOEPViHSFE8sv8wShQ; fr=17fTYOWNex2St29t5.AWVC_GQOmbuuF-WtfpmHiKTIjeY.Blgwtb.dH.AAA.0.0.Blgwu1.AWX5gOyK9-s; wd=1920x945; c_user=100012100989894; fr=1JwCsmk6KwF6JfaGq.AWXj9X8hAlIInZzfgp8KBiGol0Q.BlgwyP.dH.AAA.0.0.BlgwyP.AWVM6_eH8aQ; xs=14%3AEJgfKs9tJ5y-7w%3A2%3A1700227820%3A-1%3A8246%3A%3AAcW6vWIQ3Qz6jcetrVid2z6KARUXjvxiO2mRxSH7BOM',
  'dpr': '2',
  'origin': 'https://www.facebook.com',
  'referer': 'https://www.facebook.com/groups/128983774404488/members/',
  'sec-ch-prefers-color-scheme': 'dark',
  'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
  'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.110", "Google Chrome";v="120.0.6099.110"',
  'sec-ch-ua-mobile': '?1',
  'sec-ch-ua-model': '"Nexus 5"',
  'sec-ch-ua-platform': '"Android"',
  'sec-ch-ua-platform-version': '"6.0"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
  'viewport-width': '560',
  'x-asbd-id': '129477',
  'x-fb-friendly-name': 'GroupsCometMembersPageNewMembersSectionRefetchQuery',
  'x-fb-lsd': 'C2UigEVQTEBkqYLERhfrIf'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
