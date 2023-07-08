list_greeting = ['Hallo', 'Bonjour', 'Ola', 'Hello', 'Ciao', 'Ave']

def is_greeting(s):
    """Returns True if s is in list_greeting, else False."""
    if s in list_greeting:
        return True
    else:
        return False 


help(is_greeting)