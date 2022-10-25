from flask import Flask, render_template, url_for
import pytest




app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html', greeting="Hello!")

@pytest.fixture
def captured_template(app):
    recorded = [] 

    def record(sender, templates, context):
        recorded.append((templates, context))

    templates_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        templates_rendered.disconnect(record, app)   


def test(test_client, captured_template):
    response = test_client.get('/home')

    assert len(captured_template) == 1

    templates, context = captured_template[0]

    assert templates.name == 'home.html'
    assert 'greeting' in context
    assert context['greeting'] == 'Hello!'           

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