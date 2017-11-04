import sys
activate_this = '/home/ec2-user/LoanChain/loanchain/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))
sys.path.insert(0, '/home/ec2-user/LoanChain')
from loanchain import app as application
