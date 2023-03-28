# Just string raings
def getRating(score):
    rate = ''
    
    if (score >= 13000):
        rate = 'You can do almost anything with your processor!'
    elif (score >= 8200):
        rate = 'You can play games like Metro: Exodus, Cyberpunk 2077 and etc..'
    elif (score >= 5200):
        rate = 'You can play games like CS:GO, GTA V and etc.. Thats cool!'
    elif (score >= 2900 ):
        rate = 'Your CPUs perfs really cool!'
    elif (score >= 1900 ):
        rate = 'Your CPU really not bad!'
    elif (score >= 1000):
        rate = 'This not so bad, but bad'
    elif (score <= 1000):
        rate = 'Sry, but your CPU sucks :/'
    else:
        rate = 'nan'

    return(rate)