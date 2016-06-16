
# This is a program that removes '%%' commands from
# the tab complete feature in ipython
#
# To run this correctly, in the command line type
# ipython -i unmagic.py
ip = get_ipython()
ip.Completer.matchers.remove(ip.Completer.magic_matches)
