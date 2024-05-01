import csv
import psycopg2
from config import load_config


#def phones():
#    sql='''create sequence s;
#    create table phone_nums(
#        id integer default nextval('s'::regclass) primary key,
#        first_name varchar(255) not null,
#        last_name varchar(255) not null, 
#        phone varchar(11) not null
#    )'''
#    try:
#        config=load_config()
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute(sql)
#    except(psycopg2.DatabaseError, Exception) as error:
#        print(error)
#
#if __name__=='__main__':
#    phones()



#def read_txt():
#    data=[]
#    with open('lab10\dataforphones.txt', 'r') as file:
#        for line in file:
#            first_name, last_name, num=line.strip().split(',')
#            data.append((first_name, last_name, num))
#    return data
#data=read_txt()
#
#i=input()
#first_name, last_name, num=i.split(',')
#data.append((first_name, last_name, num))
#
#
#def insert_num(data):
#
#    sql='insert into phone_nums(first_name, last_name, phone)  values(%s,%s, %s)'
#    config=load_config()
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.executemany(sql, data)
#
#            conn.commit()
#    except (Exception, psycopg2.DatabaseError) as error:
#        print(error) 
#
#if __name__=='__main__':
#    insert_num(data)
#
#

#def update_phone(phone, first_name):
#    update_row_count=0
#
#    sql='''update phone_nums set phone=%s where first_name=%s'''
#
#    config=load_config()
#
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute(sql,(phone,first_name))
#
#            conn.commit()
#    except(Exception, psycopg2.DatabaseError) as error:
#        print(error)
#    finally:
#        return update_row_count
#
#if __name__=='__main__':
#    update_phone(87770284748, 'Dasha')
#    update_phone(87659898787,'Aziza')

#
#def get_phone():
#    config=load_config()
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute('select first_name, last_name from phone_nums order by first_name;')
#                print('Number', cur.rowcount)
#                row=cur.fetchone()
#    
#                while row is not None:
#                        print(row)
#                        row = cur.fetchone()
#    except (Exception, psycopg2.DatabaseError) as error:
#         print(error)
#if __name__=='__main__':
#     get_phone()
#

#def delete(name):
#    row_deleted=0
#    sql='''delete from phone_nums where first_name=%s;'''
#    config=load_config()
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute(sql, (name,))
#                rows_deleted=cur.rowcount
#
#            conn.commit()
#
#    except(Exception, psycopg2.DatabaseError) as error:
#        print(error)
#    finally:
#        return row_deleted
#    
#if __name__=='__main__':
#    delete('Noname')
#    delete('Noname5')