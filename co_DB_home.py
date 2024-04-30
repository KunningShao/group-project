from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Define the index route
@app.route('/')
def index():
    # 连接到数据库
    conn = sqlite3.connect('D:\快乐老家\CITS3403\P\movies.db')
    cursor = conn.cursor()

    # 执行查询
    cursor.execute('SELECT name, address FROM moviedetails')

    # 获取所有结果
    movies = cursor.fetchall()

    print(movies)

    # 关闭数据库连接
    conn.close()

    # 将查询结果传递给HTML模板
    return render_template('pront page.html', movies=movies)
    

if __name__ == '__main__':
    app.run(debug=True)

