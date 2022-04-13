from distutils.log import debug
from flask import Flask, render_template,request,redirect,session,Response,url_for,flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'educative'

# Intialize MySQL
mysql = MySQL(app)

@app.route('/auth-forgot-password-basic.html')
def auth_forgot_password_basic():
    return render_template('auth-forgot-password-basic.html')

@app.route('/auth-login-basic.html')
def auth_login_basic():
    return render_template('auth-login-basic.html')

@app.route('/auth-register-basic.html')
def auth_register_basic():
    return render_template('auth-register-basic.html')

@app.route('/cards-basic.html')
def cards_basic():
    return render_template('cards-basic.html')

@app.route('/extended-ui-perfect-scrollbar.html')
def extended_ui_perfect_scrollbar():
    return render_template('extended-ui-perfect-scrollbar.html')

@app.route('/extended-ui-text-divider.html')
def extended_ui_text_divider():
    return render_template('extended-ui-text-divider.html')

@app.route('/form-layouts-horizontal.html')
def form_layouts_horizonta():
    return render_template('form-layouts-horizontal.html')

@app.route('/form-layouts-vertical.html')
def form_layouts_vertica():
    return render_template('form-layouts-vertical.html')

@app.route('/forms-basic-inputs.html')
def forms_basic_inputs():
    return render_template('forms-basic-inputs.html')

@app.route('/forms-input-groups.html')
def forms_input_groups():
    return render_template('forms-input-groups.html')

@app.route('/icons-boxicons.html')
def icons_boxicons():
    return render_template('icons-boxicons.html')

@app.route('/index.html',methods=['GET', 'POST'])
def check_user():
    session.pop('login',None)  
    username=request.form['email-username']
    password=request.form['password']
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    mysql.connection.commit()
    res=cur.fetchall()
    global Flag
    Flag= False
    global user_type
    user_type = 0
    account_status=2
    for row in res:
        if (username==row[1] and password==row[4] and account_status==row[9]):
            user_type=row[8]
            Flag= True
            session['login']=True
            break

            # using the flag= True check for the user role
        
    if(Flag):
            if(user_type==0):
                #render admin dashboard
                # set user session as admin session
                return redirect('/admin-dashboard')
            elif(user_type==1):
                return redirect('/teacher-dashboard')
            elif(user_type==2):
                return redirect('/student-dashboard')
    else:
            # when the username or password is not found or when the account is not operational, then
            #redirect to the login page and display the error message
            session['login']=False
            return redirect('/')



            

@app.route('/admin-dashboard')
def admin_dashboard():
    return render_template('index_admin.html')

@app.route('/teacher-dashboard')
def teacher_dashboard():
    return render_template('index_teacher.html')

@app.route('/student-dashboard')
def student_dashboard():
    return render_template('index_student.html')

@app.route('/')
def index():
    return render_template('auth-login-basic.html')

