import  json


def load_candidates():  # Функция, загружающая данные из файла candidates.json
    with open('candidates.json', 'r', encoding='utf-8') as file:
        dict_candidates = json.load(file)
    return dict_candidates


def get_all():  # Выводит список всех кандидатов
    candidates = load_candidates()
    return candidates


def get_by_pk(pk):  # Вернет кандидата по его pk
    dict_candidates = load_candidates()
    for candidate in dict_candidates:
        if candidate["pk"] == pk:
            return candidate
    return "Нет такого кандидата"


def get_by_skill(skill_name):  # Вернет список кандидатов по заданному навыку
    dict_candidates = load_candidates()
    selected_candidates = []
    for candidate in dict_candidates:
        if skill_name.lower() in candidate["skills"].lower():
            selected_candidates.append(candidate)
    return selected_candidates

