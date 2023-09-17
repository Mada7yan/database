import sqlite3
from csv_manager import csv_reader, csv_dictreader
from tables_types import types
# from dummy_data.restaurant import types


class DB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        # self.conn = sqlite3.connect(db_name, "host", "user", "password", "port")
        self.cur = self.conn.cursor()

    def create_tabel(self, table_name):
        query = self.generate_query_columns(table_name)
        self.cur.execute(query)
        self.conn.commit()

    @staticmethod
    def generate_query_columns(table_name):
        columns = ", ".join([f"{col_name} {col_type}" for col_name, col_type in types[table_name].items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        return query

    def update_row(self, table_name, row):
        # at first we should call self.create_tabel(table_name)
        keys = ", ".join(row.keys())
        values = ", ".join([f"'{item}'" for item in row.values()])
        query = f"INSERT INTO {table_name} ({keys}) VALUES ({values})"
        try:
            self.cur.execute(query)
            self.conn.commit()
        except:
            print("Error: query did not execute.\n", query)

    def update_rows(self, table_name, rows):
        for row in rows:
            self.update_row(table_name, row)

    def csv2db(self, table_name):
        file_name = f"dummy_data/{table_name}.csv"
        content = csv_dictreader(file_name)
        self.update_rows(table_name, content)

    def get_table_content(self, table_name):
        self.cur.execute(f"SELECT * FROM {table_name}")
        data = self.cur.fetchall()
        return data


def main():
    tables_list = ["restaurant", "car"]
    database_name = "business.db"
    db = DB(database_name)
    for table_name in tables_list:
        db.create_tabel(table_name)

    tb_name = "restaurant"
    db.csv2db(tb_name)
    print(db.get_table_content(tb_name))


if __name__ == "__main__":
    main()