#CONSTANTS
import inspect

URL ="http://automationpractice.com/index.php?controller=authentication&back=my-account"
EMAIL = "skhenat_pr@medable.com"
PASSWORD = "medable123"

def whoami():
    return inspect.stack()[1][3]
