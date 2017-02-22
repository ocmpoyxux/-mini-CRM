import sqlite3
from bottle import route, run, debug, template, request, redirect

@route('/users')
def users_list():
    pass

@route('/departaments', method='GET')
def departaments_list():
    conn = sqlite3.connect('crm_test.db')
    c = conn.cursor()
    c.execute("SELECT departament, description, mather FROM departaments")
    result = c.fetchall()
    output = template('departaments.tpl', rows=result)
    return output
    

@route('/positions', method='GET')
def positions_list():
    conn = sqlite3.connect('crm_test.db')
    c = conn.cursor()
    c.execute("SELECT position, description FROM positions")
    result = c.fetchall()
    output = template('positions.tpl', rows=result)
    return output

    
@route('/users_new', method='GET')
def new_users():
    
    if request.GET.get('save','').strip():

        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('crm_test.db')
        c = conn.cursor()

        query = """INSERT INTO users (name,surname, birthday,
                                      number, email, position, departament)
                                      VALUES ('%s',1)""" %new
        c.execute(query)
        conn.commit()

        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        c.close

        return '<p>The new task was inserted into the database, the ID is %s</p>' %new_id

    else:
        return template('new_users.tpl')

@route('/positions_new', method='GET')
def new_positions():
    if request.GET.get('save','').strip():
        position = request.GET.get('position', '').strip()
        description = request.GET.get('description', '').strip()
        conn = sqlite3.connect('crm_test.db')
        c = conn.cursor()

        query = """INSERT INTO positions
                 (position, description)
                 VALUES ('%s','%s')""" % (position, description)
        c.execute(query)
        conn.commit()

        c.close

        return redirect("/positions_new")

       
    else:
        return template('new_position.tpl')

@route('/departaments_new', method='GET')
def new_departaments():
    if request.GET.get('save','').strip():

        departament = request.GET.get('departament', '').strip()
        description = request.GET.get('description', '').strip()
        mather = request.GET.get('mather', '').strip()

        conn = sqlite3.connect('crm_test.db')
        c = conn.cursor()

        query = """INSERT INTO departaments
                   (departament, description, mather)
                   VALUES ('%s', '%s', '%s')""" % (departament, description, mather)
        c.execute(query)
        conn.commit()

        #c.execute("SELECT last_insert_rowid()")
        #new_id = c.fetchone()[0]
        c.close

        return redirect("/departaments_new")

        #return '<p>The new task was inserted into the database, the ID is %s</p>' %new_id

    else:
        return template('new_departaments.tpl')

debug (True)
run()
