import webbrowser
webbrowser.get(using=None) # reruen a controller object for the browser type using.if using is none
webbrowser.open("https://www.python.org/",new=1)
webbrowser.open_new("https://www.python.org/") # open url in new window of the default browser if possible otherwise browser open

webbrowser.open("https://www.python.org/",new=2)
      # if new is 1 a new browser window is open
      # if new is 2 a new browser tab is open
help(webbrowser)
for i in range(10):
    print(1,2,3,4,5,6,7,8,9,sep="; ")
    print(1, 2, 3, 4, 5, 6, 7, 8, 9,end='\n')
    print()
#
chrome = webbrowser.get('google-chrome %s').open_new_tab("https://www.python.org/")
chrome = webbrowser.get('/usr/bin/google-chrome %s').open_new_tab("https://www.python.org/")
# safari = webbrowser.get(using='safari')
# safari.open("https://www.python.org/")