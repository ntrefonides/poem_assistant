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


metaphor = ['The land is a forest green dumpster', 'the ocean is a clogged toilet']
something_specific_but_utterly_preposterous = ["piss on a tree but look back cracked your neck", "trip on a stump and fall into a dumpster"]
one_image_for_each_of_the_five_senses = ["sudden fog of the ass sudden wind on my spine, shallow in the bitter pool", "sucking clouds into my nose blowing smoke from out my mouth into the childs ear"]
synaesthesia = ["the pain can see","dry cracking mouth salivates sour"]
the_proper_name_of_a_person_and_the_proper_name_of_a_place = ["Dave Archambault II leads the Standing Rock Sioux","Hernan Cortez a man of God conquers Tenochtitlan"]
#the following project will be a contradiction whether it occurs earlier or later in the poem
contradict_something_from_the_first_five_projects_of_original_prompt = ["the pain is blind","nectar of the mossy river"]
#the following is so unrelated that is gauranteed to be a change in direction
change_direction = ["a sinkhole swallows all, belches dust","1,000,000,000 years later... "]
slang = ["Smoke me down","Smoke me up"]
false_cause_and_effect_logic = ["If you jump, then you'll fly","drowning in the air"]
talk_from_dialect_or_which_you_dont_understand = ["bust that clam stand","How close do you live to your family?"]
the_adjective_concretenoun_of_abstractnoun = ["the spotted duck of honor","the hairless bear of pride"]
reverse_usual_associative_properties_of_image = ["Athena's nappy hair in drains"," "]
#for this project, the simplest way of solving is make myself do something do something i couldnt do in real life because self is a persona of every poem
something_i_couldnt_do_in_real_life = ["I'm hunting with a pack of wolves","I'm ordering a nuclear strike"]
refer_to_yourself_by_nickname_and_in_the_third_person = ["Nicky Rose pours himself a glass of wine","Nick dropped his face"]
write_in_the_future_tense = ["the brain will dry and flood","I will lock up all my gold"]
modify_a_noun_with_an_unlikely_adjective = ["dull star", "rosey trash can"]
declaritive_assertion_that_sounds_convincing_but_finally_makes_no_sense = ["drink the salt water","hold your breath and never let go"]
phrase_from_a_language_other_than_english = ["tldr?","lmfao"]
personification = ["tearful book", "squeeling knees"]
image_that_makes_no_statement_but_echoes_an_image_from_earlier_in_the_poem = ["the tree is wilting", "the waves say goodbye"]
     

setlist = [something_specific_but_utterly_preposterous,
	one_image_for_each_of_the_five_senses, 
	synaesthesia, 
	the_proper_name_of_a_person_and_the_proper_name_of_a_place, 
	contradict_something_from_the_first_five_projects_of_original_prompt, 
	change_direction, 
	slang, 
	false_cause_and_effect_logic, 
	talk_from_dialect_or_which_you_dont_understand, 
	the_adjective_concretenoun_of_abstractnoun, 
	reverse_usual_associative_properties_of_image, 
	something_i_couldnt_do_in_real_life, 
	refer_to_yourself_by_nickname_and_in_the_third_person, 
	write_in_the_future_tense, 
	modify_a_noun_with_an_unlikely_adjective, 
	declaritive_assertion_that_sounds_convincing_but_finally_makes_no_sense, 
	phrase_from_a_language_other_than_english, 
	personification]


#important the random function
import random



#This will randomly order the projects
#print('Begin the poem with a metaphor')

#random.shuffle(listx)
#for i in listx:
 # print(i) 

#print('Close the poem with a vivid image that makes no statement but "echoes" an image from earlier in the poem')


print(random.choice(metaphor))
random.shuffle(setlist)
for i in setlist:
  print(random.choice(i))
print(random.choice(image_that_makes_no_statement_but_echoes_an_image_from_earlier_in_the_poem))




