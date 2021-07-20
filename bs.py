from bs4 import BeautifulSoup

news = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Daily News</title>
</head>
<body>
    <div class="breaking-news">
        <h1>The blackout in major cities in Indonesia</h1>
    </div>
    <header>
        <nav>
            <ul id="main-navigation">
                <li><a href="#">Home</a></li>
                <li><a href="#">News</a></li>
                <li><a href="#">Politics</a></li>
                <li><a href="#">Sports</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="top-news">
            <ul>
                <li class="breaking"><a href="http://cnn.com">US President says US must also stand against racism and bigotry -- but doesn't acknowledge his own rhetoric</a></li>
                <li class="breaking"><a href="#">Trump misidentified city where one of the attacks took place</a></li>
                <li><a href="#">Classmates: Dayton gunman had a 'hit list' in high school</a></li>
                <li><a href="#">Victims' cousin has a message for Trump</a></li>
            </ul>
        </section>
        <section id="sport-news">
            <ul>
                <li><a href="#">From pantomime villain to superstar: Inside Steve Smith's world</a></li>
                <li><a href="#">Hamilton storms from behind to win Hungarian GP</a></li>
                <li><a href="#">Kyrgios and Gauff land titles in Washington</a></li>
                <li><a href="#">Hinako Shibuno wins Women's British Open on debut</a></li>
            </ul>
        </section>
    </main>
</body>
</html>
'''

soup = BeautifulSoup(news, 'html.parser')

# print(soup.head)

#print(soup.head.title.get_text())

#print(soup.find('h1').text)

#print(soup.find_all('section'))

section_one = soup.find_all('section')[0]

contents = section_one.find_all('a')

for c in contents:
    print(c.text)

sport_news = soup.select('#sport-news')

#print(sport_news)

breaking_news = soup.select('.breaking')

for bn in breaking_news:
    print(bn.text)
