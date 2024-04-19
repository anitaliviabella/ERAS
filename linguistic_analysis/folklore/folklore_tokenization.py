import spacy
nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.
import pandas as pd
import csv


folklore_lyrics = '''
The 1
I'm doing good, I'm on some new shit
Been saying "yes" instead of "no"
I thought I saw you at the bus stop, I didn't though
I hit the ground running each night
I hit the Sunday matin�e
You know the greatest films of all time were never made
I guess you never know, never know
And if you wanted me, you really should've showed
And if you never bleed, you're never gonna grow
And it's alright now
But we were something, don't you think so?
Roaring 20s, tossing pennies in the pool
And if my wishes came true
It would've been you
In my defense, I have none
For never leaving well enough alone
But it would've been fun
If you would've been the one
(Ooh)
I have this dream you're doing cool shit
Having adventures on your own
You meet some woman on the internet and take her home
We never painted by the numbers, baby
But we were making it count
You know the greatest loves of all time are over now
I guess you never know, never know
And it's another day waking up alone
But we were something, don't you think so?
Roaring 20s, tossing pennies in the pool
And if my wishes came true
It would've been you
In my defense, I have none
For never leaving well enough alone
But it would've been fun
If you would've been the one
I, I, I persist and resist the temptation to ask you
If one thing had been different
Would everything be different today?
We were something, don't you think so?
Ros� flowing with your chosen family
And it would've been sweet
If it could've been me
In my defense, I have none
For digging up the grave another time
But it would've been fun
If you would've been the one
(Ooh)
Cardigan
Vintage tee, brand new phone
High heels on cobblestones
When you are young, they assume you know nothing
Sequin smile, black lipstick
Sensual politics
When you are young, they assume you know nothing
But I knew you
Dancin' in your Levi's
Drunk under a streetlight, I
I knew you
Hand under my sweatshirt
Baby, kiss it better, I
And when I felt like I was an old cardigan
Under someone's bed
You put me on and said I was your favorite
A friend to all is a friend to none
Chase two girls, lose the one
When you are young, they assume you know nothin'
But I knew you
Playing hide-and-seek and
Giving me your weekends, I
I knew you
Your heartbeat on the High Line
Once in 20 lifetimes, I
And when I felt like I was an old cardigan
Under someone's bed
You put me on and said I was your favorite
To kiss in cars and downtown bars
Was all we needed
You drew stars around my scars
But now I'm bleedin'
'Cause I knew you
Steppin' on the last train
Marked me like a bloodstain, I
I knew you
Tried to change the ending
Peter losing Wendy, I
I knew you
Leavin' like a father
Running like water, I
And when you are young, they assume you know nothing
But I knew you'd linger like a tattoo kiss
I knew you'd haunt all of my what-ifs
The smell of smoke would hang around this long
'Cause I knew everything when I was young
I knew I'd curse you for the longest time
Chasin' shadows in the grocery line
I knew you'd miss me once the thrill expired
And you'd be standin' in my front porch light
And I knew you'd come back to me
You'd come back to me
And you'd come back to me
And you'd come back
And when I felt like I was an old cardigan
Under someone's bed
You put me on and said I was your favorite
The last great American dynasty
Rebekah rode up on the afternoon train
It was sunny
Her saltbox house on the coast took her mind off St. Louis
Bill was the heir to the Standard Oil name and money
And the town said, "How did a middle-class divorcee do it?"
The wedding was charming, if a little gauche
There's only so far new money goes
They picked out a home and called it "Holiday House"
Their parties were tasteful, if a little loud
The doctor had told him to settle down
It must have been her fault his heart gave out
And they said
"There goes the last great American dynasty
Who knows, if she never showed up, what could've been
There goes the maddest woman this town has ever seen
She had a marvelous time ruinin' everything"
Rebekah gave up on the Rhode Island set forever
Flew in all her Pack friends from the city
Filled the pool with Champagne and swam with the big names
And blew through the money on the boys and the ballet
And losin' on card game bets with Dal�
And they said
"There goes the last great American dynasty
Who knows, if she never showed up, what could've been
There goes the most shameless woman this town has ever seen
She had a marvelous time ruinin' everything"
They say she was seen on occasion
Pacing the rocks, staring out at the midnight sea
And in a feud with her neighbor
She stole his dog and dyed it key lime green
50 years is a long time
Holiday House sat quietly on that beach
Free of women with madness, their men and bad habits
And then it was bought by me
Who knows, if I never showed up, what could've been
There goes the loudest woman this town has ever seen
I had a marvelous time ruinin' everything
I had a marvelous time ruinin' everything
A marvelous time ruinin' everything
A marvelous time
I had a marvelous time
Exile
I can see you standing, honey
With his arms around your body
Laughin', but the joke's not funny at all
And it took you five whole minutes
To pack us up and leave me with it
Holdin' all this love out here in the hall
I think I've seen this film before
And I didn't like the ending
You're not my homeland anymore
So what am I defending now?
You were my town
Now I'm in exile, seein' you out
I think I've seen this film before
I can see you starin', honey
Like he's just your understudy
Like you'd get your knuckles bloody for me
Second, third, and hundredth chances
Balancin' on breaking branches
Those eyes add insult to injury
I think I've seen this film before
And I didn't like the ending
I'm not your problem anymore
So who am I offending now?
You were my crown
Now I'm in exile, seein' you out
I think I've seen this film before
So I'm leavin' out the side door
So step right out, there is no amount
Of crying I can do for you
All this time
We always walked a very thin line
You didn't even hear me out (you didn't even hear me out)
You never gave a warning sign (I gave so many signs)
All this time
I never learned to read your mind (never learned to read my mind)
I couldn't turn things around (you never turned things around)
'Cause you never gave a warning sign (I gave so many signs)
So many signs, so many signs
You didn't even see the signs
I think I've seen this film before
And I didn't like the ending
You're not my homeland anymore
So what am I defending now?
You were my town
Now I'm in exile, seein' you out
I think I've seen this film before
So I'm leavin' out the side door
So step right out, there is no amount
Of crying I can do for you
All this time
We always walked a very thin line
You didn't even hear me out (didn't even hear me out)
You never gave a warning sign (I gave so many signs)
All this time
I never learned to read your mind (never learned to read my mind)
I couldn't turn things around (you never turned things around)
'Cause you never gave a warning sign (I gave so many signs)
All this time (so many signs)
I never learned to read your mind (so many signs)
I couldn't turn things around (I couldn't turn things around)
'Cause you never gave a warning sign (you never gave a warning sign)
You never gave a warning sign
Ah, ah
My tears ricochet
We gather here, we line up
Weepin' in a sunlit room, and
If I'm on fire, you'll be made of ashes too
Even on my worst day, did I deserve, babe
All the hell you gave me?
'Cause I loved you, I swear I loved you
'Til my dying day
I didn't have it in myself to go with grace
And you're the hero flying around, saving face
And if I'm dead to you, why are you at the wake?
Cursing my name, wishing I stayed
Look at how my tears ricochet
We gather stones, never knowing what they'll mean
Some to throw, some to make a diamond ring
You know I didn't want to have to haunt you
But what a ghostly scene
You wear the same jewels that I gave you
As you bury me
I didn't have it in myself to go with grace
'Cause when I'd fight, you used to tell me I was brave
And if I'm dead to you, why are you at the wake?
Cursing my name, wishing I stayed
Look at how my tears ricochet
And I can go anywhere I want
Anywhere I want, just not home
And you can aim for my heart, go for blood
But you would still miss me in your bones
And I still talk to you (when I'm screaming at the sky)
And when you can't sleep at night (you hear my stolen lullabies)
I didn't have it in myself to go with grace
And so the battleships will sink beneath the waves
You had to kill me, but it killed you just the same
Cursing my name, wishing I stayed
You turned into your worst fears
And you're tossing out blame, drunk on this pain
Crossing out the good years
And you're cursing my name, wishing I stayed
Look at how my tears ricochet
Mirrorball
I want you to know
I'm a mirrorball
I'll show you every version of yourself tonight
I'll get you out on the floor
Shimmering beautiful
And when I break it's in a million pieces
Hush
When no one is around, my dear
You'll find me on my tallest tiptoes
Spinning in my highest heels, love
Shining just for you
Hush
I know they said the end is near
But I'm still on my tallest tiptoes
Spinning in my highest heels, love
Shining just for you
I want you to know
I'm a mirrorball
I can change everything about me to fit in
You are not like the regulars
The masquerade revelers
Drunk as they watch my shattered edges glisten
Hush
When no one is around, my dear
You'll find me on my tallest tiptoes
Spinning in my highest heels, love
Shining just for you
Hush
I know they said the end is near
But I'm still on my tallest tiptoes
Spinning in my highest heels, love
Shining just for you
And they called off the circus
Burned the disco down
When they sent home the horses
And the rodeo clowns
I'm still on that tightrope
I'm still trying everything to get you laughing at me
I'm still a believer but I don't know why
I've never been a natural
All I do is try, try, try
I'm still on that trapeze
I'm still trying everything
To keep you looking at me
Because I'm a mirrorball
I'm a mirrorball
I'll show you every version of yourself
Tonight
Seven
Weight of the world on your shoulders
I'll kiss your waist and ease your mind
I must be favored to know ya
I take my hands and trace your lines
It's the way that we can ride
It's the way that we can ride (oh-oh, oh-oh)
Think I met you in another life
So break me off another time (oh-oh, oh-oh)
You wrap around me and you give me life
And that's why night after night
I'll be lovin' you right
Monday, Tuesday, Wednesday, Thursday, Friday
Saturday, Sunday (a week)
Monday, Tuesday, Wednesday, Thursday, Friday
Seven days a week
Every hour, every minute, every second
You know night after night
I'll be lovin' you right, seven days a week
You love when I jump right in
All of me, I'm offerin'
Show you what devotion is
Deeper than the ocean is
Wind it back, I'll take it slow
Leave you with that afterglow
Show you what devotion is
Deeper than the ocean is
It's the way that we can ride
It's the way that we can ride (oh-oh, oh-oh)
Think I met you in another life
So break me off another time (oh-oh, oh-oh)
You wrap around me and you give me life
And that's why night after night
I'll be lovin' you right, oh-oh-oh
Monday, Tuesday, Wednesday, Thursday, Friday
Saturday, Sunday (a week)
Monday, Tuesday, Wednesday, Thursday, Friday
Seven days a week
Every hour, every minute, every second
You know night after night
I'll be lovin' you right, seven days a week (yeah)
Monday, Tuesday, Wednesday, Thursday, Friday
Saturday, Sunday (a week)
Monday, Tuesday, Wednesday, Thursday, Friday (oh, oh)
Seven days a week
Every hour, every minute, every second
You know night after night
I'll be lovin' you right, seven days a week (Big Latto)
Tightly take control, tightly take his soul
Take your phone and put it in the camera roll
Leave them clothes at the door
Watchu waitin' for? Better come and hit yo' goals
Uh, he jump in it, both feet
Goin' 'til the sun up, we ain't gettin' no sleep
Seven days a week, seven different sheets
Seven different angles, I could be your fantasy
Open up, say, "Ah"
Come here, baby, let me swallow yo' pride
What you on? I can match your vibe
Hit me up and I'ma Cha Cha Slide
You make Mondays feel like weekends
I make him never think 'bout cheatin' (uh)
Got you skippin' work and meetings
Let's sleep in, yeah (seven days a week, ooh)
Monday, Tuesday, Wednesday, Thursday, Friday
Saturday, Sunday (a week)
Monday, Tuesday, Wednesday, Thursday, Friday
Seven days a week
Every hour, every minute, every second (oh, oh, oh)
You know night after night
I'll be lovin' you right, seven days a week (yeah)
Monday, Tuesday, Wednesday, Thursday, Friday
Saturday, Sunday (a week)
Monday, Tuesday, Wednesday, Thursday, Friday (ooh, ooh, ooh, ooh, ooh)
Seven days a week
Every hour, every minute, every second
You know night after night
I'll be lovin' you right, seven days a week
August
Salt air, and the rust on your door
I never needed anything more
Whispers of "Are you sure?"
"Never have I ever before"
But I can see us lost in the memory
August slipped away into a moment in time
'Cause it was never mine
And I can see us twisted in bedsheets
August sipped away like a bottle of wine
'Cause you were never mine
Your back beneath the sun
Wishin' I could write my name on it
Will you call when you're back at school?
I remember thinkin' I had you
But I can see us lost in the memory
August slipped away into a moment in time
'Cause it was never mine
And I can see us twisted in bedsheets
August sipped away like a bottle of wine
'Cause you were never mine
Back when we were still changin' for the better
Wanting was enough
For me, it was enough
To live for the hope of it all
Cancel plans just in case you'd call
And say, "Meet me behind the mall"
So much for summer love and saying "us"
'Cause you weren't mine to lose
You weren't mine to lose, no
But I can see us lost in the memory
August slipped away into a moment in time
'Cause it was never mine
And I can see us twisted in bedsheets
August sipped away like a bottle of wine
'Cause you were never mine
'Cause you were never mine, never mine
But do you remember?
Remember when I pulled up and said, "Get in the car"
And then canceled my plans just in case you'd call?
Back when I was livin' for the hope of it all, for the hope of it all
"Meet me behind the mall"
Remember when I pulled up and said, "Get in the car"
And then canceled my plans just in case you'd call?
Back when I was livin' for the hope of it all (for the hope of it all)
For the hope of it all
For the hope of it all
(For the hope of it all)
(For the hope of it all)
This is me trying 
I've been having a hard time adjusting
I had the shiniest wheels, now they're rusting
I didn't know if you'd care if I came back
I have a lot of regrets about that
Pulled the car off the road to the lookout
Could've followed my fears all the way down
And maybe I don't quite know what to say
But I'm here in your doorway
I just wanted you to know
That this is me trying
I just wanted you to know
That this is me trying
They told me all of my cages were mental
So I got wasted like all my potential
And my words shoot to kill when I'm mad
I have a lot of regrets about that
I was so ahead of the curve, the curve became a sphere
Fell behind on my classmates, and I ended up here
Pouring out my heart to a stranger
But I didn't pour the whiskey
I just wanted you to know
That this is me trying
I just wanted you to know
That this is me trying
At least I'm trying
And it's hard to be at a party when I feel like an open wound
It's hard to be anywhere these days when all I want is you
You're a flashback in a film reel on the one screen in my town
And I just wanted you to know
That this is me trying
(And maybe I don't quite know what to say)
I just wanted you to know
That this is me trying
At least I'm trying
Illicit affairs
Make sure nobody sees you leave
Hood over your head, keep your eyes down
Tell your friends you're out for a run
You'll be flushed when you return
Take the road less traveled by
Tell yourself you can always stop
What started in beautiful rooms
Ends with meetings in parking lots
And that's the thing about illicit affairs
And clandestine meetings and longing stares
It's born from just one single glance
But it dies, and it dies, and it dies
A million little times
Leave the perfume on the shelf
That you picked out just for him
So you leave no trace behind
Like you don't even exist
Take the words for what they are
A dwindling, mercurial high
A drug that only worked
The first few hundred times
And that's the thing about illicit affairs
And clandestine meetings and stolen stares
They show their truth one single time
But they lie, and they lie, and they lie
A million little times
And you wanna scream
Don't call me "kid"
Don't call me "baby"
Look at this godforsaken mess that you made me
You showed me colors
You know I can't see with anyone else
Don't call me "kid"
Don't call me "baby"
Look at this idiotic fool that you made me
You taught me a secret language
I can't speak with anyone else
And you know damn well
For you, I would ruin myself
A million little times
Invisible string
Green was the color of the grass
Where I used to read at Centennial Park
I used to think I would meet somebody there
Teal was the color of your shirt�
When you were sixteen at the yogurt shop
You used to work at to make a little money
Time, curious time
Gave me no compasses, gave me no signs
Were there clues I didn't see?
And isn't it just so pretty to think
All along there was some
Invisible string
Tying you to me?
Ooh
Bad was the blood of the song in the cab�
On your first trip to LA
You ate at my favorite spot for dinner
Bold was the waitress on our three year trip�
Getting lunch down by the lakes
She said I looked like an American singer
Time, mystical time
Cuttin' me open, then healin' me fine
Were there clues I didn't see?
And isn't it just so pretty to think
All along there was some
Invisible string
Tying you to me?
Ooh
A string that pulled me
Out of all the wrong arms right into that dive bar
Something wrapped all of my past mistakes in barbed wire
Chains around my demons, wool to brave the seasons
One single thread of gold tied me to you
Cold was the steel of my axe to grind�
For the boys who broke my heart
Now I send their babies presents
Gold was the color of the leaves�
When I showed you around Centennial Park
Hell was the journey but it brought me heaven
Time, wondrous time
Gave me the blues and then purple pink skies
And it's cool, baby, with me
And isn't it just so pretty to think
All along there was some
Invisible string
Tying you to me?
Ooh
Hee
Ooh
Mad woman
What did you think I'd say to that?
Does a scorpion sting when fighting back?
They strike to kill and you know I will
You know I will
What do you sing on your drive home?
Do you see my face in the neighbor's lawn?
Does she smile?
Or does she mouth, "Fuck you forever"?
Every time you call me crazy
I get more crazy
What about that?
And when you say I seem angry
I get more angry
And there's nothin' like a mad woman
What a shame she went mad
No one likes a mad woman
You made her like that
And you'll poke that bear 'til her claws come out
And you find something to wrap your noose around
And there's nothin' like a mad woman
Now I breathe flames each time I talk
My cannons all firin' at your yacht
They say, "Move on", but you know, I won't
And women like hunting witches, too
Doing your dirtiest work for you
It's obvious that wanting me dead�
Has really brought you two together
Every time you call me crazy
I get more crazy
What about that?
And when you say I seem angry
I get more angry
And there's nothin' like a mad woman
What a shame she went mad
No one likes a mad woman
You made her like that
And you'll poke that bear 'til her claws come out
And you find something to wrap your noose around
And there's nothin' like a mad woman
I'm takin' my time
Takin' my time
'Cause you took everything from me
Watchin' you climb
Watchin' you climb
Over people like me
The master of spin
Has a couple side flings
Good wives always know
She should be mad
Should be scathing like me
But no one likes a mad woman
What a shame she went mad
You made her like that
Epiphany
Keep your helmet, keep your life, son
Just a flesh wound, here's your rifle
Crawling up the beaches now
"Sir, I think he's bleeding out"
And some things you just can't speak about
With you, I serve
With you, I fall down, down
Watch you breathe in
Watch you breathing out, out
Something med school did not cover
Someone's daughter, someone's mother
Holds your hand through plastic now
"Doc, I think she's crashing out"
And some things you just can't speak about
Only 20 minutes to sleep
But you dream of some epiphany
Just one single glimpse of relief
To make some sense of what you've seen
With you, I serve
With you, I fall down, down (down)
Watch you breathe in
Watch you breathing out, out
With you, I serve
With you, I fall down (down), down (down)
Watch you breathe in
Watch you breathing out (out), out
Only 20 minutes to sleep
But you dream of some epiphany
Just one single glimpse of relief
To make some sense of what you've seen
Betty
Betty, I won't make assumptions
About why you switched your homeroom
But I think it's 'cause of me
Betty, one time, I was ridin' on my skateboard
When I passed your house
It's like I couldn't breathe
You heard the rumors from Inez
You can't believe a word she says most times
But this time, it was true
The worst thing that I ever did
Was what I did to you
But if I just showed up at your party
Would you have me?
Would you want me?
Would you tell me to go fuck myself?
Or lead me to the garden?
In the garden, would you trust me
If I told you it was just a summer thing?
I'm only 17, I don't know anythin'
But I know I miss you
Betty, I know where it all went wrong
Your favorite song was playin'
From the far side of the gym
I was nowhere to be found
I hate the crowds, you know that
Plus, I saw you dance with him
You heard the rumors from Inez
You can't believe a word she says most times
But this time, it was true
The worst thing that I ever did
Was what I did to you
But if I just showed up at your party
Would you have me? Would you want me?
Would you tell me to go fuck myself?
Or lead me to the garden?
In the garden, would you trust me
If I told you it was just a summer thing?
I'm only seventeen, I don't know anythin'
But I know I miss you
I was walkin' home on broken cobblestones
Just thinkin' of you when she pulled up like
A figment of my worst intentions
She said "James, get in, let's drive"
Those days turned into nights
Slept next to her, but
I dreamt of you all summer long
Betty, I'm here on your doorstep
And I planned it out for weeks now
But it's finally sinkin' in
Betty, right now is the last time
I can dream about what happens when
You see my face again
The only thing I wanna do
Is make it up to you
So I showed up at your party
Yeah, I showed up at your party
Yeah, I showed up at your party
Will you have me? Will you love me?
Will you kiss me on the porch
In front of all your stupid friends?
If you kiss me, will it be just like I dreamed it?
Will it patch your broken wings?
I'm only 17, I don't know anythin'
But I know I miss you
Standin' in your cardigan
Kissin' in my car again
Stopped at a streetlight
You know I miss you
Peace
Our coming-of-age has come and gone
Suddenly the summer, it's clear
I never had the courage of my convictions
As long as danger is near
And it's just around the corner, darling
'Cause it lives in me
No, I could never give you peace
But I'm a fire, and I'll keep your brittle heart warm
If your cascade ocean wave blues come
All these people think love's for show
But I would die for you in secret
The devil's in the details, but you got a friend in me
Would it be enough if I could never give you peace?
Your integrity makes me seem small
You paint dreamscapes on the wall
I talk shit with my friends
It's like I'm wasting your honor
And you know that I'd swing with you for the fences
Sit with you in the trenches
Give you my wild, give you a child
Give you the silence that only comes when two people understand each other
Family that I chose, now that I see your brother as my brother
Is it enough?
But there's robbers to the east, clowns to the west
I'd give you my sunshine, give you my best
But the rain is always gonna come if you're standing with me
But I'm a fire, and I'll keep your brittle heart warm
If your cascade ocean wave blues come
All these people think love's for show
But I would die for you in secret
The devil's in the details, but you got a friend in me
Would it be enough if I could never give you peace?
Would it be enough if I could never give you peace?
Would it be enough if I could never give you peace?
Hoax
My only one
My smoking gun
My eclipsed sun
This has broken me down
My twisted knife
My sleepless night
My win-less fight
This has frozen my ground
Stood on the cliffside
Screaming, "Give me a reason"
Your faithless love's the only hoax
I believe in
Don't want no other shade of blue
But you
No other sadness in the world would do
My best laid plan
Your sleight of hand
My barren land
I am ash from your fire
Stood on the cliffside
Screaming "Give me a reason"
Your faithless love's the only hoax
I believe in
Don't want no other shade of blue
But you
No other sadness in the world would do
You know I left a part of me back in New York
You knew the hero died, so what's the movie for?
You knew it still hurts underneath my scars
From when they pulled me apart
You knew the password, so I let you in the door
You knew you won, so what's the point of keeping score?
You knew it still hurts underneath my scars
From when they pulled me apart
But what you did was just as dark
Darling, this was just as hard
As when they pulled me apart
My only one
My kingdom come undone
My broken drum
You have beaten my heart
Don't want no other shade of blue
But you
No other sadness in the world would do
'''

verses = folklore_lyrics.split("\n")
def preprocess(folklore_lyrics):
    doc = nlp(folklore_lyrics)
    tokens = [token.text.lower() for token in doc if not token.is_stop and not token.is_punct]
    return ' '.join(tokens)
verses_preprocessed = [preprocess(verse) for verse in verses]

print(verses_preprocessed)