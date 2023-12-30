import csv

def count_unique_profile_urls(csv_file_path):
    unique_profile_urls = set()

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            profile_url = row.get('Profile Url')
            if profile_url:
                unique_profile_urls.add(profile_url)
            # print("total rows : ", len(reader))

    return len(unique_profile_urls), unique_profile_urls

# Example usage:
eecab = 'csv/eeCAB(114000).csv'
csv_file_path = 'request_csv/businessmartbd.csv'
count, unique_urls = count_unique_profile_urls(eecab)

print(f'Total unique profile URLs: {count}')
print('Unique Profile URLs:')
# for url in unique_urls:
#     print(url)
