import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.

lyrics = '''
willow
I'm like the water when your ship rolled in that night
Rough on the surface but you cut through like a knife
And if it was an open-shut case
I never would've known from that look on your face
Lost in your current like a priceless wine
The more that you say
The less I know
Wherever you stray
I follow
I'm begging for you to take my hand
Wreck my plans
That's my man
Life was a willow and it bent right to your wind (oh)
Head on the pillow, I could feel you sneaking in
As if you were a mythical thing
Like you were a trophy or a champion ring
And there was one prize I'd cheat to win
The more that you say
The less I know
Wherever you stray
I follow
I'm begging for you to take my hand
Wreck my plans
That's my man
You know that my train could take you home
Anywhere else is hollow
I'm begging for you to take my hand
Wreck my plans
That's my man
Life was a willow and it bent right to your wind (oh)
They count me out time and time again
Life was a willow and it bent right to your wind (oh)
But I come back stronger than a 90's trend
Wait for the signal and I'll meet you after dark
Show me the places where the others gave you scars
Now this is an open-shut case
Guess I should've known from the look on your face
Every bait and switch was a work of art
The more that you say
The less I know
Wherever you stray
I follow
I'm begging for you to take my hand
Wreck my plans
That's my man
You know that my train could take you home
Anywhere else is hollow
I'm begging for you to take my hand
Wreck my plans
That's my man
The more that you say
The less I know
Wherever you stray
I follow
Begging for you to take my hand
Wreck my plans
That's my man
You know that my train could take you home
Anywhere else is hollow
Begging for you to take my hand
Wreck my plans
That's my man
Hey, that's my man
That's my man
Yeah, that's my man
Every bait and switch was a work of art
That's my man
Hey, that's my man
I'm begging for you to take my hand
Wreck my plans
That's my man
champagne problems
You booked the night train for a reason
So you could sit there in this hurt
Bustling crowds or silent sleepers
You're not sure which is worse
Because I dropped your hand while dancing
Left you out there standing
Crestfallen on the landing
Champagne problems
Your mom's ring in your pocket
My picture in your wallet
Your heart was glass, I dropped it
Champagne problems
You told your family for a reason
You couldn't keep it in
Your sister splashed out on the bottle
Now no one's celebrating
Dom Pérignon, you brought it
No crowd of friends applauded
Your hometown skeptics called it
Champagne problems
You had a speech, you're speechless
Love slipped beyond your reaches
And I couldn't give a reason
Champagne problems
Your Midas touch on the Chevy door
November flush and your flannel cure
"This dorm was once a madhouse"
I made a joke, "Well, it's made for me"
How evergreen, our group of friends
Don't think we'll say that word again
And soon they'll have the nerve to deck the halls
That we once walked through
One for the money, two for the show
I never was ready, so I watch you go
Sometimes you just don't know the answer
'Til someone's on their knees and asks you
"She would've made such a lovely bride
What a shame she's fucked in the head, " they said
But you'll find the real thing instead
She'll patch up your tapestry that I shred
And hold your hand while dancing
Never leave you standing
Crestfallen on the landing
With champagne problems
Your mom's ring in your pocket
Her picture in your wallet
You won't remember all my
Champagne problems
You won't remember all my
Champagne problems
gold rush
Gleaming
Twinkling
Eyes like sinking ships
On waters so inviting
I almost jump in
But I don't like a gold rush, gold rush
I don't like anticipating my face in a red flush
I don't like that anyone would die to feel your touch
Everybody wants you
Everybody wonders what it would be like to love you
Walk past, quick brush
I don't like slow motion double vision in rose blush
I don't like that falling feels like flying 'til the bone crush
Everybody wants you
But I don't like a gold rush
What must it be like
To grow up that beautiful?
With your hair falling into place like dominos
I see me padding 'cross your wooden floors
With my Eagles t-shirt hanging from the door
At dinner parties
I call you out on your contrarian shit
And the coastal town
We wandered 'round had never
Seen a love as pure as it
And then it fades into the gray of my day old tea
'Cause you know it could never be
'Cause I don't like a gold rush, gold rush
I don't like anticipating my face in a red flush
I don't like that anyone would die to feel your touch
Everybody wants you
Everybody wonders what it would be like to love you
Walk past, quick brush
I don't like slow motion double vision in rose blush
I don't like that falling feels like flying 'til the bone crush
Everybody wants you
But I don't like a gold rush
What must it be like
To grow up that beautiful?
With your hair falling into place like dominoes
My mind turns your life into folklore
I can't dare to dream about you anymore
At dinner parties
Won't call you out on your contrarian shit
And the coastal town
We never found will never
See a love as pure as it
'Cause it fades into the gray of my day old tea
'Cause it will never be
Gleaming
Twinkling
Eyes like sinking ships
On waters so inviting
I almost jump in
'tis damn season
If I wanted to know who you were hanging with
While I was gone I would have asked you
It's the kind of cold, fogs up windshield glass
But I felt it when I passed you
There's an ache in you put there by the ache in me
But if it's all the same to you
It's the same to me
So we could call it even
You could call me babe for the weekend
'Tis the damn season, write this down
I'm stayin' at my parents' house
And the road not taken looks real good now
And it always leads to you in my hometown
I parkеd my car right between the Methodist
And thе school that used to be ours
The holidays linger like bad perfume
You can run, but only so far
I escaped it too, remember how you watched me leave
But if it's okay with you, it's okay with me
We could call it even
You could call me babe for the weekend
'Tis the damn season, write this down
I'm stayin' at my parents' house
And the road not taken looks real good now
Time flies, messy as the mud on your truck tires
Now I'm missing your smile, hear me out
We could just ride around
And the road not taken looks real good now
And it always leads to you in my hometown
Sleep in half the day just for old times' sake
I won't ask you to wait if you don't ask me to stay
So I'll go back to L.A. and the so-called friends
Who'll write books about me, if I ever make it
And wonder about the only soul who can tell which smiles I'm fakin'
And the heart I know I'm breakin' is my own
To leave the warmest bed I've ever known
We could call it even
Even though I'm leavin'
And I'll be yours for the weekend
'Tis the damn season
We could call it even
You could call me babe for the weekend
'Tis the damn season, write this down
I'm stayin' at my parents' house
And the road not taken looks real good now
Time flies, messy as the mud on your truck tires
Now I'm missing your smile, hear me out
We could just ride around
And the road not taken looks real good now
And it always leads to you in my hometown
It always leads to you in my hometown
tolerate it
I sit and watch you reading with your
Head low
I wake and watch you breathing with your
Eyes closed
I sit and watch you
And notice everything you do or don't do
You're so much older and wiser and I
I wait by the door like I'm just a kid
Use my best colors for your portrait
Lay the table with the fancy shit
And watch you tolerate it
If it's all in my head tell me now
Tell me I've got it wrong somehow
I know my love should be celebrated
But you tolerate it
I greet you with a battle hero's welcome
I take your indiscretions all in good fun
I sit and listen
I polish plates until they gleam and glisten
You're so much older and wiser and I
I wait by the door like I'm just a kid
Use my best colors for your portrait
Lay the table with the fancy shit
And watch you tolerate it
If it's all in my head tell me now
Tell me I've got it wrong somehow
I know my love should be celebrated
But you tolerate it
While you were out building other worlds, where was I?
Where's that man who'd throw blankets over my barbed wire?
I made you my temple, my mural, my sky
Now I'm begging for footnotes in the story of your life
Drawing hearts in the byline
Always taking up too much space or time
You assume I'm fine
But what would you do if I, I
Break free and leave us in ruins
Took this dagger in me and removed it
Gain the weight of you then lose it
Believe me, I could do it
If it's all in my head tell me now
Tell me I've got it wrong somehow
I know my love should be celebrated
But you tolerate it
I sit and watch you
no body, no crime
He did it
He did it
Este's a friend of mine
We meet up every Tuesday night for dinner and a glass of wine
Este's been losing sleep
Her husband's acting different and it smells like infidelity
She says, "That ain't my merlot on his mouth"
"That ain't my jewelry on our joint account"
No, there ain't no doubt
I think I'm gonna call him out
She says
"I think he did it but I just can't prove it"
I think he did it but I just can't prove it
I think he did it but I just can't prove it
No, no body, no crime
But I ain't letting up until the day I die
No, no
I think he did it
No, no
He did it
Este wasn't there
Tuesday night at Olive Garden, at her job, or anywhere
He reports his missing wife
And I noticed when I passed his house his truck has got some brand new tires
And his mistress moved in
Sleeps in Este's bed and everything
No, there ain't no doubt
Somebody's gotta catch him out
'Cause
I think he did it but I just can't prove it (he did it)
I think he did it but I just can't prove it (he did it)
I think he did it but I just can't prove it
No, no body, no crime
But I ain't letting up until the day I die
No, no
I think he did it
No, no
He did it
Good thing my daddy made me get a boating license when I was fifteen
And I've cleaned enough houses to know how to cover up a scene
Good thing Este's sister's gonna swear she was with me ("She was with me dude")
Good thing his mistress took out a big life insurance policy
They think she did it but they just can't prove it
They think she did it but they just can't prove it
She thinks I did it but she just can't prove it
No, no body, no crime
I wasn't letting up until the day he
No, no body, no crime
I wasn't letting up until the day he
No, no body, no crime
I wasn't letting up until the day he died
happiness
Honey, when I'm above the trees
I see this for what it is
But now I'm right down in it
All the years I've given
Is just shit we're dividing up
Showed you all of my hiding spots
I was dancing when the music stopped
And in the disbelief
I can't face reinvention
I haven't met the new me yet
There'll be happiness after you
But there was happiness because of you
Both of these things can be true
There is happiness
Past the blood and bruise
Past the curses and cries
Beyond the terror in the nightfall
Haunted by the look in my eyes
That would've loved you for a lifetime
Leave it all behind
And there is happiness
Tell me, when did your winning smile
Begin to look like a smirk?
When did all our lessons start to look like weapons pointed at my deepest hurt?
I hope she'll be a beautiful fool
Who takes my spot next to you
No, I didn't mean that
Sorry, I can't see facts through all of my fury
You haven't met the new me yet
There'll be happiness after me
But there was happiness because of me
Both of these things I believe
There is happiness
In our history
Across our great divide
There is a glorious sunrise
Dappled with the flickers of light
From the dress I wore at midnight
Leave it all behind
And there is happiness
I can't make it go away by making you a villain
I guess it's the price I pay for seven years in heaven
And I pulled your body into mine every goddamn night now I get fake niceties
No one teaches you what to do
When a good man hurts you
And you know you hurt him too
Honey, when I'm above the trees
I see it for what it is
But now my eyes leak acid rain
On the pillow where you used to lay your head
After giving you the best I had
Tell me what to give after that
All you want from me now
Is the green light of forgiveness
You haven't met the new me yet
And I think she'll give you that
There'll be happiness after you
But there was happiness because of you too
Both of these things can be true
There is happiness
In our history
Across our great divide
There is a glorious sunrise
Dappled with the flickers of light
From the dress I wore at midnight
Leave it all behind
Oh, leave it all behind
Leave it all behind
And there is happiness
dorothea
Hey Dorothea
Do you ever stop and think about me?
When we were younger
Down in the park
Honey, making a lark of the misery
You got shiny friends since you left town
A tiny screen's the only place I see you now
And I got nothing but well wishes for ya
Ooh
This place is the same as it ever was
Ooh
But you don't like it that way
It's never too late
To come back to my side
The stars in your eyes
Shined brighter in Tupelo
And if you're ever tired of being known
For who you know
You know, you'll always know me
Dorothea (ah-ah)
Dorothea (ah-ah)
Ooh, you're a queen
Selling dreams
Selling make up and magazines
Ooh, from you I'd buy anything
Hey Dorothea
Do you ever stop and think about me?
When it was calmer
Skipping the prom
Just to piss off your mom
And her pageant schemes
And damn, Dorothea
They all wanna be ya
But are you still the same soul
I met under the bleachers?
Well
Ooh
I guess I'll never know
Ooh
And you'll go on with the show
But it's never too late
To come back to my side
The stars in your eyes
Shined brighter in Tupelo
And if you're ever tired of being known
For who you know
You know, you'll always know me
Dorothea (ah-ah)
Dorothea (ah-ah)
Ooh
Ooh
Ooh-woo-ooh-ooh, ooh-ooh-ooh
Ooh
Ooh
Ooh-woo-ooh-ooh, ooh-ooh-ooh
Dorothea (ah-ah)
coney island
Break my soul in two
Looking for you but you're right here
If I can't relate to you anymore
Then who am I related to?
And if this is the long haul
How'd we get here so soon?
Did I close my fist around something delicate?
Did I shatter you?
And I'm sitting on a bench in Coney Island wondering where did my baby go?
The fast times, the bright lights, the merry go
Sorry for not making you my centerfold
Over and over
Lost again with no surprises
Disappointments, close your eyes
And it gets colder and colder
When the sun goes down
The question pounds my head
"What's a lifetime of achievement?"
If I pushed you to the edge
But you were too polite to leave me
And do you miss the rogue
Who coaxed you into paradise and left you there?
Will you forgive my soul
When you're too wise to trust me and too old to care?
'Cause we were like the mall before the Internet
It was the one place to be
The mischief, the gift wrapped suburban dreams
Sorry for not winning you an arcade ring
Over and over
Lost again with no surprises
Disappointments, close your eyes
And it gets colder and colder
When the sun goes down
Were you waiting at our old spot
In the tree line by the gold clock
Did I leave you hanging every single day?
Were you standing in the hallway
With a big cake, happy birthday
Did I paint your bluest skies the darkest gray?
A universe away
And when I got into the accident
The sight that flashed before me was your face
But when I walked up to the podium
I think that I forgot to say your name
I'm on a bench in Coney Island wondering where did my baby go?
The fast times, the bright lights, the merry go
Sorry for not making you my centerfold
Over and over
Lost again with no surprises
Disappointments, close your eyes
And it gets colder and colder
When the sun goes down
When the sun goes down
The sight that flashed before me was your face
When the sun goes down
But I think that I forgot to say your name
Over and over
Sorry for not making you my
Making you my
Making you my centerfold
ivy
How's one to know?
I'd meet you where the spirit meets the bones
In a faith forgotten land
In from the snow
Your touch brought forth an incandescent glow
Tarnished but so grand
And the old widow goes to the stone every day
But I don't, I just sit here and wait
Grieving for the living
Oh, goddamn
My pain fits in the palm of your freezing hand
Taking mine, but it's been promised to another
Oh, I can't
Stop you putting roots in my dreamland
My house of stone, your ivy grows
And now I'm covered in you
I wish to know
The fatal flaw that makes you long to be
Magnificently cursed
He's in the room
Your opal eyes are all I wish to see
He wants what's only yours
Oh, goddamn
My pain fits in the palm of your freezing hand
Taking mine, but it's been promised to another
Oh, I can't
Stop you putting roots in my dreamland
My house of stone, your ivy grows
And now I'm covered
Clover blooms in the fields
Spring breaks loose, the time is near
What would he do if he found us out?
Crescent moon, coast is clear
Spring breaks loose, but so does fear
He's gonna burn this house to the ground
How's one to know?
I'd live and die for moments that we stole
On begged and borrowed time
So tell me to run
Or dare to sit and watch what we'll become
And drink my husband's wine
Oh, goddamn
My pain fits in the palm of your freezing hand
Taking mine, but it's been promised to another
Oh, I can't
Stop you putting roots in my dreamland
My house of stone, your ivy grows
And now I'm covered in you
And I'm covered in you
So yeah, it's a fire
It's a goddamn blaze in the dark
And you started it
You started it
So yeah, it's a war
It's the goddamn fight of my life
And you started it
You started it
Oh, I can't
Stop you putting roots in my dreamland
My house of stone, your ivy grows
And now I'm covered
In you
In you, you
Now I'm covered in you
In you
cowboy like me
And the tennis court was covered up
With some tent-like thing
And you asked me to dance
But I said, "Dancing is a dangerous game"
Oh, I thought
This is gonna be one of those things
Now I know
I'm never gonna love again
I've got some tricks up my sleeve
Takes one to know one
You're a cowboy like me
Never wanted love
Just a fancy car
Now I'm waiting by the phone
Like I'm sitting in an airport bar
You had some tricks up your sleeve
Takes one to know one
You're a cowboy like me
Perched in the dark
Telling all the rich folks anything they wanna hear
Like it could be love
I could be the way forward
Only if they pay for it
You're a bandit like me
Eyes full of stars
Hustling for the good life
Never thought I'd meet you here
It could be love
We could be the way forward
And I know I'll pay for it
You're a cowboy like me
Perched in the dark
Telling all the rich folks anything they wanna hear
Like it could be love
I could be the way forward
Only if they pay for it
You're a bandit like me
Eyes full of stars
Hustling for the good life
Never thought I'd meet you here
It could be love
We could be the way forward
And I know I'll pay for it
And the skeletons in both our closets
Plotted hard to fuck this up
And the old men that I've swindled
Really did believe I was the one
And the ladies lunching have their stories about
When you passed through town
But that was all before I locked it down
Now you hang from my lips
Like the Gardens of Babylon
With your boots beneath my bed
Forever is the sweetest con
I've had some tricks up my sleeve
Takes one to know one
You're a cowboy like me
And I'm never gonna love again
I'm never gonna love again
Mm, mm, oh, oh
I'm never gonna love again
long story short
Fatefully
I tried to pick my battles 'til the battle picked me
Misery
Like the war of words I shouted in my sleep
And you passed right by
I was in the alley, surrounded on all sides
The knife cuts both ways
If the shoe fits, walk in it 'til your high heels break
And I fell from the pedestal
Right down the rabbit hole
Long story short, it was a bad time
Pushed from the precipice
Clung to the nearest lips
Long story short, it was the wrong guy
Now I'm all about you
I'm all about you, ah
Yeah, yeah
I'm all about you, ah
Yeah, yeah
Actually
I always felt I must look better in the rear view
Missing me
At the golden gates they once held the keys to
When I dropped my sword
I threw it in the bushes and knocked on your door
And we live in peace
But if someone comes at us
This time, I'm ready
'Cause I fell from the pedestal
Right down the rabbit hole
Long story short, it was a bad time
Pushed from the precipice
Clung to the nearest lips
Long story short, it was the wrong guy
Now I'm all about you
I'm all about you, ah
Yeah, yeah
I'm all about you
No more keepin' score now
I just keep you warm (keep you warm)
No more tug of war now
I just know there's more (know there's more)
No more keepin' score now
I just keep you warm (keep you warm)
And my waves meet your shore
Ever and evermore
Past me
I wanna tell you not to get lost in these petty things
Your nemeses
Will defeat themselves before you get the chance to swing
And he's passing by
Rare as the glimmer of a comet in the sky
And he feels like home
If the shoe fits, walk in it everywhere you go
And I fell from the pedestal
Right down the rabbit hole
Long story short, it was a bad time
Pushed from the precipice
Climbed right back up the cliff
Long story short, I survived
Now I'm all about you (and now)
I'm all about you, ah (and now)
I'm all about you (and now)
I'm all about you, ah
Yeah, yeah
I'm all about you (and now)
Yeah, yeah
I'm all about you
Long story short, it was a bad time
Long story short, I survived
marjorie
Never be so kind, you forget to be clever
Never be so clever, you forget to be kind
And if I didn't know better
I'd think you were talking to me now
If I didn't know better
I'd think you were still around
What died didn't stay dead
What died didn't stay dead
You're alive, you're alive in my head
What died didn't stay dead
What died didn't stay dead
You're alive, so alive
Never be so polite, you forget your power
Never wield such power, you forget to be polite
And if I didn't know better
I'd think you were listening to me now
If I didn't know better
I'd think you were still around
What died didn't stay dead
What died didn't stay dead
You're alive, you're alive in my head
What died didn't stay dead
What died didn't stay dead
You're alive, so alive
The autumn chill that wakes me up
You loved the amber skies so much
Long limbs and frozen swims
You'd always go past where our feet could touch
And I complained the whole way there
The car ride back and up the stairs
I should've asked you questions
I should've asked you how to be
Asked you to write it down for me
Should've kept every grocery store receipt
'Cause every scrap of you would be taken from me
Watched as you signed your name Marjorie
All your closets of backlogged dreams
And how you left them all to me
What died didn't stay dead
What died didn't stay dead
You're alive, you're alive in my head
What died didn't stay dead
What died didn't stay dead
You're alive, so alive
And if I didn't know better
I'd think you were singing to me now
If I didn't know better
I'd think you were still around
I know better
But I still feel you all around
I know better
But you're still around
closure
It's been a long time
And seeing the shape of your name
Still spells out pain
It wasn't right
The way it all went down
Looks like you know that now
Yes, I got your letter
Yes, I'm doing better
It cut deep to know ya
Right to the bone
Yes, I got your letter
Yes, I'm doing better
I know that it's over
I don't need your closure
Your closure
Don't treat me like some situation that needs to be handled
I'm fine with my spite
And my tears
And my beers and my candles
I can feel you smoothing me over
Yes, I got your letter
Yes, I'm doing better
It cut deep to know ya
Right to the bone
Yes, I got your letter
Yes, I'm doing better
I know that it's over
I don't need your closure
Your closure
Your closure
Your closure
I know I'm just a
Wrinkle in your new life
Staying friends
Would iron it out so nice
Guilty, guilty reaching out across the sea
That you put between you and me
But it's fake
And it's oh so unnecessary
Yes, I got your letter
Yes, I'm doing better
It cut deep to know ya
Right to the bone
Yes, I got your letter
Yes, I'm doing better
I know that it's over
I don't need your closure, closure
Your closure
Your closure
evermore
Gray November
I've been down since July
Motion capture
Put me in a bad light
I replay my footsteps on each stepping stone
Trying to find the one where I went wrong
Writing letters
Addressed to the fire
And I was catching my breath
Staring out an open window
Catching my death
And I couldn't be sure
I had a feeling so peculiar
That this pain would be for
Evermore
Hey December
Guess I'm feeling unmoored
Can't remember
What I used to fight for
I rewind the tape but all it does is pause
On the very moment all was lost
Sending signals
To be double crossed
And I was catching my breath
Barefoot in the wildest winter
Catching my death
And I couldn't be sure
I had a feeling so peculiar
That this pain would be for
Evermore
(Evermore)
Can't not think of all the cost
And the things that will be lost
Oh, can we just get a pause?
To be certain we'll be tall again
Whether weather be the frost
Or the violence of the dog days
I'm on waves, out being tossed
Is there a line that I could just go cross?
And when I was shipwrecked (can't think of all the cost)
I thought of you (all the things that will be lost now)
In the cracks of light (can we just get a pause?)
I dreamed of you (to be certain we'll be tall again)
(If you think of all the costs)
It was real enough (whether weather be the frost)
To get me through (or the violence of the dog days)
(Out on waves being tossed)
But I swear (is there a line that we could just go cross?)
You were there
And I was catching my breath
Floors of a cabin creaking under my step
And I couldn't be sure
I had a feeling so peculiar
This pain wouldn't be for
Evermore
Evermore (evermore)
Evermore
This pain wouldn't be for evermore (evermore)
Evermore
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
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='afmhot', mask=circle_mask).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
