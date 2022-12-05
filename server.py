from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "Nothing to see here"

@app.route('/')
def count_up():
    if 'visits' in session:
        session['visits'] += 1
    else:
        session['visits'] = 1
    return render_template("counter.html")

@app.route('/destroy_session')
def reset_counter():
    session.pop('visits')
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)