@app.route('/user-register',methods=['GET','POST'])
def user_register():
    name=request.form['Name']
    register_num=request.form['RegisterNumber']
    email=request.form['email']
    phone=request.form['phoneNumber']
    password=request.form['Password']
    department=request.form['Department']
    country=request.form['Country']
    zipcode=request.form['zipCode']
    state=request.form['state']
    address=request.form['address']
    age=request.form['Age']
    role=2
    account_status=0
    cls=1
    cur=mysql.connection.cursor()
    cur.execute("INSERT INTO users(Name,Dept,Age,Password,email,phone,Address,Role,account_status,State,Country,Zipcode,Class,RegisterNum) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,department,age,password,email,phone,address,role,account_status,state,country,zipcode,cls,register_num))
    mysql.connection.commit()
    return redirect('/')

    # try:
    #     cur=mysql.connection.cursor()
    #     cur.execute("INSERT INTO users(Name,Dept,Age,Password,email,phone,Address,Role,account_status,State,Country,Zipcode,Class) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,department,age,password,email,phone,address,role,account_status,state,country,zipcode,cls,register_num))
    #     mysql.connection.commit()
    #     return redirect('/')
    # except mysql.IntegrityError:
    #     return redirect('/user-register')
    # finally:
    #     return redirect('/')

    






@app.route('/layouts-blank.html')
def ayouts_blank():
    return render_template('layouts-blank.html')

@app.route('/layouts-container.html')
def ayouts_container():
    return render_template('layouts-container.html')

@app.route('/layouts-fluid.html')
def ayouts_fluid():
    return render_template('layouts-fluid.html')

@app.route('/layouts-without-menu.html')
def ayouts_without_menu():
    return render_template('layouts-without-menu.html')

@app.route('/layouts-without-navbar.html')
def ayouts_without_navbar():
    return render_template('layouts-without-navbar.html')

@app.route('/pages-account-settings-account.html')
def pages_account_settings_accoun():
    return render_template('pages-account-settings-account.html')


@app.route('/edit-account')
def editaccount():
    # fetching the id
    rid=request.args.get('rid')
    # fetching details of the account
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Id=%s",rid)
    res=cur.fetchall()
    mysql.connection.commit()
    return render_template('pages-account-settings-edit.html',rlist=res)

@app.route('/update-account',methods=['GET', 'POST'])
def updateaccount():
    rid=request.args.get('rid')
    name=request.form['Name']
    register_num=request.form['RegisterNumber']
    email=request.form['email']
    phone=request.form['phoneNumber']
    password=request.form['Password']
    department=request.form['Department']
    country=request.form['Country']
    zipcode=request.form['zipCode']
    state=request.form['state']
    address=request.form['address']
    role=request.form['Role']
    account_status=2
    cls=1
    try:
        cur=mysql.connection.cursor()
        cur.execute("UPDATE users SET Name=%s,Dept=%s,Password=%s,email=%s,phone=%s,Address=%s,Role=%s,account_status=%s,State=%s,Country=%s,Zipcode=%s,Class=%s WHERE Id=%s",name,department,password,email,phone,address,role,account_status,state,country,zipcode,cls,register_num,rid)
        mysql.connection.commit()
        return redirect('/pages-account-settings-connections.html')
    except mysql.IntegrityError:
        return redirect('/pages-misc-error.html')
    finally:
        return redirect('/pages-account-settings-connections.html')

   
@app.route('/admin-user-register',methods=['GET', 'POST'])
def admin_user_register():
    name=request.form['Name']
    register_num=request.form['RegisterNumber']
    email=request.form['email']
    phone=request.form['phoneNumber']
    password=request.form['password']
    department=request.form.get('Department')
    country=request.form.get('Country')
    zipcode=request.form['zipCode']
    state=request.form['state']
    address=request.form['address']
    role=request.form.get('Role')
    account_status=2
    cls=1

    try:
        cur=mysql.connection.cursor()
        cur.execute("INSERT INTO users(Name,Dept,Password,email,phone,Address,Role,account_status,State,Country,Zipcode,Class,RegisterNum) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,department,password,email,phone,address,role,account_status,state,country,zipcode,cls,register_num))
        mysql.connection.commit()
        return redirect('/pages-account-settings-account.html')
    except mysql.IntegrityError:
        print(mysql.integrity_error)
    # finally:
    #     return redirect('/pages-misc-error.html')


@app.route('/pages-account-settings-edit.html')
def pages_account_settings_edit():
     return render_template('pages-account-settings-edit.html')



@app.route('/pages-account-settings-connections.html')
def pages_account_settings_connections():
    # fetching details of all students
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Role=2 AND account_status=2")
    res=cur.fetchall()
    mysql.connection.commit()

    # fetching details of faculty
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE Role=1 AND account_status=2")
    tres=cur.fetchall()
    mysql.connection.commit()

    return render_template('pages-account-settings-connections.html',slist=res,tlist=tres)

@app.route('/pages-account-settings-notifications.html')
def pages_account_settings_notifications():
    # fetching details of users in the users table with account_status 1
    cur=mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE account_status=1")
    res=cur.fetchall()
    mysql.connection.commit()
    return render_template('pages-account-settings-notifications.html',rlist=res)

@app.route('/delete-account')
def deleteaccount():
    # fetching the id
    rid=request.args.get('rid')
    # deleting the account with the corresponding id
    cur=mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE Id=%s",rid)
    mysql.connection.commit()
    return(redirect(url_for('pages_saccount_settings_notifications')))

@app.route('/approve-account')
def approveaccount():
    # fetching Id
    rid=request.args.get('rid')
    cur=mysql.connection.cursor()
    cur.execute(" UPDATE users SET account_status=2 WHERE Id=%s",rid)
    mysql.connection.commit()
    return(redirect(url_for('pages_account_settings_notifications')))






@app.route('/pages-misc-error.html')
def pages_misc_error():
    return render_template('pages-misc-error.html')

@app.route('/pages-misc-under-maintenance.html')
def pages_misc_under_maintenance():
    return render_template('pages-misc-under-maintenance.html')

@app.route('/tables-basic.html')
def ables_basic():
    return render_template('tables-basic.html')

@app.route('/ui-accordion.html')
def ui_accordion():
    return render_template('ui-accordion.html')

@app.route('/ui-alerts.html')
def ui_alerts():
    return render_template('ui-alerts.html')

@app.route('/ui-badges.html')
def ui_badges():
    return render_template('ui-badges.html')

@app.route('/ui-buttons.html')
def ui_buttons():
    return render_template('ui-buttons.html')

@app.route('/ui-carousel.html')
def ui_carouse():
    return render_template('ui-carousel.html')

@app.route('/ui-collapse.html')
def ui_collapse():
    return render_template('ui-collapse.html')

@app.route('/ui-dropdowns.html')
def ui_dropdowns():
    return render_template('ui-dropdowns.html')

@app.route('/ui-footer.html')
def ui_footer():
    return render_template('ui-footer.html')

@app.route('/ui-list-groups.html')
def ui_list_groups():
    return render_template('ui-list-groups.html')

@app.route('/ui-modals.html')
def ui_modals():
    return render_template('ui-modals.html')

@app.route('/ui-navbar.html')
def ui_navbar():
    return render_template('ui-navbar.html')

@app.route('/ui-offcanvas.html')
def ui_offcanvas():
    return render_template('ui-offcanvas.html')

@app.route('/ui-pagination-breadcrumbs.html')
def ui_pagination_breadcrumbs():
    return render_template('ui-pagination-breadcrumbs.html')

@app.route('/ui-progress.html')
def ui_progress():
    return render_template('ui-progress.html')

@app.route('/ui-spinners.html')
def ui_spinners():
    return render_template('ui-spinners.html')

@app.route('/ui-tabs-pills.html')
def ui_tabs_pills():
    return render_template('ui-tabs-pills.html')

@app.route('/ui-toasts.html')
def ui_toasts():
    return render_template('ui-toasts.html')

@app.route('/ui-tooltips-popovers.html')
def ui_tooltips_popovers():
    return render_template('ui-tooltips-popovers.html')

@app.route('/ui-typography.html')
def ui_typography():
    return render_template('ui-typography.html')

if __name__ == '__main__':
    app.secret_key = 'super secret key'
    app.run(debug=True)