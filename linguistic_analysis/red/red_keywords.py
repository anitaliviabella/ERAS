import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.

folklore_lyrics = '''
State of Grace
I'm walking fast through the traffic lights
Busy streets and busy lives
And all we know is touch and go
We are alone with our changing minds
We fall in love 'til it hurts or bleeds, or fades in time
And I never (never)
Saw you coming
And I'll never (never)
Be the same
You come around and the armor falls
Pierce the room like a cannonball
Now all we know is don't let go
We are alone, just you and me
Up in your room and our slates are clean
Just twin fire signs, four blue eyes
So you were never a saint
And I've loved in shades of wrong
We learn to live with the pain
Mosaic broken hearts
But this love is brave and wild
And I never (never)
Saw you coming
And I'll never (never)
Be the same
This is a state of grace
This is the worthwhile fight
Love is a ruthless game
Unless you play it good and right
These are the hands of fate
You're my Achilles heel
This is the golden age of something good and right and real
And I never (never)
Saw you coming
And I'll never
Be the same
And I never (never)
Saw you coming
And I'll never (so you were never a saint)
(And I've loved in shades of wrong)
Be the same (we learn to live with the pain)
(Mosaic broken hearts)
(But this love is brave and wild)
This is a state of grace
This is the worthwhile fight
Love is a ruthless game
Unless you play it good and right
Red
Loving him is like driving a new Maserati down a dead end street
Faster than the wind, passionate as sin, ending so suddenly
Loving him is like trying to change your mind
Once you're already flying through the free fall
Like the colors in autumn, so bright, just before they lose it all
Losing him was blue, like I'd never known
Missing him was dark gray, all alone
Forgetting him was like trying to know
Somebody you never met
But loving him was red
Loving him was red
Touching him was like realizing all you ever wanted
Was right there in front of you
Memorizing him was as easy as knowing all the words
To your old favorite song
Fighting with him was like trying to solve a crossword
And realizing there's no right answer
Regretting him was like wishing you never found out
That love could be that strong
Losing him was blue, like I'd never known
Missing him was dark gray, all alone
Forgetting him was like trying to know
Somebody you never met
But loving him was red
Oh, red
Burning red
Remembering him comes in flashbacks and echoes
Tell myself it's time now gotta let go
But moving on from him is impossible
When I still see it all in my head
In burning red
Burning, it was red
Oh, losing him was blue, like I'd never known
Missing him was dark gray, all alone
Forgetting him was like trying to know
Somebody you never met
'Cause loving him was red
Yeah, yeah, red
Burning red
And that's why he's spinning 'round in my head
Comes back to me, burning red
Yeah, yeah
His love was like driving a new Maserati down a dead end street
Treacherous
Put your lips close to mine
As long as they don't touch
Out of focus, eye to eye
'Til the gravity's too much
And I'll do anything you say
If you say it with your hands
And I'd be smart to walk away
But you're quicksand
This slope is treacherous
This path is reckless
This slope is treacherous
And I, I, I like it
I can't decide if it's a choice
Getting swept away
I hear the sound of my own voice
Asking you to stay
And all we are is skin and bone
Trained to get along
Forever going with the flow
But you're friction
This slope is treacherous
This path is reckless
This slope is treacherous
I, I, I like it
Two headlights shine through the sleepless night
And I will get you, and get you alone
Your name has echoed through my mind
And I just think you should, think you should know
That nothing safe is worth the drive
And I would follow you, follow you home
I'll follow you, follow you home
This hope is treacherous
This daydream is dangerous
This hope is treacherous
I, I, I
I, I, I
I, I, I
Two headlights shine through the sleepless night
And I will get you, and get you alone
Your name has echoed through my mind
And I just think you should, think you should know
That nothing safe is worth the drive
And I will follow you, follow you home
I'll follow you, follow you home
I'll follow you, follow you home
I'll follow you, follow you home
This slope is treacherous
I, I, I like it
I know you were trouble
Once upon a time
A few mistakes ago
I was in your sights
You got me alone
You found me
You found me
You found me
I guess you didn't care
And I guess I liked that
And when I fell hard
You took a step back
Without me
Without me
Without me
And he's long gone
When he's next to me
And I realize
The blame is on me
'Cause I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been
'Til you put me down, oh
I knew you were trouble when you walked in
So, shame on me now
Flew me to places I'd never been
Now I'm lyin' on the cold hard ground
Oh, oh
Trouble, trouble, trouble
Oh, oh
Trouble, trouble, trouble
No apologies
He'll never see you cry
Pretends he doesn't know
That he's the reason why
You're drowning
You're drowning
You're drowning
And I heard you moved on
From whispers on the street
A new notch in your belt
Is all I'll ever be
And now I see
Now I see
Now I see
He was long gone
When he met me
And I realize
The joke is on me, hey
I knew you were trouble when you walked in (oh)
So shame on me now
Flew me to places I'd never been
'Til you put me down, oh
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been, yeah
Now I'm lyin' on the cold hard ground
Oh, oh (yeah)
Trouble, trouble, trouble
Oh, oh
Trouble, trouble, trouble
And the saddest fear
Comes creepin' in
That you never loved me
Or her
Or anyone
Or anything
Yeah
I knew you were trouble when you walked in
So shame on me now
Flew me to places I'd never been (never been)
'Til you put me down, oh
I knew you were trouble when you walked in (knew it right there)
So shame on me now (knew it right there)
Flew me to places I'd never been
(Ooh) now I'm lyin' on the cold hard ground
Oh, oh
Trouble, trouble, trouble (oh)
Oh, oh
Trouble, trouble, trouble
I knew you were trouble when you walked in
Trouble, trouble, trouble
I knew you were trouble when you walked in
Trouble, trouble, trouble
22
It feels like a perfect night to dress up like hipsters
And make fun of our exes, uh uh uh uh
It feels like a perfect night for breakfast at midnight
To fall in love with strangers uh uh uh uh
Yeaaaah
We're happy free confused and lonely at the same time
It's miserable and magical oh yeah
Tonight's the night when we forget about the deadlines, it's time uh uh

I don't know about you but im feeling 22 Everything will be alright if you keep me next to you
You don't know about me but I bet you want to
Everything will be alright if we just keep dancing like we're 22, 22

It seems like one of those nights
This place is too crowded too many cool kids
It seems like one of those nights
We ditch the whole scene and end up dreaming instead of sleeping
Yeaaaah
We're happy free confused and lone in the best way
It's miserable and magical oh yeah
Tonight's the night when we forget about the heartbreaks, it's time uh uh

I don't know about you but im feeling 22
Everything will be alright if you keep me next to you
You don't know about me but I bet you want to
Everything will be alright if we just keep dancing like we're 22, 22

I don't know about you, 22, 22
It feels like one of those nights
We ditch the whole scene
It feels like one of those nights
We won't be sleeping
It feels like one of those nights
You look like bad news I gotta have you, I gotta have you

I don't know about you but im feeling 22
Everything will be alright if you keep me next to you
You don't know about me but I bet you want to
Everything will be alright if we just keep dancing like we're 22, 22

Dancing like 22, yeah, 22, yeah yeah

It feels like one of those nights
We ditch the whole scene
It feels like one of those nights
We won't be sleeping
It feels like one of those nights
You look like bad news I gotta have you, I gotta have you
I almost do
I bet
This time of night you're still up
I bet
You're tired from a long hard week
I bet
You're sittin' in your chair by the window
Looking out at the city
And I bet
Sometimes you wonder 'bout me
And I just wanna tell you
It takes everything in me not to call you
And I wish I could run to you
And I hope you know that every time I don't
I almost do
I almost do
I bet
You think I either moved on or hate you
'Cause each time you reach out there's no reply
I bet
It never ever occurred to you
That I can't say "Hello" to you
And risk another goodbye
And I just wanna tell you
It takes everything in me not to call you
And I wish I could run to you
And I hope you know that every time I don't
I almost do
I almost do
Oh, we made quite a mess, babe
It's probably better off this way
And I confess, babe
In my dreams you're touching my face
And asking me if I wanna try again with you
And I almost do
And I just wanna tell you
It takes everything in me, not to call you
And I wish I could run to you
And I hope you know that every time I don't
I almost do
I almost do
Uh-uh-uh
I bet
This time of night you're still up
I bet
You're tired from a long hard week
I bet
You're sittin' in your chair by the window
Looking out at the city
And I hope
Sometimes you wonder 'bout me
We are never ever getting back together
I remember when we broke up the first time
Saying, "This is it, I've had enough"
'Cause like, we hadn't seen each other in a month
When you said you needed space
What?
Then you come around again and say
"Baby, I miss you, and I swear I'm gonna change, trust me"
Remember how that lasted for a day?
I say, "I hate you", we break up, you call me, "I love you"
Ooh, ooh-ooh-ooh-ooh
We called it off again last night but
Ooh, ooh-ooh-ooh-ooh
This time, I'm telling you, I'm telling you
We are never, ever, ever getting back together
We are never, ever, ever getting back together
You go talk to your friends, talk to my friends, talk to me
But we are never, ever, ever, ever getting back together
Like, ever
I'm really gonna miss you picking fights
And me falling for it, screaming that I'm right
And you would hide away and find your peace of mind
With some indie record that's much cooler than mine
Ooh, ooh-ooh-ooh-ooh
You called me up again tonight but
Ooh, ooh-ooh-ooh-ooh
This time, I'm telling you, I'm telling you
We (we) are never, ever, ever getting back together
We are never, ever, ever getting back together
You go talk to your friends, talk to my friends, talk to me (talk to me)
But we are never, ever, ever, ever getting back together
Ooh, ooh-ooh-ooh-ooh (yeah!)
Ooh, ooh-ooh-ooh-ooh-ooh (yeah!)
Ooh, ooh-ooh-ooh-ooh (yeah!)
Oh-oh-oh!
I used to think that we were forever, ever
And I used to say, never say never
Pfft, so he calls me up, and he's like, "I still love you"
And I'm like, I'm just, I mean, this is exhausting
You know, like we are never getting back together
Like, ever (no!)
We are never, ever, ever getting back together
We are never, ever, ever getting back together
You go talk to your friends, talk to my friends, talk to me
But we are never, ever, ever, ever getting back together
We (ooh, ooh-ooh-ooh-ooh, ooh, ooh-ooh-ooh-ooh-ooh)
Getting back together
We (ooh, ooh-ooh-ooh-ooh), oh
Getting back together
You go talk to your friends, talk to my friends, talk to me (talk to me)
But we are never, ever, ever, ever getting back together
I'm pretty sure we almost broke up last night
I threw my phone across the room at you
I was expecting some dramatic turn away
But you stayed
This morning I said we should talk about it
'Cause I read you should never leave a fight unresolved
That's when you came in wearing a football helmet
And said, "Okay, let's talk"
And I said
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay
Before you, I'd only dated self indulgent takers
Who took all of their problem out on me
But you carry my groceries and now I'm always laughing
And I love you, because you have given me no choice but to
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay
Stay, stay, stay
You took the time to memorize me
My fears, my hopes and dreams
I just like hanging out with you
All the time
All those times that you didn't leave
It's been occurring to me
I'd like to hang out with you
For my whole life
Stay
And I'll be loving you for quite some time
No one else is gonna love me when I get mad, mad, mad
So I think that it's best if we both stay, stay, stay
Stay, stay, stay
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
But I think that it's best if we both stay
Stay, stay, stay, stay, stay
Stay, stay, stay
I've been loving you for quite some time, time, time
You think that it's funny when I'm mad, mad, mad
I think that it's best if we both stay
"That's so fun"
The last time
Find myself at your door
Just like all those times before
I'm not sure how I got there
All roads, they lead me here
I imagine you are home
In your room, all alone
And you open your eyes into mine
And everything feels better
And right before your eyes
I'm breaking
No past, no reasons why
Just you and me
This is the last time I'm asking you this
Put my name at the top of your list
This is the last time I'm asking you why
You break my heart in the blink of an eye, eye, eye
You find yourself at my door
Just like all those times before
You wear your best apology
But I was there to watch you leave
And all the times I let you in
Just for you to go again
Disappear when you come back
Everything is better
And right before your eyes
I'm aching
Run fast, nowhere to hide
Just you and me
This is the last time I'm asking you this
Put my name at the top of your list
This is the last time I'm asking you why
You break my heart in the blink of an eye, eye, eye
This is the last time you tell me I've got it wrong
This is the last time I say it's been you all along
This is the last time I let you in my door
This is the last time, I won't hurt you anymore
Oh-oh oh-oh oh-oh oh-oh
Oh-oh oh-oh oh-oh oh-oh
This is the last time I'm asking you this
Put my name at the top of your list
This is the last time I'm asking you why
You break my heart in the blink of an eye
This is the last time I'm asking you this
(This is the last time I'm asking you this)
Put my name at the top of your list
(Put my name at the top of your list)
This is the last time I'm asking you why
(This is the last time I'm asking you why)
You break my heart in the blink of an eye
(You break my heart)
This is the last time I'm asking you
Last time I'm asking you
Last time I'm asking you this
This is the last time I'm asking you
Last time I'm asking you
Last time I'm asking you this
This is the last time I'm asking you
Last time I'm asking you
Last time I'm asking you this
This is the last time I'm asking you
Last time I'm asking you
Last time I'm asking you this
Holy Ground
I was reminiscing just the other day
While having coffee all alone, and Lord, it took me away
Back to a first glance feeling on New York time
Back when you fit my poems like a perfect rhyme
Took off faster than a green light, go
Yeah, you skip the conversation when you already know
I left a note on the door with a joke we'd made
And that was the first day
And darling, it was good
Never looking down
And right there where we stood
Was holy ground
Spinning like a girl in a brand-new dress
We had this big wide city all to ourselves
We blocked the noise with the sound of "I need you"
And for the first time I had something to lose
And I guess we fell apart in the usual way
And the story's got dust on every page
But sometimes I wonder how you think about it now
And I see your face in every crowd
'Cause darling, it was good
Never looking down
And right there where we stood
Was holy ground
Tonight, I'm gonna dance
For all that we've been through
But I don't wanna dance
If I'm not dancing with you
Tonight, I'm gonna dance
Like you were in this room
But I don't wanna dance
If I'm not dancing with you
It was good
Never looking down
And right there where we stood
Was holy ground
Tonight I'm gonna dance
For all that we've been through
But I don't wanna dance
If I'm not dancing with you
Tonight, I'm gonna dance
Like you were in this room
But I don't wanna dance
If I'm not dancing with you
Sad beautiful tragic
Long handwritten note
Deep in your pocket
Words, how little they mean
When you're a little too late
I stood right by the tracks
Your face in a locket
Good girls, hopeful they'll be and long they will wait
We had a beautiful magic love there
What a sad beautiful tragic love affair
In dreams
I meet you in warm conversation
We both wake
In lonely beds
In different cities
And time
Is taking its sweet time erasing you
And you've got your demons
And darlin' they all look like me
'Cause we had a beautiful magic love there
What a sad beautiful tragic love affair
Distance, timing
Breakdown, fighting
Silence, the train runs off its tracks
Kiss me, try to fix it
Could you just try to listen?
Hang up, give up
For the life of us we can't get back
A beautiful magic love there
What a sad
Beautiful tragic
Beautiful tragic
Beautiful
What we had a beautiful magic love there (uh-uh)
What a sad beautiful tragic love affair
We had a beautiful magic love there
What a sad beautiful tragic love affair
The lucky one
New to town with a made-up name
In the angel's city, chasing fortune and fame
And the camera flashes make it look like a dream
You had it figured out since you were in school
Everybody loves pretty, everybody loves cool
So overnight, you look like a '60s queen
Another name goes up in lights
Like diamonds in the sky
And they'll tell you now, you're the lucky one
Yeah, they'll tell you now, you're the lucky one
But can you tell me now you're the lucky one?
Oh, oh, oh
Now it's big black cars and Riviera views
And your lover in the foyer doesn't even know you
And your secrets end up splashed on the news front page
And they tell you that you're lucky, but you're so confused
'Cause you don't feel pretty, you just feel used
And all the young things line up to take your place
Another name goes up in lights
You wonder if you'll make it out alive
And they'll tell you now, you're the lucky one
Yeah, they'll tell you now, you're the lucky one
Can you tell me now you're the lucky one?
Oh, oh, oh, oh-oh-oh-oh-oh, oh
Oh-oh-oh-oh-oh-oh-oh-oh-oh
It was a few years later, I showed up here
And they still tell the legend of how you disappeared
How you took the money and your dignity and got the hell out
They say you bought a bunch of land somewhere
Chose the Rose Garden over Madison Square
And it took some time, but I understand it now
'Cause now my name is up in lights
But I think you got it right
Let me tell you now, you're the lucky one
Let me tell you now, you're the lucky one
Let me tell you now, you're the lucky one
Oh, oh, oh
Yeah, they'll tell you now, you're the lucky one
Yeah, they'll tell you now, you're the lucky one
Let me tell you now, you're the lucky one
Oh, oh, oh
Oh, oh-oh, oh-oh
You good to go?
All I knew
This morning when I woke
Is I know something now
Know something now I didn't before
And all I've seen
Since eighteen hours ago
Is green eyes and freckles and your smile
In the back of my mind making me feel like
I just wanna know you better, know you better, know you better now
I just wanna know you better, know you better, know you better now
I just wanna know you better, know you better, know you better now
I just wanna know you, know you, know you
'Cause all I know is we said, "Hello"
And your eyes look like comin' home
All I know is a simple name
And everything has changed
All I know is you held the door
You'll be mine and I'll be yours
All I know since yesterday
Is everything has changed
And all my walls
Stood tall painted blue
But I'll take 'em down, take 'em down
And open up the door for you
And all I feel
In my stomach is butterflies
The beautiful kind, makin' up for lost time
Takin' flight, makin' me feel like
I just wanna know you better, know you better, know you better now
I just wanna know you better, know you better, know you better now
I just wanna know you better, know you better, know you better now
I just wanna know you, know you, know you
'Cause all I know is we said, "Hello"
And your eyes look like comin' home
All I know is a simple name
Everything has changed
All I know is you held the door
And you'll be mine and I'll be yours
All I know since yesterday
Is everything has changed
Come back and tell me why
I'm feelin' like I've missed you all this time
And meet me there tonight
And let me know that it's not all in my mind
I just wanna know you better, know you better, know you better now
I just wanna know you, know you, know you
All I know is we said, "Hello"
Your eyes look like comin' home
All I know is a simple name
And everything has changed
All I know is you held the door
You'll be mine and I'll be yours
All I know since yesterday
Is everything has changed
All I know is we said, "Hello"
So dust off your highest hopes
All I know is pouring rain
And everything has changed
All I know is a new found grace
All my days, I'll know your face
All I know since yesterday
Is everything has changed
Starlight
I said, "Oh my, what a marvelous tune"
It was the best night, never would forget how we moved
The whole place
Was dressed to the nines
And we were dancing, dancing
Like we're made of starlight
Like we're made of starlight
I met Bobby on the boardwalk summer of '45
Picked me up late one night out the window
We were seventeen and crazy running wild, wild
Can't remember what song he was playing when we walked in
The night we snuck into a yacht club party
Pretending to be a duchess and a prince
And I said, "Oh my, what a marvelous tune"
It was the best night, never would forget how we moved
The whole place
Was dressed to the nines
And we were dancing, dancing
Like we're made of starlight, starlight
Like we're made of starlight, starlight
He said, "Look at you, worrying so much about things you can't change
You'll spend your whole life singing the blues
If you keep thinking that way"
He was tryna to skip rocks on the ocean saying to me
"Don't you see the starlight, starlight
Don't you dream impossible things"
Like, "Oh my, what a marvelous tune"
It was the best night, never would forget how we moved
The whole place
Was dressed to the nines
And we were dancing, dancing
Like we're made of starlight, starlight
Like we're made of starlight, starlight
Ooh, ooh he's talking crazy
Ooh, ooh dancing with me
Ooh, ooh we could get married
Have ten kids and teach 'em how to dream
"Oh, my what a marvelous tune"
It was the best night, never would forget how we moved
The whole place
Was dressed to the nines
And we were dancing, dancing
Like we're made of starlight, starlight
Like we're made of starlight, starlight
Like we're made of starlight, starlight
Like we dream impossible dreams
Like starlight, starlight
Like we dream impossible dreams
Don't you see the starlight, starlight
Don't you dream impossible things
Begin again
Took a deep breath in the mirror
He didn't like it when I wore high heels
But I do
Turn the lock and put my headphones on
He always said he didn't get this song
But I do, I do
Walked in expecting you'd be late
But you got here early and you stand and wave
I walk to you
You pull my chair out and help me in
And you don't know how nice that is
But I do
And you throw your head back laughing
Like a little kid
I think it's strange that you think I'm funny, 'cause
He never did
I've been spending the last eight months
Thinking all love ever does
Is break and burn, and end
But on a Wednesday in a cafe
I watched it begin again
You said you never met one girl who had
As many James Taylor records as you
But I do
We tell stories and you don't know why
I'm coming off a little shy
But I do
But you throw your head back laughing
Like a little kid
I think it's strange that you think I'm funny, 'cause
He never did
I've been spending the last eight months
Thinking all love ever does
Is break and burn, and end
But on a Wednesday in a cafe
I watched it begin again
And we walked down the block, to my car
And I almost brought him up
But you start to talk about the movies
That your family watches every single Christmas
And I want to talk about that
And for the first time
What's past is past
'Cause you throw your head back laughing
Like a little kid
I think it's strange that you think I'm funny, 'cause
He never did
I've been spending the last eight months
Thinking all love ever does
Is break and burn, and end
But on a Wednesday in a cafe
I watched it begin again
But on a Wednesday in a cafe
I watched it begin again
The moment I knew
You should've been there
Should've burst through the door
With that "Baby, I'm right here" smile
And it would've felt like
A million little shining stars had just aligned
And I would've been so happy
Christmas lights glisten
I've got my eye on the door
Just waiting for you to walk in
But the time is ticking
People ask me how I've been
As I comb back through my memory
How you said you'd be here
You said you'd be here
And it was like slow motion
Standing there in my party dress
In red lipstick
With no one to impress
And they're all laughing
As I'm looking around the room
But there was one thing missing
And that was the moment I knew
And the hours pass by
Now I just wanna be alone
But your close friends always seem to know
When there's something really wrong
So they follow me down the hall
And there in the bathroom
I try not to fall apart
And the sinking feeling starts
As I say hopelessly
"He said he'd be here"
And it was like slow motion
Standing there in my party dress
In red lipstick
With no one to impress
And they're all laughing
And asking me about you
But there was one thing missing (missing, missing)
And that was the moment I knew
What do you say, when tears are streaming down your face
In front of everyone you know?
And what do you do when the one who means the most to you
Is the one who didn't show?
You should've been here
And I would've been so happy
And it was like slow motion
Standing there in my party dress
In red lipstick
With no one to impress
And they're all standing around me singing
"Happy birthday to you"
But there was one thing missing
And that was the moment I knew
Ooh, I knew
Ooh
You called me later
And said, "I'm sorry, I didn't make it"
And I said, "I'm sorry too"
And that was the moment I knew
Come back...be here
You said it in a simple way
4:00 a.m. the second day
How strange that I don't know you at all
Stumbled through the long goodbye
One last kiss, then catch your flight
Right when I was just about to fall
I told myself, don't get attached
But in my mind, I play it back
Spinning faster than the plane that took you
And this is when the feeling sinks in
I don't wanna miss you like this
Come back, be here
Come back, be here
I guess you're in New York today
I don't wanna need you this way
Come back, be here
Come back, be here
The delicate beginning rush
The feeling you can know so much
Without knowing anything at all
And now that I can put this down
If I had known what I'd known now
I never would've played so nonchalant
Taxi cabs and busy streets
That never bring you back to me
I can't help but wish you took me with you
And this is when the feeling sinks in
I don't wanna miss you like this
Come back, be here
Come back, be here
I guess you're in London today
And I don't wanna need you this way
Come back, be here
Come back, be here
This is falling in love in the cruelest way
This is falling for you and you are worlds away
In New York, be here
But you're in London, and I break down
'Cause it's not fair that you're not around
This is when the feeling sinks in
I don't wanna miss you like this
Come back, be here
Come back, be here
I guess you're in New York today
And I don't wanna need you this way
Come back, be here
Come back, be here
Oh-oh, oh-oh
I don't wanna miss you like this
Oh-oh, oh-oh
Come back, be here
Come back, be here
Girl at home
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that, ah-ah
Don't look at me, you got a girl at home
And everybody knows that
I don't even know her
But I feel a responsibility to do what's upstanding and right
It's kinda like a code, yeah
And you've been getting closer and closer, and crossing so many lines
And it would be a fine proposition
If I was a stupid girl
But honey, I am no-one's exception
This I have previously learned
So don't look at me, you got a girl at home
And everybody knows that, everybody knows that, ah-ah
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I see you turn off your phone
And now you got me alone, and I say
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I just wanna make sure
You understand perfectly, you're the kind of man who makes me sad
While she waits up
You chase down the newest thing and take for granted what you have
And it would be a fine proposition
If I was a stupid girl
And yeah, I might go with it
If I hadn't once been just like her
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that, ah-ah
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
I see you turn off your phone
And now you got me alone, and I say
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Call a cab, lose my number, you're about to lose your girl
Call a cab, lose my number, let's consider this lesson learned
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that, ah-ah
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Want to see you pick up your phone
And tell her you're coming home
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
Don't look at me, you got a girl at home
And everybody knows that, everybody knows that
It would be a fine proposition
If I hadn't once been just like her
I'm walking fast through the traffic lights
Busy streets and busy lives
And all we know is touch and go
We are alone with our changing minds
We fall in love 'til it hurts or bleeds, or fades in time
And I never (never)
Saw you coming
And I'll never (never)
Be the same
You come around and the armor falls
Pierce the room like a cannonball
Now all we know is don't let go
We are alone, just you and me
Up in your room and our slates are clean
Just twin fire signs, four blue eyes
So you were never a saint
And I've loved in shades of wrong
We learn to live with the pain
Mosaic broken hearts
But this love is brave and wild
And I never (never)
Saw you coming
And I'll never (never)
Be the same
This is a state of grace
This is the worthwhile fight
Love is a ruthless game
Unless you play it good and right
These are the hands of fate
You're my Achilles heel
This is the golden age of something good and right and real
And I never (never)
Saw you coming
And I'll never
Be the same
And I never (never)
Saw you coming
And I'll never (so you were never a saint)
(And I've loved in shades of wrong)
Be the same (we learn to live with the pain)
(Mosaic broken hearts)
(But this love is brave and wild)
This is a state of grace
This is the worthwhile fight
Love is a ruthless game
Unless you play it good and right
Ronan
I remember your bare feet down the hallway
I remember your little laugh
Race cars on the kitchen floor, plastic dinosaurs
I love you to the moon and back
I remember your blue eyes looking into mine
Like we had our own secret club
I remember you dancing before bedtime
Then jumping on me, waking me up
I can still feel you hold my hand, little man
And even the moment I knew
You fought it hard like an army guy
Remember I leaned in and whispered to you?
Come on, baby, with me
We're gonna fly away from here
You were my best four years
I remember the drive home when the blind hope
Turned to crying and screaming, "Why?"
Flowers pile up in the worst way, no one knows what to say
About a beautiful boy who died
And it's about to be Halloween, you could be anything
You wanted if you were still here
I remember the last day when I kissed your face
And whispered in your ear
Come on, baby, with me
We're gonna fly away from here
Out of this curtained room
In this hospital grey, we'll just disappear
Come on, baby, with me
We're gonna fly away from here
You were my best four years
What if I'm standing in your closet
Trying to talk to you?
And what if I kept the hand-me-downs
You won't grow into?
And what if I really thought some miracle
Would see us through?
What if the miracle was even getting
One moment with you?
Come on, baby, with me
We're gonna fly away from here
Come on, baby, with me
We're gonna fly away from here
You were my best four years
I remember your bare feet down the hallway
I love you to the moon and back
Better man
I know I'm probably better off on my own
Than lovin' a man who didn't know
What he had when he had it
And I see the permanent damage you did to me
Never again, I just wish I could forget when it was magic
I wish it wasn't 4 a.m., standing in the mirror
Saying to myself, you know you had to do it
I know the bravest thing I ever did was run
Sometimes, in the middle of the night, I can feel you again
But I just miss you, and I just wish you were a better man
But I know why we had to say goodbye like the back of my hand
But I just miss you, and I just wish you were a better man
A better man
I know I'm probably better off all alone
Than needing a man who could change his mind at any given minute
And it was always on your terms
I waited on every careless word
Hoping they might turn sweet again
Like it was in the beginning
But your jealousy, oh, I can hear it now
Talking down to me like I'll always be around
Push my love away like it was some kind of loaded gun
Oh, you never thought I'd run
Sometimes, in the middle of the night, I can feel you again
But I just miss you, and I just wish you were a better man
But I know why we had to say goodbye like the back of my hand
But I just miss you, and I just wish you were a better man
A better man
I hold onto this pride because, these days, it's all I have
And I gave to you my best, and we both know you can't say that
I wish you were a better man
I wonder what we would've become
If you were a better man
We might still be in love
If you were a better man
You would've been the one
If you were a better man
Yeah, yeah
Sometimes, in the middle of the night, I can feel you again
But I just miss you, and I just wish you were a better man
But I know why we had to say goodbye like the back of my hand
But I just miss you, and I just wish you were a better man
A better man
We might still be in love, if you were a better man
(But I just miss you, and I just wish you were a better man) yeah, yeah
I know why we had to say goodbye like the back of my hand
But I just miss you and I just wish you were a better man
A better man
We might still be in love, if you were a better man
You would've been the one
If you were a better man
Nothing new
They tell you while you're young
"Girls, go out and have your fun"
Then they hunt and slay the ones who actually do it
Criticize the way you fly
When you're soaring through the sky
Shoot you down and then they sigh
And say, "She looks like she's been through it"
Lord, what will become of me
Once I've lost my novelty?
I've had too much to drink tonight
And I know it's sad, but this is what I think about
And I wake up in the middle of the night
It's like I can feel time moving
How can a person know everythin' at 18
But nothin' at 22?
And will you still want me
When I'm nothing new?
How long will it be cute, all this cryin' in my room?
When you can't blame it on my youth
And roll your eyes with affection
And my cheeks are growing tired
From turning red and faking smiles
Are we only biding time 'til I lose your attention?
And someone else lights up the room (ah)
People love an ingénue (ah)
I've had (I've had) too much to drink tonight
How did I go from growin' up to breaking down?
And I wake up (wake up) in the middle of the night
It's like I can feel time movin'
How can a person know everything at 18
But nothing at 22?
And will you still want me
When I'm nothing new?
I know someday I'm gonna meet her, it's a fever dream
The kind of radiance you only have at 17
She'll know the way, and then she'll say she got the map from me
I'll say I'm happy for her, then I'll cry myself to sleep
Oh, whoa, oh (oh)
Oh, whoa, oh, whoa, oh (oh)
I've had (I've had) too much to drink tonight
But I wonder if they'll miss me once they drive me out
I wake up (wake up) in the middle of the night
And I can feel time moving
How can a person know everything at 18
But nothing at 22?
And will you still want me
Will you still want me
Will you still want me
When I'm nothing new
What about your promises, promises?
What about your promises, promises, promises? No
What a shame
Didn't want to be the one that got away, yeah
Big mistake, you broke the sweetest promise
That you never should have made
I'm here on the kitchen floor
You call, but I won't hear it
You said no one else, how could you do this, babe?
You really blew this, babe
We ain't getting through this one, babe (yeah, yeah, yeah)
This is the last time I'll ever call you, babe
(This is the last time, this is the last time)
This is the last time I'll ever call you, babe
(What about your promises, promises, promises? No)
What a waste
Taking down the pictures and the plans we made, yeah
And it's strange how your face doesn't look so innocent
Your secret has its consequence and that's on you, babe
I break down every time you call
We're a wreck, you're the wrecking ball
We said no one else, how could you do this, babe?
You really blew this, babe
We ain't getting through this one, babe (yea, yea, yea)
This is the last time I'll ever call you, babe
(This is the last time, this is the last time)
This is the last time I'll ever call you
Since you admitted it (oh-oh), I keep picturing (oh-oh)
Her lips on your neck (oh-oh), I can't unsee it (oh-oh)
I hate that because of you, I can't love you, babe
What a shame
Didn't want to be the one that got away
How could you do this, babe? (Eh, eh, eh, eh, eh)
You really blew this, babe (babe, eh, yeah, eh)
We ain't getting through this one, babe (yeah, yeah, yeah)
This is the last time I'll ever call you, babe
(This is the last time, this is the last time)
This is the last time I'll ever call you
I'm here on the kitchen floor
You call, but I won't hear it
You said no one else
We ain't getting through this one, babe
I break down every time you call
We're a wreck, you're the wrecking ball
You said no one else
This is the last time I'll never call you, babe (yeah, yeah, yeah)
Message in a bottle
I know that you like me
And it's kinda frightenin'
Standing here waitin', waitin'
And I became hypnotized
By freckles and bright eyes
Tongue tied
But now
You're so far away and I'm down
Feelin' like a face in the crowd
I'm reachin' for you, terrified
'Cause you could be the one that I love
I could be the one that you dream of
Message in a bottle is all I can do
Standin' here, hopin' it gets to you
You could be the one that I keep, and I
Could be the reason you can't sleep at night
Message in a bottle is all I can do
Standin' here, hopin' it gets to you
These days I'm restless
Work days are endless
Look how you've made me, made me
But time moves faster
Replaying your laughter
Disaster
'Cause now
You're so far away and I'm down
Feelin' like a face in the crowd
I'm reachin' for you, terrified
'Cause you could be the one that I love
I could be the one that you dream of
Message in a bottle is all I can do
Standin' here, hopin' it gets to you (it gets to you)
You could be the one that I keep, and I (I)
Could be the reason you can't sleep at night
Message in a bottle is all I can do
Standin' here, hopin' it gets to you
How is it in London? (London)
Where are you while I'm wonderin' (wonderin')
If I'll ever see you again?
You could be the one that I love, mm-mm
And now I'm standin' here, hopin' it gets to you
'Cause you could be the one that I love
I could be the one that you dream of
Message in a bottle is all I can do
Standin' here, hopin' it gets to you (it gets to you)
You could be the one that I keep, and I
Could be the reason you can't sleep at night (you can't sleep at night)
Message in a bottle is all I can do (yeah, yeah)
Standin' here, hopin' it gets to you (yeah, yeah)
You could be the one that I love
(Love)
You could be the one that I love
(Love) my love
And now I'm standin' here, hopin' this gets to you
I bet you think about me
3 AM and I'm still awake, I'll bet you're just fine
Fast asleep in your city that's better than mine
And the girl in your bed has a fine pedigree
And I'll bet your friends tell you she's better than me, huh
Well, I tried to fit in with your upper-crust circles
Yeah, they let me sit in back when we were in love
Oh, they sit around talkin' 'bout the meaning of life
And the book that just saved 'em that I hadn't heard of
But now that we're done and it's over
I bet you couldn't believe
When you realized I'm harder to forget than I was to leave
And I bet you think about me
You grew up in a silver-spoon gated community
Glamorous, shiny, bright Beverly Hills
I was raised on a farm, no, it wasn't a mansion
Just livin' room dancin' and kitchen table bills
But you know what they say, you can't help who you fall for
And you and I fell like an early spring snow
But reality crept in, you said we're too different
You laughed at my dreams, rolled your eyes at my jokes
Mr. Superior Thinkin'
Do you have all the space that you need?
I don't have to be your shrink to know that you'll never be happy
And I bet you think about me
I bet you think about me, yes
I bet you think about me
Oh, block it all out
The voices so loud, sayin'
"Why did you let her go?"
Does it make you feel sad
That the love that you're lookin' for
Is the love that you had
Now you're out in the world, searchin' for your soul
Scared not to be hip, scared to get old
Chasin' make-believe status, last time you felt free
Was when none of that shit mattered 'cause you were with me
But now that we're done and it's over
I bet it's hard to believe
But it turned out I'm harder to forget than I was to leave
And, yeah, I bet you think about me
I bet you think about me, yes
I bet you think about me
I bet you think about me when you're out
At your cool indie music concerts every week
I bet you think about me in your house
With your organic shoes and your million-dollar couch
I bet you think about me when you say
"Oh my God, she's insane, she wrote a song about me"
I bet you think about me
Forever winter
He says he doesn't believe anything much he hears these days
He says, "Why fall in love, just so you can watch it go away?"
He spends most of his nights wishing it was how it used to be
He spends most of his flights getting pulled down by gravity
I call just checking up on him
He's up, 3 a.m., pacing
He says, "It's not just a phase I'm in"
My voice comes out begging
All this time I didn't know
You were breaking down
I'd fall to pieces on the floor
If you weren't around
Too young to know it gets better
I'll be summer sun for you forever
Forever winter if you go, uh-uh, oh
He seems fine most of the time, forcing smiles and never minds
His laugh is a symphony, when the lights go out, it's hard to breathe
I pull at every thread, trying to solve the puzzles in his head
Live my life scared to death, he'll decide to leave instead
I call just checking upon him
He's up, 5 a.m., wasted
Long gone, not even listening
My voice comes out screaming
All this time I didn't know
You were breaking down
I'd fall to pieces on the floor
If you weren't around
Too young to know it gets better
I'll be summer sun for you forever
Forever winter if you go, uh-uh, oh
If I was standing there in your apartment
I'd take that bomb in your head and disarm it
I'd say "I love you" even at your darkest and
Please don't go, uh-oh
I didn't know you were breaking down
I'd fall to pieces on the floor
If you weren't around
Too young to know it gets better
I'll be summer sun for you forever
Forever winter if you go, uh-uh, oh
I'll be your summer sun forever
At 3 a.m., pacing
All this time I didn't know
At 5 a.m., wasted
I'd be in pieces on the floor
Forever winter if you go
He says he doesn't believe anything much he hears these days
I say, "Believe in one thing, I won't go away"
Run
One, two, three, four
Give me the keys, I'll bring the car back around
We shouldn't be in this town
And my so-called friends, they don't know
I'd drive away before I let you go
So give me a reason and don't say no, no
There's a chain 'round your throat, piece of paper where I wrote
"I'll wait for you"
There's a key on the chain, there's a picture in a frame
Take it with you
And run, like you'd run from the law
Darling, let's run
Run from it all
We can go where our eyes can take us
Go where no one else is, run
Oo-oo-oo, we'll run
Oo-oo-oo, we'll run
Oo-oo-oo, we'll run
So you laugh like a child
And I'll sing like no one cares
No one to be, no one to tell
I could see this view a hundred times
Pale blue sky reflected in your eyes
So give me a reason and don't say no, no
And the note from the locket, you keep it in your pocket
Since I gave it to you
There's a heart on your sleeve
I'll take it when I leave
And hold it for you
And run, like you'd run from the law
Darling, let's run
Run from it all
We can go like they're trying to chase us
Go where no one else is, run
Oo-oo-oo, we'll run
Oo-oo-oo, we'll run
Oo-oo-oo, we'll run
There's been this hole in my heart
This thing was a shot in the dark
Say you'll never let 'em tear us apart
And I'll hold onto you while we run (and we run, and we run, and we run)
Like you'd run from the law (and we run, and we run, and we run)
Darling, let's run (and we run, and we run, and we run)
Run from it all (and we run, and we run, and we run)
We can go where our eyes can take us (and we run, and we run, and we run)
Go where no one else is, run (and we run, and we run, and we run)
Oo-oo-oo, we'll run (and we run, and we run, and we run)
Oo-oo-oo, we'll run (and we run, and we run, and we run)
Oo-oo-oo, we'll run (and we run, and we run, and we run)
Oo-oo-oo, and we'll run
The very first night
I wish I could fly
I'd pick you up and we'd go back in time
I'd write this in the sky
I miss you like it was the very first night
And so it goes, every weekend, the same party
I never go alone and I don't seem broken-hearted
My friends all say they know everything I'm going through
I drive down different roads but they all lead back to you
'Cause they don't know about the night in the hotel
They weren't ridin' in the car when we both fell
Didn't read the note on the Polaroid picture
They don't know how much I miss you
I wish I could fly
I'd pick you up and we'd go back in time
I'd write this in the sky
I miss you like it was the very first night
And so it was, we never saw it comin'
Not tryin' to fall in love, but we did like children runnin'
Back then we didn't know we were built to fall apart
We broke the status quo, then we broke each other's hearts
But don't forget about the night out in L.A.
Danced in the kitchen, chased me down through the hallway
No one knows about the words that we whispered
No one knows how much I miss you
I wish I could fly
I'd pick you up and we'd go back in time
I'd write this in the sky
I miss you like it was the very first night
Take me away, take me away
Take me away to you, to you
Take me away, take me away
Take me away to you, to you
I remember the night at the hotel
I was ridin' in the car when we both fell
I'm the one on the phone as you whisper
"Do you know how much I miss you?"
I wish that we could go back in time
And I'd say to you
I miss you like it was the very first night
I wish I could fly
I'd pick you up and we'd go back in time
I'd write this in the sky
I miss you like it was the very first night
take me away
(Take) take me away to you, to you
(Take) take me away, (take) take me away
(Take) take me away to you, to you
I walked through the door with you, the air was cold
But somethin' 'bout it felt like home somehow
And I left my scarf there at your sister's house
And you've still got it in your drawer, even now

Oh, your sweet disposition and my wide-eyed gaze
We're singin' in the car, getting lost upstate
Autumn leaves fallin' down like pieces into place
And I can picture it after all these days

And I know it's long gone and
That magic's not here no more
And I might be okay, but I'm not fine at all
Oh, oh, oh

'Causе there we arе again on that little town street
You almost ran the red 'cause you were lookin' over at me
Wind in my hair, I was there
I remember it all too well

Photo album on the counter
Your cheeks were turnin' red
You used to be a little kid with glasses in a twin-sized bed
And your mother's tellin' stories 'bout you on the tee-ball team
You taught me 'bout your past thinkin' your future was me

And you were tossing me the car keys
Fuck The Patriarchy keychain on the ground
We were always skippin' town
And I was thinkin' on the drive down: Any time now
He's gonna say it's love
You never called it what it was

Till we were dead and gone and buried
Check the pulse and come back swearing, it's the same
After three months in the grave
And then you wondered where it went to as I reached for you
But all I felt was shame
And you held my lifeless frame

And I know it's long gone and
There was nothing else I could do
And I forget about you long enough
To forget why I needed to

'Cause there we are again in the middle of the night
We're dancin' 'round the kitchen in the refrigerator light
Down the stairs, I was there
I remember it all too well

And there we are again when nobody had to know
You kept me like a secret, but I kept you like an oath
Sacred prayer and we'd swear
To remember it all too well, yeah

Well, maybe we got lost in translation
Maybe I asked for too much
But maybe this thing was a masterpiece till you tore it all up
Runnin' scared, I was there
I remember it all too well

And you call me up again just to break me like a promise
So casually cruel in the name of bein' honest
I'm a crumpled-up piece of paper lyin' here
'Cause I remember it all, all, all

They say all's well that ends well
But I'm in a new hell every time
You double-cross my mind
You said if we had been closer in age
Maybe it would've been fine
And that made me want to die

The idea you had of me, who was she?
A never-needy, ever-lovely jewel
Whose shine reflects on you
Not weepin' in a party bathroom
Some actress askin' me what happened: You
That's what happened: You

You who charmed my dad with self-effacing jokes
Sippin' coffee like you're on a late-night show
But then he watched me watch the front door all night
Willin' you to come
And he said: It's supposed to be fun
Turning 21

Time won't fly, it's like I'm paralyzed by it
I'd like to be my old self again
But I'm still tryin' to find it
After plaid shirt days and nights when you made me your own
Now you mail back my things and I walk home alone

But you keep my old scarf from that very first week
'Cause it reminds you of innocence and it smells like me
You can't get rid of it
'Cause you remember it all too well, yeah

'Cause there we are again when I loved you so
Back before you lost the one real thing you've ever known
It was rare, I was there
I remember it all too well

Wind in my hair, you were there
You remember it all
Down the stairs, you were there
You remember it all
It was rare, I was there
I remember it all too well

And I was never good at tellin' jokes, but the punch line goes
I'll get older, but your lovers stay my age
From when your Brooklyn broke my skin and bones
I'm a soldier who's returning half her weight

And did the twin flame bruise paint you blue?
Just between us, did the love affair maim you too?
'Cause in this city's barren cold
I still remember the first fall of snow
And how it glistened as it fell
I remember it all too well

Just between us, did the love affair maim you all too well?
Just between us, do you remember it all too well?
Just between us (just between us) I remember it all too well (wind in my hair)
(I was there, I was there)
(Down the stairs, I was there, I was there)
(Sacred prayer, I was there, I was there)
(It was rare, you remember it all too well)

(Wind in my hair, I was there, I was there)
(Down the stairs, I was there, I was there)
(Sacred prayer, I was there, I was there)
(It was rare, you remember it all too well)

(Wind in my hair, I was there, I was there)
(Down the stairs, I was there, I was there)
(Sacred prayer, I was there, I was there)
(It was rare, you remember it)

(Wind in my hair, I was there, I was there)
(Down the stairs, I was there, I was there)
(Sacred prayer, I was there, I was there)
'''

# Process the lyrics text
doc = nlp(folklore_lyrics)

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
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='autumn', mask=circle_mask).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()