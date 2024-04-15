from flask import Flask, render_template, request
'''<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='styles.css') }}">'''
app = Flask(__name__)

# Список заметок (в виде объектов класса)
class Note:
    def __init__(self, id, title, description, important=False):
        self.id = id
        self.title = title
        self.description = description
        self.important = important

notes = [
    Note(1, 'Заметка 1', 'Описание заметки 1', False),
    Note(2, 'Заметка 2', 'Описание заметки 2', True),
    Note(3, 'Заметка 3', 'Описание заметки 3', False)
]

# Отображение всех заметок
@app.route('/')
def index():
    return render_template('index.html', notes=notes)

# Добавление новой заметки
@app.route('/add', methods=['POST'])
def add_note():
    title = request.form['title']
    description = request.form['description']
    important = 'important' in request.form
    notes.append(Note(len(notes) + 1, title, description, important))
    return render_template('index.html', notes=notes)

# Удаление заметки
@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    global notes
    notes = [note for note in notes if note.id != note_id]
    return render_template('index.html', notes=notes)

if __name__ == '__main__':
    app.run(debug=True)
