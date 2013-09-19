label chapter1:
    $ kirinoname = "Kirino"
    
    scene black
    
    "I screwed up big time."
    
    "There is no way she will forgive me for this."
    
    "All it took to ruin her modeling career was a simple suggestion to play an online game together."

    scene bg kyosuke room
    with dissolve

    "Oddly enough Kirino actually agreed to play with me."
    
    "Surprising me further was the fact that she managed to reserve, at the last minute, a NerveGear unit and a copy of the game Sword Art Online using her contacts in modeling."
    
    "If the news was to be believed, all 10,000 copies had been sold since the game went on sale yesterday.  Some people had been waiting in line for four days just to get a copy."
    
    "I did want to play, but I wasn't that crazy about it."
    
    "Still, I was pretty lucky I suppose.  Yesterday after visiting several stores and waiting in line for each one, I happened upon a copy as well."
     
    "I guess the moral of this story is that if I just had the looks, I would not have needed to waste an entire Saturday waiting in line."
    
    "Heh...yeah, right."
    
    #"Last night, Kirino helped me install Sword Art Online into my Nerve Gear last night."
    
    "Kirino returned a little before noon today.  She had been out visiting her friends earlier.  Right now we were in our respective rooms, waiting for the servers to come online at 1PM."
    
    "With nothing better to do, I scrolled to the next page of the manual before looking at the alarm clock on my desk.  10 minutes left."
    
    "Little did I, Kyosuke Kosaka, know that this spur-of-the-moment decision would probably be the worst mistake of my life."
    
    # scene change
    
    scene bg starting city
    with dissolve
    
    stat "Floor 1. «Starting City»\n\nParty Members:\n Kyosuke (Lvl 1)\n\nCol: 200"
    
    show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350]])
    
    $hb_kirino.health = 100

    kir "Where are you?!"
    
    "I had a message from Kirino the moment that I logged in.  Character creation had taken some time but I thought I looked pretty cool."
    
    "It took me a moment to figure out how to reply."
    
    kyo "I don't know.  There's a fountain nearby."
    
    kir "Come to the bridge."
    
    "Bridge?  What bridge? Glancing around, I soon caught a glimpse of what looked like a lake.  Where there's water, there's going to be a bridge, right?"
    
    "And then I found my first problem."
    
    "Walking is a simple process where one foot is placed in front of the other, right?"
    
    "Let's see then.  Take one step and..."
    
    "...faceplant.  Wonderful." with Shake((0, 0, 0, 0), 0.3, dist=30) 
    
    "Despite being surprisingly informative, it turns out that reading the manual was no substitute for learning how to walk in the virtual world."
    
    show kirino avatar annoyed at left with noisedissolve
    #hide kirino with noisedissolve
    
    
    "I found her waiting angrily next to a small duck.  Or at least I thought it was her.  The person that I ended up meeting was a bishounen with blue hair."
    
    $ kirinoname = "Boy"
    
    kir "What kept y-"
    
    $hb_kirino.setHealth(30)
    
    "There was an awkward pause as the boy standing in front of me looked me up and down several times before he started laughing."
    
    kir "Ahahaha"
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350], ['Kirino', 100] ])
    
    "...I'm pretty certain that this is Kirino."
       
    $ kirinoname = "Kirino"
    
    kir "Tha-That's your avatar, Aniki?"
    
    kyo "What do you mean?  What's wrong with it?"
    
    kir "Noth-*snrk*-ing ~"
    
    "I don't get it. Was it the rugged stubble on the chin?  Was it the bandanna? I thought it looked cool.  There was something I was even more curious about however..."
    
    kyo "So, why a guy?"
    
    kir "Eh?"
    
    "I gestured at her avatar."
    
    kyo "Do you secretly wish to be a guy or something?"
    
    kir "What?  No!  Gross!  It's like this so I can play the role of an Oniichan once I find a little sister."
    
    "Sigh...I figured as much."
    
    kyo "Whatever.  Let's get started.  But first..."
    
    kir "What's this?"
    
    kyo "[[Kirino denied your party request]?  Huh?"
    
    "I tried again."
    
    kyo "[[Kirino denied your party request]. Why?"
    
    "I looked up at her.  She looked a bit strange."
    
    kir "Because..."
    
    kyo "Because?"
    
    kir "Ahh!  Forget it!  No, just no!"
    
    kyo "..."
    
    "When we first logged into the game Sword Art Online we were awestruck at the beauty of this world called Aincrad."
    
    "We cheerfully wandered the markets looking at all the merchandise admiring the detail of everything."
    
    "As we arrived at a weapons vendor Kirino picked up a beginner's dagger that gleamed in the sunlight."
    
    "After looking at the different swords I picked out a well-balanced bastard sword that had watermarks along the blade."
    
    "Draining the last of our beginning Col on other miscellaneous items, we headed out of Starting City."
    
    scene bg fields
    with dissolve
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350], ['Kirino', 85] ])
    
    show monster boar at center
    show slash slant with CropMove(0.15, mode='wipeleft')
    hide slash slant
    
    kir "Yaaah!"
        
    show kirino avatar annoyed at left
    show monster boar at right
    
    "With a vicious cross slash, Kirino succeeded in missing the boar completely."
    
    kir "What is this?!  Hold still and die already!"
    
    hide kirino avatar
    show monster boar at center
    
    show slash slant with CropMove(0.15, mode='wipeleft')
    hide slash slant
    
    "She tried again.  Instead of laying down to die however, the boar shot forward crossing the short distance to my sister in an instant."
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350], ['Kirino', 82] ])
    $hb.NewVal(82)
    show kirino avatar hit at left, Shake(None, 0.5, dist=30) 
    show monster boar at right
    
    
    kir "Gwah."
    
    "Looks like it was a glancing blow as she hadn't lost much health from that charge."  
     
    kyo "Need help?"
    
    "I admit, I was enjoying this.  It wasn't often that I got a chance to see my talented sister actually struggle at something."
    
    show kirino avatar furious
    
    kir "Shut up! Shut up!  Raaagh!"
    
    hide kirino avatar
    show monster boar at center
    
    show slash slant with CropMove(0.15, mode='wipeleft')
    hide slash slant
    
    show monster boar at center, Shake(None, 0.5, dist=30)

    "She angrily swung just as the boar charged again.  This time she connected.  And so did the boar."
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350], ['Kirino', 76] ])

    show monster boar at right
    show kirino avatar hit at left, Shake(None, 0.5, dist=30) 
    kir "Ooof!"
    
    # "As far as the exchange went, Kirino was now down a quarter of her hp while the boar still looked like it hadn't been touched."
    "As far as the exchange went, the boar still looked like it hadn't been touched.  If Kirino's expression were anything to go by, it appeared that she lost that exchange."
    
    "I couldn't resist."
    
    kyo "50 more ti- {w=0.5}\n\nWoah!"
    
    show slash slant with CropMove(0.15, mode='wipeleft')
    hide slash slant
    
    "I barely jumped out of the way in time as a flash of steel sliced right where I had been standing.  It landed harmlessly on the ground with a loud clatter." 
    
    kyo "What was that for?!"
    
    show kirino avatar mocking
    
    kir "Ah!  Sorry, my fingers sli-"
    
    show monster boar at left
    show kirino avatar mocking at center, Shake((1.0, 0.0, 1.0, 0.0), 0.5, dist=30) 
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350], ['Kirino', 65] ])
    
    "Her smug expression disappeared when the boar crashed into her from behind, knocking her facefirst into the dirt."
    
    kir "You stupid pig!"
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 350, 1, 350], ['Kirino', 59] ])
    
    show monster boar at right
    show kirino avatar furious at center, Shake((0.0, 0.0, 0.0, 0.0), 0.5, dist=30) 
    
    "I struggled to contain my laughter as she stood up and tried to kick it only to receive a counterattack for her efforts."
    
    kir "What are you standing there for?!  Do something about this pig!"
     
    "That was my cue.  With a casual shrug, I raised my two-handed sword over my head and waited for it to glow."
    
    "As I swung, I felt the system take over from there."
    
    hide kirino avatar
    show monster boar at center:
        pause 0.2
        alpha 1.0
        linear 0.5 alpha 0.0
    
    show slash down with CropMove(0.15, 'wipedown')
    hide slash down
    skill "«Vertical»" 
    
    show boom with flash
    
    "With a squeal, the boar broke into a mess of polygons soon after." 
    
    hide boom           # general housekeeping, but needed if we're skipping through text.
    
    "I tried not to show it, but I was impressed as well.  For a moment there, I thought that the blade wasn't going to reach."
    
    "I turned to my sister.  She was gaping."
    
    kir "What did you do?! I was fighting that pig for hours. And you took it down with one hit.  And the glowy sword thingy."
    
    "Mentally patting myself on the back for having the foresight to read the manual, I prepared myself for what was probably a once-in-a-lifetime opportunity."
    
    kyo "What you just saw was one of the many «Sword Skills» in the game."
    
    "And from there, I explained the basics of one of the most important mechanics in the game."
    
    "A benefit to having a complete model student as a sister is that she learns quickly."
    
    "Of course she was angry that I had withheld such vital information from her.  But we were surrounded by a field of fat leisurely boars, the perfect targets to redirect her anger."
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 175, 2, 500], ['Kirino', 29] ])
    show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 175, 2, 500] ])
    
    "After destroying several boars with our newly acquired abilities we decided to take a break and eat some of the food we bought."
    
    # show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 500, 2, 500], ['Kirino', 100] ])
    show screen bar_test3(floortext="Floor 1", characters=[ ['Kyosuke', 500, 2, 500] ])
    
    "As I took a few bites of the roast meat that looked like an oversized chicken leg we gazed at the beautiful landscape constructed from countless polygons."
    
    kir "I wonder if this game has little sister Npcs?"
    
    kyo "Pffft"
    
    "I had nearly choked on my bite when I heard that.  I coughed several times as I struggled in vain to swallow."
    
    kyo "Why? Why would you ask that of all things?"
    
    kir "Why wouldn't I? It'd be so cute if you could have a little sister follow you around and ask how your day fighting monsters was as she made you a snack?"
         
    "There is a faraway look in her eyes as she says that. I just sat there and stared for a minute before I rubbed my chin in thought.  If Kirino were to ask me how my day went as she prepared dinner..." 
    
    kir "What's with that sigh?" 
    
    "...that would never happen.  Before I could save myself from her irritation, however..."
     
    msg "ding, ding"
    
    "A pair of bell sounds rang across the field."  
    
    "We had no time to figure out what was happening as a blue pillar sprang up around us and the world seemed to fade away."
    
    scene bg tutorial
    with dissolve
    
    "When we regained our bearings, we were at the starting point surrounded by what seemed like every player in the game."
    
    "There Kayaba Akihiko gave the speech that lead us to our current predicament."
    
    "The missing log out button was not a bug."
    
    "«Sword Art Online» was not a game anymore.  It was our new reality."
    
    "We cannot depend on anyone outside to save us.  If they tried to remove or tamper with the Nerve Gear, we would die when the Nerve Gear destroys our brain with an electromagnetic pulse.  This has already happened."
    
    "We need to reach the top of the castle to leave the game."
    
    "What scared me the most was the final warning: \"From now on, any form of revival in the game will no longer work. The moment your HP reaches 0, your avatar will be gone forever. And at the same time...\""
    
    "It did not take a genius to understand what followed that pause."
    
    "Of course I wanted to laugh it off as a joke from an overzealous GM.  Really, they should fire this Kayaba Akihiko, whoever he is."
    
    "Then a «Hand Mirror» appeared in our inventory."
    
    "When I held it up, I saw my customized face in the mirror.  What was so special about this mirror?" 
    
    "When the white light surrounding me had died away, I had my answer.  I was now seeing what I looked like in real life."
    
    "As bright flashes continued to occur all around the plaza, I felt the hand mirror slip from my fingers as I stared at Kirino"
    
    "When my sister had changed from the blue haired boy back to herself, I finally remembered where I had heard of Kayaba Akihiko..."
    
    "...He was mentioned at the end of the manual as the development director of SAO and the designer of the Nerve Gear units that we were using..."
    
    "...He wasn't just a GM."
    
    #scene change
    scene bg bench night
    with dissolve
    
    stat "Floor 1. «Starting City»\n\nParty Members:\n Kirino (Lvl 3)\n Kyosuke (Lvl 3)\n\nCol: 103"
    
    "Stepping out of the store after selling what I could to the shop NPC, I proceeded to the small park across the way."
    
    "I had left Kirino in the park for a moment while I sold some items for spending money." 
    
    "I found her sitting on a wooden bench with her hands in her lap, a blank expression on her face."
    
    "I reached out to her to let her know that I had returned only to pull back when her eyes snapped up to glare angrily towards me."
    
    kir "...sibility."
    
    kyo "?"
    
    kir "This crazy situation has to be your fault somehow.  You are going to take responsibility for this, right?"
    
    "Her voice was so quiet that, had I not seen her lips move, I would have believed that I was imagining it. Just as fast as she looked my way, her vacant gaze had returned to the ground. Her body gave a slight tremble."
    
    kir "I want a consultation about life."
    
    kyo "Here?  Now?  Are you serious?"
    
    "She nods."
    
    "Guess she is.  I sigh before I straighten up."
    
    kyo "Okay, what do you want to know?"
    
    show kirino haughty
    
    kir "This is a dream right?"
    
    "What a great way to start off..."
    
    kir "Ah~  This is great.  I'm having a life consultation with my worthless brother in a dream of all things."
    
    kir "No wait.  If Aniki is in it, it's got to be a nightmare!"
    
    "Gee, thanks."
    
    "......"
    
    "..."
    
    "When she stopped ranting to stare at me, I had a feeling that I had said that out loud."
    
    kir "Why?  Why did this have to happen?"
    
    "Why?  I've been asking that myself."
    
    kir "What's going to happen to us?"
    
    "Another difficult question that I don't know how to answer."
    
    kir "I want to leave.  Mom, Dad, Ayase, the black one.  Can't anyone help us?"
    
    "I'm pretty certain that she already knows the answer to that question."
    
    kir "Aaah!  There is a new Meruru movie coming out in a month!  We need to get out by then!"
    
    "While she ranted, I continued to think."
    
    "Like all of the other life consultations, this one is tough.  This time, however, I had a feeling that the problem wasn't going to solve itself in a week or two."
    
    "Okay wait.  Now that we're like this, time doesn't matter.  Now how was I going to free her?"
    
    "Like all the other consultations, a vague plan was already forming.  And just like all of the other ones, I already knew that it was probably going to cause me no end of trouble."
    
    "Troublesome, ungrateful, disrespectful...she has an endless variety of personality problems that give me grief."
    
    "However, there were two undisputed facts that were going to make me jump in anyway, no matter how troublesome."
    
    "She's still a fourteen-year-old junior high school student..."
    
    "...and I'm her brother."
    
    "Looks like I'm starting to realize that no matter how much trouble she gives me, I'll still face her troubles head on for her."
    
    "...And she's looking at me.  I guess I've been silent for too long."
    
    kyo "We'll be saved.  We just need to hang on until then."
    
    kir "When will that be?"
    
    kyo "A month?"
    
    "At her hopeful expression, I could only shake my head."
    
    kyo "No sorry.  That was a horrible guess.  I'm not going to lie to you, but with my luck it probably won't be anytime soon."
    
    show kirino haughty
    
    kir "Then do something about your luck."
    
    "I gave her a halfhearted grin."
    
    kyo "Still, there is one thing you can count on."
    
    kir "?"
    
    kyo "Me."
    
    kir "What?"
    
    kyo "As long as I can help it you will never be alone in this world. I swear to make sure you get out alive."
    
    kir "Pfft.  What kind of cheesy line is that?"
    
    kyo "Hey, I thought it was pretty good."
    
    kir "Yeah, whatever.  You're not lying right?  You'll really get me out?"
    
    kyo "Of course I will. Who do you think I am?"
    
    "........."
    
    "......"
    
    "..."
    
    kir "Okay."
    
    "She stopped staring at me and glanced both ways before she shifted slightly to make a spot on the bench.  Patting it twice, she let me know that I could take a seat."
    
    "As I sat down next to Kirino, she closed her eyes and let her head fall onto my shoulder."

    "She must be feeling tired considering we have been in this world for over eight hours straight." 
    
    show kirino happy
    
    kir "Thank you...Oniichan."
    
    "The even breathing that followed that whisper told me that she had fallen asleep.  I sat there, basking in the glory of what she had just said."
    
    "Oniichan, huh?  How long has it been since she last called me that?"
    
    "Unfortunately, I couldn't sit there and relax forever. I had to decide where we were going to spend the night." 
    
    "I sighed and stood up, carefully keeping Kirino from flopping over as I did so.  Turning, I gingerly lifted Kirino onto my back."
    
    "Or, at least, I tried to.  I know that she isn't this heavy in real life...\n\n...and I refuse to reveal how I know this."
    
    "I do not know what was going on, but it felt like I was trying to lift a car with one hand."
    
    "I would later find out that my STR stat was too low at the time. For now though, I was left with no choice but to shake her awake."
    
    kir "Nn? Oniichan?"
    
    "Yes!  She called me Oniichan again!"
    
    kyo "Come on, let's go rest at an inn."
     
    kir "Dun wanna"
     
    "She started to nod off again."
    
    "Before that could happen, I shook her again."
    
    kyo "Not yet."
    
    show kirino angry
    
    kir "No!  When I say I dun wanna I don wanna."
    
    ".....I shook her again."
    
    kir "Stop it!"
    
    kyo "Just a little bit longer.  All we need to do is find an inn and then you can sleep as long as you want."
    
    kir "You're being annoying."
         
    kyo "Would you like it if I left you here?"
    
    "........."
    
    "......"
    
    "..."
    
    show kirino haughty
    
    kir "Then carry me."
    
    kyo "What?"
    
    kir "Carry me."
    
    kyo "I can't."
    
    show kirino angry
    
    kir "What's with that? Your beautiful and noble sister is giving you an order.  You should thank me for the honor of even looking in your direction."
    
    kyo "Look, I seriously can't."
    
    kir "Do it."
    
    kyo "No."
    
    kir "Do it!"
    
    kyo "No."
    
    kir "Can't do it?"
    
    kyo "Yes."
    
    kir "Yes, you will carry me?"
    
    kyo "No I can't."
    
    kir "What do you mean you can't?"
    
    kyo "I just...can't."
    
    kir "I can't believe you're saying that just to get out of helping your delicate sister."
    
    kyo "I'm not running away from anything!"
    
    kir "Then why aren't you jumping at the opportunity to carry me?!"
    
    #kyo "You're too heavy."
    kyo "Don't you think I haven't tried?"
    
    kir "Doesn't seem like it!"
    
    kyo "Here, look!"
    
    "Both" "{color=#F39494}Wha?!  What are you doing?! \n\n{/color}{w=0.5}{color=#6D83CD}Ugh.  It's like lifting a brick wall.{/color}"
    
    "........"
    
    "......"
    
    "..."
    
    kir "What was that?"
    
    kyo "Wait. Waitwaitwait.  Let me explain."

    
    #scene change
    
    scene bg inn
    with dissolve
    
    "After a while we came to an average looking inn. The atmosphere inside was quiet, almost chilling."
    
    "The crackling fire did nothing to warm the atmosphere as many of the players sitting at the tables in the main area had hopeless expressions on their faces."
    
    "From the broken chairs and tables scattered throughout the room, it looks like several fights had broken out as well."
    
    "I walked up to the crying innkeeper NPC and proceeded to rent a room for both Kirino and I to share."
    
    "Much as I would like to rent a second room, I didn't have much money left and Kirino had not visited an NPC yet to sell her inventory."
    
    "I was glad, then, that her exhaustion was catching up to her as she merely gave a half-hearted protest before falling silent."
    
    "The instant that I hit \'YES\' and the col was deducted from my inventory, Kirino was already trudging up the stairs with the key."
    
    "I gave another glance around the room, wondering why the broken chairs and tables had not shattered into polygons yet."
    
    "When no answer came to me, I shrugged and proceeded up the stairs after her."
    
    #scene change
    
    "Inside of the room, I found Kirino flopped out on the bed, already asleep."
    
    "I was pleased to note that it was easy to tuck her in.  First I vanished the blanket out from right out from under her like a magician.  Then, materializing it from my inventory, I threw it right over her."
     
    "I found extra blankets and pillows in the closet.  Grabbing a set, I made myself comfortable on the floor."
    
    jump endchapter1
    
    
    # Changes
    # Expanded on some details over the original source
    # The inn's mood was changed from cheery to cold.
    # Moved some text around.
    # Adjusted some of the dialogue.
    # Kirino is overweight.  This change was taken from the fanfiction SAO: Final Regrets (24. The Day Before)