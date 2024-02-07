# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#1
def r(x):
    if x['imdb']>5.5:
        return(True)
    else:
        return(False)

for i in movies:
    print(r(i))

#2
l=list()
def e(x):
    if x['imdb']>5.5:
        l.append(i['name'])
for i in movies:
    e(i)

print(l)

#3
l=input()
def c(z):
    if z["category"]==l:
        print (z['name'])

for i in movies:
    c(i)


#4
def a(x, y):
    sum=0
    n=0
    for i in range(x, y+1):
        sum+=movies[i-1]['imdb']
        n+=1
    print(sum/n)

a(2,5)
    
#5
def aw(x):
    n=0
    sum=0
    for i in movies:
        if i["category"]==x:
            sum+=i["imdb"]
            n+=1
    print(sum/n)

for i in movies:
    aw(i)
