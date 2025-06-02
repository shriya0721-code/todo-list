from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

todos = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            todos.append(task)
        return redirect("/")
    return render_template_string("""
    <h2>Simple To-Do List</h2>
    <form method="post">
        <input name="task" placeholder="Enter new task" autocomplete="off">
        <button type="submit">Add</button>
    </form>
    <ul>
    {% for task in todos %}
        <li>{{ task }}</li>
    {% endfor %}
    </ul>
    """, todos=todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
