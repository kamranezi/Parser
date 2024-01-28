import json

# Функция для добавления поля "color_links": [] если оно отсутствует
def add_color_links(json_data):
    for item in json_data:
        if 'color_links' not in item:
            item['color_links'] = []
    return json_data

# Путь к файлу JSON, который вы будете обновлять
json_file_path = 'files/lin.json'

# Чтение JSON файла
with open(json_file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Добавление поля "color_links" там, где оно отсутствует
updated_data = add_color_links(data)

# Запись обновленных данных обратно в JSON файл
with open(json_file_path, 'w', encoding='utf-8') as file:
    json.dump(updated_data, file, indent=4)
