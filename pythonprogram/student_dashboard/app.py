from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression

app = Flask(__name__)
DATA_PATH = 'data/students.csv'
PLOT_PATHS = {
    'avg_scores': 'static/avg_scores.png',
    'pass_fail': 'static/pass_fail_pie.png',
    'attendance_vs_score': 'static/attendance_vs_score.png'
}

def generate_plots(df):
    # 1. Average Subject Scores
    avg_scores = df[['Math', 'Science', 'English']].mean()
    plt.figure(figsize=(6, 4))
    avg_scores.plot(kind='bar', color='skyblue')
    plt.title('Average Scores by Subject')
    plt.ylabel('Score')
    plt.tight_layout()
    plt.savefig(PLOT_PATHS['avg_scores'])
    plt.close()

    # 2. Pass vs Fail Pie Chart
    pass_fail_counts = df['Passed'].value_counts()
    labels = ['Pass', 'Fail']
    plt.figure(figsize=(5, 5))
    plt.pie(pass_fail_counts, labels=labels, autopct='%1.1f%%', colors=['green', 'red'])
    plt.title('Pass vs Fail Distribution')
    plt.tight_layout()
    plt.savefig(PLOT_PATHS['pass_fail'])
    plt.close()

    # 3. Attendance vs Final Score Scatter Plot
    plt.figure(figsize=(6, 4))
    plt.scatter(df['Attendance'], df['FinalScore'], c='purple')
    plt.title('Attendance vs Final Score')
    plt.xlabel('Attendance (%)')
    plt.ylabel('Final Score')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(PLOT_PATHS['attendance_vs_score'])
    plt.close()

def train_models(df):
    X = df[['Math', 'Science', 'English']]
    y_reg = df['FinalScore']
    model_reg = LinearRegression().fit(X, y_reg)
    y_clf = df['Passed']
    model_clf = LogisticRegression().fit(X, y_clf)
    return model_reg, model_clf

@app.route('/')
def index():
    df = pd.read_csv(DATA_PATH)
    generate_plots(df)
    return render_template('index.html',
                           image_avg=PLOT_PATHS['avg_scores'],
                           image_pie=PLOT_PATHS['pass_fail'],
                           image_attendance=PLOT_PATHS['attendance_vs_score'],
                           table=df.to_html(classes='data'))

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        df = pd.read_csv(DATA_PATH)
        model_reg, model_clf = train_models(df)

        math = int(request.form['math'])
        science = int(request.form['science'])
        english = int(request.form['english'])
        attendance = int(request.form['attendance'])
        name = request.form['name']

        new_scores = pd.DataFrame([[math, science, english]], columns=['Math', 'Science', 'English'])
        predicted_score = model_reg.predict(new_scores)[0]
        passed = int(model_clf.predict(new_scores)[0])

        new_data = {
            'Name': name,
            'Math': math,
            'Science': science,
            'English': english,
            'Attendance': attendance,
            'FinalScore': round(predicted_score, 2),
            'Passed': passed
        }

        df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
        df.to_csv(DATA_PATH, index=False)

        return render_template('result.html',
                               name=name,
                               math=math,
                               science=science,
                               english=english,
                               attendance=attendance,
                               final_score=round(predicted_score, 2),
                               status="Pass" if passed == 1 else "Fail")

    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
