#!/usr/bin/env python
"""This script contains the SQL codes necessary to make requests to the DB Postgres"""
import postgres

def count_intances_pending(username, date):
    """Count instances for today"""
    conn = postgres.conecct()
    cur = conn.cursor()
    cur.execute(
        """SELECT COUNT(*)
         FROM habits_recurrentinstance as r
         inner join habits_habit as h on h.id = r.habit_id
         inner join users_user as u on u.id = h.owner_id
         WHERE  r.created::DATE=%s and u.username = %s  """,
        (date, username,))
    count = cur.fetchone()
    return count


def count_intances_done(username, date):
    """Count instances done for today"""
    conn = postgres.conecct()
    cur = conn.cursor()
    cur.execute(
        """SELECT COUNT(*)
        FROM habits_recurrentinstance as r
        inner join habits_habit as h on h.id = r.habit_id
        inner join users_user as u on u.id = h.owner_id
        WHERE r.created::DATE=%s and u.username = %s and r.done = 'True' """, (date, username,))
    count = cur.fetchone()
    return count


def all_score(username, date):
    """ select all scores for a user"""
    conn = postgres.conecct()
    cur = conn.cursor()
    cur.execute(
        """SELECT value,date
        FROM score
        WHERE owner_score = %s  and date <= %s  """, (username, date,))
    count = cur.fetchall()
    return count


def insert_score(value, date, username):
    """ insert a score for a user """
    conn = postgres.conecct()
    cur = conn.cursor()
    cur.execute(
        """insert into score
        (value,date,owner_score)
        values(%s,%s,%s)""", (value, date, username,))
    conn.commit()
