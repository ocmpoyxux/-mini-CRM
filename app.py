import sqlite3
from bottle import route, run, debug, template, request

@route('/users')
def users_list():
    pass

@route('/departaments', method='GET')
def departaments_list():
    pass

@route('/positions', method='GET')
def positions_list():
    pass

@route('/users_new', method='GET')
def new_users():
    
    if request.GET.get('save','').strip():

        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        query = "INSERT INTO todo (task,status) VALUES ('%s',1)" %new
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
        conn = sqlite3.connect('/home/v.ostrouhih/miniCRM/crm_test.db')
        c = conn.cursor()

        query = "INSERT INTO positions (position, description) VALUES ('%s','%s')" % (position, description)
        c.execute(query)
        conn.commit()

        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        c.close

        return '<p>The new task was inserted into the database, the ID is %s</p>' %new_id

    else:
        return template('new_position.tpl')

@route('/departaments/new', method='GET')
def new_departaments():
    if request.GET.get('save','').strip():

        new = request.GET.get('task', '').strip()
        conn = sqlite3.connect('todo.db')
        c = conn.cursor()

        query = "INSERT INTO todo (task,status) VALUES ('%s',1)" %new
        c.execute(query)
        conn.commit()

        c.execute("SELECT last_insert_rowid()")
        new_id = c.fetchone()[0]
        c.close

        return '<p>The new task was inserted into the database, the ID is %s</p>' %new_id

    else:
        return template('new_departaments.tpl')

debug (True)
run()


