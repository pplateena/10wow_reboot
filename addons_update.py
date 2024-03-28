import requests
import zipfile
import os


def getcreds():
    with open('personal_cache/maintainer_creds.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

    creds = lines[2].strip(), lines[3].strip()
    return creds

def download_and_extract_zip(url, target_folder):
    try:
        response = requests.get(url)
        response.raise_for_status()

        with open(os.path.join(target_folder, "downloaded.zip"), "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(os.path.join(target_folder, "downloaded.zip"), 'r') as zip_ref:
            zip_ref.extractall(target_folder)

        print(f"Zip file downloaded and extracted to: {target_folder}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


creds = getcreds()

download_url = creds[0] + "/keeper/addons_download"
target_dir = creds[1]

# download_and_extract_zip(download_url, target_dir)