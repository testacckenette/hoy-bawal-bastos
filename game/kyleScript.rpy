# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Main Character
define p = Character("[playername]")
define m = Character("Me")
define y = Character("You")

# Side Character
define e = Character("Elise")
define z = Character("Zack")
define k = Character("Karl")
define l = Character("Lady(Victim)")


# Script starts here.
label startKyleScript:
    # Take player name
    python:
        p = renpy.input("What is your first name?", length=32)
        p = p.strip()

        if not p:
            p = "Shy Guy"

    # Start of the story    
    "Hello there [p]"
       
    # Show a black screen with text on top of it
    scene black 

    centered "Case 1: \n\n\nKarl's Desperation"
    
    centered "\“On the 7th of April Year 2019, a new law called {color=#f00}{b}Republic Act 11313{/b}{/color} 
    or also known as {color=#f00}{b}Safe Spaces Act{/b}{/color} has been approved by the president.\"" 

    centered "\"This law stated that both men and women must have equality, 
    security and safety not only in private, but also on the streets, public spaces, online, workplaces 
    and educational and training institutions……\”"

    #
    scene bg clubroom

    e "Hey, how many times you gonna read that again? [p]"

    m "Well, this is a reminder for myself..Hmm??!!"

    "{i}Your phone starts ringing...{/i}"

    z "[p!u]!!!!"
    
    z "The client’s accusation is real! I also already recorded the scene for the evidence!"
    
    z "Go to the backside of the gym!!! Hurry!!! Before he do something bad to the client!!!"

    m "I see, good work Major Zack."

    z "Ohh really thanks hahahahah!.......wait…..Please! Just hurry up General!!!"

    m "Don’t worry, we will arrive in the scene in no time."

    m "Lieutenant Elise! Get ready, we've got a mission to complete."

    e "Okay! Give me a minute. Also! Don’t call me Lieutenant! Geez"
    
    m "Whatever you say, anyway let’s make haste Lieutenant Elise!"

    e "........"

    jump backsidegym

label backsidegym:
    
    scene bg backsidegym
    
    "{i}[y] and [e] arrive the scene at the Backside of the Gym.{/i}"

    "{i}[z] was already there.{/i}"

    m "How’s the scene, Major Zack?"

    z "Finally both of you are here! Anyway look over there!!"

    "{i}Everyone looked at the direction of his fingers.{/i}"

    "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    k "Hehe….hehe…Oh come on lady why are you so playing hard to get……hehehe!"

    l "Noo!! Please just get away from me! Stop following me!!"
    
    k "Hehehe…Come on, don’t you understand how I am obsessed to you.
     I already gave you a lot of hints of how much I love you by staring at you romantically."

    l "Please anyone help me!!...."

    m "Hmmm….. it seems this man is really desperate."

    z "Yeah, we better give him the right punishment General."

    e "What are you doing you two just step up to the scene already before this become more worst than it already is!"

    z "A wise decision, Lieutenant Elise. I commended you for that."

    e "Geez!! Just do something already!!"

    "[e] smacked your head painfully."

    m "Aww! Okay Lieutenant!"

    jump confrontation

label confrontation:

    "[y] stepped up to the scene"

    m "Hold it right there! Belligerent scum!"

    k "Huhh?!!! How long have you guys been standing there?"

    m "Hahahaha!!...."

    k "Don…t..Don’t tell me you guys are the student council!"

    m "No, you are wrong about that…"

    k "Then just tell me who are you guys!!! And also how did you find us here?" 
    
    k "{i}(I am pretty sure that I looked around cautiously before I dragged the lady.){/i}"

    m "Hahahaha!!…. As always, that’s Major Zack for you. Despite being an airhead, he knows 
    the ways to secretly sneak up to his target."

    z "Haha, thanks General!"

    k "Suspect?! You sound like your saying I did something wrong!"

    m "Well, before we proceed on that. First let us introduce ourselves! Major Zack you may proceed first."

    z "Oh I need to introduce myself? Okay, I am Major.Zack. Nice to meet you!"

    "{i}Zack Salkelberg aka Major Zack, from class 3-C. Despite being an airhead like I mentioned 
    earlier, Major Zack has proficient skills on concealing his presence. Which gives him the perfect 
    role for spy mission investigations.{/i}"

    m "Lieutenant Elise, the stage is all yours now."
    
    e "Okay…fine..Also! How many times am I gonna tell you to stop calling me Lieutenant. It’s 
    embarassing you know, especially when there are other people around us!"

    e "Ohh! Sorry about that! My name is Elise Fonillia, A third year student. Pleased to meet 
    you."

    "{i}Elise Fonillia aka Lieutenant Elise, from class 3-B. Like many other people say, “Don't 
    judge a book by its cover” and that applies to Lieutenant Elise. She maybe look like a normal 
    highschool student but don’t get fool by that, ever since I met Lieutenant Elise, I noticed that she 
    has a strength greater than a six-footer gorilla.{/i}"

    m "Thank you for the wonderful and elegant introductions everyone… As for the next 
    introduction, the next is..."

    m "The last but not the least……, the tactician, the strategist, the mastermind, the leader of 
    the {color=#f00}HHB Club{/color}!!...., it is I! General [p] Zealsphere, from class 3-A! at your service!!...."

    z "OOHH YEAHH!! WUHH HOOO!!! GOOOO GENERAL!"

    e "How stupid… I really hate your all high and mighty cocky attitude! I don’t really 
    understand why I even going along with you…."

    m "Don’t say that Lieutenant Elise, I may be your General but am still a human who got 
    feelings that can be easily shatter."

    k "HEHEHEHE!!! What the hell!!! HEHEHEH!!!!...you guys are not the student council 
    after all!!! To be honest I also got scared…but THAT’S! not the problem anymore! Hehehe!!!"

    m "Hahahaha, how foolish of you we may not be the student council of this school but we 
    still have the right authorities to bring justice to your crime!!"

    k "Wha..Whatt do you mean! In the first place I did not do anything wrong!!"

    l "That’s not true!!! Mr.Ray please help me!!!! What I discuss to you last time is 
    true!!!"

    m "Don’t worry, dear client, we hear your humble words that’s why where here to bring the 
    truth and justice!"

    m "Major Zack, bring me the document files!"

    "{i}[y] read the document files...{/i}"

    m "I see, Mr.[k] Daberth, from class 2-C. you got a accusation from this humble lady.
    She stated that you been staring and stalking her lately."

    k "Ah..Ahh well so what!!! It’s not like I did something illegal!"

    m "Well Mr.[k] Daberth, have you heard of this law..."

    k "Wha…What kind of law are you talking about! Just get to the point already!!"

    jump questionTime

label questionTime:

    menu:
        m "Ahhh… What is the Republic Act No. again? That has been approved on April 17,2019." 

        "Re-semiprivate Act 11313":
            "Wrong"

        "Reprivate Act 11313":
            "Wrong"

        "Republic Act 11313":
            "Correct"

        "Rebuild Act 11313":
            "Wrong"

    # Implement a loop where the question will restart if wrong (?)   

return
