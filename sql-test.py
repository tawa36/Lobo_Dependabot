import sqlite3

def execute_query(user_input):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # 脆弱なコード: ユーザー入力が直接SQLクエリに組み込まれる
    cursor.execute(f"SELECT * FROM users WHERE username = '{user_input}'")
    results = cursor.fetchall()
    conn.close()
    return results

# テスト用入力
user_input = "john_doe' OR '1'='1"  # 脆弱な入力
results = execute_query(user_input)
print(results)
