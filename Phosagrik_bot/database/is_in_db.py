from sqlite3 import *


def is_in_db(user_id: int):
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\user.db')
    cur = conn.cursor()

    cur.execute('''
    SELECT user_id
    FROM user
    WHERE user_id == ?
    ''', (user_id,))

    result = cur.fetchone()
    # если нету в базе
    if result is None:
        return False
    # если есть
    else:
        return True


