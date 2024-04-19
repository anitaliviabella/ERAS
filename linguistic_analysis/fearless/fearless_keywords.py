import spacy
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

nlp = spacy.load("en_core_web_sm") #nlp object that undestands english language.

fearless_lyrics = '''
Fearless
There's somethin' bout the way
The street looks when it's just rained
There's a glow off the pavement
You walk me to the car
And you know I wanna ask you to dance right there
In the middle of the parking lot
Yeah
Oh, yeah
We're drivin' down the road
I wonder if you know
I'm tryin' so hard not to get caught up now
But you're just so cool
Run your hands through your hair
Absent mindedly makin' me want you
And I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why
But with you I'd dance in a storm
In my best dress
Fearless
So baby drive slow
'Til we run out of road in this one horse town
I wanna stay right here in this passenger seat
You put your eyes on me
In this moment now capture it, remember it
'Cause I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why
But with you I'd dance in a storm
In my best dress
Fearless
Oh, oh
Well you stood there with me in the doorway
My hands shake
I'm not usually this way but
You pull me in and I'm a little more brave
It's the first kiss, it's flawless, really something, it's fearless
Oh, yeah
'Cause I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why
But with you I'd dance in a storm
In my best dress
Fearless
'Cause I don't know how it gets better than this
You take my hand and drag me head first
Fearless
And I don't know why
But with you I'd dance in a storm
In my best dress
Fearless
Oh, oh, oh yeah
Fifteen
You take a deep breath
And you walk through the doors
It's the morning of your very first day
You say hi to your friends you ain't seen in awhile
Try and stay out of everybody's way
It's your freshman year
And you're gonna be here for the next four years
In this town
Hoping one of those senior boys
Will wink at you and say
"You know I haven't seen you around, before"
'Cause when you're fifteen
And somebody tells you they love you
You're gonna believe them
And when you're fifteen
Feeling like there's nothing to figure out
Well, count to ten
Take it in
This is life before you know who you're gonna be
At fifteen
You sit in class next to a red-head named Abigail
And soon enough you're best friends
Laughing at the other girls
Who think they're so cool
We'll be out of here as soon as we can
And then you're on your very first date
And he's got a car
And you're feeling like flying
And your mama's waiting up
And you're thinking he's the one
And you're dancing 'round your room when the night ends
When the night ends
'Cause when you're fifteen
And somebody tells you they love you
You're gonna believe them
And when you're fifteen
And your first kiss makes your head spin around
Well, in your life you'll do things
Greater than dating the boy on the football team
I didn't know it at fifteen
When all you wanted
Was to be wanted
Wish you could go back
And tell yourself what you know now
Back then I swore I was gonna marry him someday
But I realized some bigger dreams of mine
And Abigail gave everything she had
To a boy who changed his mind
And we both cried
'Cause when you're fifteen
And somebody tells you they love you
You're gonna believe them
And when you're fifteen
Don't forget to look before you fall
But I've found time can heal most anything
And you just might find who you're supposed to be
I didn't know who I was supposed to be
At fifteen
La-la la-la la-la-la-la
La-la la-la la-la-la-la
La-la la-la
Your very first day
Take a deep breath girl
Take a deep breath as you walk through the doors
Love story
We were both young when I first saw you
I close my eyes and the flashback starts
I'm standin' there
On a balcony in summer air
See the lights, see the party, the ball gowns
See you make your way through the crowd
And say, "Hello"
Little did I know
That you were Romeo, you were throwin' pebbles
And my daddy said, "Stay away from Juliet"
And I was cryin' on the staircase
Beggin' you, "Please don't go, " and I said
Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story, baby, just say, "Yes"
So I sneak out to the garden to see you
We keep quiet, 'cause we're dead if they knew
So close your eyes
Escape this town for a little while, oh oh
'Cause you were Romeo, I was a scarlet letter
And my daddy said, "Stay away from Juliet"
But you were everything to me
I was beggin' you, "Please don't go, " and I said
Romeo, take me somewhere we can be alone
I'll be waiting, all there's left to do is run
You'll be the prince and I'll be the princess
It's a love story, baby, just say, "Yes"
Romeo, save me, they're tryna tell me how to feel
This love is difficult, but it's real
Don't be afraid, we'll make it out of this mess
It's a love story, baby, just say, "Yes"
Oh, oh
I got tired of waiting
Wonderin' if you were ever comin' around
My faith in you was fading
When I met you on the outskirts of town, and I said
Romeo, save me, I've been feeling so alone
I keep waiting for you, but you never come
Is this in my head? I don't know what to think
He knelt to the ground and pulled out a ring
And said, "Marry me, Juliet
You'll never have to be alone
I love you and that's all I really know
I talked to your dad, go pick out a white dress
It's a love story, baby, just say, "Yes"
Oh, oh, oh
Oh, oh, oh, oh
'Cause we were both young when I first saw you
Hey Stephen
Mmm-mm, mm-mm, mm-mm
Mmm-mm, mm-mm
Mmm-mm, mm-mm, mm-mm
Mmm-mm, yeah
Hey Stephen, I know looks can be deceiving
But I know I saw a light in you
And as we walked we would talk
And I didn't say half the things I wanted to
Of all the girls tossing rocks at your window
I'll be the one waiting there even when it's cold
Hey Stephen, boy, you might have me believing
I don't always have to be alone
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain, so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
Hey Stephen, I've been holding back this feeling
So I've got some things to say to you (ha)
I've seen it all, so I thought
But I never seen nobody shine the way you do
The way you walk, way you talk, way you say my name
It's beautiful, wonderful, don't you ever change
Hey Stephen, why are people always leaving?
I think you and I should stay the same
'Cause I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain, so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
They're dimming the street lights
You're perfect for me
Why aren't you here tonight?
I'm waiting alone now
So come on and come out
And pull me near
And shine, shine, shine
Hey Stephen, I could give you 50 reasons
Why I should be the one you choose
All those other girls, well, they're beautiful
But would they write a song for you? (Ha-ha)
I can't help it if you look like an angel
Can't help it if I wanna kiss you in the rain, so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm, I can't help myself
If you look like an angel
Can't help it if I wanna kiss you in the rain, so
Come feel this magic I've been feeling since I met you
Can't help it if there's no one else
Mmm I can't help myself
Myself
Can't help myself, I can't help myself
Oh, oh, oh
Mmm-mm, mm-mm, mm-mm
Mmm-mm, mm-mm
Mmm-mm, mm-mm, mm-mm
Mmm-mm, mm-mm
Mm-mm
White horse
Say you're sorry, that face of an angel
Comes out just when you need it to
As I paced back and forth all this time
'Cause I honestly believed in you
Holdin' on, the days drag on
Stupid girl, I should've known, I should've known
That I'm not a princess, this ain't a fairy tale
I'm not the one you'll sweep off her feet
Lead her up the stairwell
This ain't Hollywood, this is a small town
I was a dreamer before you went and let me down
Now it's too late for you and your white horse
To come around
Maybe I was naive, got lost in your eyes
And never really had a chance
My mistake, I didn't know to be in love
You had to fight to have the upper hand
I had so many dreams about you and me
Happy endings, now I know
I'm not a princess, this ain't a fairy tale
I'm not the one you'll sweep off her feet
Lead her up the stairwell
This ain't Hollywood, this is a small town
I was a dreamer before you went and let me down
Now it's too late for you and your white horse
To come around
And there you are on your knees
Begging for forgiveness, begging for me
Just like I always wanted but I'm so sorry
'Cause I'm not your princess, this ain't a fairytale
I'm gonna find someone someday
Who might actually treat me well
This is a big world, that was a small town
There in my rear-view mirror disappearing now
And it's too late for you and your white horse
Now it's too late for you and your white horse
To catch me now
Oh, whoa, whoa, whoa
Try and catch me now, oh
It's too late
To catch me now
You belong with me
You're on the phone with your girlfriend, she's upset
She's going off about something that you said
'Cause she doesn't get your humor like I do
I'm in the room, it's a typical Tuesday night
I'm listening to the kind of music she doesn't like
And she'll never know your story like I do
But she wears short skirts
I wear T-shirts
She's Cheer Captain, and I'm on the bleachers
Dreaming about the day when you wake up and find
That what you're looking for has been here the whole time
If you could see that I'm the one
Who understands you
Been here all along
So, why can't you see?
You belong with me
You belong with me
Walk in the streets with you in your worn-out jeans
I can't help thinking this is how it ought to be
Laughing on a park bench thinking to myself
Hey, isn't this easy?
And you've got a smile
That can light up this whole town
I haven't seen it in a while
Since she brought you down
You say you're fine, I know you better than that
Hey, what you doing with a girl like that?
She wears high heels
I wear sneakers
She's Cheer Captain, and I'm on the bleachers
Dreaming about the day when you wake up and find
That what you're looking for has been here the whole time
If you could see that I'm the one
Who understands you
Been here all along
So, why can't you see?
You belong with me
Standing by and waiting at your backdoor
All this time how could you not know, baby?
You belong with me
You belong with me
Oh, I remember you driving to my house
In the middle of the night
I'm the one who makes you laugh
When you know you're 'bout to cry
And I know your favorite songs
And you tell me 'bout your dreams
Think I know where you belong
Think I know it's with me
Can't you see that I'm the one
Who understands you?
Been here all along
So, why can't you see?
You belong with me
Standing by and waiting at your backdoor
All this time how could you not know, baby?
You belong with me
You belong with me
You belong with me
Have you ever thought just maybe
You belong with me?
You belong with me
Breathe
I see your face in my mind as I drive away,
'Cause none of us thought it was gonna end that way
People are people,
And sometimes we change our minds
But it's killing me to see you go after all this time
Music starts playin' like the end of a sad movie,
It's the kinda ending you don't really wanna see
'Cause it's tragedy and it'll only bring you down,
Now I don't know what to be without you around
And we know it's never simple,
Never easy
Never a clean break, no one here to save me
You're the only thing I know like the back of my hand,
And I can't,
Breathe,
Without you,
But I have to,
Breathe,
Without you,
But I have to
Never wanted this, never wanna see you hurt
Every little bump in the road I tried to swerve
People are people,
And sometimes it doesn't work out,
Nothing we say is gonna save us from the fall out
And we know it's never simple,
Never easy
Never a clean break, no one here to save me
You're the only thing I know like the back of my hand,
And I can't,
Breathe,
Without you,
But I have to,
Breathe,
Without you,
But I have to
It's two am
Feelin' like I just lost a friend
Hope you know it's not easy,
Easy for me
It's two am
Feelin' like I just lost a friend
Hope you know this ain't easy,
Easy for me
And we know it's never simple,
Never easy
Never a clean break, no one here to save me
I can't,
Breathe,
Without you,
But I have to,
Breathe,
Without you,
But I have to
Breathe,
Without you,
But I have to
Sorry (oh) sorry
Sorry sorry
Sorry sorry
Tell me why
I took a chance, I took a shot
And you might think I'm bulletproof, but I'm not
You took a swing, I took it hard
And down here from the ground, I see who you are
I'm sick and tired of your attitude
I'm feeling like I don't know you
You tell me that you love me, then you cut me down
And I need you like a heartbeat
But you know you got a mean streak
Makes me run for cover when you're around
And here's to you and your temper
Yes, I remember what you said last night
And I know that you see what you're doing to me
Tell me why
You could write a book on
How to ruin someone's perfect day
Well, I get so confused and frustrated
Forget what I'm trying to say, oh
I'm sick and tired of your reasons
I got no one to believe in
You tell me that you want me, then push me around
And I need you like a heartbeat
But you know you got a mean streak
Makes me run for cover when you're around
Here's to you and your temper
Yes, I remember what you said last night
And I know that you see what you're doing to me
Tell me why
Why do you have to make me feel small
So you can feel whole inside?
Why do you have to put down my dreams
So you're the only thing on my mind?
When I'm sick and tired of your attitude
I'm feeling like I don't know you
You tell me that you want me, then cut me down
I'm sick and tired of your reasons
I've got no one to believe in
You ask me for my love, then you push me around
Here's to you and your temper
Yes, I remember what you said last night
And I know that you see what you're doing to me
Tell me why, why?
Tell me why
I take a step back, let you go
I told you I'm not bulletproof
Now you know
You're not sorry
All this time I was wasting
Hoping you would come around
I've been giving out chances every time
And all you do is let me down
And it's taking me this long
Baby but I figured you out
And you're thinking we'll be fine again
But not this time around
You don't have to call anymore
I won't pick up the phone
This is the last straw
Don't wanna hurt anymore
And you can tell me that you're sorry
But I don't believe you baby
Like I did before
You're not sorry, no no, no no
Looking so innocent
I might believe you if I didn't know
Could've loved you all my life
If you hadn't left me waiting in the cold
And you got your share of secrets
And I'm tired of being last to know
And now you're asking me to listen
Cause it's worked each time before
But you don't have to call anymore
I won't pick up the phone
This is the last straw
Don't wanna hurt anymore
And you can tell me that you're sorry
But I don't believe you baby
Like I did before
You're not sorry, no no
You're not sorry, no no
You had me crawling for you honey
And it never would've gone away, no
You used to shine so bright
But I watched all of it fade
You don't have to call anymore
I won't pick up the phone
This is the last straw there's nothing left to beg for
And you can tell me that you're sorry
But I don't believe you baby
Like I did before you're not sorry
No, no, no
You're not sorry, no no (no)
The way I loved you
He is sensible and so incredible
And all my single friends are jealous
He says everything I need to hear, and it's like
I couldn't ask for anything better
He opens up my door and I get into his car
And he says, "You look beautiful tonight"
And I feel perfectly fine
But I miss screaming and fighting and kissing in the rain
And it's 2 a.m. and I'm cursing your name
So in love that you act insane
And that's the way I loved you
Breaking down and coming undone
It's a roller coaster kind of rush
And I never knew I could feel that much
And that's the way I loved you
He respects my space
And never makes me wait
And he calls exactly when he says he will
He's close to my mother
Talks business with my father
He's charming and endearing
And I'm comfortable
But I miss screaming and fighting and kissing in the rain
And It's 2 a.m. and I'm cursing your name
You're so in love that you act insane
And that's the way I loved you
Breaking down and coming undone
It's a roller coaster kind of rush
And I never knew I could feel that much
And that's the way I loved you
He can't see the smile I'm faking
And my heart's not breaking
'Cause I'm not feeling anything at all
And you were wild and crazy
Just so frustrating, intoxicating, complicated
Got away by some mistake and now
I miss screaming and fighting and kissing in the rain
It's 2 a.m. and I'm cursing your name
I'm so in love that I acted insane
And that's the way I loved you
Breaking down and coming undone
It's a roller coaster kind of rush
And I never knew I could feel that much
And that's the way I loved you
Whoa-whoa-oh-oh, oh
And that's the way I loved you
Oh-oh-oh-oh, oh-oh-oh-oh
Never knew I could feel that much
And that's the way I loved you
Forever and always
Once upon a time, I believe it was a Tuesday when I caught your eye
And we caught onto something
I hold onto the night, you looked me in the eye and told me you loved me
Were you just kidding?
'Cause it seems to me, this thing is breaking down
We almost never speak
I don't feel welcome anymore
Baby what happened? Please tell me
'Cause one second it was perfect, now you're halfway out the door
And I stare at the phone, he still hasn't called
And then you feel so low you cant feel nothing at all
And you flashback to when he said, "Forever and always"
Oh, and it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said, "Forever and always"
Was I out of line?
Did I say something way too honest, made you run and hide
Like a scared little boy
I looked into your eyes
Thought I knew you for a minute, now I'm not so sure
So here's to everything coming down to nothing
Here's to silence, that cuts me to the core
Where is this going? Thought I knew for a minute, but I don't anymore
And I stare at the phone, he still hasn't called
And then you feel so low you cant feel nothing at all
And you flashback to when he said, "Forever and always"
Oh, and it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said, "Forever and always"
You didn't mean it baby, I don't think so
Oh back up, baby, back up
Did you forget everything?
Back up, baby, back up
Did you forget everything?
'Cause it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said, "Forever and always"
Oh, I stare at the phone, he still hasn't called
And then you feel so low you cant feel nothing at all
And you flashback to when we said, "Forever and always"
And it rains in your bedroom
Everything is wrong
It rains when you're here and it rains when you're gone
'Cause I was there when you said, "Forever and always"
You didn't mean it baby,
You said, "Forever and always", yeah.
The best day
I'm five years old
It's getting cold
I've got my big coat on
I hear your laugh
And look up smiling at you
I run and run
Past the pumpkin patch
And the tractor rides
Look now, the sky is gold
I hug your legs
And fall asleep on the way home
I don't know why all the trees change in the fall
But I know you're not scared of anything at all
Don't know if Snow White's house is near or far away
But I know I had the best day with you today
I'm thirteen now
And don't know how
My friends could be so mean
I come home crying
And you hold me tight
And grab the keys
And we drive and drive
Until we found a town far enough away
And we talk and window shop
'Till I forgotten all their names
I don't know who I'm gonna talk to now at school
But I know I'm laughing
On the car ride home with you
Don't know how long it's gonna take to feel okay
But I know I had the best day with you today
I have an excellent father
His strength is making me stronger
God smiles on my little brother
Inside and out he's better than I am
I grew up in a pretty house
And I had space to run and I
had the best days with you
There is a video I found
From back when I was three
You set up a paint set in the kitchen
And you're talking to me
It's the age of princesses and pirate ships
And the seven dwarfs
And Daddy's smart
And you're the prettiest lady in the whole wide world
And now I know why the all the trees change in the fall
I know you were on my side
Even when I was wrong
And I love you for giving me your eyes
Staying back and watching me shine and
I didn't know if you knew
So I'm taking this chance to say
That I had the best day with you today
Change
And it's a sad picture, the final blow hits you
Somebody else gets what you wanted again and
You know it's all the same, another time and place
Repeating history and you're getting sick of it
But I believe in whatever you do
And I'll do anything to see it through
Because these things will change
Can you feel it now?
These walls that they put up to hold us back will fall down
It's a revolution, the time will come
For us to finally win
And we'll sing hallelujah, we'll sing hallelujah
So we've been outnumbered
Raided and now cornered
It's hard to fight when the fight ain't fair
We're getting stronger now
Find things they never found
They might be bigger
But we're faster and never scared
You can walk away, say we don't need this
But there's something in your eyes
Says we can beat this
Because these things will change
Can you feel it now?
These walls that they put up to hold us back will fall down
It's a revolution, the time will come
For us to finally win
And we'll sing hallelujah, we'll sing hallelujah
Tonight we'll stand, get off our knees
Fight for what we've worked for all these years
And the battle was long, it's the fight of our lives
But we'll stand up champions tonight
It was the night things changed
Can you see it now?
These walls that they put up to hold us back fell down
It's a revolution, throw your hands up
'Cause we never gave in
And we'll sing hallelujah, we sang hallelujah
Hallelujah
Jump then fall
I like the way you sound in the mornin'
We're on the phone and without a warnin'
I realize your laugh is the best sound I have ever heard
I like the way I can't keep my focus
I watch you talk, you didn't notice
I hear the words but all I can think is we should be together
Every time you smile, I smile
And every time you shine, I'll shine for you
Whoa-oh, I'm feelin' you, baby
Don't be afraid to jump then fall
Jump then fall into me
Baby, I'm never gonna leave you
Say that you wanna be with me too
So I'ma stay through it all
So jump then fall
Well, I like the way your hair falls in your face
You got the keys to me, I love each freckle on your face
Oh, I've never been so wrapped up, honey
I like the way you're everything I ever wanted
I had time to think it oh, over
And all I can say is come closer
Take a deep breath and jump then fall into me
'Cause every time you smile, I smile
And every time you shine, I'll shine for you
Whoa-oh, I'm feeling you, baby
Don't be afraid to jump then fall
Jump then fall into me
Baby, I'm never gonna leave you
Say that you wanna be with me too
So I'ma stay through it all
So jump then fall
The bottom's gonna drop out from under our feet
I'll catch you, I'll catch you
When people say things that bring you to your knees
I'll catch you
The time is gonna come when you're so mad, you could cry
But I'll hold you through the night until you smile
Whoa-oh, I need you, baby
Don't be afraid, please, jump then fall
Jump then fall into me
Baby, I'm never gonna leave you
Say that you wanna be with me too
So I'ma stay through it all
So jump then fall
Jump then fall, baby
Jump then fall into me, into me
Every time you smile, I smile
And every time you shine, I'll shine
And everytime you're here
Baby, I'll show you, I'll show you
You can jump then fall
Jump then fall
Jump then fall into me
Into me, yeah
Untouchable
Where the moon glows in your hair 
and the rain falls down 
on a ground that’s cold and bare
dripping from the clouds
where I sing because I care
till my lungs fall out 
I’m asleep but well aware
that the word is out
 
There's a love and a sense of direction
in the matter that keeps us apart
there’s a light coming out of the woodworks  
from a crack in the door to my heart
cause the summer is taking forever
cause I can’t take the heat anymore
cause I know that for worse or for better
I’m at war with the one that I want
A tree falls down
almost unintentional
the earth starts burning 
with no one around
I hear you say
it's not too late
and we become
brave and untouchable
Until the daylight comes around
and the morning breaks
in the centre of this town
I’ll be wide awake
I’ll be out drifting about
with a heart that aches
and a head that’s spinning round
from the sound that it makes
Cause I feel like I’m walking a rainbow
cause I don’t know where I do belong 
cause there’s no one above or beside you 
because you have been crying too long 
I’ve been climbing the walls of the city
on the run from the things that I miss
I’ve been drying my eyes to see clearly
cause I know that there’s so much more than this 
A tree falls down
almost unintentional
the earth starts burning 
with no one around
I hear you say
it's not too late
and we become
brave and untouchable
A tree falls down
almost unintentional
the earth starts burning 
with no one around
I hear you say
it's not too late
and we become
brave and untouchable
Come in with the rain
I could go back to every laugh
But I don't wanna go there anymore
And I know all the steps up to your door
But I don't wanna go there anymore
Talk to the wind, talk to the sky
Talk to the man with the reasons why
And let me know what you find
I'll leave my window open
'Cause I'm too tired at night to call your name
Just know I'm right here hoping
That you'll come in with the rain
I could stand up and sing you a song
But I don't wanna have to go that far
And I, I've got you down, I know you by heart
And you don't even know where I start
Talk to yourself, talk to the tears
Talk to the man who put you here
And don't wait for the sky to clear
I'll leave my window open
'Cause I'm too tired at night to call your name, oh
Just know I'm right here hoping
That you'll come in with the rain
I've watched you so long, screamed your name
I don't know what else I can say
I'll leave my window open
'Cause I'm too tired at night for all these games
Just know I'm right here hoping
That you'll come in with the rain
I could go back to every laugh
But I don't wanna go there anymore
Superstar
This is wrong, but I can't help but feel like
There ain't nothing more right, babe
Misty morning comes again and I can't
Help but wish I could see your face
I knew from the first note played
I'd be breaking all my rules to see you
You smile that beautiful smile
And all the girls in the front row scream your name
So dim that spotlight, tell me things like
"I can't keep my eyes off of you"
I'm no one special, just another wide-eyed girl
Who's desperately in love with you
Give me a photograph to hang on my wall
Superstar
Morning loneliness comes around
When I'm not dreaming about you
When my world wakes up today
You'll be in another town
And I knew when I saw your face
I'd be counting down the ways to see you
And you smile that beautiful smile
And all the girls in the front row scream your name
So dim that spotlight, tell me things like
"I can't take my eyes off of you"
I'm no one special, just another wide-eyed girl
Who's desperately in love with you
Give me a photograph to hang on my wall
Superstar
You played in bars, you play guitar
I'm invisible and everyone knows who you are
And you'll never see, you sing me to sleep
Every night from the radio
So dim that spotlight, tell me things like
"I can't take my eyes off of you"
I'm no one special, just another wide-eyed girl
Who's desperately in love with you
Give me a photograph to hang on my wall
Superstar
Sweet, sweet superstar
Superstar
The other side of the door
In the heat of the fight, I walked away
Ignoring words that you were saying, trying to make me stay
I said, "This time I've had enough"
And you've called a hundred times, but I'm not pickin' up
'Cause I'm so mad, I might tell you that it's over
But if you look a little closer
I said, "Leave", but all I really want is you
To stand outside my window, throwing pebbles
Screaming, "I'm in love with you"
Wait there in the pourin' rain, come back for more
And don't you leave, 'cause I know
All I need is on the other side of the door
Me and my stupid pride, sittin' here alone
Going through the photographs, staring at the phone
I keep going back over the things we both said
And I remember the slammin' door and all the things that I misread
So, babe, if you know everything, tell me, why you couldn't see
That when I left, I wanted you to chase after me? Yeah
I said, "Leave", but all I really want is you
To stand outside my window, throwing pebbles
Screaming, "I'm in love with you"
Wait there in the pourin' rain, come back for more
And don't you leave, 'cause I know
All I need is on the other side of the door
And I scream out the window, I can't even look at you
I don't need you, but I do, I do, I do
I said, "There's nothing you can say to make this right again
I mean it, I mean it, " but what I mean is
I said, "Leave", but, baby, all I want is you
To stand outside my window, throwing pebbles
Screaming, "I'm in love with you"
Wait there in the pourin' rain, come back for more
And don't you leave, 'cause I know
All I need is on the other side of the door
With your face and the beautiful eyes
And the conversation with the little white lies
And the faded picture of a beautiful night
You carry me from your car up the stairs
And I broke down cryin', was she worth this mess?
After everything and that little black dress
After everything, I must confess I need you
Today was a fairytale
Today was a fairytale, you were the prince
I used to be a damsel in destress
You took me by the hand and you pick me up at six
Today was a fairytale
Today was a fairytale
Today was a fairytale, I wore a dress
You wore a dark gray T-shirt
You told me I was pretty when I looked like a mess
Today was a fairytale
Time slows down
Whenever you're around
But can you feel this magic in the air?
It must've been the way you kissed me
Fell in love when I saw you standing there
It must've been the way, today was a fairytale
It must've been the way, today was a fairytale
Today was a fairytale, you got a smile, takes me to another planet
Every move you make, everything you said is right
Today was a fairytale
Today was a fairytale, all that I can say, is now it's gettin' so much clearer
Nothing made sense till the time I saw your face
Today was a fairytale
Time slows down
Whenever you're around, yeah
But can you feel this magic in the air?
It must've been the way you kissed me
Fell in love when I saw you standing there
It must've been the way, today was a fairytale
It must've been the way, today was a fairytale
Time slows down, whenever you're around
I can feel my heart, it's beating in my chest
Did you feel it?
I can't put this down
But can you feel this magic in the air?
It must've been the way you kissed me
Fell in love when I saw you standing there
It must've been the way
But can you feel this magic in the air?
It must've been the way you kissed me
Fell in love when I saw you standing there
It must've been the way, today was a fairytale
It must've been the way, today was a fairytale
Oh-oh, oh-oh
Yeah, oh
Today was a fairytale
You all over me
Once the last drop of rain has dried off the pavement
Shouldn't I find a stain, but I never do
The way the tires turn stones, on old county roads
They leave 'em muddy underneath
Reminds me of you
You find graffiti on the walls of old bathroom stalls
You know, you can scratch it right off
It's how it used to be
But like the dollar in your pocket, it's been spent and traded in
You can't change where it's been
Reminds me of me
I lived, and I learned
Had you, got burned
Held out, and held on
God knows, too long
And wasted time, lost tears
Swore that I'd get out of here
But no amount of freedom gets you clean
I've still got you all over me
The best and worst day of June
Was the one that I met you
With your hands in your pockets
And your 'don't you wish you had me' grin
But I did, so I smiled, and I melted like a child
Now every breath of air I breathe reminds me of then
And I lived, and I learned
Had you, got burned
Held out, and held on
God knows, too long
And wasted time, lost tears
Swore that I'd get out of here
But no amount of freedom gets you clean
I've still got you all over me
I lived, and I learned
And found out what it was to turn around
And see, that we
Were never really meant to be
So I lied, and I cried
And I watched a part of myself die
'Cause no amount of freedom gets you clean
I've still got you all over me
I've still got you all over me
Still got you all over me
Mr. Perfectly fine
Mr. "Perfect face"
Mr. "Here to stay"
Mr. "Looked me in the eye and told me you would never go away"
Everything was right
Mr. "I've been waiting for you all my life"
Mr. "Every single day until the end, I will be by your side"
But that was when I got to know Mr. "Change of heart"
Mr. "Leaves me all alone, " I fall apart
It takes everything in me just to get up each day
But it's wonderful to see that you're okay
Hello Mr. "Perfectly fine"
How's your heart after breaking mine?
Mr. "Always at the right place at the right time, " baby
Hello Mr. "Casually cruel"
Mr. "Everything revolves around you"
I've been Miss "Misery" since your goodbye
And you're Mr. "Perfectly fine"
Mr. "Never told me why"
Mr. "Never had to see me cry"
Mr. "Insincere apology so he doesn't look like the bad guy"
He goes about his day
Forgets he ever even heard my name
Well, I thought you might be different than the rest
I guess you're all the same
'Cause I hear he's got his arm 'round a brand-new girl
I've been pickin' up my heart, he's been pickin' up her
And I never got past what you put me through
But it's wonderful to see that it never phased you
Hello Mr. "Perfectly fine"
How's your heart after breakin' mine?
Mr. "Always at the right place at the right time, " baby
Hello Mr. "Casually cruel"
Mr. "Everything revolves around you"
I've been Miss "Misery" since your goodbye
And you're Mr. "Perfectly fine"
So dignified in your well-pressed suit
So strategized, all the eyes on you
Sashay away to your seat
It's the best seat, in the best room
Oh, he's so smug, Mr. "Always wins"
So far above me in every sense
So far above feeling anything
And it's really such a shame
It's such a shame
'Cause I was Miss "Here to stay"
Now I'm Miss "Gonna be alright someday"
And someday maybe you'll miss me
But by then, you'll be Mr. "Too late"
Goodbye Mr. "Perfectly fine"
How's your heart after breakin' mine?
Mr. "Always at the right place at the right time, " baby
Goodbye Mr. "Casually cruel"
Mr. "Everything revolves around you"
I've been Miss "Misery" for the last time
And you're Mr. "Perfectly fine"
You're perfectly fine
Mr. "Look me in the eye and told me you would never go away"
You said you'd never go away
We were happy 
We used to walk along the streets
When the porch lights were shinin' bright
Before I had somewhere to be
Back when we had all night
And we were happy
I do recall a good while back
We snuck into the circus
You threw your arms around my neck
Back when I deserved it
And we were happy
When it was good, baby, it was good, baby
We showed 'em all up
No one could touch the way we laughed in the dark
Talkin' 'bout your daddy's farm we were gonna buy someday
And we were happy
We used to watch the sun go down
On the boats in the water
That's sorta how I feel right now
And goodbye's so much harder
'Cause we were happy
When it was good, baby, it was good, baby
We showed 'em all up
No one could touch the way we laughed in the dark
Talkin' 'bout your daddy's farm we were gonna buy someday
And we were happy
We were happy
Oh, I hate those voices
Tellin' me I'm not in love anymore
But they don't give me choices
And that's what these tears are for
'Cause we were happy
We were happy
When it was good, baby, it was good, baby
We showed 'em all up
No one could touch the way we laughed in the dark
Talkin' 'bout your daddy's farm
And you were gonna marry me
And we were happy
We were happy
Oh
We were happy
That's when 
You said, "I know"
When I said, "I need some time, need some space
To think about all of this"
You watched me go
And I knew my words were hard to hear
And harder to ever take back
And I said, "When can I come back?"
And you said, that's when, when I wake up in the mornin'
That's when, when it's sunny or stormin'
Laughin' when I'm cryin'
And that's when I'll be waitin' at the front gate
That's when, when I see your face
I'll let you in, and baby that's when
Mm-mm
I said, "I know"
When you said, "I did you wrong, made mistakes
And put you through all of this" (through all of this)
Then through the phone
Came all your tears
And I said "Leave those all in our past"
And you said "When can I come back?"
And I said, that's when, when I wake up in the mornin'
That's when, when it's sunny or stormin'
Laughin' when I'm cryin'
And that's when I'll be waitin' at the front gate
That's when, when I see your face
I'll let you in, and baby that's when
And you said, "Honestly
When you were gone, did you ever think of me?"
And I said, that's when, when I woke up in the mornin'
That's when it was sunny or stormin'
Laughin' when I was cryin'
And that's when you were waitin' at the front gate
That's when, when I saw your face
You let me in, and baby that's when
yeah
(That's when it was sunny or stormin')
When I'm laughin', when I'm cryin'
(That's when I'll be waitin' at the front gate) that's when I miss you
(That's when, when I see your face)
That's when I want you
That's when I love you
That's when
Don't you
Hey, I knew I'd run into you somewhere
It's been a while, I didn't mean to stare
I heard she's nothin' like me
I'm sure she'll make you happy
But don't you
Don't you smile at me and ask me how I've been
Don't you say you've missed me if you don't want me again
You don't know how much I feel I love you still
So why don't you, don't you?
Ah, ah, ah, ah, ah, ah, ah
Sometimes I really wish that I could hate you
I've tried, but that's just somethin' I can't do
My heart knows what the truth is
I swore I wouldn't do this
But don't you
Don't you smile at me and ask me how I've been
Don't you say you've missed me if you don't want me again
You don't know how much I feel I love you still
So why don't you, don't you?
So I walk outta here tonight
Try to go on with my life
And you can say we're still friends
(But I don't wanna pretend)
So if I see you again
Don't you (don't you)
Don't you smile at me and ask me how I've been
Don't you (don't you), say you've missed me if you don't want me again
You don't (you don't), know how much I feel I love you still
So why don't you, don't you?
Ah, ah, ah, ah
Don't you, ah, ah, ah
Bye bye baby
It wasn't just like a movie
The rain didn't soak through my clothes, down to my skin
I'm driving away and I, I guess you could say
This is the last time I'll drive this way again
Lost in the gray and I try to grab at the fray
'Cause I, I still love you but I can't
Bye, bye, to everything I thought was on my side
Bye, bye, baby
I want you bad but it's come down to nothing
And all I have is your sympathy
'Cause you took me home but you just couldn't keep me
Bye, bye, baby
Bye, bye, baby
The picture frame is empty
On the dresser, vacant just like me
I see your writing on the dash
Then back to your hesitation
I was so sure of everything
Everything I thought we'd always have
Guess I never doubted it
Then the here and the now floods in
Feels like I'm becoming a part of your past
Bye, bye, to everything I thought was on my side
Bye, bye, baby
I want you bad but it's come down to nothing
And all I have is your sympathy
'Cause you took me home but you just couldn't keep me
Bye, bye, baby
There's so much that I can't touch
You're all I want but it's not enough this time
And all the pages are just slipping through my hands
And I'm so scared of how this ends
Bye, bye, to everything I thought was on my side
Bye, bye, baby
I want you bad but it's come down to nothing
And all I have is your sympathy
'Cause you took me home but you just couldn't keep me
Bye, bye, to everything I thought was on my side
Bye, bye, baby
I want you bad but it's come down to nothing
And all I have is your sympathy
'Cause you took me home but you just couldn't keep me
Oh, you took me home, I thought you were gonna keep me
Bye, bye, baby
Bye, bye, baby
'''
# Process the lyrics text
doc = nlp(fearless_lyrics)

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
wordcloud = WordCloud(width=800, height=800, background_color='white', colormap='copper', mask=circle_mask).generate_from_frequencies(word_freq)

# Display the word cloud using matplotlib
plt.figure(figsize=(8, 8))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
