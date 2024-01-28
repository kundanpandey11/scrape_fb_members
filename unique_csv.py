import csv


def extract_and_save_unique_profiles(input_csv_file, output_csv_file):
    unique_profiles = set()

    # Read the input CSV file and extract unique profile URLs
    with open(input_csv_file, 'r', newline='', encoding='utf-8') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)  # Read the header
        url_index = header.index('Profile URL') if 'Profile URL' in header else -1

        if url_index != -1:
            for row in reader:
                if len(row) > url_index:
                    profile_url = row[url_index]
                    unique_profiles.add(profile_url)

    # Write unique rows to a new CSV file
    with open(output_csv_file, 'w', newline='', encoding='utf-8') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)  # Write header
        
        total = len(unique_profiles)
        count = 0

        # Read the input CSV file again to get matching rows
        with open(input_csv_file, 'r', newline='', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            next(reader)  # Skip the header

            for row in reader:
                count += 1
                profile_url = row[url_index] if len(row) > url_index else None
                if profile_url in unique_profiles:
                    writer.writerow(row)
                    unique_profiles.remove(profile_url)
                    print(f"{count} / {total}")

    print(f"Unique rows based on Profile URLs saved to {output_csv_file}")



def count_unique_profile_urls(csv_file_path):
    unique_profile_urls = set()

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            profile_url = row.get('Profile URL')
            if profile_url:
                unique_profile_urls.add(profile_url)
            # print("total rows : ", len(reader))
    print(f"{csv_file_path} : {len(unique_profile_urls)}")
    return len(unique_profile_urls), unique_profile_urls


if __name__ == "__main__":
    
    # Example usage:
    eecab = 'final_csv/eeCAB.csv'
    wecom = "final_csv/wecomforum.csv"
    dse =  "final_csv/DSEntrepreneurs.csv"
    csv_file_path = 'request_csv/businessmartbd.csv'
    count, unique_urls = count_unique_profile_urls(eecab)
    count, unique_urls = count_unique_profile_urls(wecom)
    count, unique_urls = count_unique_profile_urls(dse)
    

    # print(f'Total unique profile URLs: {count}')
    # print('Unique Profile URLs:')
    # for url in unique_urls:
    #     print(url)
    # extract_and_save_unique_profiles(input_csv_file="csv/eeCAB(8120).csv", output_csv_file="final_csv/eeCAB.csv")

