import pytest

def test_landing(client):
    landing = client.get('/')
    html = landing.data.decode()

    assert b'<form action="https://www.google.com/search" method="get" class="example">' in html 

    assert landing.statu_code == 200

def test_landing_aliases(client):
    landing = client.get('/')

    assert client.get('/home').data == landing.data    