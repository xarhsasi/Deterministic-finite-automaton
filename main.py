from Runnable import Runnable
from helpers.CLIColor import CLIColor as color

try:
    program = Runnable()
    program.run()
except:
    print(color.RED("Something went wrong"))
