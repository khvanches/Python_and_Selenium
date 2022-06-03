# Description

<p>The following repo related to UI testing with Python and Selenium based on
course <a href="https://stepik.org/course/575/syllabus">Stepik: Automation Testing</a>.
The repo contains two projects:
<ul>
    <li><strong>simple_shop_test</strong> - just a simple test of a shop. The main idea is to
use fixtures to choose language and browser</li>
    <li><strong>page_object_test</strong> - is an example of page object pattern. Also, fixtures, negative tests and custom
markers are used in this project </li>
</ul>
<p>

## How to store requirements for project

Store requirements:
<ul><em> pip freeze > requirements.txt</em></ul>

Install in your project:
<ul><em>pip install -r requirements.txt</em></ul>

## How to start tests
<ul>
    <li><strong>simple_shop_test:</strong> pytest --language=es test_items.py </li>
    <li><strong>page_object_test:</strong> pytest -v --tb=line --language=en -m need_review</li>
</ul>
Also, you can specify language by --language=YOUR_VARIANT or browser by browser_name=YOUR_VARIANT (firefox or chrome)