import postgres

"""Count instances for today"""
def countIntancesPending(username):
    conn = postgres.conecct()
    cur = conn.cursor()
    
    cur.execute(

    """SELECT COUNT(*) 
        FROM recurrences_recurrentinstance as r 
        inner join habits_habit as h on h.id = r.habit_id
        inner join users_user as u on u.id = h.owner_id
        WHERE r.created = (current_date-1)::DATE::TIMESTAMP WITH TIME ZONE and u.username = %s""",

    (username,)
    )
    count = cur.fetchone()
    
    return count

"""Count instances done for today"""
def countIntancesDone(username):
     conn = postgres.conecct()
     cur = conn.cursor()
    
     cur.execute(

     """SELECT COUNT(*) 
        FROM recurrences_recurrentinstance as r 
        inner join habits_habit as h on h.id = r.habit_id
        inner join users_user as u on u.id = h.owner_id
        WHERE r.created = (current_date-1)::DATE::TIMESTAMP WITH TIME ZONE and u.username = %s and r.done = 'True'""",

     (username,)
     )
     count = cur.fetchone()
    
     return count

""" Count instances done for yesterday"""
def countIntancesDoneYesterday(username):
     conn = postgres.conecct()
     cur = conn.cursor()
    
     cur.execute(

     """SELECT COUNT(*) 
        FROM recurrences_recurrentinstance as r 
        inner join habits_habit as h on h.id = r.habit_id
        inner join users_user as u on u.id = h.owner_id
        WHERE r.created = (current_date-1)::DATE::TIMESTAMP WITH TIME ZONE and u.username = %s r.done = 'True' """,

     (username,)
     )
     count = cur.fetchone()
    
     return count

""" select all scores for a user"""
def allScore(username):
     conn = postgres.conecct()
     cur = conn.cursor()
    
     cur.execute(

     """SELECT value,date
        FROM score         
        WHERE owner_score = %s """,

     (username,)
     )
     count = cur.fetchone()
    
     return count

""" insert a score for a user """
def insertScore(value,date,username):
     conn = postgres.conecct()
     cur = conn.cursor()
    
     cur.execute(

     """insert into score
        (value,date,owner_score)     
        values(%s,%s,%s)""",

     (value,date,username,)
     )
     
     conn.commit()