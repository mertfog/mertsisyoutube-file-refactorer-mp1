import os, shutil


class FileRefactorer:
    def __init__(self, folder_path):
        self._folder_path = folder_path

    def get_files(self) -> list:
        """
        Gets files list by given folder path defination
        """
        directory_list = os.listdir(self._folder_path)

        files = [
            file for file in directory_list
            if os.path.isfile(os.path.join(self._folder_path, file))
        ]

        return files

    def get_extensions(self):
        """
        Gets extensions list by given folder path defination
        """
        files = self.get_files()
        extensions = list(set(map(lambda file: file.rsplit('.')[-1].upper(), files)))

        return extensions

    def create_and_get_folders(self) -> list:
        """
        Creates a new folders with extensions like JPG Folder, GIF Folder etc...
        """
        extension_list = self.get_extensions()
        folders = []

        for extension in extension_list:
            folder_path = os.path.join(self._folder_path, extension)
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)
            folders.append(folder_path)

        return folders

    def refactor(self):
        """
        Simple Function to manage all refactor operations
        """

        files = self.get_files()
        folders = self.create_and_get_folders()

        for folder in folders:
            folder_type = folder.split(os.sep)[-1].upper()
            for file in files:
                file_type = file.rsplit('.')[-1].upper()
                if file_type == folder_type:
                    current_dest = os.path.join(self._folder_path, file)
                    new_dest = os.path.join(folder)
                    shutil.move(current_dest, new_dest)
