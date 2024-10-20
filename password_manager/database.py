import sqlite3
from Trace import TraceLogger
from contextlib import contextmanager

class DatabasePassword:
    def __init__(self, db_file, trace_file):
        self.db_file = db_file
        self.trace = TraceLogger(trace_file)

    @contextmanager
    def connect(self):
        connection = None
        try:
            connection = sqlite3.connect(self.db_file)
            cursor = connection.cursor()
            self.trace.write_trace("Conexao com o banco de dados estabelecida.")
            yield cursor
        except sqlite3.Error as e:
            self.trace.write_trace(f"Erro ao conectar ao banco de dados: {e}")
        finally:
            if connection:
                connection.commit()
                connection.close()
                self.trace.write_trace("Conexao com o banco de dados fechada.")

    def execute_select(self, query, params=None):
        try:
            with self.connect() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                result = cursor.fetchall()
                self.trace.write_trace("Consulta realizada com sucesso.")
                return result
        except sqlite3.Error as e:
            self.trace.write_trace(f"Erro ao executar a consulta: {e}")
            return None

    def execute_write(self, query, params=None):
        try:
            with self.connect() as cursor:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                self.trace.write_trace("Alteracao realizada com sucesso.")
        except sqlite3.Error as e:
            self.trace.write_trace(f"Erro ao executar a alteracao: {e}")

    def log_custom_message(self, message):
        self.trace.write_trace(message)

# SELECT
# select_query = "SELECT * FROM Users WHERE username = ?"
# result = db.execute_select(select_query, (username,))

# INSERT, UPDATE and DELETE
# insert_query = "INSERT INTO Users (username, email, password) VALUES (?, ?, ?)"
# db.execute_write(insert_query, (username, email, password))
