from jinja2 import Template, escape

name = 'Bishkek'
age = 30

tm = Template('Hi{{name}}')
msg = tm.render(name=name)
print(msg)