import os
import shutil
import requests
from zipfile import ZipFile

# Adding a default to avoid problems non-english characters (like 'ñ' or 'ç')
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Variables to use
repo_owner = "Ludeon"
official_repo = "RimWorld-SpanishLatin"
branch = "master"

# Function declarations

def download_github_repo(owner, repo, branch="master"):
    """
    Download the GitHub repository specified as a zip file and extract it.
    """
    try:
        # Create the download link for the repo using GitHub's REST API
        repo_url = f"https://api.github.com/repos/{owner}/{repo}/zipball/{branch}"

        # Download the repo
        r = requests.get(repo_url)
        with open(f"{owner}-{repo}-{branch}.zip", "wb") as zip_file:
            zip_file.write(r.content)

        # Extract the zip file
        with ZipFile(f"{owner}-{repo}-{branch}.zip", "r") as zip_ref:
            zip_ref.extractall()

        os.remove(f"{owner}-{repo}-{branch}.zip")

    except requests.RequestException as e:
        print(f"Error al descargar el repositorio de GitHub: {e}")
        exit(1)


def update_content(local_repo, name):
    """
    Update the translations of the specified official content.
    """
    try:
        # Create the path to that Content's languages folder
        translations_folder = os.path.join(".", "Data", name, "Languages")

        if not os.path.exists(translations_folder):
            return

        # Find the translation directory name specifically for SpanishLatin
        translation_dir = next(filter(lambda x: x.startswith("SpanishLatin"), os.listdir(os.path.join(".", local_repo, name))), None)

        if translation_dir is None:
            return

        # Remove old translation files
        tar_file = os.path.join(translations_folder, f"{translation_dir}.tar")
        if os.path.exists(tar_file):
            os.remove(tar_file)

        translation_dir_path = os.path.join(translations_folder, translation_dir)
        if os.path.exists(translation_dir_path):
            shutil.rmtree(translation_dir_path)

        # Copy the new translations
        shutil.copytree(os.path.join(".", local_repo, name, translation_dir), translation_dir_path)

    except Exception as e:
        print(f"Error al actualizar las traducciones: {e}")
        exit(1)


# Script's Entrypoint
if __name__ == "__main__":
    try:
        # Download the repository from GitHub
        download_github_repo(repo_owner, official_repo, branch)

        # Rename the repository directory to match the format (owner-repo)
        local_repo = next(filter(lambda x: f"{repo_owner}-{official_repo}" in x, os.listdir(".")))
        os.rename(local_repo, f"{repo_owner}-{official_repo}")

        # Update the game's translation files with those from the downloaded repo
        for name in ["Core", "Royalty", "Ideology", "Biotech", "Anomaly"]:
            update_content(f"{repo_owner}-{official_repo}", name)

        # Delete the downloaded repo
        shutil.rmtree(f"{repo_owner}-{official_repo}")

    except Exception as e:
        print(f"Error general en el script: {e}")
        exit(1)

# Wait for user input bef
