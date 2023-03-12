import sqlite3
import pandas as pd

con = sqlite3.connect("smart_register.sqlite")
cur = con.cursor()


def display_accounts():  # display all accounts
    query = 'select * from accounts'
    print(pd.read_sql_query(query, con))


# update account balances given given account rfid number and amount
def update_balance(rfid, amount):
    query = f"select balance from accounts where rfid='{rfid}'"
    balance = cur.execute(query).fetchone()[0]
    query = f"update accounts set balance = {balance + amount} where rfid='{rfid}'"
    cur.execute(query)
    con.commit()


def get_product(upc):  # returns name and price of product given upc
    query = f"select item_name, item_cost from catalog where item_upc='{upc}'"
    name, price = cur.execute(query).fetchone()  # [0]
    cur.execute(query)
    con.commit()
    return name, price


def main():
    upc = '978215396047'
    name, price = get_product(upc)
    print(name, price)


if __name__ == '__main__':
    main()
