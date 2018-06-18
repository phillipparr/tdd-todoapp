from splinter import Browser

browser = Browser('chrome')
url = 'http://localhost:5000'
browser.visit(url)
assert 'Todo' in browser.title
header = browser.find_by_tag('h1').first
assert 'Todo list' in header.text

browser.quit()