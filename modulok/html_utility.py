def correct_html(title,content):
    return"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{}</title>
</head>
<body>
{}
</body>
</html>""".format(title,content)