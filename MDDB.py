import sqlite3

# 连接到数据库（如果不存在则创建）
conn = sqlite3.connect('movies.db')

# 创建游标对象
cursor = conn.cursor()

# 创建表格
cursor.execute('''CREATE TABLE IF NOT EXISTS moviedetails
                  (address varchar(500),
                   name TEXT(100) PRIMARY KEY, 
                   type varchar(50), 
                   rating varchar(10),
                   release_date varchar(50),
                   runtime varchar(30),
                   plot varchar(1000)
                   )''')

data = [
    ("https://pic.nximg.cn/file/20170618/9413594_232044240000_2.jpg", 
     "Spirited Away", "animation", "8.6/10", "July 20, 2001", "125 minutes", 
     "The film tells the story of Chihiro Ogino, a sullen ten-year-old girl who, while moving to a new neighborhood, becomes trapped in an alternate reality that is inhabited by spirits and monsters. After her parents are transformed into pigs by the witch Yubaba, Chihiro takes a job working in Yubaba's bathhouse to find a way to free herself and her parents and return to the human world."
    ),
    ("https://image.tmdb.org/t/p/original/ji94IIScMTk0SARR3XIgBgLjuYB.jpg",
     "Shining", "horror", "8.4/10", "May 23, 1980", "146 minutes", 
     "The story follows Jack Torrance, an aspiring writer and recovering alcoholic, who takes a job as the winter caretaker of the isolated Overlook Hotel in the Colorado Rockies. Jack moves in with his wife, Wendy, and his young son, Danny, who possesses psychic abilities known as 'the shining.' As the winter snow traps them in the hotel, Jack's sanity begins to unravel, influenced by the malevolent spirits haunting the Overlook and the hotel's dark history."
    ),
   
    # 更多数据...
]

for movie_data in data:
    cursor.execute("INSERT OR REPLACE INTO moviedetails (address, name, type, rating, release_date, runtime, plot) VALUES (?, ?, ?, ?, ?, ?, ?)", movie_data)

# 提交更改
conn.commit()

# 关闭连接
conn.close()

