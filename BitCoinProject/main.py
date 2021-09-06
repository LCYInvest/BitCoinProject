# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyupbit

access = "OTpBSxD7JOU4nag5I6x90xnXauQ7h3haT790LeYI"
secret = "zOU6RHrHdapUMw7npOPtpiG4XYLdO16UQEuhWlEn"

upbit = pyupbit.Upbit(access, secret)
print(upbit.get_balances())
