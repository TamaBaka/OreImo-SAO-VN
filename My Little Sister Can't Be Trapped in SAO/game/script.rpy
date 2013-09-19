# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image placeholder = "placeholder.jpg"
image slash down = "slashdown.png"
image slash slant = "slashslant.png"
image bg kyosuke room = "KyosukeRoom.png"
image bg starting city = "Starting City.png"
image bg tutorial = "Tutorial.png"
image bg fields = "Fields.png"
image bg bench night = "Bench Night.png"
image bg inn = "Inn.png"
image monster boar = "Boar.png"

image anim_indicator = Animation("indicator01.png", 0.07, "indicator02.png", 0.08, "indicator03.png", 0.08, "indicator04.png", 0.08, "indicator05.png", 0.08, "indicator06.png", 0.08, "indicator07.png", 0.08, "indicator08.png", 0.07,
                            "indicator09.png", 0.08, "indicator10.png", 0.08, "indicator11.png", 0.08, "indicator12.png", 0.08, "indicator13.png", 0.08, "indicator14.png", 0.08)

define hb_kirino = HealthBar(100, 100, 200, 2, 30)     # use 30 for single and double bar.  20 for triple and quadruple bars.
image healthbar_kirino = hb_kirino

image kirino avatar annoyed = LiveComposite(
    (352, 572),
    (0, 0), "Kirino Avatar v1.png",
    (101, 50), 'anim_indicator',
    (200, 200), 'healthbar_kirino'
    )
image kirino avatar furious = "Kirino Avatar v1.png"
image kirino avatar mocking = "Kirino Avatar v1.png"
image kirino avatar hit = LiveComposite(
    (352, 572),
    (0, 0), "Kirino Basic Armor.png",
    (101, 50), 'anim_indicator',
    (200, 200), 'healthbar_kirino'
    )
image kirino haughty = "Kirino Basic Armor.png"
image kirino angry = "Kirino Basic Armor Angry.png"
image kirino happy = "Kirino Basic Armor Happy.png"
image kuroneko = "Kuroneko.png"
image kobato upset = "Kobato Upset.png"
image kobato upset flip = im.Flip("Kobato Upset.png", horizontal=True)

image emo_note = im.MatrixColor("Note.png", im.matrix.tint(0.5, 0.8, 0.5))

# Declare characters used by this game.
define kyo = Character('Kyosuke', color="#6D83CD", show_two_window=True, what_prefix="“", what_suffix="”")
define kir = DynamicCharacter("kirinoname", color="#F39494", show_two_window=True, what_prefix="“", what_suffix="”")
define kuro = DynamicCharacter('kuronekoname', color="#FF0000", show_two_window=True, what_prefix="“", what_suffix="”")
define argo = DynamicCharacter('argoname', color="FFFFFF", show_two_window=True, what_prefix="“", what_suffix="”")
define kob = DynamicCharacter("kobatoname", color="#F39494", show_two_window=True, what_prefix="“", what_suffix="”")
define msg = Character(None, what_prefix="{color=#000000}[[", what_suffix="{/color}{fast}]")
define stat=Character(None, what_prefix="{color=#000000}", what_suffix="{/color}{fast}")
define skill=Character(None, what_prefix="{color=#6666FF}", what_suffix="{/color}{fast}{w=0.3}{nw}")  # it sounds counterintuitive, but the w makes it wait 0.3 seconds before the nw clears the say statement.
define sndfx=Character(None, what_prefx="{color=#6666FF}", what_suffix="{/color}{fast}{w=0.3}{nw}")

init:
    transform fragmentfade:
        pause 0.2
        alpha 1.0
        linear 0.5 alpha 0.0
        alpha 1.0                       # reset the alpha so that we scroll back and advance again
        repeat                          # repeat in case we want to replay
    
    image boom = Particles(ExplodeFactory([At("fragment1.png", fragmentfade), At("fragment2.png", fragmentfade), At("fragment3.png", fragmentfade)], explodeTime=0.7, numParticles=320))
    
    $ flash = Fade(.25, 0, .75, color="#fff")
    $ partydata = PartyData()
    
    $ noisedissolve = MultipleTransition(   [False, ImageDissolve(im.Tile("shatter.png"), 0.3, 1),
                                            False, Fade(.25, 0, .75, color="#fff"),
                                            True])
    $ teleport = MultipleTransition([False, dissolve, "#fff", dissolve, False, 
                                     dissolve, "#fff", dissolve,
                                     True, dissolve, "#fff", dissolve, True])
    
# The game starts here.
label start:
    
    #show screen alpha_magic

    jump chapter1
    label endchapter1:

    jump chapter2
    label endchapter2:
        
    jump chapter3
    label endchapter3:

    jump chapter4
    label endchapter4:
        
    return
