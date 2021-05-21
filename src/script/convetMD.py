# convert md for td

import re

def onSetupParameters(scriptOp):
	page = scriptOp.appendCustomPage('Custom')

	return

def onPulse(par):
	return

def checkContent(content):
	if len(content.rstrip()):
		replace_list = [['text', content.rstrip(), '']]
	else:
		replace_list = []

	# check header
	header_pattern = '^#+\s'
	header_match = re.search(header_pattern, content)
	if header_match:
		header_name = re.sub(header_pattern, '', content)
		header_level = header_match.end() - 1
		replace_list = [['h' + str(header_level), header_name]]

	# check Horizontal Rules
	horizontal_pattern = '---'
	horizontal_match = re.match(horizontal_pattern, content)
	if horizontal_match:
		replace_list = [['h_rules', content]]

	# check path
	path_pattern = '^path:\s'
	path_match = re.match(path_pattern, content)
	if path_match:
		path = re.sub(path_pattern, '', content)
		replace_list = [['op_path', path, path]]

	# check media
	media_pattern = '\!\[.*\]\(.*\)'
	media_match = re.match(media_pattern, content)
	if media_match:
		media_content = media_match.group()
		anchor_text = re.sub('\!\[|\]', '', re.match('\!\[.*\]', media_content).group())
		link_text = re.sub('\(|\)', '', re.search('\(.*\)', media_content).group())
		replace_list = [['media', anchor_text, link_text]]

	# check link
	url_pattern = 'https?://[\w/:%#\$&\?\(\)~\.=\+\-]+'
	url_match = re.search(url_pattern, content)

	if url_match:
		url_str = url_match.group()

		markdown_url_pattern = "\[.*\]\(https?://[\w/:%#\$&\?\(\)~\.=\+\-]+\)"
		match_str = re.search(markdown_url_pattern, content)

		replace_list = []
		for i in content.replace(match_str.group(), '\n' + match_str.group() + '\n').split():
			link_match = re.match('\[.*\]', i)
			if link_match:
				anchor_text = re.sub('\[|\]', '' , re.match('\[.*\]', i).group())
				link = url_str
				replace_list.append(['link', anchor_text, link])
			else:
				replace_list.append(['text', i.rstrip(), ''])
	checked_content = replace_list
	return checked_content

def onCook(scriptOp):
	content_list = []
	for i in range(scriptOp.inputs[0].numRows):
		content_list.append(scriptOp.inputs[0][i,0].val)
	scriptOp.clear()
	scriptOp.appendRow(['type', 'string', 'link'])

	for contents in content_list:
		c = checkContent(contents)
		for i in c:
			scriptOp.appendRow(i)

	return
