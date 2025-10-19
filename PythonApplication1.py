import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        # Set a modern theme
        self.style = ttk.Style()
        self.style.theme_use("arc")  # Professional light theme

        # Configure colors and fonts
        self.style.configure("TButton", font=("Segoe UI", 12), padding=10)
        self.style.configure("TLabel", font=("Segoe UI", 12), background="#ffffff", foreground="#333333")
        self.style.configure("TFrame", background="#ffffff")

        # Main container frame
        self.container = ttk.Frame(root)
        self.container.pack(fill=tk.BOTH, expand=True)

        # Add main menu UI elements
        self.title_label = ttk.Label(
            self.container, text="File Organizer", font=("Segoe UI", 24, "bold"), anchor="center"
        )
        self.title_label.pack(pady=20)

        self.select_files_button = ttk.Button(
            self.container, text="📄 Select Files", command=self.select_files, style="TButton"
        )
        self.select_files_button.pack(pady=10, fill=tk.X)

        self.select_folder_button = ttk.Button(
            self.container, text="📁 Select Folder", command=self.select_folder, style="TButton"
        )
        self.select_folder_button.pack(pady=10, fill=tk.X)

        self.sort_button = ttk.Button(
            self.container, text="🔀 Sort Files", command=self.sort_files, style="TButton"
        )
        self.sort_button.pack(pady=10, fill=tk.X)

    def select_files(self):
        self.selected_files = filedialog.askopenfilenames(title="Select Files to Sort")
        if self.selected_files:
            messagebox.showinfo("Files Selected", f"{len(self.selected_files)} files selected.")

    def select_folder(self):
        self.selected_folder = filedialog.askdirectory(title="Select Folder to Sort")
        if self.selected_folder:
            messagebox.showinfo("Folder Selected", f"Folder selected: {self.selected_folder}")

    def sort_files(self):
        if not self.selected_files and not self.selected_folder:
            messagebox.showwarning("No Input", "Please select files or a folder first.")
            return

        if self.selected_folder:
            # Organize files within the selected folder
            self.organize_folder_contents(self.selected_folder)
        else:
            # Sort the selected files into system folders
            for file_path in self.selected_files:
                self.move_file_to_system_folder(file_path)

        messagebox.showinfo("Success", "Files sorted successfully!")
        self.selected_files = []  # Clear the list after sorting
        self.selected_folder = ""  # Clear the folder path after sorting

    def organize_folder_contents(self, folder_path):
        # Define possible subfolders
        subfolders = {
            "Documents": os.path.join(folder_path, "Documents"),
            "Music": os.path.join(folder_path, "Music"),
            "Pictures": os.path.join(folder_path, "Pictures"),
            "Videos": os.path.join(folder_path, "Videos"),
            "Others": os.path.join(folder_path, "Others"),
        }

        # Track which subfolders are needed
        needed_subfolders = set()

        # First pass: Determine which subfolders are needed
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if root == folder_path:  # Only process files in the root of the selected folder
                    file_type = self.get_file_type(file_name)
                    if file_type:
                        needed_subfolders.add(file_type)

        # Create only the necessary subfolders
        for subfolder in needed_subfolders:
            os.makedirs(subfolders[subfolder], exist_ok=True)

        # Second pass: Move files into their respective subfolders
        for root, _, files in os.walk(folder_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if root == folder_path:  # Only process files in the root of the selected folder
                    self.move_file_to_subfolder(file_path, subfolders)

    def move_file_to_subfolder(self, file_path, subfolders):
        file_name = os.path.basename(file_path)
        file_type = self.get_file_type(file_name)
        if file_type:
            destination_folder = subfolders[file_type]
            shutil.move(file_path, os.path.join(destination_folder, file_name))

    def get_file_type(self, file_name):
        extension = os.path.splitext(file_name)[1].lower()
        if extension in [".docx", ".pdf", ".txt", ".xlsx"]:
            return "Documents"
        elif extension in [".mp3", ".wav", ".flac"]:
            return "Music"
        elif extension in [".jpg", ".png", ".gif"]:
            return "Pictures"
        elif extension in [".mp4", ".mkv", ".avi"]:
            return "Videos"
        else:
            return "Others"

    def move_file_to_system_folder(self, file_path):
        file_name = os.path.basename(file_path)
        destination_folder = self.get_destination_system_folder(file_name)
        if destination_folder:
            shutil.move(file_path, os.path.join(destination_folder, file_name))

    def get_destination_system_folder(self, file_name):
        extension = os.path.splitext(file_name)[1].lower()
        folders = {
            ".lnk": os.path.join(os.environ["USERPROFILE"], "Desktop"),
            ".exe": os.path.join(os.environ["USERPROFILE"], "Desktop"),
            ".docx": os.path.join(os.environ["USERPROFILE"], "Documents"),
            ".pdf": os.path.join(os.environ["USERPROFILE"], "Documents"),
            ".txt": os.path.join(os.environ["USERPROFILE"], "Documents"),
            ".xlsx": os.path.join(os.environ["USERPROFILE"], "Documents"),
            ".mp3": os.path.join(os.environ["USERPROFILE"], "Music"),
            ".wav": os.path.join(os.environ["USERPROFILE"], "Music"),
            ".flac": os.path.join(os.environ["USERPROFILE"], "Music"),
            ".jpg": os.path.join(os.environ["USERPROFILE"], "Pictures"),
            ".png": os.path.join(os.environ["USERPROFILE"], "Pictures"),
            ".gif": os.path.join(os.environ["USERPROFILE"], "Pictures"),
            ".mp4": os.path.join(os.environ["USERPROFILE"], "Videos"),
            ".mkv": os.path.join(os.environ["USERPROFILE"], "Videos"),
            ".avi": os.path.join(os.environ["USERPROFILE"], "Videos"),
        }
        return folders.get(extension)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()