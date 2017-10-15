newFile = open('index.html', 'w', encoding="utf-8")
newFile.write('''
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8"/>
<title>Python File</title>
</head>
<body>
<h1>Hello World made in Python</h1>
</body>
</html>
''')
newFile.close()
