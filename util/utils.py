import os
from typing import List


def load_common_words() -> List[str]:
    file_name = 'common_words.txt'
    current_folder = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_folder, f'{file_name }')

    with open(file_path, 'r', encoding='utf-8') as common_words:
        return common_words.readlines()