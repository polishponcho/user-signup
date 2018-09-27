from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

signup_form = """
<!DOCTYPE html>

<html>
    <head>
    <h1> Signup</h1>
        <style>
           .error {{ color: red; }}
          
        </style>
    </head>
    <body>
        <form action="/validate_signup" method="POST">
            <label for="user">Username
            <input id="user" type="text" name="user" value='{user}'/></label>
            <p class="error">{username_error}</p>

            <label for="password">Password
            <input id="password" type="password" name="password" value="{password}"/></label>
            <p class="error">{password_error}</p>


            <label for="verify">Verify Password
            <input id="verify" type="password" name="verify" value="{verify}"/></label>
            <p class="error">{verify_error}</p>

            <label for ="email">Email (optional)
            <input id="email" type="text" name="email" value="{email}"/></label>
            <p class="error">{email_error}</p>
            <input type="submit" />

        </form>
    </body>
</html>
"""

@app.route('/')
def index():
    return signup_form.format(user='', username_error='', password='', password_error='', verify='', verify_error='', email='', email_error='')

@app.route('/validate_signup', methods=['POST'])
def display_signup_form():

    user = request.form['user']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    space = ' '
    period = '.com'
    at = '@'
   #username error 

    def is_space(str):
        try:
            str.index(space)
            return True
        except ValueError:
            return False

    def is_at(str):
        try:
            str.index(at)
            return True
        except ValueError:
            return False


    if is_space(user) == True:
        username_error = 'No Spaces'
        user = ''
    else:
        if len(user) < 3 or len(user) > 20:
            username_error = 'Not a valid username'
            user = ''

    #password error
     
    if is_space(password) == True:
        password_error = 'No Spaces'
        password = ''
    elif (password != verify) == True:
        password_error = 'Passwords do not match'
        password = ''
    else:
        if len(password) < 3 or len(password) > 20:
            password_error = 'Not a valid password'
            password = ''

    #verify error
    '''
    if (password != verify) == True:
        verify_error = 'Passwords do not match'
        verify = ''
    '''
    
    if len(verify) < 3 or len(verify) > 20:
        verify_error = 'Not a valid password'
        verify = ''

    #email errors
    #add optional
    if len(email) == 0:
        email_error = ''
    elif (len(email) < 3 or len(email) > 20):
        email_error = "Invalid email"
        email = ''
    
    elif is_space(email) == True:
        email_error = 'No Spaces'
        email = ''

    elif not is_at(email):
        email_error = 'Requires @'
        email = ''

    elif email.endswith(period) == False:
        email_error = 'Must contain .'
        email = ''
    
    else:
        if len(email) < 3 or len(email) > 20: 
            email_error = "Invalid email"
            email = ''

    if not username_error and not password_error and not verify_error:
        return "Welcome, " + user
    else:
        return signup_form.format(username_error=username_error, user=user, password_error=password_error, password=password, verify_error=verify_error, verify=verify, email_error=email_error, email=email)

'''
@app.route('/validate_signup', methods=['POST'])
def validate_signup():
'''



app.run()