import os
import sys

cmd = "curl -d \"text=" + sys.argv[1] + "\" http://text-processing.com/api/sentiment/"
# returns output as byte string
returned_output = os.system(cmd)

print(returned_output)