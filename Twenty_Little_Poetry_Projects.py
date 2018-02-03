#Twenty Little Poetry Projects is a prompt created by Jim Simmerman published in The Practice of Poetry:

#“Give each project at least one line. You should open the poem with the first project, and close it with the last, but otherwise use the projects in whatever order you like. Do all twenty. Let different ones be in different voices. Don’t take things too seriously.

listx = [
	'Say something specific but utterly preposterous',
	'Use at least one image for each of the five senses, either in succession or scattered randomly throughout the poem',
	'Use one example of synaethesia (mixing the senses)',
	'Use the proper name of a person and the proper name of a place',
	'Contradict something you said earlier in the poem',
	'Change direction or digress from the last thing you said',
	'Use a word (slang?) youve never seen in a poem',
	'Use a piece of false cause-and-effect logic',
	'Use a piece of "talk" youve actually heard (preferably in dialect and/or which you dont understand)',
	'Create a metaphor using the following construction: The (adjective) (concrete noun) of (abstract noun',
	'Use an image in such a way as to reverse its usual associative qualities',
	'Make the persona or character in the poem do something they could not do in "real life"',
	'Refer to yourself by nickname and in the third person',
	'Write in the future tense, such that part of the poem seems to be a prediction',
	'Modify a noun with an unlikely adjective',
	'Make a declaritive assertion that sounds convincing but finally makes no sense',
	'Use a phrase from a language other than english',
	'Make a nonhuman object say or do something human (personification)',
	]

import random

print('Begin the poem with a metaphor')

random.shuffle(listx)
for i in listx:
  print(i) 

print('Close the poem with a vivid image that makes no statement but "echoes" an image from earlier in the poem')
