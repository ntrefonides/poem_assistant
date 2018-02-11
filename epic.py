
#rhyming




A = ["take me to the mountain gate","whom the higher crows berate","I'm gangly with a gangly gate", "the gun it triggered late"]
B = ["left to fancy the decay", "the mountain man, the mounting way","there's a bucket there's beday","there is nothing i wont say"]
C = ["in the ocsillating sky", "your the cabbage of my sty", "fadad with the jaded die","another truths another lie"]
D = ["damn the moon to craters","fuck boy I'm a hater", "waiting on the waiters"]
E = ["lost in all directions", "searching for the loser section", "I'll find my spleen in this disection"]
F = ["I'm gone with wind and snow", "lost but I didnt know", "I told her that I'll never show"]
G = ["glancing at my compass", "peter piped her pompass", "this baby lumps a lumpus"]
H = ["gliding in the dark", "bless the fuckin' narc", "steal the donkeys from the arc"]
I = ["I've died I'll die again", "these eggs their hatching hens", "who what where why when"]

#A = ["Think of sweet and chocolate,", "left to follow or to fate,","Whom the lower gods berate"]
#B = ["Whom the higher gods forgot,","What was never and is not","What is ever and is not","Buxom berries beyond rot,"," "
#C = ["Fancying on the featherbed","Physical and underfed","Littering the little head","Light upon the featherbed","Pretty tatters blue and red" ]
#D = ["Western clouds and quarter-stars","Fairy-sweet of old guitars" ]
#E = ["Think of ripe and rompabout,","Who shall rub her secrets out" ]
#F = ["All her harvest buttoned in,","Waiting for the paladin","Watching for the paladin","With a dimple in his chin" ]
#G = ["All her ornaments untried;","Prosperous and ocean-eyed","And behold the hinted bride" ]
#H = ["Which no woman ever had,","Paradisaical and sad"," "Ruralist and rather bad"]
#I = ["And the mountains in the mind;","Cosmopolitan and kind.","
#J = ["Think of thaumaturgic lass","Looking in her looking-glass" ]
#K = ["At the unembroidered brown;", "Taming all that anger down", ]
#LM = ["Printing bastard roses there","Then emotionally aware","Of the black and boisterous hair"," "
#N = ["And a man of tan engages","Eats th green by easy stages,","But no ravishment enrages.","
#O = ["For the springtime of her pride","No dominion is defied  "
#P = ["Nibbles at the root beneath","With intimidating teeth"," " ]
#Q = ["Narrow master master-calls;","Roisters through her, gnaws the walls,","And consumes her where she falls" ]
#R = ["Cavalierly on his brow.","And the godhead glitters now"," "
#S = ["What a hot theopathy","In her gilt humility.","Stutter. Where the reveille","Is staccato majesty.","The hunched hells across the sea."  ]
#T = ["How he postures at his height;","Contemplating by cloud-light" ]
#U = ["Unfamiliar, to be sure,","With celestial furniture","Trying if the pomp be pure"
#V = ["His bejewelled diadem;","As for jewels, counting them,"
#W = ["In the beam his track diffuses","Like a nun of crimson ruses","For the path his pocket chooses;"," " ]
#X = ["Down her dusted demi-gloom","Leads her to a lowly room.","Not that woman! (Not that room!","Not that dusted demi-gloom!)]
#Y = ["Which she makes a chapel of","Where she genuflects to love","Or the dolour of a dove"]
#Z = ["All the prayerbooks in her eyes","Open soft and sacrifice","Hieroglyphics of her eyes","Blink upon a paradise"]
#AA = ["Tender candles ray by ray","Warm and gratify the gray"]
#BB = ["Silver flowers fill the eves","And her set excess believes","Spits upon the silver leaves.","Denigrates the dainty eves","Dear dexterity achieves."]
#CC = ["Of the metamorphosis","Sicken off to hit-or-miss"]
#DD = ["Incorruptibly that no","Silver has to gape or go,","Deviate to underglow,","Throws to columns row on row","Then to marches. Then to know"]
#EE = ["Doomer, though, cresendo-comes","Prophesying hecatombs."]
#FF = ["Surrealist and cynical.","Garrulous and gutteral.",""]
#GG = ["Names him. Tames him. Takes him off","Where he makes the rifles cough,","With his helmet's final doff","Soldier lifts his power off."]
#HHII = ["Vaunting hands are now devoid","Paralyzed and paranoid"
#JJ = ["But idea and body too", "Clamor Skirmishes can do.", "Then he will come back to you."]
#KK = ["Less than ruggedly he kindles","Hies he home, the bumps and brindles"]
#LL = ["Pallors into broken fire.","Of his rummage of desire","Tosses to her lap entire."]
#MM = ["Hearing still such eerie stutter.","Caring not if candles gutter."]
#NN = ["Tan man twitches: for for long", "Little as an inch of song," ]
#OO = ["Life was little as a sand,", "Little as the aching hand","Little as a drop from grand"]
#PP = ["That would fashion mountains, such", "When a heart decides "Too much!--",  ]
#QQ = ["Yet there was a drama, drought","Retch and wheeling and cold shout,"
#RR = ["Scarleted about the brim","Not with blood alone for him,",]
#SS = ["Flood, with blossom in between","Suffocation, with a green","Moist sweet breath for mezzanine."]
#TT = ["Hometown hums with stoppages.","And this white and greater chess"]
#UU = ["Now the doughty meanings die","That observe the funny fly","Till the stickum stops the cry.","Chases stilts and straps to vie","With reession of the sky."]
#VV = ["As costumery from streets.","Baffles tan man. Gone the heats"]
#WW = ["Soldier bare and chilly then","Wants his power back again","Before quick-feast quick famish Men"
#XX = ["No confection languider","Than the candy crowns that were"]
#YY = ["Hunts a further fervor now."Stiffens: yellows: wonders how"]
#ZZ = ["Chases root and vehemence,"Shudders for his impotence""Woman fits for recompense"]
#a = ["Nothing limpid, nothing meek.","But a gorgeous and gold shriek","With her tongue tucked in her cheek,"]
#b = ["Hissing gauzes in her gaze,","Coiling oil upon her ways"]
#c = ["Gets a maple banshee. Gets","Oh those violent vinaigrettes!"
#d = ["A sleek slit-eyed moan.","Oh bad honey that can hone","Oilily the bluntest stone!"
#e = ["Oh mad bacchanalian lass","That his random passion has!"]
#
#
#
#















#creates a seven line stanza with randomly selected rhyme scheme consisting of any combination of A, B, and C rhymes
import random 




all_lines = [A,B,C,D,E,F,G,H,I] 
length_stanza =7
number_of_stanzas = 1


for n in range (number_of_stanzas):
  rhyme_set = random.sample(all_lines,3)
  print('\n') 
  for n in range (length_stanza):
    i = random.choice(rhyme_set)
    if len(i) > 0:
      random.shuffle(i)
      print(i[-1])
      del i[-1]


print(
"Running through the rain \n and sandy path forest \n to gooseberry point \n Gus the Boston Terrier \n was alive again alongside me \n at 4am this morning his heart burst \n in my mother's lap\n his grey-blue eyes closed \n like collapsing sky") 
