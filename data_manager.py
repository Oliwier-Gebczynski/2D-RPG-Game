import os
import json

class DataManager:
    def __init__(self):
        self.saves_dir = "saves"

    def create_save(self, save_data, save_name, overwrite=False):
        save_dir = os.path.join(self.saves_dir, save_name)

        if not os.path.exists(save_dir):
            try:
                os.makedirs(save_dir)
            except OSError as e:
                print(f"Error creating save directory: {e}")
                return

        save_path = os.path.join(save_dir, f"{save_name}.json")

        if os.path.exists(save_path) and not overwrite:
            print(f"Save file '{save_name}' already exists. Use 'overwrite=True' to overwrite.")
            return

        try:
            with open(save_path, 'w') as save_file:
                json.dump(save_data, save_file, indent=4)
            print(f"Save created: {save_path}")
        except OSError as e:
            print(f"Error saving data: {e}")

    def load_save(self, save_name):
        save_dir = os.path.join(self.saves_dir, save_name)
        save_path = os.path.join(save_dir, f"{save_name}.json")

        if not os.path.exists(save_path):
            raise FileNotFoundError(f"Save file '{save_name}' not found.")

        with open(save_path, 'r') as save_file:
            save_data = json.load(save_file)
            return save_data

    def get_all_saves(self):
        save_names = []
        for save_dir in os.listdir(self.saves_dir):
            if os.path.isdir(os.path.join(self.saves_dir, save_dir)):
                save_names.append(save_dir)
        return save_names
