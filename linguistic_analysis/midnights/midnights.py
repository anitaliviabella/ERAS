import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.

lyrics = '''
Lavander haze
Meet me at midnight
Starin' at the ceilin' with you
Oh, you don't ever say too much
And you don't really read into
My melancholia
I've been under scrutiny (yeah, oh, yeah)
You handle it beautifully (yeah, oh, yeah)
All this shit is new to me (yeah, oh, yeah)
I feel the lavender haze creepin' up on me
Surreal, I'm damned if I do give a damn what people say
No deal, the 1950s shit they want from me
I just wanna stay in that lavender haze
All they keep askin' me (all they keep askin' me)
Is if I'm gonna be your bride
The only kind of girl they see (only kind of girl they see)
Is a one-night or a wife
I find it dizzying (yeah, oh, yeah)
They're bringin' up my history (yeah, oh, yeah)
But you aren't even listening (yeah, oh, yeah)
(Ooh-whoa)
I feel the lavender haze creepin' up on me
Surreal, I'm damned if I do give a damn what people say
No deal, the 1950s shit they want from me
I just wanna stay in that lavender haze
That lavender haze
Talk your talk and go viral
I just need this love spiral
Get it off your chest
Get it off my desk (get it off my desk)
Talk your talk and go viral
I just need this love spiral
Get it off your chest
Get it off my desk
(Ooh-whoa)
I feel (I feel) the lavender haze creepin' up on me
Surreal, I'm damned if I do give a damn what people say (oh, yeah)
No deal (no deal), the 1950s shit they want from me
I just wanna stay in that lavender haze
Get it off your chest
Get it off my desk
That lavender haze, I just wanna stay
I just wanna stay in that lavender haze
Maroon
When the morning came we were cleaning incense off your vinyl shelf
'Cause we lost track of time again
Laughing with my feet in your lap
Like you were my closest friend
"How'd we end up on the floor anyway?" You say
"Your roommate's cheap-ass screw-top rosé, that's how"
I see you every day now
And I chose you
The one I was dancin' with
In New York, no shoes
Looked up at the sky and it was
The burgundy on my T-shirt when you splashed your wine into me
And how the blood rushed into my cheeks, so scarlet, it was
The mark you saw on my collarbone, the rust that grew between telephones
The lips I used to call home, so scarlet, it was maroon
When the silence came, we were shaking blind and hazy
How the hell did we lose sight of us again?
Sobbin' with your head in your hands
Ain't that the way shit always ends?
You were standin' hollow-eyed in the hallway
Carnations you had thought were roses, that's us
I feel you no matter what
The rubies that I gave up
And I lost you
The one I was dancin' with
In New York, no shoes
Looked up at the sky and it was maroon
The burgundy on my T-shirt when you splashed your wine into me
And how the blood rushed into my cheeks, so scarlet, it was (maroon)
The mark you saw on my collarbone, the rust that grew between telephones
The lips I used to call home, so scarlet, it was (maroon)
And I wake with your memory over me
That's a real fucking legacy, legacy (it was maroon)
And I wake with your memory over me
That's a real fucking legacy to leave
The burgundy on my T-shirt when you splashed your wine into me
And how the blood rushed into my cheeks, so scarlet (it was maroon)
The mark you saw on my collarbone, the rust that grew between telephones
The lips I used to call home, so scarlet (it was maroon)
It was maroon
It was maroon
Anti-Hero
I have this thing where I get older but just never wiser
Midnights become my afternoons
When my depression works the graveyard shift
All of the people I've ghosted stand there in the room
I should not be left to my own devices
They come with prices and vices
I end up in crisis (tale as old as time)
I wake up screaming from dreaming
One day I'll watch as you're leaving
'Cause you got tired of my scheming
(For the last time)
It's me, hi, I'm the problem, it's me
At tea time, everybody agrees
I'll stare directly at the sun but never in the mirror
It must be exhausting always rooting for the anti-hero
Sometimes I feel like everybody is a sexy baby
And I'm a monster on the hill
Too big to hang out, slowly lurching toward your favorite city
Pierced through the heart, but never killed
Did you hear my covert narcissism I disguise as altruism
Like some kind of congressman? (Tale as old as time)
I wake up screaming from dreaming
One day I'll watch as you're leaving
And life will lose all its meaning
(For the last time)
It's me, hi, I'm the problem, it's me (I'm the problem, it's me)
At tea time, everybody agrees
I'll stare directly at the sun but never in the mirror
It must be exhausting always rooting for the anti-hero
I have this dream my daughter in-law kills me for the money
She thinks I left them in the will
The family gathers 'round and reads it and then someone screams out
"She's laughing up at us from hell"
It's me, hi, I'm the problem, it's me
It's me, hi, I'm the problem, it's me
It's me, hi, everybody agrees, everybody agrees
It's me, hi (hi), I'm the problem, it's me (I'm the problem, it's me)
At tea (tea) time (time), everybody agrees (everybody agrees)
I'll stare directly at the sun but never in the mirror
It must be exhausting always rooting for the anti-hero
Snow on the beach
One night, a few moons ago
I saw flecks of what could've been lights
But it might just have been you
Passing by unbeknownst to me
Life is emotionally abusive
And time can't stop me quite like you did
And my flight was awful, thanks for asking
I'm unglued, thanks to you
And it's like snow at the beach
Weird but fuckin' beautiful
Flying in a dream, stars by the pocketful
You wanting me tonight feels impossible
But it's comin' down, no sound, it's all around
Like snow on the beach
Like snow on the beach
Like snow on the beach
Like snow, oh, oh oh
This scene feels like what I once saw on a screen
I searched aurora borealis green
I've never seen someone lit from within
Blurring out my periphery
My smile is like I won a contest
And to hide that would be so dishonest
And it's fine to fake it 'til you make it
'Til you do, 'til it's true
Now it's like snow at the beach
Weird but fuckin' beautiful
Flying in a dream, stars by the pocketful
You wanting me tonight feels impossible
But it's comin' down, no sound, it's all around
Like snow on the beach
Like snow on the beach
Like snow on the beach
Like snow, oh, oh oh
I (I) can't (can't) speak afraid to jinx it
I (I) don't (don't) even dare to wish it
But your eyes are flying saucers from another planet
Now I'm all for you like Janet
Can this be a real thing? Can it?
Are we falling like snow at the beach? (Snow at the beach)
Weird but fuckin' beautiful
Flying in a dream, stars by the pocketful (flying in a dream)
You wanting me tonight feels impossible (you wanting me)
But it's comin' down, no sound, it's all around
Like snow on the beach (snow on the beach)
Like snow on the beach (flying in a dream)
Like snow on the beach (you wanting me)
Like snow, oh
But it's comin' down, no sound, it's all around
Like snow on the beach (it's comin' down, it's comin' down)
(It's comin' down, it's comin' down)
(Like snow on the beach)
(It's comin' down, it's comin' down, it's comin' down, it's comin' down)
(It's comin' down, it's comin' down, it's comin' down, it's comin' down)
(Comin' down, it's comin' down, it's comin' down, it's comin' down)
You are on your own kid
Summer went away
Still, the yearning stays
I play it cool with the best of them
I wait patiently
He's gonna notice me
It's okay, we're the best of friends
Anyway
I hear it in your voice
You're smoking with your boys
I touch my phone as if it's your face
I didn't choose this town
I dream of getting out
There's just one who could make me stay
All my days
From sprinkler splashes to fireplace ashes
I waited ages to see you there
I search the party of better bodies
Just to learn that you never cared
You're on your own, kid
You always have been
I see the great escape
So long, Daisy May
I picked the petals, he loves me not
Something different bloomed
Writing in my room
I play my songs in the parking lot
I'll run away
From sprinkler splashes to fireplace ashes
I called a taxi to take me there
I search the party of better bodies
Just to learn that my dreams aren't rare
You're on your own, kid
You always have been
From sprinkler splashes to fireplace ashes
I gave my blood, sweat, and tears for this
I hosted parties and starved my body
Like I'd be saved by a perfect kiss
The jokes weren't funny, I took the money
My friends from home don't know what to say
I looked around in a blood-soaked gown
And I saw something they can't take away
'Cause there were pages turned with the bridges burned
Everything you lose is a step you take
So make the friendship bracelets
Take the moment and taste it
You've got no reason to be afraid
You're on your own, kid
Yeah, you can face this
You're on your own, kid
You always have been
Midnight rain
Rain, he wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed like midnight
My town was a wasteland
Full of cages, full of fences
Pageant queens and big pretenders
But for some, it was paradise
My boy was a montage
A slow-motion, love potion
Jumping off things in the ocean
I broke his heart 'cause he was nice
He was sunshine, I was midnight rain
He wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed like midnight
It came like a postcard
Picture perfect, shiny family
Holiday, peppermint candy
But for him it's every day
So I peered through a window
A deep portal, time travel
All the love we unravel
And the life I gave away
'Cause he was sunshine
I was midnight rain
He wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed
Like midnight
Rain, he wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed
Like midnight
I guess sometimes we all get
Just what we wanted, just what we wanted
And he never thinks of me
Except when I'm on TV
I guess sometimes we all get
Some kind of haunted, some kind of haunted
And I never think of him
Except on midnights like this (midnights like this)
Question...?
Rain, he wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed like midnight
My town was a wasteland
Full of cages, full of fences
Pageant queens and big pretenders
But for some, it was paradise
My boy was a montage
A slow-motion, love potion
Jumping off things in the ocean
I broke his heart 'cause he was nice
He was sunshine, I was midnight rain
He wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed like midnight
It came like a postcard
Picture perfect, shiny family
Holiday, peppermint candy
But for him it's every day
So I peered through a window
A deep portal, time travel
All the love we unravel
And the life I gave away
'Cause he was sunshine
I was midnight rain
He wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed
Like midnight
Rain, he wanted it comfortable
I wanted that pain
He wanted a bride
I was making my own name
Chasing that fame
He stayed the same
All of me changed
Like midnight
I guess sometimes we all get
Just what we wanted, just what we wanted
And he never thinks of me
Except when I'm on TV
I guess sometimes we all get
Some kind of haunted, some kind of haunted
And I never think of him
Except on midnights like this (midnights like this)
Vigilante Shit
Draw the cat eye, sharp enough to kill a man
You did some bad things, but I'm the worst of them
Sometimes I wonder which one will be your last lie
They say looks can kill and I might try
I don't dress for women
I don't dress for men
Lately I've been dressing for revenge
I don't start it but I can tell you how it ends
Don't get sad, get even
So on the weekends
I don't dress for friends
Lately I've been dressing for revenge
She needed cold hard proof so I gave her some
She had the envelope, where you think she got it from?
Now she gets the house, gets the kids, gets the pride
Picture me thick as thieves with your ex-wife
And she looks so pretty
Driving in your Benz
Lately she's been dressing for revenge
She don't start it, but she can tell you how it ends
Don't get sad, get even
So on the weekends
She don't dress for friends
Lately she's been dressing for revenge
Ladies always rise above
Ladies know what people want
Someone sweet and kind and fun
The lady simply had enough
While he was doing lines
And crossing all of mine
Someone told his white collar crimes to the FBI
And I don't dress for villains
Or for innocents
I'm on my vigilante shh again
I don't start it, but I can tell you how it ends
Don't get sad, get even
So on the weekends
I don't dress for friends
Lately I've been dressing for revenge
Bejeweled
Baby love, I think I've been a little too kind
Didn't notice you walking all over my peace of mind
In the shoes I gave you as a present
Puttin' someone first only works when you're in their top five
And by the way, I'm going out tonight
Best believe I'm still bejeweled
When I walk in the room
I can still make the whole place shimmer
And when I meet the band
They ask, "Do you have a man?"
I can still say, "I don't remember"
Familiarity breeds contempt
Don't put me in the basement
When I want the penthouse of your heart
Diamonds in my eyes
I polish up real, I polish up real nice
Nice
Baby boy, I think I've been too good of a girl (too good of a girl)
Did all the extra credit, then got graded on a curve
I think it's time to teach some lessons
I made you my world (huh), have you heard? (Huh)
I can reclaim the land
And I miss you (I miss you)
But I miss sparkling (ah, hey)
Best believe I'm still bejeweled
When I walk in the room
I can still make the whole place shimmer
And when I meet the band
They ask, "Do you have a man?"
I can still say, "I don't remember"
Familiarity breeds contempt
Don't put me in the basement
When I want the penthouse of your heart
Diamonds in my eyes
I polish up real, I polish up real nice
Nice
Sapphire tears on my face
Sadness became my whole sky
But some guy said my aura's moonstone
Just 'cause he was high
And we're dancin' all night
And you can try to change my mind
But you might have to wait in line
What's a girl gonna do?
A diamond's gotta shine
Best believe I'm still bejeweled
When I walk in the room
I can still make the whole place shimmer (shimmer)
And when I meet the band
They ask, "Do you have a man?"
I can still say, "I don't remember"
Familiarity breeds contempt
Don't put me in the basement
When I want the penthouse of your heart
Diamonds in my eyes
I polish up real (nice), I polish up real nice
And we're dancin' all night
And you can try to change my mind
But you might have to wait in line
What's a girl gonna do? What's a girl gonna do?
I polish up nice
Best believe I'm still bejeweled
When I walk in the room
I can still make the whole place shimmer
Labyrinth
It only hurts this much right now
Was what I was thinking the whole time
Breathe in, breathe through
Breathe deep, breathe out
I'll be getting over you my whole life
You know how scared I am of elevators
Never trust it if it rises fast
It can't last
Uh oh, I'm falling in love
Oh no, I'm falling in love again
Oh, I'm falling in love
I thought the plane was going down
How'd you turn it right around
It only feels this raw right now
Lost in the labyrinth of my mind
Break up, break free, break through, break down
You would break your back to make me break a smile
You know how much I hate that everybody just expects me to bounce back
Just like that
Uh oh, I'm falling in love
Oh no, I'm falling in love again
Oh, I'm falling in love
I thought the plane was going down
How'd you turn it right around
Uh oh, I'm falling in love
Oh no, I'm falling in love again
Oh, I'm falling in love
I thought the plane was going down
How'd you turn it right around
Uh oh, I'm falling in love
Oh no, I'm falling in love again
Oh, I'm falling in love
I thought the plane was going down
How'd you turn it right around
Uh oh, I'm falling in love
Oh no, I'm falling in love again
Oh, I'm falling in love
I thought the plane was going down
How'd you turn it right around
Karma
You're talking shit for the hell of it
Addicted to betrayal, but you're relevant
You're terrified to look down
'Cause if you dare, you'll see the glare
Of everyone you burned just to get there
It's coming back around
And I keep my side of the street clean
You wouldn't know what I mean
'Cause karma is my boyfriend
Karma is a god
Karma is the breeze in my hair on the weekend
Karma's a relaxing thought
Aren't you envious that for you it's not?
Sweet like honey, karma is a cat
Purring in my lap 'cause it loves me
Flexing like a goddamn acrobat
Me and karma vibe like that
Spider-boy, king of thieves
Weave your little webs of opacity
My pennies made your crown
Trick me once, trick me twice
Don't you know that cash ain't the only price?
It's coming back around
And I keep my side of the street clean
You wouldn't know what I mean
'Cause karma is my boyfriend
Karma is a god
Karma is the breeze in my hair on the weekend
Karma's a relaxing thought
Aren't you envious that for you it's not?
Sweet like honey, karma is a cat
Purring in my lap 'cause it loves me
Flexing like a goddamn acrobat
Me and karma vibe like that
Ask me what I learned from all those years
Ask me what I earned from all those tears
Ask me why so many fade, but I'm still here
(I'm still, I'm still here)
'Cause karma is the thunder
Rattling your ground
Karma's on your scent like a bounty hunter
Karma's gonna track you down
Step by step from town to town
Sweet like justice, karma is a queen
Karma takes all my friends to the summit
Karma is the guy on the screen
Coming straight home to me
'Cause karma is my boyfriend (karma is my boyfriend)
Karma is a god
Karma is the breeze in my hair on the weekend (weekend)
Karma's a relaxing thought
Aren't you envious that for you it's not?
Sweet like honey, karma is a cat
Purring in my lap 'cause it loves me
Flexing like a goddamn acrobat
Me and karma vibe like that
Karma is my boyfriend
Karma is a god
Mm-hm
Karma's a relaxing thought
Sweet nothing
I spy with my little tired eye
Tiny as a firefly
A pebble that we picked up last July
Down deep inside your pocket
We almost forgot it
Does it ever miss Wicklow sometimes?
They said the end is coming
Everyone's up to something
I find myself running home to your sweet nothings
Outside, they're push and shoving
You're in the kitchen humming
All that you ever wanted from me was sweet nothing
On the way home
I wrote a poem
You say, "What a mind"
This happens all the time
'Cause they said the end is coming
Everyone's up to something
I find myself running home to your sweet nothings
Outside, they're push and shoving
You're in the kitchen humming
All that you ever wanted from me was nothing
Industry disruptors and soul deconstructors
And smooth-talking hucksters out glad-handing each other
And the voices that implore, "You should be doing more"
To you, I can admit that I'm just too soft for all of it
They said the end is coming
Everyone's up to something
I find myself running home to your sweet nothings
Outside, they're push and shoving
You're in the kitchen humming
All that you ever wanted from me was sweet nothing
They said the end is coming (they said the end is coming)
Everyone's up to something (everyone's up to something)
I find myself running home to your sweet nothings
Outside, they're push and shoving (outside, they're push and shoving)
You're in the kitchen humming (you're in the kitchen humming)
All that you ever wanted from me was sweet nothing
Mastermind
Once upon a time, the planets and the fates
And all the stars aligned
You and I ended up in the same room
At the same time
And the touch of a hand lit the fuse
Of a chain reaction of countermoves
To assess the equation of you
Checkmate, I couldn't lose
What if I told you none of it was accidental
And the first night that you saw me, nothing was gonna stop me?
I laid the groundwork and then, just like clockwork
The dominoes cascaded in a line
What if I told you I'm a mastermind?
And now you're mine
It was all by design
'Cause I'm a mastermind
You see, all the wisest women
Had to do it this way
'Cause we were born to be the pawn
In every lover's game
If you fail to plan, you plan to fail
Strategy sets the scene for the tale
I'm the wind in our free-flowing sails
And the liquor in our cocktails
What if I told you none of it was accidental
And the first night that you saw me, I knew I wanted your body?
I laid the groundwork and then, just like clockwork
The dominoes cascaded in a line
What if I told you I'm a mastermind?
And now you're mine
It was all my design
'Cause I'm a mastermind
No one wanted to play with me as a little kid
So I've been scheming like a criminal ever since
To make them love me and make it seem effortless
This this the first time I've felt the need to confess
And I swear
I'm only cryptic and Machiavellian 'cause I care
So I told you none of it was accidental
And the first night that you saw me, nothing was gonna stop me
I laid the groundwork and then saw a wide smirk
On your face, you knew the entire time
You knew that I'm a mastermind
And now you're mine
Yeah, all you did was smile
'Cause I'm a mastermind
'''

# Process the lyrics text
doc = nlp(lyrics)

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
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='cividis', mask=circle_mask).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
