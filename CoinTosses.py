import random

counterHead = 0
counterTail = 0

for i in range ( 1, 51 ):
    random_num = random.random()
    roundedRandom = round( random_num )
    if roundedRandom == 0:
        counterHead += 1
        print "Attempt #", i,": Throwing a coin... It's a head! ... Got", counterHead, "head(s) so far and", counterTail, "tails(0) so far"
    else:
        counterTail += 1
        print "Attempt #", i,": Throwing a coin... It's a tail! ... Got", counterHead, "head(s) so far and", counterTail, "tails(0) so far"