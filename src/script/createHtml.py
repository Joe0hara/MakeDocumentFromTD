import ast
import re

result_html = op('result_html')

result_text = ''

readme_json = args[0]

start_text = '''<html>
<head></head>
<body>
'''
close_text = '''
</body>
</html>
'''

custom_css = '''<style type="text/css">
	img {
		width: 100%;
		max-width: 750px;
		text-align: center;
		height: auto;
	}
</style>
'''

def scanDict(dict_data):
	global result_text

	child_text = ''
	children_dict = {}

	## set header
	header_level = min(dict_data['depth']+1, 6)
	child_text =  '<h' + str(header_level) + '>' + dict_data['name'] + '</h' + str(header_level) + '>\n\n'

	# set images
	if 'images' in dict_data:
		for image in dict_data['images'].values():
			child_text += '<img src="' + image + '"/>' + '\n'
		child_text += '\n'

	# set comment
	if 'comment' in dict_data:
		child_text += '<p>' + checkReadme(dict_data['comment']) + '</p>\n\n'

	# set readme
	if 'readme' in dict_data:
		child_text += '<p>' + checkReadme(dict_data['readme']) + '</p>\n\n'

	if not (('images' in dict_data) or ('comment' in dict_data) or ('readme' in dict_data)):
		child_text = '<h' + str(header_level) + '>' + dict_data['name'] + '</h' + str(header_level) + '>\n\n'

	result_text += child_text

	if 'children' in dict_data:
		for child in dict_data['children']:
			scanDict(child)
	return

def checkReadme(readme_text):
	fixed_readme = readme_text

	fixed_readme = fixed_readme.replace('\n', '<br/>\n')

	# convert URL for html
	url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
	match_str = re.search(url_pattern, readme_text)
	if match_str:
		url = match_str.group()
		fixed_readme = readme_text.replace(url, '<a href=' + url + '>' + url + '</a>')

	return fixed_readme

result_text += start_text

readme_dict = ast.literal_eval(readme_json)

scanDict(readme_dict)

result_text += custom_css
result_text += close_text

result_html.text = result_text