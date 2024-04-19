import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.

n89_lyrics = '''
Welcome to New York
Walkin' through a crowd, the village is aglow
Kaleidoscope of loud heartbeats under coats
Everybody here wanted somethin' more
Searchin' for a sound we hadn't heard before
And it said
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
It's a new soundtrack, I could dance to this beat, beat forevermore
The lights are so bright, but they never blind me, me
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
When we first dropped our bags on apartment floors
Took our broken hearts, put them in a drawer
Everybody here was someone else before
And you can want who you want
Boys and boys and girls and girls
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
It's a new soundtrack, I could dance to this beat, beat forevermore
The lights are so bright, but they never blind me, me
Welcome to New York (New York), it's been waitin' for you
Welcome to New York, welcome to New York
Like any great love, it keeps you guessing
Like any real love, it's ever-changing
Like any true love, it drives you crazy
But you know you wouldn't change anything, anything, anything
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
Welcome to New York, it's been waitin' for you
Welcome to New York, welcome to New York
It's a new soundtrack, I could dance to this beat
The lights are so bright, but they never blind me
Welcome to New York (new soundtrack), it's been waitin' for you
Welcome to New York (the lights are so bright but they never blind me)
Welcome to New York (so bright, they never blind me)
Welcome to New York
Welcome to New York
Blank Space
Nice to meet you, where you been?
I could show you incredible things
Magic, madness, heaven, sin
Saw you there and I thought
"Oh, my God, look at that face
You look like my next mistake
Love's a game, wanna play?" Ay
New money, suit and tie
I can read you like a magazine
Ain't it funny? Rumors fly
And I know you heard about me
So hey, let's be friends
I'm dying to see how this one ends
Grab your passport and my hand
I can make the bad guys good for a weekend
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless
We'll take this way too far
It'll leave you breathless, mm
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
Cherry lips, crystal skies
I could show you incredible things
Stolen kisses, pretty lies
You're the King, baby, I'm your Queen
Find out what you want
Be that girl for a month
Wait, the worst is yet to come, oh, no
Screaming, crying, perfect storms
I can make all the tables turn
Rose garden filled with thorns
Keep you second guessing like
"Oh, my God, who is she?"
I get drunk on jealousy
But you'll come back each time you leave
'Cause, darling, I'm a nightmare dressed like a daydream
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over, mm
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless (oh)
We'll take this way too far
It'll leave you breathless, mm (oh)
Or with a nasty scar
Got a long list of ex-lovers
They'll tell you I'm insane (insane)
But I've got a blank space, baby
And I'll write your name
Boys only want love if it's torture
Don't say I didn't, say I didn't warn ya
Boys only want love if it's torture
Don't say I didn't, say I didn't warn ya
So it's gonna be forever
Or it's gonna go down in flames
You can tell me when it's over (over)
If the high was worth the pain
Got a long list of ex-lovers
They'll tell you I'm insane (I'm insane)
'Cause you know I love the players
And you love the game
'Cause we're young, and we're reckless
We'll take this way too far (ooh)
It'll leave you breathless, mm
Or with a nasty scar (leave a nasty scar)
Got a long list of ex-lovers
They'll tell you I'm insane
But I've got a blank space, baby
And I'll write your name
Out of the woods
Looking at it now
It all seems so simple
We were lying on your couch
I remember
You took a Polaroid of us
Then discovered (then discovered)
The rest of the world was black and white
But we were in screaming color
And I remember thinking
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet, in the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet, in the clear yet? Good
Are we out of the woods?
Looking at it now
Last December (last December)
We were built to fall apart
And fall back together (back together)
Ooh, your necklace hanging from my neck
The night we couldn't quite forget
When we decided, we decided
To move the furniture so we could dance
Baby, like we stood a chance
Two paper airplanes flying, flying, flying
And I remember thinking
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet, in the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods? (Oh-oh, oh, oh)
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet, in the clear yet? Good
Are we out of the woods? (Yeah)
Remember when you hit the brakes too soon?
20 stitches in a hospital room
When you started crying, baby, I did too
But when the sun came up, I was looking at you
Remember when we couldn't take the heat?
I walked out, I said, "I'm setting you free"
But the monsters turned out to be just trees
When the sun came up, you were looking at me
You were looking at me, oh
You were looking at me
I remember
(Are we in the clear yet? Are we in the clear yet?)
(Are we in the clear yet, in the clear yet? Good) oh, I remember
Are we out of the woods yet? Are we out of the woods yet? (Yeah)
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet? (So, are we?)
Are we in the clear yet, in the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? (Yeah) are we in the clear yet? (Yeah)
Are we in the clear yet, in the clear yet? Good
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet, in the clear yet? Good (do you remember?)
Are we out of the woods yet? Are we out of the woods yet?
Are we out of the woods yet? Are we out of the woods?
Are we in the clear yet? Are we in the clear yet?
Are we in the clear yet, in the clear yet? Good
All you had to do was stay
People like you always want back the love they gave away
And people like me wanna believe you when you say you've changed
The more I think about it now, the less I know
All I know is that you drove us off the road
Stay
Hey, all you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
Hey, now you say you want it back
Now that it's just too late
Well, it could've been easy
All you had to do was (stay)
All you had to do was (stay)
All you had to do was (stay)
All you had to do was (stay)
All you had to do was stay
Here you are now, calling me up, but I don't know what to say
I've been picking up the pieces of the mess you made
People like you always want back the love they pushed aside
But people like me are gone forever when you say goodbye
Hey, all you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
Hey, now you say you want it back
Now that it's just too late
Well, it could've been easy
All you had to do was (stay)
All you had to do was (stay)
All you had to do was (stay)
All you had to do was (stay, stay, stay, stay, stay)
Let me remind you
This was what you wanted (oh, oh, oh-oh-oh)
You ended it
You were all I wanted (oh, oh, oh-oh-oh)
But not like this
Not like this
Not like this
Oh, all you had to do was-
Hey, all you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
Hey, now you say you want it back
Now that it's just too late
Well, it could've been easy
All you had to do was (stay)
Hey, all you had to do was stay
Had me in the palm of your hand
Then why'd you have to go and lock me out when I let you in?
Hey, now you say you want it back
Now that it's just too late
Well, it could've been easy (all you had to do was stay)
All you had to do was (stay)
All you had to do was (stay) oh
All you had to do was (stay)
All you had to do was (stay) ooh
All you had to do was (stay)
I wish you would
It's 2 A.M. in your car
Windows down, I pass my street
The memories start
You say it's in the past
And drive straight ahead
You think I'm gonna hate you now
'Cause you still don't know what I never said
I wish you would come back
Wish I'd never hung up the phone like I did
I wish you knew that
I'd never forget you as long as I'd live
And I wish you were right here, right now
It's all good
I wish you would
It's 2 A.M. in my room
Headlights pass the window pane
I think of you
We're a crooked love
In a straight line down
Makes you wanna run and hide
Then it makes you turn right back around
I wish you would come back
Wish I'd never hung up the phone like I did
I wish you knew that
I'd never forget you as long as I'd live
And I wish you were right here, right now
It's all good
I wish you would
I wish we could go back
And remember what we were fighting for
Wish you knew that
I miss you too much to be mad anymore
And I wish you were right here, right now
It's all good
I wish you would
I I I I, I I I wish, I wish, I
I I I I, I I I wish, I wish, I
I I I I, I I I wish, I wish, I
You always knew how to push my buttons (I I I I, I I I wish, I wish, I)
You gave me everything and nothing (I I I I, I I I wish, I wish, I)
This mad, mad love makes you come rushing (I I I I, I I I wish, I wish, I)
Stand back where you stood (I I I I, I I I wish, I wish, I)
I wish you would, I wish you would (I I I I, I I I wish, I wish, I)
I wish you would, I wish you would (I I I I, I I I wish, I wish, I)
(I wish you would, I wish you would) (I wish, I wish, I)
2 A.M., here we are
See your face
Hear my voice in the dark
We're a crooked love
In a straight line down
Guess you wanna run and hide
But it made us turn right back around
I wish you would come back
Wish I'd never hung up the phone like I did
I wish you knew that
I'd never forget you as long as I'd live
And I wish you were right here, right now
It's all good
I wish you would
I wish you would come back
Wish I'd never hung up the phone like I did
I wish you knew that
I'd never forget you as long as I'd live
And I wish you were right here, right now
It's all good
I wish you would
I wish we could go back
And remember what we were fighting for
Wish you knew that
I miss you too much to be mad anymore
And I wish you were right here, right now
It's all good
I wish you would
You always knew how to push my buttons (I I I I, I I I wish, I wish, I)
You gave me everything and nothing (I I I I, I I I wish, I wish, I)
This mad, mad love makes you come rushing (I I I I, I I I wish, I wish, I)
Stand back where you stood (I I I I, I I I wish, I wish, I)
I wish you would, I wish you would (I I I I, I I I wish, I wish, I)
I wish you would, I wish you would (I I I I, I I I wish, I wish, I)
(I wish you would, I wish you would)
I wish you would, I wish you would (I I I I, I I I wish, I wish, I)
(I wish you would, I wish you would) (I wish I, I wish I)
I I I I, I I I wish, I wish, I
I I I I, I I I wish, I wish, I (I wish you would)
Bad blood
'Cause baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we got bad blood (hey!)
Now we got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we got bad blood (hey!)
Did you have to do this?
I was thinking that you could be trusted
Did you have to ruin
What was shining? Now it's all rusted
Did you have to hit me
Where I'm weak? Baby, I couldn't breathe
And rub it in so deep
Salt in the wound like you're laughing right at me
Oh, it's so sad to think about the good times
You and I
'Cause baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we got bad blood (hey!)
Now we got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we got bad blood (hey!)
Did you think we'd be fine?
Still got scars on my back from your knife
So don't think it's in the past
These kind of wounds they last and they last
Now did you think it all through?
All these things will catch up to you
And time can heal, but this won't
So if you come in my way, just don't
Oh, it's so sad to think about the good times
You and I
'Cause baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we got bad blood (hey!)
Now we got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we got bad blood (hey!)
Band-aids don't fix bullet holes
You say sorry just for show
If you live like that, you live with ghosts (ghosts, ghosts)
Band-aids don't fix bullet holes (hey!)
You say sorry just for show (hey!)
If you live like that, you live with ghosts (hey!)
Hm, if you love like that, blood runs cold
'Cause baby, now we got bad blood
You know it used to be mad love
So take a look what you've done
'Cause baby, now we got bad blood (hey!)
Now we got problems
And I don't think we can solve 'em (think we can solve 'em)
You made a really deep cut
And baby, now we got bad blood (hey!)
'Cause baby, now we got bad blood
You know it used to be mad love
So take a look what you've done (look what you've done)
'Cause baby, now we got bad blood (hey!)
Now we got problems
And I don't think we can solve 'em
You made a really deep cut
And baby, now we got bad blood (hey!)
How you get the girl
Stand there like a ghost
Shaking come the rain, rain
She'll open up the door
And say, are you insane, -ane?
Say it's been a long six months (oh oh oh, oh oh oh, oh oh, oh oh)
And you were too afraid to tell her what you want, want (oh oh oh, oh oh oh, oh oh, oh oh)
And that's how it works
That's how you get the girl
And then you say
I want you for worse or for better
I would wait for ever and ever
Broke your heart, I'll put it back together
I would wait for ever and ever
And that's how it works
That's how you get the girl, girl, oh
And that's how it works
That's how you get the girl, girl
Remind her how it used to be, be
Yeah, with pictures in frames of kisses on cheeks, cheeks
Tell her how you must've lost your mind (oh oh oh, oh oh oh, oh oh, oh oh)
When you left her all alone and never told her why, why (oh oh oh, oh oh oh, oh oh, oh oh)
And that's how it works
That's how you lost the girl
And now you say
I want you for worse or for better
I would wait for ever and ever (ever and ever)
Broke your heart, I'll put it back together
I would wait for ever and ever
And that's how it works
That's how you get the girl, girl, oh
And that's how it works
That's how you get the girl, girl, yeah
And you could know, oh
That I don't want you to go
Remind me how it used to be
Pictures in frames of kisses on cheeks
And say you want me, yeah, yeah
And then you say I want you for worse or for better (worse or for better)
I would wait for ever and ever (ever and ever)
Broke your heart, I'll put it back together
I would wait for ever and ever (I want you for ever and ever)
And that's how it works
That's how you get the girl, girl, oh
(That's how it works) and that's how it works
That's how you get the girl, girl, oh (get the girl)
and that's how it works
That's how you get the girl, girl, oh
And that's how it works
That's how you get the girl, girl, oh
And that's how it works
That's how you got the girl
This Love
Clear blue water
High tide came and brought you in
And I could go on and on, on and on, and I will
Skies grew darker
Currents swept you out again
And you were just gone and gone, gone and gone
In silent screams
In wildest dreams
I never dreamed of this
This love is good
This love is bad
This love is alive back from the dead, oh, oh, oh
These hands had to let it go free, and
This love came back to me, oh, oh, oh
Ohh
Oh, oh, oh
Tossing, turning
Struggled through the night with someone new
And I could go on and on, on and on
Lantern, burning
Flickered in the night, only you
But you were still gone, gone, gone
In losing grip
On sinking ships
You showed up just in time
This love is good
This love is bad
This love is alive back from the dead, oh, oh, oh
These hands had to let it go free, and
This love came back to me, oh, oh, oh
This love left a permanent mark
This love is glowing in the dark, oh, oh, oh
These hands had to let it go free, and
This love came back to me, oh, oh, oh
Your kiss, my cheek
I watched you leave
Your smile, my ghost
I fell to my knees
When you're young, you just run
But you come back to what you need
This love is good
This love is bad
This love is alive back from the dead, oh, oh, oh
These hands had to let it go free, and
This love came back to me, oh, oh, oh
This love left a permanent mark
This love is glowing in the dark, oh, oh, oh
These hands had to let it go free, and
This love came back to me, oh, oh, oh
This love came back to me, oh, oh, oh
Clean
The drought was the very worst
(Oh-oh, oh-oh)
When the flowers that we'd grown together died of thirst
It was months and months of back and forth
(Oh-oh, oh-oh)
You're still all over me
Like a wine-stained dress I can't wear anymore
Hung my head as I lost the war
And the sky turned black like a perfect storm
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning
Gone was any trace of you, I think I am finally clean
(Oh, oh, oh, oh)
There was nothing left to do
(Oh-oh, oh-oh)
When the butterflies turned to dust that covered my whole room
So I punched a hole in the roof
(Oh-oh, oh-oh)
Let the flood carry away all my pictures of you
The water filled my lungs, I screamed so loud
But no one heard a thing
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning
Gone was any trace of you, I think I am finally clean
(Oh, oh, oh, oh)
I think I am finally clean
(Oh, oh) Oh, oh, oh, oh, oh-oh
Said, I think I am finally clean
(Oh, oh) Oh, oh, oh, oh, oh-oh
Ten months sober, I must admit
Just because you're clean, don't mean you don't miss it
Ten months older, I won't give in
Now that I'm clean, I'm never gonna risk it
The drought was the very worst
(Oh-oh, oh-oh)
When the flowers that we'd grown together died of thirst
(Oh)
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning
Gone was any trace of you, I think I am finally clean
Rain came pouring down
When I was drowning, that's when I could finally breathe
And by morning
Gone was any trace of you, I think I am finally clean
Finally clean
Think I'm finally clean (oh, oh)
Oh-oh, oh-oh
(Oh, oh, oh) Think I'm finally clean
Wonderland
Flashing lights and we
Took a wrong turn and we
Fell down a rabbit hole
You held on tight to me
'Cause nothing's as it seems
And spinning out of control
Didn't they tell us don't rush into things?
Didn't you flash your green eyes at me?
Haven't you heard what becomes of curious minds?
Ooh, didn't it all seem new and exciting?
I felt your arms twisting around me
I should've slept with one eye open at night
We found Wonderland
You and I got lost in it
And we pretended it could last forever, eh, eh
We found Wonderland
You and I got lost in it
And life was never worse but never better, eh, eh
(Eh, eh, eh, eh, eh) in Wonderland
(Eh, eh, eh, eh, eh) in Wonderland
(Eh, eh, eh, eh, eh) in Wonderland
(Eh, eh, eh, eh, eh) in Wonderland
So we went on our way
Too in love to think straight
All alone, or so it seemed
But there were strangers watching
And whispers turned to talking
And talking turned to screams, oh
Didn't they tell us don't rush into things?
Didn't you flash your green eyes at me?
Didn't you call my fears with a Cheshire Cat smile?
Ooh, didn't it all seem new and exciting?
I felt your arms twisting around me
It's all fun and games 'til somebody loses their mind
Oh, darling, we found Wonderland
You and I got lost in it
And we pretended it could last forever, eh, eh
We found Wonderland
You and I got lost in it
And life was never worse but never better, eh, eh
(Eh, eh, eh, eh, eh) in Wonderland
(Eh, eh, eh, eh, eh) in Wonderland
(Eh, eh, eh, eh, eh) in Wonderland
(Eh, eh, eh, eh, eh) in Wonderland
I reached for you
But you were gone
I knew I had to go back home
You search the world for something else
To make you feel like what we had
And in the end, in Wonderland, we both went mad
Oh, we found Wonderland
You and I got lost in it
And we pretended it could last forever, eh, eh (last forever)
We found Wonderland
You and I got lost in it (got lost in it)
And life was never worse but never better, eh, eh (never better)
We found Wonderland (eh, eh, eh, eh, eh)
You and I got lost in it (in Wonderland)
And we pretended it (eh, eh, eh, eh, eh)
Could last forever (in Wonderland)
We found Wonderland (eh, eh, eh, eh, eh)
You and I got lost in it (in Wonderland)
And life was never worse but never better (eh, eh, eh, eh, eh)
In Wonderland
New romantics
We're all bored
We're all so tired of everything
We wait for trains that just aren't coming
We show off our different scarlet letters
Trust me, mine is better
We're so young
But we're on the road to ruin
We play dumb but we know exactly what we're doin'
We cry tears of mascara in the bathroom
Honey, life is just a classroom
(Ah-ah-ah-ah-ah-ah)
'Cause baby, I could build a castle
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
Baby, we're the new romantics
Come on, come along with me
Heartbreak is the national anthem
We sing it proudly
We are too busy dancing
To get knocked off our feet
Baby, we're the new romantics
The best people in life are free
We're all here
The lights and noise are blinding
We hang back
It's all in the timing
It's poker
He can't see it in my face
But I'm about to play my Ace (ah)
We need love
But all we want is danger
We team up
Then switch sides like a record changer
The rumors are terrible and cruel
But honey, most of them are true
(Ah-ah-ah-ah-ah-ah)
'Cause baby, I could build a castle
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
Baby, we're the new romantics
Come on, come along with me
Heartbreak is the national anthem
We sing it proudly
We are too busy dancing
To get knocked off our feet
Baby, we're the new romantics
The best people in life are free
Oh-oh
(Oh, oh, oh-oh, oh)
So, come on, come along with me
(Oh, oh, oh-oh, oh)
The best people in life are free
(Oh, oh, oh-oh, oh)
Please take my hand and
Please take me dancing, and
Please leave me stranded
It's so romantic (it's so romantic)
(Ah-ah-ah-ah-ah-ah)
Oh, 'cause baby, I could build a castle
Out of all the bricks they threw at me
And every day is like a battle (oh-oh)
But every night with us is like a dream
'Cause baby, I could build a castle (castle)
Out of all the bricks they threw at me
And every day is like a battle
But every night with us is like a dream
Baby, we're the new romantics
Come on, come along with me
Heartbreak is the national anthem
We sing it proudly
We are too busy dancing
To get knocked off our feet
Baby, we're the new romantics
The best people in life are free
"Slut!"
Flamingo pink
Sunrise Boulevard
Clink, clink
Being this young is art
Aquamarine
Moonlit swimming pool
What if all I need is you?
Got lovestruck, went straight to my head
Got lovesick, all over my bed
Love to think you'll never forget
Handprints in wet cement
Adorned with smoke on my clothes
Lovelorn and nobody knows
Love thorns all over this rose
I'll pay the price, you won't
But if I'm all dressed up
They might as well be looking at us
And if they call me a slut
You know it might be worth it for once
And if I'm gonna be drunk
Might as well be drunk in love
Send the code, he's waiting there
The sticks and stones they throw froze mid-air
Everyone wants him
That was my crime
The wrong place at the right time
And I break down, then he's pullin' me in
In a world of boys, he's a gentleman
Got lovestruck, went straight to my head
Got lovesick, all over my bed
Love to think you'll never forget
We'll pay the price, I guess
But if I'm all dressed up
They might as well be looking at us
If they call me a slut
You know it might be worth it for once
And if I'm gonna be drunk
I might as well be drunk in love
Half asleep
Taking your time
In the tangerine, neon light
This is luxury
You're not saying you're in love with me
But you're going to
Half awake
Taking your chance
It's a big mistake
I said it might blow up in your pretty face
I'm not saying do it anyway
But you're going to
And if they call me a slut
You know it might be worth it for once
And if I'm gonna be drunk
Might as well be drunk in love
Now that we don't talk
You went to a party
I heard from everybody
You part the crowd like the Red Sea
Don't even get me started
Did you get anxious though
On the way home?
I guess I'll never, ever know
Now that we don't talk
You grew your hair long
You got new icons
And from the outside
It looks like you're tryin' lives on
I miss the old ways
You didn't have to change
But I guess I don't have a say
Now that we don't talk
I call my mom, she said that it was for the best
Remind myself the more I gave, you'd want me less
I cannot be your friend
So I pay the price of what I lost
And what it cost
Now that we don't talk
What do you tell your friends we
Shared dinners, long weekends with
Truth is I can't pretend it's
Platonic, it's just ended
So I call my mom, she said to get it off my chest (off my chest)
Remind myself the way you faded 'til I left ('til I left)
I cannot be your friend
So I pay the price of what I lost (of what I lost)
And what it cost
Now that we don't talk
I don't have to pretend I like acid rock
Or that I'd like to be on a mega yacht
With important men who think important thoughts
Guess maybe I am better off
Now that we don't talk
And the only way back to my dignity
Was to turn into a shrouded mystery
Just like I had been when you were chasing me
Guess this is how it has to be
Now that we don't talk
Suburban Legends
You had people who called you on unmarked numbers
In my peripheral vision
I let it slide like a hose on a slippery plastic summer
All was quickly forgiven
You were so magnetic it was almost obnoxious
Flush with the currency of cool
I was always turning out my empty pockets
And when it came to you
I didn't come here to make friends
We were born to be suburban legends
When you hold me, it holds me together
And you kiss me in a way that's gonna screw me up forever
I had the fantasy that maybe our mismatched star signs would surprise the whole school
When I ended up back at our class reunion walking in with you
You'd be more than a chapter in my old diaries with the pages ripped out
I am standing in a 1950s gymnasium and I can still see you now
I didn't come here to make friends
We were born to be suburban legends
When you hold me, it holds me together
And you kiss me in a way that's gonna screw me up forever
I know that you still remember
We were born to be national treasures
When you told me we'd get back together
And you kissed me in a way that's gonna screw me up forever
Tick-tock on the clock
I pace down your block
I broke my own heart 'cause you were too polite to do it
Waves crash on the shore
I dash to the door
You don't knock anymore
And my whole life's ruined
Tick-tock on the clock
I pace down your block
I broke my own heart 'cause you were too polite to do it
Waves crash to the shore
I dash to the door
You don't knock anymore
And I always knew it
That my life would be ruined
Sweeter than fiction
Hit the ground, hit the ground, hit the ground, oh oh
Only sound, only sound that you hear is, "No"
You never saw it coming, slipped when you started running
And now you've come undone and I, I, I, I
Seen you fall, seen you crawl on your knees, eh eh
Seen you lost in a crowd, seen your colors fade
Wish I could make it better, someday you won't remember
This pain you thought would last forever and ever
There you'll stand, ten feet tall
I will say I knew it all along
Your eyes wider than distance
This life is sweeter than fiction
Just a shot, just a shot in the dark, oh oh
All you got, all you got are your shattered hopes
They never saw it coming, you hit the ground running
And now you're onto something, I, I, I say
What a sight, what a sight when the light came on
Proved me right, proved me right when you proved them wrong
And in this perfect weather, it's like we don't remember
The rain we thought would last forever and ever
There you'll stand, ten feet tall
I will say I knew it all along
Your eyes wider than distance
This life is sweeter than fiction (sweeter than fiction)
There you'll stand next to me (next to me)
All at once, the rest is history
Your eyes wider than distance
This life is sweeter than fiction (sweeter than fiction)
I'll be one of the many saying
Look at you now, look at you now, now
I'll be one of the many saying
You made us proud, you made us proud, proud
I'll be one of the many saying
Look at you now, look at you now, now
I'll be one of the many saying
You made us proud, you made us proud, proud
And when they call your name
And they put your picture in a frame
You know that I'll be there time and again
'Cause I loved you when, when you
Hit the ground, hit the ground, hit the ground, oh oh
Only sound, only sound that you heard was, "No"
Now in this perfect weather, it's like we don't remember
The rain we thought would last forever and ever (forever)
There you'll stand, ten feet tall (ten feet tall)
I will say I knew it all along
Your eyes wider than distance (knew it all along)
This life is sweeter than fiction (sweeter than fiction)
There you'll stand next to me (next to me)
All at once, the rest is history
Your eyes wider than distance (knew it all along)
This life is sweeter than fiction (sweeter than fiction)
It's sweeter than fiction
It's sweeter, yeah
It's sweeter, it's sweeter
Sweeter than fiction
Is it over now?
Once the flight had flown
With the wilt of the rose
I slept all alone
You still wouldn't go
Let's fast forward to three hundred takeout coffees later
I see your profile and your smile on unsuspecting waiters
You dream of my mouth before it called you a lying traitor
You search in every maiden's bed for something greater
Baby, was it over
When she laid down on your couch?
Was it over when he unbuttoned my blouse?
"Come here, " I whispered in your ear
In your dream as you passed out, baby
Was it over then?
And is it over now?
When you lost control
Red blood, white snow
Blue dress on a boat
Your new girl is my clone
And did you think I didn't see you?
There were flashing lights
At least I had the decency
To keep my nights out of sight
Only rumors 'bout my hips and thighs
And my whispered sighs
Oh, Lord, I think about
Jumping off of very tall somethings
Just to see you come running
And say the one thing I've been wanting
But no
Let's fast forward to three hundred awkward blind dates later
If she's got blue eyes, I will surmise that you'll probably date her
You dream of my mouth before it called you a lying traitor
You search in every model's bed for something greater
Baby, was it over
When she laid down on your couch?
Was it over when he unbuttoned my blouse?
"Come here, " I whispered in your ear
In your dream as you passed out, baby
Was it over then?
And is it over now?
Think I didn't see you?
There were flashing lights
At least I had the decency
To keep my nights out of sight
Only rumors 'bout my hips and thighs
And my whispered sighs
Oh, Lord, I think about
Jumping off of very tall somethings
Just to see you come running
And say the one thing I've been wanting
But no
Let's fast forward to three hundred takeout coffees later
(Flashing lights) I was hoping you'd be there
And say the one thing (oh, Lord) I've been wanting (oh, Lord)
But no
Say don't go
I've known it from the very start
We're a shot in the darkest dark
Oh no, oh no, I'm unarmed
The waiting is a sadness
Fading into madness
Oh no, oh no, it won't stop
I'm standin' on a tightrope alone
I hold my breath a little bit longer
Halfway out the door, but it won't close
I'm holdin' out hope for you to
Say, "Don't go"
I would stay forever if you say, "Don't go"
Why'd you have to lead me on?
Why'd you have to twist the knife?
Walk away and leave me bleedin', bleedin'?
Why'd you whisper in the dark?
Just to leave me in the night?
Now your silence has me screamin', screamin'
go"
I would stay forever if you (say) say, "(don't) don't (go) go"
(Say, say, say, say)
Now I'm pacin' on shaky ground
Strike a match, then you blow it out
Oh no, oh no, it's not fair
'Cause you kiss me and it stops time
And I'm yours, but you're not mine
Oh no, oh no, you're not there
I'm standin' on the sidewalk alone
I wait for you to drive by
I'm tryna see the cards that you won't show
I'm about to fold unless you
go"
I would stay forever if you (say) say, "(don't) don't (go) go"
Why'd you have to lead me on?
Why'd you have to twist the knife?
Walk away and leave me bleedin', bleedin'?
Why'd you whisper in the dark?
Just to leave me in the night?
Now your silence has me screamin', screamin'
go"
I would stay forever if you (say) say, "(don't) don't (go) go, " whoa
(Say, say, say, say)
Why'd you have to (why'd you have to)
Make me want you (make me want you)?
Why'd you have to (why'd you have to)
Give me nothin' back?
Why'd you have to (why'd you have to)
Make me love you (make me love you)?
I said, "I love you" (I said, "I love you")
You say nothin' back
Why'd you have to lead me on? (Oh)
Why'd you have to twist the knife?
Walk away and leave me bleedin', bleedin'?
Why'd you whisper in the dark
Just to leave me in the night?
Now your silence has me screamin', screamin'
go"
I would stay forever if you (say) say, "(don't) don't (go) go, " whoa
(Say, say, say, say)
But you won't, but you won't, but you won't
I would stay forever if you say, "don't go"
But you won't, but you won't, but you won't
Wildest dreams
He said, "Let's get out of this town
Drive out of the city, away from the crowds"
I thought Heaven can't help me now
Nothing lasts forever
But this is gonna take me down
He's so tall and handsome as hell
He's so bad, but he does it so well
I can see the end as it begins
My one condition is
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just in your wildest dreams, ah-ah, ha
Wildest dreams, ah-ah, ha
I said, "No one has to know what we do"
His hands are in my hair, his clothes are in my room
And his voice is a familiar sound
Nothing lasts forever
But this is getting good now
He's so tall and handsome as hell
He's so bad, but he does it so well
And when we've had our very last kiss
My last request is
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just in your wildest dreams, ah-ah, ha (ha-ah, ha)
Wildest dreams, ah-ah, ha
You'll see me in hindsight
Tangled up with you all night
Burning it down
Someday when you leave me
I bet these memories
Follow you around
You'll see me in hindsight
Tangled up with you all night
Burning (burning) it (it) down (down)
Someday when you leave me
I bet these memories
Follow (follow) you (you) around (follow you around)
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just pretend
Say you'll remember me
Standing in a nice dress
Staring at the sunset, babe
Red lips and rosy cheeks
Say you'll see me again
Even if it's just (pretend, just pretend) in your wildest dreams, ah-ah, ha (ah)
In your wildest dreams, ah-ah, ha
Even if it's just stayed in your wildest dreams, ah-ah, ha
In your wildest dreams, ah-ah, ha
You are in love
One look, dark room
Meant just for you
Time moved too fast
You play it back
Buttons on a coat
Light-hearted joke
No proof, not much
But you saw enough
Small talk, he drives
Coffee at midnight
The light reflects
The chain on your neck
He says, "Look up"
And your shoulders brush
No proof, one touch
But you felt enough
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
Morning, his place
Burnt toast, Sunday
You keep his shirt
He keeps his word
And for once, you let go
Of your fears and your ghosts
One step, not much
But it said enough
You kiss on sidewalks
You fight and you talk
One night he wakes
Strange look on his face
Pauses, then says
You're my best friend
And you knew what it was
He is in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
And so it goes
You two are dancing in a snow globe, 'round and 'round
And he keeps the picture of you in his office downtown
And you understand now why they lost their minds and fought the wars
And why I've spent my whole life tryin' to put it into words
'Cause you can hear in the silence
You can feel it on the way home
You can see it with the lights out
You are in love, true love
You are in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
You can hear it in the silence, silence, you
You can feel it on the way home, way home, you
You can see it with the lights out, lights out
You are in love, true love
You are in love
I know places
I-I-I, I, I-I-I, I
I-I-I, I, I-I-I, I
I-I-I, I, I-I-I, I, I, I
You stand with your hand on my waistline
It's a scene, and we're out here in plain sight
I can hear them whisper as we pass by
It's a bad sign, bad sign
Somethin' happens when everybody finds out
See the vultures circling, dark clouds
Love's a fragile little flame, it could burn out
It could burn out
'Cause they got the cages, they got the boxes
And guns
They are the hunters, we are the foxes
And we run
Baby, I know places we won't be found, and
They'll be chasing their tails trying to track us down
'Cause I, I know places we can hide
I know places
I know places
Lights flash and we'll run for the fences
Let them say what they want, we won't hear it
Loose lips sink ships all the damn time
Not this time
Just grab my hand and don't ever drop it
My love
They are the hunters, we are the foxes
And we run
Baby, I know places we won't be found, and
They'll be chasing their tails trying to track us down
'Cause I, I know places we can hide
I know places
They are the hunters, we are the foxes
And we run
Just grab my hand and don't ever drop it
My love
Baby, I know places we won't be found, and
They'll be chasing their tails trying to track us down
'Cause I, I know places we can hide
I know places
they take their shots, but we're bulletproof
I know places
(Hide) and you know for me, it's always you
I know places
(I) in the dead of night, your eyes so green
I know places
(Hide) and I know for you, it's always me
I know places
I-I-I, I, I-I-I, I
I-I-I, I, I-I-I, I
I stay out too late
Got nothing in my brain
That's what people say, mm-mm
That's what people say, mm-mm
I go on too many dates
But I can't make 'em stay
At least that's what people say, mm-mm
That's what people say, mm-mm
But I keep cruisin'
Can't stop, won't stop movin'
It's like I got this music in my mind
Sayin' it's gonna be alright
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
I never miss a beat
I'm lightnin' on my feet
And that's what they don't see, mm-mm
That's what they don't see, mm-mm
I'm dancin' on my own (dancin' on my own)
I make the moves up as I go (moves up as I go)
And that's what they don't know, mm-mm
That's what they don't know, mm-mm
But I keep cruisin'
Can't stop, won't stop groovin'
It's like I got this music in my mind
Sayin' it's gonna be alright
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
Heartbreakers gonna break, break, break, break, break
And the fakers gonna fake, fake, fake, fake, fake
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
Shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off (hoo-hoo-hoo)
Hey, hey, hey
Just think, while you've been gettin' down and out about the liars
And the dirty, dirty cheats of the world
You could've been gettin' down to this sick beat
My ex-man brought his new girlfriend
She's like, "Oh my God!" but I'm just gonna shake
And to the fella over there with the hella good hair
Won't you come on over, baby? We can shake, shake, shake (yeah)
Yeah, oh, oh
'Cause the players gonna play, play, play, play, play
And the haters gonna hate, hate, hate, hate, hate (haters gonna hate)
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
Heartbreakers gonna break, break, break, break, break (mmm)
And the fakers gonna fake, fake, fake, fake, fake (and fake and fake and fake)
Baby, I'm just gonna shake, shake, shake, shake, shake
I shake it off, I shake it off (hoo-hoo-hoo)
Shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
I, I, I shake it off (yeah), I shake it off (hoo-hoo-hoo)
Shake it off, I shake it off
I, I, I shake it off, I shake it off (you got to)
I, I, I shake it off, I shake it off
I, I, I shake it off, I shake it off
Style
Midnight
You come and pick me up, no headlights
Long drive
Could end in burning flames or paradise
Fade into view, oh
It's been a while since I have even heard from you (heard from you)
And I should just tell you to leave 'cause I
Know exactly where it leads, but I
Watch us go 'round and 'round each time
You got that James Dean daydream look in your eye
And I got that red lip classic thing that you like
And when we go crashing down, we come back every time
'Cause we never go out of style, we never go out of style
You got that long hair, slicked back, white T-shirt
And I got that good girl faith and a tight little skirt
And when we go crashing down, we come back every time
'Cause we never go out of style, we never go out of style
So it goes
He can't keep his wild eyes on the road, mm
Takes me home
The lights are off, he's taking off his coat, mm, yeah
I say, "I heard, oh
That you've been out and about with some other girl, some other girl"
He says, "What you heard is true, but I
Can't stop thinkin' 'bout you and I"
I said, "I've been there too a few times"
'Cause you got that James Dean daydream look in your eye
And I got that red lip classic thing that you like
And when we go crashing down, we come back every time
'Cause we never go out of style, we never go out of style
You got that long hair, slicked back, white T-shirt
And I got that good girl faith and a tight little skirt (a tight little skirt)
And when we go crashing down, we come back every time
'Cause we never go out of style (we never go), we never go out of style
Take me home
Just take me home
Yeah, just take me home
Oh, whoa, oh
(Out of style)
Oh, you got that James Dean daydream look in your eye
And I got that red lip classic thing that you like
And when we go crashing down (now we go), we come back every time
'Cause we never go out of style, we never go out of style

'''
# Process the lyrics text
doc = nlp(n89_lyrics)

# Filter out stopwords and punctuation
keywords = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]

# Calculate word frequency
word_freq = Counter(keywords)

# Display the most common keywords
print("Most common keywords:")
for word, freq in word_freq.most_common(20):
    print(f"{word}: {freq}")


# Create a circular mask using PIL and NumPy
circle_mask = np.array(Image.new('L', (800, 800), 0))
y, x = np.ogrid[:800, :800]
mask = (x - 400) ** 2 + (y - 400) ** 2 > 400 ** 2
circle_mask[mask] = 255

# Generate word cloud from frequencies
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='magma', mask=circle_mask).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

