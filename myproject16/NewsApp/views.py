from django.shortcuts import render

# Create your views here.
def input(request):
    return render(request, 'base.html')

def political_news_view(request):
    political_news_1 = "It rains heavily in the next 48 hrs"
    political_news_2 = "Babu warning Jagan......"
    political_news_3 = "IPL started yesterday grandly!!!"
    political_news_4 = "William came back successfully"
    dict1={'news1':political_news_1, 'news2':political_news_2, 'news3':political_news_3, 'news4':political_news_4}
    return render(request, 'politics.html', dict1)

def sports_news_view(request):
    sports_news_1 = "Sunriser hyderabad beats Rajasthan royals by 44 runs"
    sports_news_2 = "CSK won the toss, and elected to ball first against MI"
    sports_news_3 = "Ishan kishan tons helps sunriser to put 287 on the board"
    sports_news_4 = "Harshal patel won the man of the match award"
    dict1={'news1':sports_news_1, 'news2':sports_news_2, 'news3':sports_news_3, 'news4':sports_news_4}
    return render(request, 'movies.html', dict1)

def movies_news_view(request):
    movies_news_1 = "Hollywood Flashback: The Year of the Dueling Snow Whites"
    movies_news_2 = "Peruvian Drama ‘Reinas’ Wins Swiss Film Awards"
    movies_news_3 = "Zach Cregger’s ‘Resident Evil’ Reboot Eyes Austin Abrams to Star"
    movies_news_4 = "‘Texas Chainsaw Massacre’ Rights Up for Grabs, Sending Hollywood Foaming"
    dict1={'news1':movies_news_1, 'news2':movies_news_2, 'news3':movies_news_3, 'news4':movies_news_4}
    return render(request, 'sports.html', dict1)