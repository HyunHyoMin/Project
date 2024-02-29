from flask import Flask, render_template, request
import random, os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')

db = SQLAlchemy(app)

class GameHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_choice = db.Column(db.Integer)
    computer_choice = db.Column(db.Integer)
    result = db.Column(db.Integer)

with app.app_context():
    db.create_all()

def rps_func(num, num2):
    if num == num2:
        return ("무승부")
    elif (num=="가위" and num2=="바위") or (num=="바위" and num2=="보") or (num=="보" and num2=="가위"):
        return ('패배')
    elif (num=="가위" and num2=="보") or (num=="바위" and num2=="가위") or (num=="보" and num2=="바위"):
        return ('승리')

@app.route('/')
def home():
    rps = ('가위', '바위', '보')
    cpu_rps = random.choice(rps) # cpu_rps = 가위, 바위, 보
    user_answer = request.args.get('rps_input')
    rps_result = rps_func(user_answer, cpu_rps) # rps_result = 무승부, 패배, 승리
    gamehistory = GameHistory(user_choice = user_answer, computer_choice = cpu_rps, result = rps_result)
    if request.args.get('rps_input'):
        db.session.add(gamehistory)
        db.session.commit()
    if request.args.get('reset') == "reset":
        GameHistory.query.delete()
        db.session.commit()
    game_count = {
        'win' : GameHistory.query.filter_by(result = "승리").count(),
        'lose' : GameHistory.query.filter_by(result = "패배").count(),
        'draw' : GameHistory.query.filter_by(result = "무승부").count(),
    }
    game_data = GameHistory.query.all()
    return render_template('index.html', data = game_data, count = game_count)

if __name__ == '__main__':  
    app.run(debug=True)