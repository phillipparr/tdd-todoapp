from todoapp import app

def test_home_page_header():
    client = app.test_client()
    rsp = client.get('/')
    assert rsp.status == '200 OK'
    html =rsp.get_data(as_text=True)
    assert '<title>Todo</title>' in html
    assert '<h1>Todo list</h1>' in html
    assert '<form>' in html
    assert '<input id=' in html