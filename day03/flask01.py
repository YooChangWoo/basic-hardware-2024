from flask import Flask

app = Flask(__name__)  #name 이름을 통한 flask

@app.route("/")  # 라우팅을 위한 뷰함수 등록
def hello():
	return "Hong kil-dong"

if __name__=="__main__":  # 터미널에서 직접실행
	app.run(host="0.0.0.0", port"10111",debug=True)
