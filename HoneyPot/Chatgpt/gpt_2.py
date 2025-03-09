import paramiko
import os

class MySFTPServer(paramiko.SFTPServerInterface):
    def __init__(self, server, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.server = server
        self.base_path = os.path.abspath("sftp_root")  # Base directory for files

    def _realpath(self, path):
        # Convert the virtual path to a real path, ensuring it stays within the base directory
        return os.path.abspath(os.path.join(self.base_path, path.lstrip("/")))

    def list_folder(self, path):
        # List the contents of a directory
        real_path = self._realpath(path)
        if not os.path.isdir(real_path):
            raise paramiko.SFTPServerError("Path is not a directory")
        
        file_list = []
        for filename in os.listdir(real_path):
            file_path = os.path.join(real_path, filename)
            attrs = paramiko.SFTPAttributes.from_stat(os.stat(file_path))
            attrs.filename = filename
            file_list.append(attrs)
        return file_list

    def stat(self, path):
        # Provide file metadata (used by clients for file details)
        real_path = self._realpath(path)
        return paramiko.SFTPAttributes.from_stat(os.stat(real_path))

    def open(self, path, flags, attr):
        # Open a file for reading
        real_path = self._realpath(path)
        if not os.path.isfile(real_path):
            raise paramiko.SFTPServerError("File not found")
        return open(real_path, "rb")
