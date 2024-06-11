from flask import render_template, request, redirect
from app import app

# Данные анкеты хранятся в списке
entries = []


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        city = request.form['city']
        hobby = request.form['hobby']
        age = request.form['age']

        # Добавляем данные анкеты в список
        entries.append({
            'name': name,
            'city': city,
            'hobby': hobby,
            'age': age
        })

        return redirect('/')

    return render_template('blog.html', entries=entries)

