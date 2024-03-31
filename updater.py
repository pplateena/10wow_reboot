import requests
import zipfile
import os

def get_local_version():
    with open('personal_cache/credentials.txt', 'r') as file:
        lines = file.readlines()

    creds = lines[0].strip(), lines[1].strip()
    lv_script, lv_addons = int(lines[2].strip()), int(lines[3].strip())

    with open('personal_cache/maintainer_creds.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

    creds = lines[2].strip(), lines[3].strip()

    return lines, lv_script, lv_addons

def get_actual_version():
    # Replace 'http://localhost:5000' with the actual URL of your Flask application
    base_url = 'http://172.23.0.153:5000/keeper'

    try:
        # Make a POST request to the /keeper endpoint
        response = requests.post(base_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            av_script = data.get('script_version')
            addons_version = data.get('addons_version')
            return av_script, addons_version
        else:
            print(f'Error: {response.status_code} - {response.text}')
    except requests.RequestException as e:
        print(f'Request error: {e}')


def download_script():

    download_url = f'{base_url}/keeper/script_download'

    try:
        # Make a GET request to the script_download endpoint
        response = requests.get(download_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Save the received content to a local file
            with open('10wow_reboot.zip', 'wb') as f:
                f.write(response.content)
            print('File downloaded successfully.')
        else:
            print(f'Error: {response.status_code} - {response.text}')
    except requests.RequestException as e:
        print(f'Request error: {e}')

def extract_zip(zip_file_path, extract_path='.'):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_path)
    os.remove(zip_file_path)


if __name__ == '__main__':

    lines, lv_script, lv_addons = get_local_version()
    av_script, av_addons = get_actual_version()

    print(f"local: {lv_script, lv_addons} \nactual: {av_script, av_addons}")
    if av_script != lv_script:
        print('need to upadte')
        download_script()
        extract_zip(zip_file_path = '10wow_reboot.zip')
        lines[2] = str(av_script) + '\n'
        print(lines)
        with open('personal_cache/credentials.txt', 'w') as file:
            for line in lines:
                file.write(line)
        print('finished')


    else:
        print('no need in upd')      


    # download_script()
    # extract_zip(zip_file_path = '10wow_reboot.zip')
