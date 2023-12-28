from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty list to store to-do items
todos = []

@app.route('/')
def index():
    return render_template('index.html', todos=todos)


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit(index):
    if 0 <= index < len(todos):
        if request.method == 'POST':
            updated_item = request.form.get('updated_item')
            todos[index] = updated_item
            return redirect(url_for('index'))
        return render_template('edit.html', index=index, todos=todos)
    return redirect(url_for('index'))

@app.route('/add', methods=['POST'])
def add():
    todo_item = request.form.get('todo_item')
    if todo_item:
        todos.append(todo_item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(todos):
        del todos[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False)
