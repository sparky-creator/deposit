import os
import shutil
import datetime


def delete_folder_if_exists(folder_path):
    """Deletes the folder if it exists."""
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_path}' deleted successfully.")
    else:
        print(f"Folder '{folder_path}' does not exist.")


def move_folder_to_backup(folder_path, backup_folder, verbose=0):
    """Moves a folder to a backup folder, renaming it with a timestamp."""

    if os.path.exists(folder_path):
        # Create backup folder if it doesn't exist
        os.makedirs(backup_folder, exist_ok=True)

        # Generate a new name for the folder with a timestamp
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        new_folder_name = os.path.basename(folder_path) + "_" + timestamp
        new_folder_path = os.path.join(backup_folder, new_folder_name)

        # Move the folder
        shutil.move(folder_path, new_folder_path)
        if verbose > 0:
            print(f"Moved '{folder_path}' to '{new_folder_path}'")
    else:
        if verbose > 0:
            print(f"Folder '{folder_path}' does not exist.")
