import json
TDF = op.TDModules.mod.TDFunctions

document_format = parent().par.Fileformat

target_op = op(parent.MakeDocument.par.Component)

def scanOp(target):
	target_dict = {}
	name = target.name
	target_dict.update({'name': name, 'path': target.path})

	if target.comment:
		target_dict.update({'comment': target.comment})
		have_comment = True

	depth = TDF.parentLevel(op(parent.MakeDocument.par.Component), op(target.path))
	target_dict.update({'depth': depth})

	if target.family == 'COMP':
		readme_op = target.findChildren(name='*readme*', maxDepth=1)
		if len(readme_op):
			target_dict.update({'readme' :readme_op[0].text})
			have_readmeDAT = True

		screenshot_ops = target.findChildren(name='*screenshot*', maxDepth=1)
		if len(screenshot_ops):
			have_screenshot = True
			target_dict.update({'images': {}})
			image_dict = {}
			for i in range(len(screenshot_ops)):
				op(screenshot_ops[i]).save(parent().par.Outputfolder + '/images/' + op(screenshot_ops[i]).parent().name + '_' + screenshot_ops[i].name + parent().par.Imageformat, asynchronous=True, createFolders=True)
				image_dict[screenshot_ops[i].name] = 'images/' + op(screenshot_ops[i]).parent().name + '_' + screenshot_ops[i].name + parent().par.Imageformat
			target_dict['images'] = image_dict

		children_comps = target.findChildren(type=COMP, maxDepth=1)
		children_xops = []
		for xop in target.findChildren(comment='?*', maxDepth=1):
			if not xop.isCOMP: #search op without comp
				children_xops.append(xop)
		print(children_xops)

		children_ops = children_xops + children_comps

		if len(children_ops):
			children_list = []
			for child in children_ops:
				if child.isCOMP:
					if (child.comment != '') or (child.findChildren(name='*readme*') != []) or (child.findChildren(name='*screenshot*') != []) or (child.findChildren(comment='?*') !=[]):
						c = scanOp(child)
						children_list.append(c)
				else:
					c = scanOp(child)
					children_list.append(c)
			target_dict.update({'children': []})
			target_dict['children'] = children_list
	return target_dict

readme_dict = {}

readme_dict = scanOp(target_op)

readme_json = json.dumps(readme_dict, indent=2, ensure_ascii=False)

if document_format == 'md':
	op('createMarkdown').run(readme_json)
elif document_format == 'html':
	op('createHtml').run(readme_json)
elif document_format == 'json':
	op('createJson').run(readme_json)

