import requests
import subprocess
import os

def check_for_updates():
    repo_owner = 'YourGitHubUsername'
    repo_name = 'YourRepoName'
    current_version = '0.1'  # Replace with your app's current version

    response = requests.get(f'https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest')
    if response.status_code == 200:
        latest_version = response.json()['tag_name']
        if latest_version != current_version:
            print("A new version is available. Updating...")
            download_url = response.json()['assets'][0]['browser_download_url']  # Replace with your asset URL
            download_and_update(download_url)
        else:
            print("You have the latest version.")

def download_and_update(download_url):
    updated_app_path = 'updated_app.exe'  # Replace with your app's file name
    with open(updated_app_path, 'wb') as file:
        response = requests.get(download_url)
        file.write(response.content)

    current_app_path = 'your_script.exe'  # Replace with your current app's file name
    os.replace(updated_app_path, current_app_path)

    print("Update successful. Please restart the application.")

check_for_updates()
