import psycopg2
from config import load_config

#def func1():
#     
#    sql='''create or replace function param(pattern text)
#returns table(firstname varchar(255), lastname varchar(255), numbers varchar(11)) 
#as 
#$$
#begin
#RETURN QUERY
#select first_name,last_name, phone from phone_nums where first_name like pattern;
#end;$$
#language plpgsql;'''
#    config=load_config()
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute(sql)
#            conn.commit()
#    except(psycopg2.DatabaseError, Exception) as error:
#        print(error)
#
#if __name__=='__main__':
#    func1()


#def func2():
#    sql='''create or replace procedure insert(name varchar(255), lastname varchar(255), numbers varchar(11))
#language plpgsql
#as $$
#
#
#begin
#if exists(select first_name from phone_nums where first_name=name) then
#update phone_nums set phone=numbers where first_name=name;
#else 
#insert into phone_nums(first_name, last_name, phone) values(name,lastname,numbers);
#end if;
#end; $$
#'''
#    config=load_config()
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute(sql)
#            conn.commit()
#    except(psycopg2.DatabaseError, Exception) as error:
#        print(error)
#
#if __name__=='__main__':
#    func2()
#


#def func4():
#    sql='''create or replace function p(num1 integer, num2 integer)
#    returns table(id integer, fname varchar(255), lname varchar(255), numm varchar(11))
#    language plpgsql
#    as $$
#    begin 
#    return query
#    select * from phone_nums limit num1 offset num2;
#    end;
#    $$
#    '''
#    config=load_config()
#    try:
#        with psycopg2.connect(**config) as conn:
#            with conn.cursor() as cur:
#                cur.execute(sql)
#            conn.commit()
#    except(psycopg2.DatabaseError, Exception) as error:
#        print(error)
#
#if __name__=='__main__':
#    func4()


def func5():
    sql='''create or replace procedure delete(name varchar(255), numbers varchar(11))
language plpgsql
as $$


begin
if exists(select first_name from phone_nums where first_name=name or phone=numbers) then
delete from phone_nums where first_name=name or phone=numbers;
end if;
end; $$
'''
    config=load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
            conn.commit()
    except(psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__=='__main__':
    func5()