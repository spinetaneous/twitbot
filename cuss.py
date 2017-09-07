"""
* a dictionary of all the swear words that the bot will censor
* each entry is in the following format:
    swear : [list, of, replacement, words]
* the order matters! words that contain other words are placed higher
"""
#FIXME when tweeting @ ppl using many swear words say "your mother would be ashamed"

words = {
"hella" : ["a hecka lotta"],
"hell" : ["heck", "h-e-double-hockey-sticks"],
"fuck" : ["frick", "fudge"],
"shitty" : ["unfortunate in a poopy manner"],
"shithead" : ["buttlips"],
"shit" : ["turd", "shoot", "sheesh"],
"crap" : ["doodoo", "caca", "poopoo", "poopie"],
"bitch" : ["lil honey biscuit", "bacon bit"],
"bastard" : ["booger snot", "fartknocker"],
"tf" : ["the heckle"],
"af" : ["as frick"],
"mf" : ["biscuit eater"],
"wtf" : ["kiss my grits", "heavens to betsy", "shut the front door", "what the devil"],
"wth" : ["gee whiz", "geeze louise", "gee whillikers"],
"cunt" : ["pleasure orb", "clam tongue"],
"pussy" : ["snatch", "beaver", "vajayjay"],
"dick" : ["long boi", "donger", "ding-dong", "pleasure rod", "yogurt slinger"],
"ass" : ["butt", "booty"],
"nigger" : ["african american brother"],
"nigga" : ["darker skinned comrade"], #racism is bad
"faggot" : ["wigglin' wuss"],
"gangbang" : ["entourage barrage"]
}
