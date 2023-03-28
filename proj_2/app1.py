#step1 - to import FLASK
from flask import Flask, request

#step2- create the object with a parameter __name__
app=Flask(__name__)

#user_names=['Shilpi Rani','Shreya','Vandana Gupta','Sapna Kumari']

#step3 - create an END POINT using routes and bind them with a functionality
@app.route('/')
def home_page():
    return 'Welcome to HOME PAGE'

'''@app.route('/search', methods=['POST'])
 def search_page():
    return 'Welcome to SEARCH PAGE' '''


# it takes the user name in the query parameter from the URL, converts it to UPPER CASE and displays it on the browser
@app.route('/upper')
def uppercase():
    n = request.args.get('n')
    return (n.upper())

#dynamic route
'''@app.route('/in/<user>')
def profile_page(user):
    if user in user_names:
         return f"Welcome " 
    else:
        return "user name not found" '''
    
#step4 - run the app
if __name__=='__main__':
    app.run(debug=True)