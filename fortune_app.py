from flask import Flask, render_template, request
import openai
import config

app = Flask(__name__)

# OpenAI APIキーの設定（config.pyから読み込み）
openai.api_key = config.OPENAI_API_KEY

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fortune', methods=['POST'])
def fortune():
    name = request.form['name']
    gender = request.form['gender']
    birthdate = request.form['birthdate']
    zodiac = request.form['zodiac']
    theme = request.form['theme']
    timeframe = request.form['timeframe']
    
    # 占いの内容を生成するためのプロンプト
    prompt = (
        f"{name}さん（{gender}、生年月日: {birthdate}、星座: {zodiac}）の"
        f"{timeframe}の{theme}についての運勢を占います。"
    )
    
    # ChatCompletionを使った占い結果の生成
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 例としてgpt-3.5-turboを使用
        messages=[
            {"role": "system", "content": "あなたは親切な占い師です。"},
            {"role": "user", "content": prompt}
        ]
    )
    result = response.choices[0].message['content'].strip()
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)