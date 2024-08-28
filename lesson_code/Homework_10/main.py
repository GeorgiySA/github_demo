from flask import Flask
import utils

app = Flask(__name__)

@app.route("/")  # Главная страница
def page_index():
    dict_candidates = utils.load_candidates()
    result_list = ''
    for line in dict_candidates:
        result_list += line['name'] + '\n'
        result_list += line['position'] + '\n'
        result_list += line['skills'] + '\n'
        result_list += '\n'
    return '<pre>' + result_list + '</pre>'

@app.route('/candidates/<int:x>')  # Эта страница выводит данные кандидата х
def candidates(x):
    dict_candidates = utils.get_all()
    result_list = ''
    url = "https://www.dropbox.com/scl/fi/coti2py1thh5bi505bwgd/Nature.jpg?rlkey=7x7dmndbusj031f45u74bnxk1&st=88rxhwe7&dl=0"
    result_list += '<pre>' + dict_candidates[x]['name'] + '</pre>'
    result_list += '<pre>' + dict_candidates[x]['position'] + '</pre>'
    result_list += '<pre>' + dict_candidates[x]['skills'] + '</pre>'
    return f"<img src='{url}'> {result_list}"

@app.route('/skills/<skill_name>')  # Эта страница выводит кандидатов с требуемыми навыками
def skills(skill_name):
    dict_candidates = utils.get_by_skill(skill_name)
    result_list = ''
    for line in dict_candidates:
        result_list += line['name'] + '\n'
        result_list += line['position'] + '\n'
        result_list += line['skills'] + '\n'
        result_list += '\n'
    return '<pre>' + result_list + '</pre>'


app.run()