import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.

folklore_lyrics = '''
Mine
Oh, oh, oh
Oh, oh, oh
You were in college, working part-time waiting tables
Left a small town, never looked back
I was a flight risk, with a fear of fallin'
Wondering why we bother with love, if it never lasts
I say, "Can you believe it?"
As we're lyin' on the couch
The moment, I can see it
Yes, yes, I can see it now
Do you remember, we were sittin' there by the water?
You put your arm around me for the first time
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
Flash forward, and we're takin' on the world together
And there's a drawer of my things at your place
You learn my secrets and you figure out why I'm guarded
You say we'll never make my parents' mistakes
But we got bills to pay
We got nothin' figured out
When it was hard to take
Yes, yes
This is what I thought about
Do you remember, we were sittin' there by the water?
You put your arm around me, for the first time
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
Do you remember all the city lights on the water?
You saw me start to believe for the first time
You made a rebel of a careless man's careful daughter
You are the best thing that's ever been mine
Oh, oh, oh
And I remember that fight, 2:30 AM
As everything was slipping right out of our hands
I ran out, crying, and you followed me out into the street
Braced myself for the goodbye
'Cause that's all I've ever known
Then you took me by surprise
You said, "I'll never leave you alone"
You said, "I remember how we felt, sitting by the water
And every time I look at you, it's like the first time
I fell in love with a careless man's careful daughter
She is the best thing that's ever been mine"
Hold on and make it last
Hold on, never turn back
(Hold on) you made a rebel of a careless man's careful daughter
(Hold on) you are the best thing that's ever been mine (hold on)
Do you believe it? (Yeah, yeah, yeah)
We're gonna make it now (yeah, yeah, yeah)
And I can see it (yeah, yeah)
I can see it now
Sparks fly
The way you move is like a full on rainstorm
And I'm a house of cards
You're the kind of reckless that should send me running
But I kinda know that I won't get far
And you stood there in front of me just
Close enough to touch
Close enough to hope you couldn't see
What I was thinking of
Drop everything now
Meet me in the pouring rain
Kiss me on the sidewalk
Take away the pain
'Cause I see sparks fly, whenever you smile
Get me with those green eyes, baby
As the lights go down
Gimme something that'll haunt me when you're not around
'Cause I see sparks fly, whenever you smile
My mind forgets to remind me you're a bad idea
You touch me once and it's really something
You find I'm even better than you imagined I would be
I'm on my guard for the rest of the world
But with you, I know it's no good
And I could wait patiently
But I really wish you would
Drop everything now
Meet me in the pouring rain
Kiss me on the sidewalk
Take away the pain
'Cause I see sparks fly, whenever you smile
Get me with those green eyes, baby
As the lights go down
Gimme something that'll haunt me when you're not around
'Cause I see sparks fly, whenever you smile
I run my fingers through your hair
And watch the lights go wild
Just keep on keeping your eyes on me
It's just wrong enough to make it feel right
And lead me up the staircase
Won't you whisper soft and slow
I'm captivated by you, baby
Like a fireworks show
Drop everything now
Meet me in the pouring rain
Kiss me on the sidewalk
Take away the pain
'Cause I see sparks fly whenever you smile
Get me with those green eyes, baby
As the lights go down
Gimme something that'll haunt me when you're not around
'Cause I see sparks fly, whenever you smile
And the sparks fly, oh, baby, smile
And the sparks fly
Back to December
I'm so glad you made time to see me
How's life? Tell me, how's your family?
I haven't seen them in a while
You've been good, busier than ever
We small talk, work and the weather
Your guard is up and I know why
Because the last time you saw me
Is still burned in the back of your mind
You gave me roses and I left them there to die
So this is me swallowin' my pride
Standin' in front of you sayin' I'm sorry for that night
And I go back to December all the time
It turns out freedom ain't nothin' but missin' you
Wishin' I'd realized what I had when you were mine
I'd go back to December, turn around and make it alright
I go back to December all the time
These days, I haven't been sleepin'
Stayin' up playin' back myself leavin'
When your birthday passed and I didn't call
Then I think about summer, all the beautiful times
I watched you laughin' from the passenger's side
And realized I loved you in the fall
And then the cold came, the dark days
When fear crept into my mind
You gave me all your love and all I gave you was goodbye
So this is me swallowin' my pride
Standin' in front of you sayin' I'm sorry for that night
And I go back to December all the time
It turns out freedom ain't nothin' but missin' you
Wishin' I'd realized what I had when you were mine
I'd go back to December, turn around and change my own mind
I go back to December all the time
I miss your tan skin, your sweet smile
So good to me, so right
And how you held me in your arms that September night
The first time you ever saw me cry
Maybe this is wishful thinkin'
Probably mindless dreamin'
But if we loved again, I swear I'd love you right
I'd go back in time and change it, but I can't
So if the chain is on your door, I understand
But this is me swallowin' my pride
Standin' in front of you sayin' I'm sorry for that night
And I go back to December
It turns out freedom ain't nothin' but missin' you
Wishin' I'd realized what I had when you were mine
I'd go back to December, turn around and make it alright
I'd go back to December, turn around and change my own mind
I go back to December all the time
All the time
Speak now
I am not the kind of girl
Who should be rudely barging in on a white veil occasion
But you are not the kind of boy
Who should be marrying the wrong girl
I sneak in and see your friends
And her snotty little family all dressed in pastel
And she is yelling at a bridesmaid
Somewhere back inside a room
Wearing a gown shaped like a pastry
This is surely not what you thought it would be
I lose myself in a daydream
Where I stand and say
Don't say yes, run away now
I'll meet you when you're out of the church at the back door
Don't wait, or say a single vow
You need to hear me out
And they said, "Speak now"
Fond gestures are exchanged
And the organ starts to play
A song that sounds like a death march
And I am hiding in the curtains
It seems that I was uninvited by your lovely bride-to-be
She floats down the aisle like a pageant queen
But I know you wish it was me
You wish it was me
Don't you?
Don't say yes, run away now
I'll meet you when you're out of the church at the back door
Don't wait, or say a single vow
You need to hear me out
And they said, "Speak now"
Don't say yes, run away now
I'll meet you when you're out of the church at the back door
Don't wait, or say a single vow
Your time is running out
And they said, "Speak now"
I hear the preacher say, "Speak now or forever hold your peace"
There's the silence, there's my last chance
I stand up with shaky hands, all eyes on me
Horrified looks from everyone in the room
But I'm only looking at you
I am not the kind of girl
Who should be rudely barging in on a white veil occasion
But you are not the kind of boy
Who should be marrying the wrong girl
So don't say yes, run away now
I'll meet you when you're out of the church at the back door
Don't wait, or say a single vow
You need to hear me out
And they said, "Speak now"
And you'll say, "Let's run away now"
I'll meet you when I'm out of my tux at the back door
Baby, I didn't say my vows
So glad you were around
When they said, "Speak now"
Dear John
Long were the nights when
My days once revolved around you
Counting my footsteps
Praying the floor won't fall through again
And my mother accused me of losing my mind
But I swore I was fine
You paint me a blue sky
And go back and turn it to rain
And I lived in your chess game
But you changed the rules every day
Wondering which version of you I might get on the phone tonight
Well, I stopped picking up and this song is to let you know why
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with?
The girl in the dress, cried the whole way home
I should've known
Well, maybe it's me
And my blind optimism to blame
Or maybe it's you and your sick need
To give love then take it away
And you'll add my name to your long list of traitors
Who don't understand
And I'll look back and regret how I ignored when they said
"Run as fast as you can"
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with?
The girl in the dress, cried the whole way home
Dear John, I see it all now, it was wrong
Don't you think nineteen's too young
To be played by your dark, twisted games when I loved you so?
I should've known
You are an expert at sorry and keeping the lines blurry
Never impressed by me acing your tests
All the girls that you've run dry have tired lifeless eyes
'Cause you burned them out
But I took your matches before fire could catch me
So don't look now
I'm shining like fireworks over your sad empty town
Oh, oh
Dear John, I see it all now that you're gone
Don't you think I was too young to be messed with?
The girl in the dress, cried the whole way home
I see it all now that you're gone
Don't you think I was too young to be messed with?
The girl in the dress wrote you a song
You should've known
You should've known
Don't you think I was too young?
You should've known
Mean
You
With your words like knives and swords and weapons
That you use againt me
You
Will knock me of my feet again
Got me feeling like a nothing
You
With your voice like nails on a chalkboard
Calling me out when i'am wounded
You
Picking on the weaker man
Well you can take me down
With just one single blow
But you dont know what you dont know
Someday i'll be living in a big old city
And all you're ever gonna be is mean
Someday i'll be big enough so you cant hit me
And all you're ever gonna be is mean
Why you gotta be so mean?
You
With your switching sides
And your walk by lies
And your humiliation
You
Are pointing out my flaws again
As if i dont already see them
I'll walk with my head down
Trying to block you out
Cause i'll never impress you
I just wanna feel okay again
I bet you got pushed around
Somebody made you cold
But the cycle ends right now
Cause you cant lead me down that road
And you dont know what you dont know
Someday i'll be living in a big old city
And all you're ever gonna be is mean
Someday i'll be big enough so you can't hit me
And all you're are ever gonna be is mean
Why you gotta be so mean?
And i can see you years from now in a bar
Talking over a football game
With that same big mouth opinion
But nobody is listening
Washed up and ranting about
The same old bitter things
Drunk and grumbling on about
How i cant sing
But all you are is mean
All you are is mean
And a liar
And pathetic
And alone in life
And mean
And mean
And mean
And mean
But someday i'll be living in a big old city
And all you're ever gonna be is mean
Yeah
Someday i'll be big enough so you cant hit me
And all you're ever gonna be is mean
Why you gotta be so mean someday
I'll be living in a big old city
And all you're ever gonna be is mean
Why you gotta be so mean someday
I'll be big enough so you cant hit me
And all youre ever gonna be is mean
Why you gotta be so mean?
The story of us
I used to think one day we'd tell the story of us
How we met and the sparks flew instantly
And people would say, "They're the lucky ones"
I used to know my place was a spot next to you
Now I'm searching the room for an empty seat
'Cause lately I don't even know what page you're on
Oh, a simple complication
Miscommunications lead to fall out
So many things that I wish you knew
So many walls up I can't break through
Now I'm standing alone in a crowded room
And we're not speaking and I'm dying to know
Is it killing you like it's killing me? Yeah
I don't know what to say since the twist of fate
When it all broke down
And the story of us looks a lot like a tragedy now
Next chapter
How'd we end up this way?
See me nervously pulling at my clothes
And trying to look busy
And you're doing your best to avoid me
I'm starting to think one day I'll tell the story of us
How I was losing my mind when I saw you here
But you held your pride like you should have held me
Oh, I'm scared to see the ending
Why are we pretending this is nothing?
I'd tell you I miss you but I don't know how
I've never heard silence quite this loud
Now I'm standing alone in a crowded room
And we're not speaking and I'm dying to know
Is it killing you like it's killing me? Yeah
I don't know what to say since the twist of fate
When it all broke down
And the story of us looks a lot like a tragedy now
This is looking like a contest
Of who can act like they care less
But I liked it better when you were on my side
The battle's in your hands now
But I would lay my armor down
If you'd say you'd rather love than fight
So many things that you wish I knew
But the story of us might be ending soon
Now I'm standing alone in a crowded room
And we're not speaking and I'm dying to know
Is it killing you like it's killing me, yeah
But I don't know what to say since the twist of fate
When it all broke down
And the story of us looks a lot like a tragedy now, now, now
And we're not speaking and I'm dying to know
Is it killing you like it's killing me? Yeah
I don't know what to say since the twist of fate
'Cause we're going down
And the story of us looks a lot like a tragedy now
The end
Never grow up
Your little hand's wrapped around my finger
And it's so quiet in the world tonight
Your little eyelids flutter 'cause you're dreamin'
So I tuck you in, turn on your favorite night light
To you, everything's funny
You got nothing to regret
I'd give all I have honey
If you could stay like that
Oh, darlin', don't you ever grow up
Don't you ever grow up
Just stay this little
Oh, darlin', don't you ever grow up
Don't you ever grow up
It could stay this simple
I won't let nobody hurt you
Won't let no one break your heart
And no one will desert you
Just try to never grow up
Never grow up
You're in the car on the way to the movies
And you're mortified your mom's droppin' you off
At fourteen, there's just so much you can't do
And you can't wait to move out someday and call your own shots
But don't make her drop you off around the block
Remember that she's gettin' older too
And don't lose the way that you dance
Around in your PJs getting ready for school
Oh, darlin', don't you ever grow up
Don't you ever grow up
Just stay this little
Oh, darlin', don't you ever grow up
Don't you ever grow up
It could stay this simple
And no one's ever burned you
Nothing's ever left you scarred
And even though you want to
Just try to never grow up
Take pictures in your mind of your childhood room
Memorize what it sounded like when your dad gets home
Remember the footsteps, remember the words said
And all your little brother's favorite songs
I just realized everything I have is someday gonna be gone
So here I am in my new apartment
In a big city, they just dropped me off
It's so much colder than I thought it would be
So I tuck myself in and turn my nightlight on
Wish I'd never grown up
I wish I'd never grown up
Oh, I don't wanna grow up
Wish I'd never grown up
Could still be little
Oh, I don't wanna grow up
Wish I'd never grown up
It could still be simple
Oh, darlin', don't you ever grow up
Don't you ever grow up
Just stay this little
Oh, darlin', don't you ever grow up
Don't you ever grow up
It could stay this simple
I won't let nobody hurt you
Won't let no one break your heart
And even though you want to
Please try to never grow up
Oh, oh
Don't you ever grow up
Oh (never grow up)
Just never grow up
Enchanted
There I was again tonight
Forcing laughter, faking smiles
Same old tired, lonely place
Walls of insincerity, shifting eyes and vacancy
Vanished when I saw your face
All I can say is, it was enchanting to meet you
Your eyes whispered, "Have we met?"
'Cross the room your silhouette
Starts to make its way to me
The playful conversation starts
Counter all your quick remarks
Like passing notes in secrecy
And it was enchanting to meet you
All I can say is, I was enchanted to meet you
This night is sparkling, don't you let it go
I'm wonderstruck, blushing all the way home
I'll spend forever wondering if you knew
I was enchanted to meet you
The lingering question kept me up
2 AM, who do you love?
I wonder 'til I'm wide awake
And now I'm pacing back and forth
Wishing you were at my door
I'd open up and you would say, "Hey"
It was enchanting to meet you
All I know is, I was enchanted to meet you
This night is sparkling, don't you let it go
I'm wonderstruck, blushing all the way home
I'll spend forever wondering if you knew
That this night is flawless, don't you let it go
I'm wonderstruck, dancing around all alone
I'll spend forever wondering if you knew
I was enchanted to meet you
This is me praying that
This was the very first page
Not where the story line ends
My thoughts will echo your name, until I see you again
These are the words I held back, as I was leaving too soon
I was enchanted to meet you
Please don't be in love with someone else
Please don't have somebody waiting on you
Please don't be in love with someone else
Please don't have somebody waiting on you
This night is sparkling, don't you let it go
I'm wonderstruck, blushing all the way home
I'll spend forever wondering if you knew
This night is flawless, don't you let it go
I'm wonderstruck, dancing around all alone
I'll spend forever wondering if you knew
I was enchanted to meet you
Please don't be in love with someone else
Please don't have somebody waiting on you
Better than revenge
Now go stand in the corner and think about what you did
Ha, time for a little revenge
The story starts when it was hot and it was summer
And, I had it all I had him right there where I wanted him
She came along, got him alone, and let's hear the applause
She took him faster than you could say sabotage
I never saw it coming, nor would I have suspected it
I underestimated just who I was dealing with
She had to know the pain was beating on me like a drum
She underestimated just who she was stealing from
She's not a saint and she's not what you think
She's an actress, whoa
She's better known for the things that she does
On the mattress, whoa
Soon she's gonna find
Stealing other people's toys on the playground
Won't make you many friends
She should keep in mind
She should keep in mind
There is nothing I do better than revenge, ha
She looks at life like it's a party and she's on the list
She looks at me like I'm a trend and she's so over it
I think her ever present frown is a little troubling
And, she thinks I'm psycho
'Cause I like to rhyme her name with things, but
Sophistication isn't what you wear, or who you know
Or pushing people down to get you where you wanna go
Oh they didn't teach you that in prep school
So it's up to me
But no amount of vintage dresses gives you dignity
(Think about what you did)
She's not a saint and she's not what you think
She's an actress, whoa
She's better known for the things that she does
On the mattress, whoa
Soon she's gonna find
Stealing other people's toys on the playground
Won't make you many friends
She should keep in mind
She should keep in mind
There is nothing I do better than revenge, ha
I'm just another thing for you to roll your eyes at honey
You might have him, but haven't you heard
I'm just another thing for you to roll your eyes at honey
You might have him, but I'll always get the last word
Whoa
She's not a saint and she's not what you think
She's an actress, whoa
She's better known for the things that she does
On the mattress, whoa
Soon she's gonna find
Stealing other people's toys on the playground
Won't make you many friends
She should keep in mind
She should keep in mind
There is nothing I do better than revenge, ha
And do you still feel like you know what you're doing
'Cause I don't think you do, oh
Do you still feel like you know what you're doing
I don't think you do, I don't think you do
Let's hear the applause
C'mon show me how much better you are
See you deserve some applause
'Cause you're so much better
She took him faster than you could say sabotage
Innocent
I guess you really did it this time
Left yourself in your warpath
Lost your balance on a tightrope
Lost your mind tryin' to get it back
Wasn't it easier in your lunchbox days?
Always a bigger bed to crawl into
Wasn't it beautiful when you believed in everything
And everybody believed in you?
It's alright, just wait and see
Your string of lights is still bright to me
Oh, who you are is not where you've been
You're still an innocent
You're still an innocent
Did some things you can't speak of
But at night you live it all again
You wouldn't be shattered on the floor now
If only you had seen what you know now then
Wasn't it easier in your firefly-catchin' days?
And everything out of reach
Someone bigger brought down to you
Wasn't it beautiful runnin' wild 'til you fell asleep
Before the monsters caught up to you?
It's alright, just wait and see
Your string of lights is still bright to me
Oh, who you are is not where you've been
You're still an innocent
It's okay, life is a tough crowd
32 and still growin' up now
Who you are is not what you did
You're still an innocent
Time turns flames to embers
You'll have new Septembers
Everyone of us has messed up too, ooh, ooh
Minds change like the weather
I hope you remember
Today is never too late to be brand new
Oh, oh, oh, oh, oh, oh
It's alright, just wait and see
Your string of lights is still bright to me
Oh, who you are is not where you've been
You're still an innocent
It's okay, life is a tough crowd
32 and still growin' up now
Who you are is not what you did
You're still an innocent
You're still an innocent
Lost your balance on a tightrope, oh
It's never too late to get it back
Haunted
You and I walk a fragile line
I have known it all this time
But I never thought I'd live to see it break
It's getting dark and it's all too quiet
And I can't trust anything now
And it's coming over you like it's all a big mistake
Oh, I'm holding my breath
Won't lose you again
Something's made your eyes go cold
Come on, come on, don't leave me like this
I thought I had you figured out
Something's gone terribly wrong
You're all I wanted
Come on, come on, don't leave me like this
I thought I had you figured out
Can't breathe whenever you're gone
Can't turn back now, I'm haunted
Stood there and watched you walk away
From everything we had
But I still mean every word I said to you
He will try to take away my pain
And he just might make me smile
But the whole time I'm wishing he was you instead
Oh, holding my breath
Won't see you again
Something keeps me holding on to nothing
Come on, come on, don't leave me like this
I thought I had you figured out
Something's gone terribly wrong
You're all I wanted
Come on, come on, don't leave me like this
I thought I had you figured out
Can't breathe whenever you're gone
Can't turn back now, I'm haunted
I know
I know
I just know
You're not gone, you can't be gone, no
Come on, come on, don't leave me like this
I thought I had you figured out
Something's gone terribly wrong
Won't finish what you started
Come on, come on, don't leave me like this
I thought I had you figured out
Can't breathe whenever you're gone
Can't go back, I'm haunted
Oh-oh, oh-oh, oh-oh, oh-oh-oh
You and I walk a fragile line
I have known it all this time
Never ever thought I'd see it break
Never thought I'd see it
Last kiss
I still remember the look on your face
Lit through the darkness at 1:58
The words that you whispered for just us to know
You told me you loved me
So why did you go away?
Away
I do recall now, the smell of the rain
Fresh on the pavement, I ran off the plane
That July ninth, the beat of your heart
It jumps through your shirt
I can still feel your arms
But now I'll go
Sit on the floor wearing your clothes
All that I know is I don't know
How to be something you miss
I never thought we'd have a last kiss
I never imagined we'd end like this
Your name, forever the name on my lips
I do remember the swing of your step
The life of the party, you're showing off again
And I'd roll my eyes and then you'd pull me in
I'm not much for dancing, but for you, I did
Because I love your handshake, meeting my father
I love how you walk with your hands in your pockets
How you'd kiss me when I was in the middle of saying something
There's not a day I don't miss those rude interruptions
And I'll go
Sit on the floor wearing your clothes
All that I know is I don't know
How to be something you miss
I never thought we'd have a last kiss
I never imagined we'd end like this
Your name, forever the name on my lips
So I'll watch your life in pictures like I used to watch you sleep
And I feel you forget me like I used to feel you breathe
And I'll keep up with our old friends just to ask them how you are
Hope it's nice where you are
And I hope the sun shines and it's a beautiful day
And something reminds you, you wish you had stayed
You can plan for a change in the weather and time
But I never planned on you changing your mind
So I'll go
Sit on the floor wearing your clothes
All that I know is I don't know
How to be something you miss
I never thought we'd have a last kiss
Never imagined we'd end like this
Your name, forever the name on my lips
Just like our last kiss
Forever the name on my lips
Forever the name on my lips
Just like our last
Long live
I said remember this moment
In the back of my mind
The time we stood with our shaking hands
The crowds in stands went wild
We were the kings and the queens
And they read off our names
The night you danced like you knew our lives
Would never be the same
You held your head like a hero
On a history book page
It was the end of a decade
But the start of an age
Long live the walls we crashed through
How the kingdom lights shined just for me and you
I was screaming, "Long live all the magic we made"
And bring on all the pretenders
One day we will be remembered
I said remember this feeling
I passed the pictures around
Of all the years that we stood there on the sidelines
Wishing for right now
We are the kings and the queens
You traded your baseball cap for a crown
When they gave us our trophies
And we held them up for our town
And the cynics were outraged
Screaming, "This is absurd"
'Cause for a moment, a band of thieves
In ripped up jeans got to rule the world
Long live the walls we crashed through
How the kingdom lights shined just for me and you
I was screaming, "Long live all the magic we made"
And bring on all the pretenders, I'm not afraid
Long live all the mountains we moved
I had the time of my life fighting dragons with you
I was screaming, "Long live that look on your face"
And bring on all the pretenders
One day we will be remembered
Hold on to spinning around
Confetti falls to the ground
May these memories break our fall
Will you take a moment?
Promise me this
That you'll stand by me forever
But if, God forbid, fate should step in
And force us into a goodbye
If you have children someday
When they point to the pictures
Please tell them my name
Tell them how the crowds went wild
Tell them how I hope they shine
Long live the walls we crashed through
I had the time of my life with you
Long, long live the walls we crashed through
How the kingdom lights shined just for me and you
And I was screaming, "Long live all the magic we made"
And bring on all the pretenders, I'm not afraid
Singing long live all the mountains we moved
I had the time of my life fighting dragons with you
And long, long live the look on your face
And bring on all the pretenders
One day, we will be remembered
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
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='plasma', mask=circle_mask).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
