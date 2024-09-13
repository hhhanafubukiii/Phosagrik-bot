from sqlite3 import *
from logging.config import dictConfig
from logging import *

from config.logging.logging_settings import logging_config

dictConfig(logging_config)

logger = getLogger(__name__)
logger.propagate = False


def create_db_user():
    conn = connect('user.db')
    cur = conn.cursor()

    cur.execute('''
    DROP TABLE IF EXISTS user
    ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS user(
    user_id INTEGER, 
    page INTEGER NOT NULL, 
    UNIQUE(user_id,page))
    ''')

    logger.info('Была создана база данных user')
    conn.close()


def create_db_bookmarks():
    conn = connect('bookmarks.db')
    cur = conn.cursor()

    cur.execute('''
        DROP TABLE IF EXISTS bookmarks
        ''')

    cur.execute('''
    CREATE TABLE IF NOT EXISTS bookmarks(
    user_id INTEGER,
    page INTEGER,
    bookmark TEXT,
    UNIQUE(page,bookmark))
    ''')

    logger.info('Была создана база данных bookmarks')
    conn.close()


def set_page(user_id: int, page: int) -> None:
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\user.db')
    cur = conn.cursor()

    cur.execute('''
    INSERT INTO user(user_id, page)
    VALUES(?, ?)
    ''', (user_id, page))

    conn.commit()
    logger.info('nothing')
    conn.close()


def get_page(user_id: int):
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\user.db')
    cur = conn.cursor()

    cur.execute('''
    SELECT page
    FROM user
    WHERE user_id == ?
    ''', (user_id,))

    result = cur.fetchone()[0]

    conn.close()
    return result


def update_page(user_id: int, page: int):
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\user.db')
    cur = conn.cursor()

    cur.execute('''
    UPDATE user
    SET page = ?
    WHERE user_id == ?
    ''', (page, user_id))

    conn.commit()
    conn.close()


def set_new_bookmark(user_id: int, page: int, bookmark: str) -> None:
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\bookmarks.db')
    cur = conn.cursor()

    cur.execute('''
    INSERT INTO bookmarks(user_id, page, bookmark)
    VALUES (?, ?, ?)
    ''', (user_id, page, bookmark))

    conn.commit()
    conn.close()


def get_bookmarks(user_id: int):
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\bookmarks.db')
    cur = conn.cursor()

    bookmarks: set[int] = set()
    cur.execute('''
    SELECT page, bookmark
    FROM bookmarks
    WHERE user_id == ?
    ''', (user_id,))

    results = cur.fetchall()
    for item in results:
        bookmarks.add(item[0])
    conn.close()

    return bookmarks


def delete_bookmark(user_id: int, page: int):
    conn = connect(r'D:\Phosagrik bot\Phosagrik_bot\database\bookmarks.db')
    cur = conn.cursor()

    cur.execute('''
    DELETE FROM bookmarks
    WHERE user_id == ? AND page == ?
    ''', (user_id, page))

    conn.commit()
    conn.close()


# create_db_user()
# create_db_bookmarks()
# set_page(user_id=1209547541, page=1)
# a = get_page(user_id=1209547541)
# print('heh')
# print(a)
# update_page(1209547541, 2)
# set_new_bookmark(user_id=1209547541, page=53, bookmark='popka')
# get_bookmarks(user_id=1209547541)
# delete_bookmark(user_id=1209547541, page=5)