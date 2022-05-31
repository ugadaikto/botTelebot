import sqlite3

class Database:
  try:
    def __init__(self, db_file):
      self.connection = sqlite3.connect(db_file, check_same_thread=False)
      self.cursor = self.connection.cursor()

    # -#-#-#-#-#-#-#-#-#-#-#-#-#- #
    # -#-#-#-#-# USERS #-#-#-#-#- #
    # -#-#-#-#-#-#-#-#-#-#-#-#-#- #

    def user_exist(self, user_id):
      with self.connection:
        result = self.cursor.execute("SELECT * FROM `users` WHERE `id` = ?", (user_id,)).fetchall()
        return bool(len(result))

    def add_user(self, user_id):
      with self.connection:
        self.cursor.execute("INSERT INTO `users` (`id`) VALUES (?)", (user_id,))

    def all_userids(self):
      with self.connection:
        result = self.cursor.execute(f"SELECT `id` FROM `users`").fetchall()
        return result

    def all(self, table):
      with self.connection:
        result = self.cursor.execute(f"SELECT * FROM `{table}`").fetchall()
        return len(result)

    def user_info(self, user_id):
      with self.connection:
        result = self.cursor.execute(f"SELECT * FROM `users` WHERE `id` = '{user_id}'").fetchone()
        return result

    def edit_user_info(self, user_id, referral=None, step=None, role=None, balance=None, all_clients=None):
      var = []
      if role != None:
        var.append(f"role='{role}'")
      if referral != None:
        var.append(f"referral='{referral}'")
      if step != None:
        var.append(f"step='{step}'")
      if balance != None:
        var.append(f"balance='{balance}'")
      if all_clients != None:
        var.append(f"all_clients='{all_clients}'")
      with self.connection:
        self.cursor.execute(f"UPDATE `users` SET {', '.join(var)} WHERE id = '{user_id}'")

    #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*
    #*#*#*#*#*#* ---> PAYMENTS <--- #*#*#*#*#*#*
    #*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*#*

    def create_payments(self, user_id, rand_number, amount):
      with self.connection:
        self.cursor.execute("INSERT INTO `payments` (`user_id`, `rand_number`, `amount`) VALUES (?, ?, ?)", (user_id, rand_number, amount,))

    def return_payments(self, user_id):
      with self.connection:
        result = self.cursor.execute("SELECT * FROM `payments` WHERE `user_id` = ?", (user_id,)).fetchall()
        return result[-1]

    def delete_payments(self, user_id):
      with self.connection:
        return self.cursor.execute("DELETE FROM `payments` WHERE `user_id` = ?", (user_id,))
  except:
    pass
