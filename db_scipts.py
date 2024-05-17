import sqlite3

db_name = 'quiz.db'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def create():
    open()
    do('''CREATE TABLE quiz(
            id INTEGER PRIMARY KEY,
            name VARCHAR)''')
    
    do('''CREATE TABLE questions(
        id INTEGER PRIMARY KEY,
        question VARCHAR,
        answer VARCHAR,
        wrong1 VARCHAR,
        wrong2 VARCHAR,
        wrong3 VARCHAR)''')
    
    do('''CREATE TABLE quiz_content(
                    id INTEGER PRIMARY KEY,
                    quiz_id INTEGER,
                    question_id INTEGER,
                    FOREIGN KEY (quiz_id) REFERENCES quiz (id),
                    FOREIGN KEY (question_id) REFERENCES questions (id))''')
    
    close()

def clear_db():
    ''' видаляє всі таблиці '''
    open()
    query = '''DROP TABLE IF EXISTS questions'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz'''
    do(query)
    query = '''DROP TABLE IF EXISTS quiz_content'''
    do(query)
    close()

def add_quizes():
    open()
    quizes = [
        ("Моя гра",),
        ("математика",),
        ("література",),
        ("історія",)
    ]
    cursor.executemany(''' INSERT INTO quiz (name) VALUES (?)''', quizes)
    conn.commit()
    close()

def add_question():
    open()
    questions = [
    ('Яка найвища гора в світі?', 'Еверест', 'Кіліманджаро', 'Маккінлі', 'Аконкагуа'),
    ('Який метал не реагує з водою?', ' Натрій', 'Магній', 'Цинк', 'Алюміній'),
    ('Хто написав "Ромео і Джульєтта"?', 'Уільям Шекспір', 'Федор Достоєвський', 'Джейн Остін', ') Марк Твен'),
    ('Яка країна має найбільшу кількість населення?', ' Індія', 'Китай', 'США', 'Росія'),
    ('Який планета є найбільшою в Сонячній системі?', 'Земля', 'Юпітер', 'Марс','Венера'),
    ('Що більше слона і нічого не важить?', 'Тінь слона', 'Повітряна куля', 'Парашут', 'Хмара')
]
    cursor.executemany(' INSERT INTO questions (question, answer, wrong1, wrong2, wrong3) VALUES (?, ?, ?, ?, ?)', questions)
    conn.commit()
    close()

def add_links():
    open()
    cursor.execute("PRAGMA foreing_keus=on")
    answer = input("додати звязок? (y/n)")
    while answer !='n':
        quiz_id = int(input("Введіть номер вікторини"))
        question_id = int(input("Введіть номер вікторини"))
        cursor.execute('INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)',[quiz_id, question_id])
        conn.commit()
        answer = input("додати звязок? (y/n)")
    close()



def main():
    clear_db()
    create()
    add_quizes()
    add_question()
    add_links()
main()