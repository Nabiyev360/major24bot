import sqlite3

path_to_db = 'data/db.sqlite3'


def create_tables():
    """Create 'bot_users', 'bot_referrals'"""
    conn = sqlite3.connect(path_to_db)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS bot_users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tg_id INTEGER UNIQUE NOT NULL,
            fullname TEXT NOT NULL,
            phone TEXT NOT NULL,
            is_active INTEGER NOT NULL DEFAULT 1,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS bot_referrals (
            invitation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            inviter_id INTEGER NOT NULL,
            follower_id INTEGER UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (inviter_id) REFERENCES bot_users (tg_id) ON DELETE CASCADE,
            FOREIGN KEY (follower_id) REFERENCES bot_users (tg_id) ON DELETE CASCADE
        )
    """)

    conn.commit()
    conn.close()


#
# def get_all_categories():
#     conn = sqlite3.connect(path_to_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT category_id, name FROM categories")
#     categories = cur.fetchall()
#     return categories
#
#
# def get_random_test_ids(category_id):
#     conn = sqlite3.connect(path_to_db)
#     cur = conn.cursor()
#     cur.execute("SELECT quiz_id FROM quizzes WHERE category_id = ?", (category_id,))
#     test_ids = [row[0] for row in cur.fetchall()]
#     conn.close()
#     if len(test_ids) <= 10:
#         return test_ids
#     return random.sample(test_ids, 10)
#
#
# def create_new_battle(user1_id, category_id, quiz_id_list: list):
#     conn = sqlite3.connect(path_to_db)
#     cur = conn.cursor()
#     SQL = f"INSERT INTO battles(user1_id, category_id, tests) VALUES(?, ?, ?)"
#     cur.execute(SQL, (user1_id, category_id, str(quiz_id_list)))
#     conn.commit()
#     cur.execute(f"SELECT battle_id FROM battles ORDER BY battle_id DESC LIMIT 1")
#     last_battle_id = cur.fetchone()[0]
#     conn.close()
#     return last_battle_id
#


# # BATTLES DB
# def check_vs_battle(category, user_id):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT battle_id, user1_id, category, tests FROM battles \
#         WHERE user2_id IS NULL AND category= '{category}' AND user1_id != '{user_id}'")
#     battle = cur.fetchone()
#     return battle
#
#
# def vs_battle(battle_id, user2_id):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"UPDATE battles\
#         SET user2_id= {user2_id} WHERE battle_id= {battle_id}")
#     conn.commit()
#     conn.close()
#
#
# def new_battle(user1_id, category, tests):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"INSERT INTO battles(user1_id, category, tests)\
#         VALUES({user1_id}, '{category}', '{tests}')")
#     conn.commit()
#     cur.execute(f"SELECT COUNT(battle_id) FROM battles")
#     last_battle_id = cur.fetchone()[0]
#     conn.close()
#     return last_battle_id
#
#
# def new_revansh_battle(user1_id, user2_id, category, tests):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"INSERT INTO battles(user1_id, user2_id, category, tests)\
#         VALUES({user1_id}, {user2_id}, '{category}', '{tests}')")
#     conn.commit()
#     cur.execute(f"SELECT COUNT(battle_id) FROM battles")
#     last_battle_id = cur.fetchone()[0]
#     conn.close()
#     return last_battle_id
#
#
# # Django'ga moslangan (+quizzes_{category})
# def get_quiz(category, quiz_id):
#     conn = sqlite3.connect(path_to_quiz_db)
#     cur = conn.cursor()
#     cur.execute(
#         f"SELECT question, variant_1, variant_2, variant_3, answer, quiz_photo FROM quizzes_{category} WHERE quiz_id= {quiz_id}")
#     vars = cur.fetchone()
#     return vars
#
#
# def check_answer(category, quiz_id):
#     conn = sqlite3.connect(path_to_quiz_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT answer FROM quizzes_{category} WHERE quiz_id= {quiz_id}")
#     vars = cur.fetchone()[0]
#     return vars
#
#
# def quiz_count(category):
#     conn = sqlite3.connect(path_to_quiz_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT COUNT(quiz_id) FROM quizzes_{category}")
#     count = cur.fetchone()[0]
#     return count
#
#
# #
# def get_variant(battle_id):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT tests FROM battles WHERE battle_id= {battle_id}")
#     variant = cur.fetchone()[0]
#     return variant
#
#
# def check_emoji(battle_id, user_id, symbol):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT user1_id, user2_id FROM battles WHERE battle_id= {battle_id}")
#     players = cur.fetchone()
#     user1_id = players[0]
#     user2_id = players[1]
#
#     if user_id == user1_id:
#         cur.execute(f"SELECT result_1 FROM battles WHERE battle_id= {battle_id}")
#         result_1 = cur.fetchone()[0]
#         if result_1 == None:
#             result_1 = ''
#         next_result = result_1 + symbol
#         cur.execute(f"UPDATE battles SET result_1= '{next_result}' WHERE battle_id= {battle_id}")
#
#     elif user_id == user2_id:
#         cur.execute(f"SELECT result_2 FROM battles WHERE battle_id= {battle_id}")
#         result_2 = cur.fetchone()[0]
#         if result_2 == None:
#             result_2 = ''
#         next_result = result_2 + symbol
#         cur.execute(f"UPDATE battles SET result_2= '{next_result}' WHERE battle_id= {battle_id}")
#     conn.commit()
#     conn.close()
#
#
# def overall_result(battle_id):
#     conn = sqlite3.connect(path_to_battles_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT user1_id, result_1, user2_id, result_2 FROM battles WHERE battle_id= {battle_id}")
#     overall = cur.fetchone()
#     return overall
#
#
# # USERS DB
# def add_user(user_id, first_name, last_name='None', username=None):
#     conn = sqlite3.connect(path_to_users_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT * FROM users WHERE user_id = '{user_id}'")
#     if not cur.fetchone():
#         sql_query = f"INSERT INTO users(user_id, first_name, last_name, username) VALUES (?,?,?,?)"
#         new_data = (user_id, first_name, last_name, username)
#         cur.execute(sql_query, new_data)
#     else:
#         sql_query = "UPDATE users SET first_name=?, last_name=?, username=? WHERE user_id = ?"
#         new_data = (first_name, last_name, username, user_id)
#         cur.execute(sql_query, new_data)
#     conn.commit()
#     conn.close()
#
#
# def get_user(user_id):
#     conn = sqlite3.connect(path_to_users_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT * FROM users WHERE user_id= {user_id}")
#     overall = cur.fetchone()
#     return overall
#
#
# def update_diamond(user_id):
#     conn = sqlite3.connect(path_to_users_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT diamond FROM users WHERE user_id= {user_id}")
#     user_diamonds = cur.fetchone()[0]
#     cur.execute(f"UPDATE users SET diamond= {user_diamonds + 10} WHERE user_id= {user_id}")
#     conn.commit()
#     conn.close()
#
#
# def update_diamond_be_equal(user_id, count):
#     conn = sqlite3.connect(path_to_users_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT diamond FROM users WHERE user_id= {user_id}")
#     user_diamonds = cur.fetchone()[0]
#     cur.execute(f"UPDATE users SET diamond= {user_diamonds + count} WHERE user_id= {user_id}")
#     conn.commit()
#     conn.close()
#
#
# def get_diamonds_stat(user_id):
#     conn = sqlite3.connect(path_to_users_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT first_name, diamond FROM users ORDER BY diamond DESC LIMIT 20")
#     diamonds_stat = cur.fetchall()
#     cur.execute(f"SELECT first_name, diamond FROM users WHERE user_id= {user_id}")
#     diamonds_stat.append(cur.fetchone())
#     cur.execute(f"SELECT diamond FROM users")
#     all = cur.fetchall()
#     return diamonds_stat, all
#
#
# def get_public_results():
#     conn = sqlite3.connect(path_to_users_db)
#     cur = conn.cursor()
#     cur.execute(f"SELECT user_id, first_name, last_name, diamond FROM users ORDER BY diamond DESC LIMIT 10")
#     diamonds_stat = cur.fetchall()
#     return diamonds_stat
#
#
# def get_users_id():
#     conn = sqlite3.connect(path_to_users_db)
#     c = conn.cursor()
#     c.execute(f"SELECT user_id FROM users")
#     sender_id = c.fetchall()
#     return sender_id
#
#
# def count_users():
#     conn = sqlite3.connect(path_to_users_db)
#     c = conn.cursor()
#     c.execute(f"SELECT COUNT() FROM users")
#     count = c.fetchone()[0]
#     return count
#
#
# def clear_diamonds():
#     conn = sqlite3.connect(path_to_users_db)
#     c = conn.cursor()
#     c.execute(f"UPDATE users SET diamond=0")
#     conn.commit()
#     conn.close()
#
#
# def get_my_result(battle_id, user_id):
#     conn = sqlite3.connect(path_to_battles_db)
#     c = conn.cursor()
#     c.execute(f"SELECT * FROM battles WHERE battle_id={battle_id} AND (user1_id= {user_id} OR user2_id= {user_id})")
#     res = c.fetchone()
#     return res
#
#
# ### SHORT FUNCTIONS
# def get_one(db_name, table, params='*', where_param='', where_data=''):
#     where = ''
#     if where_param and where_data:
#         where = f"WHERE {where_param} = '{where_data}'"
#
#     conn = sqlite3.connect(db_name)
#     c = conn.cursor()
#     c.execute(f"SELECT {params} FROM {table} {where}")
#     res = c.fetchone()
#     return res
#
#
# def update_db(db_name, table, param, new_data, where_param, where_data):
#     where = ''
#     if where_param and where_data:
#         where = f'WHERE {where_param} = {where_data}'
#
#     conn = sqlite3.connect(db_name)
#     c = conn.cursor()
#     c.execute(f'UPDATE {table} SET {param}="{new_data}" {where}')
#     conn.commit()
#     conn.close()
#
#
# ### SIMPLE FUNCTIONS
#
#
# def set_started(battle_id, user_id, time):
#     conn = sqlite3.connect('data/battles.db')
#     c = conn.cursor()
#     c.execute(f"SELECT * FROM battles WHERE battle_id={battle_id} AND (user1_id= {user_id} OR user2_id= {user_id})")
#     res = c.fetchone()
#
#     user1_id, user2_id = res[1], res[2]
#
#     if user_id == user1_id:
#         param = 'started_at1'
#     elif user_id == user2_id:
#         param = 'started_at2'
#
#     update_db('data/battles.db', 'battles', param, time, 'battle_id', battle_id)
#
#
# # CHANNEL
#
# def get_channel_quiz(category, quiz_id):
#     conn = sqlite3.connect(path_to_quiz_db)
#     cur = conn.cursor()
#     cur.execute(
#         f"SELECT question, variant_1, variant_2, variant_3, answer, quiz_photo FROM quizzes_{category} WHERE quiz_id= {quiz_id}")
#     quiz = cur.fetchone()
#
#     return quiz
#
#
# def get_answer(category, question):
#     conn = sqlite3.connect(path_to_quiz_db)
#     cur = conn.cursor()
#     data = (question,)
#     cur.execute(f"SELECT answer FROM quizzes_{category} WHERE question=?", data)
#     answer = cur.fetchone()[0]
#     return answer
