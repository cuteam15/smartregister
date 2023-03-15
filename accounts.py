import sqlite3
import pandas as pd

con = sqlite3.connect("smart_register.sqlite")
cur = con.cursor()


def display_table(table):  # display all accounts
    query = f'select * from {table}'
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
    con.commit()
    return name, price


def create_receipt():
    query = f"select count(name) from sqlite_master where type='table' and name='receipt'"
    if cur.execute(query).fetchone()[0] == 0:  # check if table exists
        print("deleted")
        query = f"create table receipt (item VARCHAR NOT NULL, price INT not null, upc varchar(20) not null)"
        cur.execute(query)
        con.commit()


def del_receipt():
    query = f"select count(name) from sqlite_master where type='table' and name='receipt'"
    if cur.execute(query).fetchone()[0] == 1:
        query = f"drop table receipt"
        cur.execute(query)
        con.commit()
        print("deleted")


def add_to_receipt(upc):
    query = f"select item_name from catalog where item_upc='{upc}'"
    name = cur.execute(query).fetchone()[0]
    query = f"select item_cost from catalog where item_upc='{upc}'"
    price = cur.execute(query).fetchone()[0]
    query = f"insert into receipt values('{name}', {price}, '{upc}')"
    cur.execute(query)
    con.commit()


def remove_from_receipt(upc):
    query = f"select exists(select 1 from receipt where upc='{upc}')"
    if cur.execute(query).fetchone()[0] == 1:
        query = f"select item_name from catalog where item_upc='{upc}'"
        name = cur.execute(query).fetchone()[0]
        query = f"delete from receipt where item='{name}'"
        cur.execute(query)
        con.commit()


def main():
    del_receipt()
    create_receipt()
    add_to_receipt("978215396047")
    add_to_receipt("563210784330")
    display_table('receipt')
    remove_from_receipt("978215396047")
    display_table('receipt')


if __name__ == '__main__':
    main()
