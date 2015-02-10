import re

line = "Cats are smarter than dogs, are they?"

matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I )

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group() : ", matchObj.group(1)
    print "matchObj.group() : ", matchObj.group(2)
else:
    print "No match!"



