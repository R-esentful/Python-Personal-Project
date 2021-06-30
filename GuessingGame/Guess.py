import random
story1 = "My three-year-old daughter was trying to roast a marshmallow for the first time. Her first and second attempts ended in flames. Both times, I took the scorched marshmallow off of the roasting stick and threw it into the fire. The third time, I helped her a lot more and, together, we achieved a perfectly toasty golden brown. Once it was cool, I handed her the marshmallow which she promptly threw into the fire. No one had told her she was supposed to eat it. —Submitted by Lou Roess, Parachute, Colorado."
story1split = story1.split()
story1len = len(story1split)
class GuessMe:
    def Word():
        RanNum = random.randint(0,story1len-1)
        RanWord = story1split[RanNum]
        Reverse = RanWord[::-1]
        Replace = story1.replace(RanWord,Reverse)
        print(story1)
        print(Replace)

GuessMe.Word()
