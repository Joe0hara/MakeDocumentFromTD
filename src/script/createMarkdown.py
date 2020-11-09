import ast
import re

result_md = op('result_md')

result_text = ''

readme_json = args[0]

def scanDict(dict_data):

	object_text = ''
	# set header
	header_level = min(dict_data['depth']+1, 6)
	object_text += '#'*header_level + ' ' + dict_data['name'] + '\n\n'

	# set path
	path = dict_data['path']
	object_text += 'path: ' + path + '\n\n'

	# set comment
	if 'comment' in dict_data:
		object_text += convertURLforMD(dict_data['comment']) + '\n\n'

	# set readme
	if 'readme' in dict_data:
		object_text += convertURLforMD(dict_data['readme']) + '\n\n'

	# set images
	if 'images' in dict_data:
		for k, v in dict_data['images'].items():
			object_text += '![' + k + '](' + v + ')' + '\n'
		# object_text += '\n'

	# exclude no contents, set only header
	if not (('images' in dict_data) or ('comment' in dict_data) or ('readme' in dict_data)):
		object_text = '#'*header_level + ' ' + dict_data['name'] + '\n\n'

	object_text += '\n'

	# set children
	if 'children' in dict_data:
		for child in dict_data['children']:
			object_text += scanDict(child)
	return object_text

def convertURLforMD(readme_text):
	fixed_readme = readme_text

	# convert URL for md
	url_pattern = "https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
	match_str = re.search(url_pattern, fixed_readme)
	if match_str:
		url = match_str.group()
		fixed_readme = readme_text.replace(url, '[' + url + ']' + '(' + url + ')')

	return fixed_readme

readme_dict = ast.literal_eval(readme_json)

result_md.text = scanDict(readme_dict)