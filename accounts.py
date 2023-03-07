import sqlite3
import pandas as pd

con = sqlite3.connect("smart_register.sqlite")
cur = con.cursor()


def display_accounts():
    query = 'select * from accounts'
    print(pd.read_sql_query(query, con))


def update_balance(rfid, amount):
    query = f"select balance from accounts where rfid='{rfid}'"
    balance = cur.execute(query).fetchone()[0]
    query = f"update accounts set balance = {balance + amount} where rfid='{rfid}'"
    cur.execute(query)
    con.commit()


def main():
    rfid = '1111000011'
    display_accounts()
    update_balance(rfid, 200000)
    display_accounts()


if __name__ == '__main__':
    main()
