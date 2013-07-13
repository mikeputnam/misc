import random

gradelevels = (1,3,5)
qa = [
    [5,"Does matter change from solid to liquid at melting point or at freezing point?","MELTING POINT"]
    ,[5,"What part of the skeleton protects the lungs, heart, and other organs?","RIB CAGE"]
    ,[5,"What vitamin do citrus fruits supply?","VITAMIN C"]
    ,[5,"After circulation through the body, where does blood go?","BACK TO THE HEART"]
    ,[5,"What are the three branches of government?","LEGISLATIVE, EXECUTIVE, JUDICIAL"]
    ,[5,"What state has two capitals?","MARYLAND"]
    ,[5,"What time zone do we live in?","CENTRAL TIME ZONE"]
    ,[5,"Name the five Great Lakes.","HURON, ONTARIO, MICHIGAN, ERIE, SUPERIOR"]
    ,[5,"What kind of map gives you information about elevation and the shape of the land?","TOPOGRAPHIC MAP"]
    ,[5,"Which part of the human body has a cornea?","THE EYE"]
    ,[5,"What is a piece of land called that extends into the water from a larger piece of land?","PENINSULA"]
    ,[5,"What are the two largest countries of North America?","THE UNITED STATES AND CANADA"]
    ,[5,"In 1981, who was the first female justice on the U.S. Supreme Court?","SANDRA DAY O'CONNOR"]
    ,[5,"Who were the first three Presidents of the United States?","GEORGE WASHINGTON, JOHN ADAMS, THOMAS JEFFERSON"]
    ,[5,"How many Senators are in the Unites States Senate?","100 (2 FROM EACH STATE)"]
    ,[5,"Which shares a border with Florida - Georgia or South Carolina?","GEORGIA"]
    ,[5,"What is Wisconsin's statue motto?","FORWARD"]
    ,[5,"Which state was the first to join the union?","DELAWARE"]
    ,[5,"Is Nebraska east or west of the Mississippi River?","WEST"]
    ,[5,"What degree of latitude is used for the Equator?","0 DEGREES"]
    ,[5,"How many degrees are in a right angle?","90 DEGREES"]
    ,[5,"Put in order from least to greatest - 12.35, 12, 12.3","12, 12.3, 12.35"]
    ,[5,"If 100 x 80 = 8,000; what does 1,000 x 80 equal","80,000"]
]
res = "0"
while (int(res) not in gradelevels):
        res = raw_input("Enter grade [1,3,5]:")
print "===Grade " + res + "==="
qlist = [question for question in qa if question[0] == int(res)]
while len(qlist) > 0:
    aquestion = random.choice(qlist)
    foo = raw_input("=================\n\nQuestion: "+aquestion[1]+"\n<Press ENTER to see the answer>")
    print "\n\nAnswer: "+aquestion[2]+"\n\n"
    qlist.remove(aquestion)
