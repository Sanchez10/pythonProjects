import sqlite3
from Trace import TraceLogger

class DatabasePassword:
    def __init__(self, db_file, trace_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None
        self.trace = TraceLogger(trace_file)

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.cursor = self.connection.cursor()
            self.trace.write_trace("Conexão com o banco de dados estabelecida.")
        except sqlite3.Error as e:
            self.trace.write_trace("Erro ao conectar ao banco de dados:", e)

    def close(self):
        if self.connection:
            self.connection.commit()
            self.cursor.close()
            self.connection.close()
            self.trace.write_trace("Conexão com o banco de dados fechada.")

    def execute_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            self.trace.write_trace("Erro ao executar a query:", e)
            return None

    def execute_update(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            self.trace.write_trace("Query executada com sucesso.")
        except sqlite3.Error as e:
            self.trace.write_trace("Erro ao executar a query:", e)
