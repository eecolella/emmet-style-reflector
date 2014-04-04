# Emmet 
# Create anchors and references for easily move everywhere!
# Hosted at https://github.com/eecolella/GoToAnchor

import sublime, sublime_plugin
import urllib, urllib.parse, time, re, webbrowser, os 

class Node(dict):
	def __init__(self,s,p=None,i=''):
		self._parent=p
		self.selector='>' + s if (s!=None and # exclude root
									re.search('\.|\#|header|footer|script|style|link|meta|body|html',s)==None and # exclude ID, Class, header, etc
									len(s)>0) else s 
		self.childrens=[]
		self.indentation=i

	def addChildren(self,selector):
		indent = self.indentation + '\t' if self.selector != None else ''
		n = Node(selector,self,indent)
		self.childrens.append(n)
		return n

	def parent(self):
		if self._parent!=None:
			return self._parent
		else:
			return self

	def toString(self):
		childrens = ''

		for child in self.childrens:
			childrens += '\n%s\n' % (child.toString())		
		
		if self.selector==None or self.selector == '':
			return childrens
		else:
			return '%s%s {\n%s\n%s}' % (self.indentation, self.selector, childrens, self.indentation)

def generateTree(str):
	debug=False

	if debug:
		print("DEBUG generate-tree ## str init: %s" % str)
		counterDebug = 0


	tree = Node(None)
	selector = re.search('^[^\^|\>|\+]*',str).group(0)
	str = re.sub('^[^\^|\>|\+]*','',str)
	pointer = tree.addChildren(selector)
	groupMemory = []
	storePointerFlag = False

	while len(str)>0:

		if debug:
			counterDebug+=1
			print("DEBUG generate-tree ## str %s: %s" % (counterDebug, str))

		# operator = str[:1]
		# str = str[1:]

		operator = str[:1]
		if operator != ')':
			str = str[1:]
		else:
			operator = str[1:2]
			str = str[2:]
			pointer= groupMemory.pop()

		startGroup = str[:1]
		if startGroup == '(':
			# group = re.search('(?<=\()([\w|\>]*)(?=\))',str).group(0)
			# print('group: ', group)
			storePointerFlag = True
			str = str[1:]

		selector = re.search('^[^\^|\>|\+\)]*',str).group(0)
		str = re.sub('^[^\^|\>|\+\)]*','',str)
		if operator=='>':
			pointer = pointer.addChildren(selector)
		elif operator=='^':
			pointer = pointer.parent().parent().addChildren(selector)
		elif operator=='+':
			pointer = pointer.parent().addChildren(selector)

		if storePointerFlag:			
			groupMemory.append(pointer)
			storePointerFlag = False


	if debug:
		print("DEBUG generate-tree ## str final: %s" % str)

	return tree

class EmmetStyleReflector(sublime_plugin.EventListener):
	def on_text_command(self, view, command_name, args):
		debug = True
		if(command_name=='expand_abbreviation_by_tab'):

			if debug:
				print("\nDEBUG START emmet_style_reflector")

			line = view.lines(sublime.Region(view.sel()[0].begin(), view.sel()[0].begin()))[0]
			lineStr = view.substr(line).strip()

			sublime.status_message('#Emmet Style Reflector# Corresponding style of "%s" saved in clipboard (Ctrl/Super+V for paste)' % lineStr)
			# remove tag if there are class or id | delete element Multiplication | delete parameters | delete text
			lineStr = re.sub("\w*(?=[#,\.])|[\$\@\-\*]([|0-9]*)|\[(.*?)\]|\{(.*?)\}",'', lineStr)

			tree = generateTree(lineStr)
			result = tree.toString()
			result = re.sub("\n\n\n","\n", result)

			sublime.set_clipboard(result)



  