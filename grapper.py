import requests
import csv
import json
import os
import traceback

def fetch_security_txt(url):
    try:
        # Ensure the URL ends with a forward slash
        if not url.endswith('/'):
            url += '/'

        # Fetch the security.txt file
        security_url = url + '.well-known/security.txt'
        response = requests.get(security_url)

        # Check if the request was successful
        if response.status_code == 200:
            print(f"Security.txt found for {url}")
            return response.text
        else:
            print(f"Security.txt not found for {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred while fetching security.txt for {url}: {e}")
        print(traceback.format_exc())
        return None

def read_urls_from_csv(file_path):
    results = {}
    try:
        with open(file_path, mode='r', newline='') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                url = row['url']
                security_txt = fetch_security_txt(url)
                if security_txt:
                    results[url] = security_txt
    except OSError as e:
        print(f"OSError: {e.strerror} (Errno {e.errno})")
        print(f"File descriptor: {file.fileno()}")
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        print(traceback.format_exc())
    return results

def write_results_to_json(results, output_file):
    try:
        with open(output_file, mode='w') as file:
            json.dump(results, file, indent=4)
        print(f"Results written to {output_file}")
    except Exception as e:
        print(f"An error occurred while writing to the JSON file: {e}")
        print(traceback.format_exc())

if __name__ == "__main__":
    # Replace with the absolute path to your CSV file
    urls_csv_path = os.path.abspath("urls.csv")
    output_json_path = os.path.abspath("security_results.json")

    # Read URLs from CSV and fetch security.txt contents
    security_results = read_urls_from_csv(urls_csv_path)

    # Write the results to a JSON file
    write_results_to_json(security_results, output_json_path)
