import json
import requests
import os
import zipfile
def get_paths():
    with open('personal_cache/maintainer_creds.txt') as file:
        lines = file.readlines()
        main_url = lines[2]
        addons_path = lines[3]
        return main_url, addons_path

def update_chad(url):
    chad_folder = os.getcwd()
    final_url = url.strip() + '/keeper/script_download'
    print('script url: ', final_url, 'chad folder: ', chad_folder)

    try:
        response = requests.get(final_url)
        response.raise_for_status()

        with open(os.path.join(chad_folder, "downloaded_script.zip"), "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(os.path.join(chad_folder, "downloaded_script.zip"), 'r') as zip_ref:
            zip_ref.extractall(chad_folder)

        os.remove(chad_folder + '/downloaded_script.zip')

        print(f"updated from script from site here: {chad_folder}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return print('done with script')

def update_addons(url, target_folder):
    final_url = url.strip() + '/keeper/addons_download'
    print('script url: ', final_url)

    try:
        response = requests.get(final_url)
        response.raise_for_status()

        with open(os.path.join(target_folder, "downloaded_addons.zip"), "wb") as f:
            f.write(response.content)

        with zipfile.ZipFile(os.path.join(target_folder, "downloaded_addons.zip"), 'r') as zip_ref:
            zip_ref.extractall(target_folder)

        os.remove(target_folder, 'downloaded_addons.zip')

        print(f"addons updated: {target_folder}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main_url, addons_path = get_paths()
    print(f'url: {main_url}addons_path: {addons_path}\ntype: addons (A),script (S) or both (B)')
    mode = input().lower()
    match mode:

        case 's':
            update_chad(main_url)
            print('updated chad')

        case 'a':
            update_addons(main_url, addons_path)
            print('updated addons')
        case 'b':
            update_addons(main_url, addons_path)
            update_chad(main_url)
            print('updated both')

        case _:
            print('idk watudu fuk ya')
