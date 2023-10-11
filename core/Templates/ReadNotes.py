"""

    Created by Colin Gelling on 09/10/2023
    Using Pycharm Professional

"""

from core.app_information import AppInformation


class ReadNotes:
    def __init__(self):
        super().__init__()

    @staticmethod
    def find_template():

        # Declare application root path
        app_info = AppInformation()

        # Declare the template file
        filename = "default_note_template.txt"

        # Get a list of default templates
        templates = app_info.application_templates()

        for template in templates:
            if filename in template:
                return template

    @staticmethod
    def read_template(template):

        left_side_values = []

        with open(template, 'r') as template_file:
            for line in template_file:
                # Split each line at ':' to separate the left and right sides
                parts = line.split(':')
                if len(parts) > 0:
                    left_side = parts[0].strip()  # Remove leading/trailing spaces
                    left_side_values.append(left_side)

                # Print the list of left side values
            print(left_side_values)
