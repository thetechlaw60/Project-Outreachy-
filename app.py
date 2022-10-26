from flask import Flask, render_template, url_for





app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html', greeting="Hello!")

          
@app.route('/lead')
def lead():
    return render_template('lead.html')



@app.route('/dash')
def dash():
    return render_template('dash.html')

def test(test_client):
    response = test_client.get('/home')
    assert b'<form action="https://www.google.com/search" method="get" class="example">' in response.data   
    

  

if __name__ == "__main__":
    app.run(debug=True)   