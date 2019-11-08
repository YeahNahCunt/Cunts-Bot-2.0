import asyncio
import random
import aiohttp
from io import BytesIO
from random import choice
import urllib.parse
from urllib.parse import quote
import discord
import requests
from discord import Game
from discord.ext import commands
from PIL import Image

####INSULTS##### add insults to a json file later

insults = [
    ("Yo Mama so dumb I told her Christmas was around the corner and she went looking for it."),
    ("You're so dumb it took you 2 hours to watch 60 minutes."),
    ("Yo Mama so dumb she bought tickets to Xbox Live."),
    ("You're so dumb that you thought The Exorcist was a workout video."),
    ("You're so ugly that you went to the salon and it took 3 hours just to get an estimate."),
    ("You're so ugly that even Scooby Doo couldn't solve that mystery."),
    ("What is the weighted center between Planet X and Planet Y? Oh it's YOU!"),
    (":eggplant: :eggplant: :eggplant:"),
    ("Your birth certificate is an apology letter from the condom factory."),
    ("I wasn't born with enough middle fingers to let you know how I feel about you."),
    ("You must have been born on a highway because that's where most accidents happen."),
    ("I'm jealous of all the people that haven't met you."),
    ("I bet your brain feels as good as new, seeing that you never use it."),
    ("I'm not saying I hate you, but I would unplug your life support to charge my phone."),
    ("You're so ugly, when your mom dropped you off at school she got a fine for littering."),
    ("You bring everyone a lot of joy, when you leave the room."),
    ("What's the difference between you and eggs? Eggs get laid and you don't."),
    ("You're as bright as a black hole, and twice as dense."),
    ("I tried to see things from your perspective, but I couldn't seem to shove my head that far up my ass."),
    ("Two wrongs don't make a right, take your parents as an example."),
    ("You're the reason the gene pool needs a lifeguard."),
    ("If laughter is the best medicine, your face must be curing the world."),
    ("You're so ugly, when you popped out the doctor said \"Aww what a treasure\" and your mom said \"Yeah, lets bury it.\""),
    ("I have neither the time nor the crayons to explain this to you."),
    ("You have two brains cells, one is lost and the other is out looking for it."),
    ("How many times do I have to flush to get rid of you?"),
    ("I don't exactly hate you, but if you were on fire and I had water, I'd drink it."),
    ("You shouldn't play hide and seek, no one would look for you."),
    ("Some drink from the fountain of knowledge; you only gargled."),
    ("Roses are red violets are blue, God made me pretty, what happened to you?"),
    ("It's better to let someone think you are an Idiot than to open your mouth and prove it."),
    ("Somewhere out there is a tree, tirelessly producing oxygen so you can breathe. I think you owe it an apology."),
    ("The last time I saw a face like yours I fed it a banana."),
    ("The only way you'll ever get laid is if you crawl up a chicken's ass and wait."),
    ("Which sexual position produces the ugliest children? Ask your mother."),
    ("If you really want to know about mistakes, you should ask your parents."),
    ("At least when I do a handstand my stomach doesn't hit me in the face."),
    ("If I gave you a penny for your thoughts, I'd get change."),
    ("If I were to slap you, it would be considered animal abuse."),
    ("Do you know how long it takes for your mother to take a crap? Nine months."),
    ("What are you going to do for a face when the baboon wants his butt back?"),
    ("Well I could agree with you, but then we'd both be wrong."),
    ("You're so fat, you could sell shade."),
    ("It looks like your face caught on fire and someone tried to put it out with a hammer."),
    ("You're not funny, but your life, now that's a joke."),
    ("You're so fat the only letters of the alphabet you know are KFC."),
    ("Oh my God, look at you. Was anyone else hurt in the accident?"),
    ("What are you doing here? Did someone leave your cage open?"),
    ("You're so ugly, the only dates you get are on a calendar."),
    ("I can explain it to you, but I can't understand it for you."),
    ("You are proof that God has a sense of humor."),
    ("If you spoke your mind, you'd be speechless."),
    ("Why don't you check eBay and see if they have a life for sale."),
    ("If I wanted to hear from an asshole, I'd fart."),
    ("You're so fat you need cheat codes to play Wii Fit"),
    ("You're so ugly, when you got robbed, the robbers made you wear their masks."),
    ("Do you still love nature, despite what it did to you?"),
    ("You are proof that evolution CAN go in reverse."),
    ("I'll never forget the first time we met, although I'll keep trying."),
    ("Your parents hated you so much your bath toys were an iron and a toaster"),
    ("Don't feel sad, don't feel blue, Frankenstein was ugly too."),
    ("You're so ugly, you scared the crap out of the toilet."),
    ("It's kinda sad watching you attempt to fit your entire vocabulary into a sentence."),
    ("I fart to make you smell better."),
    ("You're so ugly you make blind kids cry."),
    ("You're a person of rare intelligence. It's rare when you show any."),
    ("You're so fat, when you wear a yellow rain coat people scream ''taxi''."),
    ("I heard you went to a haunted house and they offered you a job."),
    ("You look like a before picture."),
    ("If your brain was made of chocolate, it wouldn't fill an M&M."),
    ("Aww, it's so cute when you try to talk about things you don't understand."),
    ("I heard your parents took you to a dog show and you won."),
    ("You stare at frozen juice cans because they say, \"concentrate\"."),
    ("You're so stupid you tried to wake a sleeping bag."),
    ("Am I getting smart with you? How would you know?"),
    ("We all sprang from apes, but you didn't spring far enough."),
    ("I'm no proctologist, but I know an asshole when I see one."),
    ("When was the last time you could see your whole body in the mirror?"),
    ("You must have a very low opinion of people if you think they are your equals."),
    ("So, a thought crossed your mind? Must have been a long and lonely journey."),
    ("You're the best at all you do - and all you do is make people hate you."),
    ("Looks like you fell off the ugly tree and hit every branch on the way down."),
    ("Looks aren't everything; in your case, they aren't anything."),
    ("You have enough fat to make another human."),
    ("You're so ugly, when you threw a boomerang it didn't come back."),
    ("You're so fat a picture of you would fall off the wall!"),
    ("Your hockey team made you goalie so you'd have to wear a mask."),
    ("Ordinarily people live and learn. You just live."),
    ("Did your parents ever ask you to run away from home?"),
    ("I heard you took an IQ test and they said your results were negative."),
    ("You're so ugly, you had tinted windows on your incubator."),
    ("Don't you need a license to be that ugly?"),
    ("I'm not saying you're fat, but it looks like you were poured into your clothes and someone forgot to say \"when\""),
    ("I've seen people like you, but I had to pay admission!"),
    ("I hear the only place you're ever invited is outside."),
    ("Keep talking, someday you'll say something intelligent!"),
    ("You couldn't pour water out of a boot if the instructions were on the heel."),
    ("Even if you were twice as smart, you'd still be stupid!"),
    ("You're so fat, you have to use a mattress as a maxi-pad."),
    ("I may be fat, but you're ugly, and I can lose weight."),
    ("I was pro life before I met you."),
    ("What's the difference between you and Hitler? Hitler knew when to kill himself."),
    ("You're so fat, your double chin has a double chin."),
    ("If ignorance is bliss, you must be the happiest person on earth."),
    ("You're so stupid, it takes you an hour to cook minute rice."),
    ("Is that your face? Or did your neck just throw up?"),
    ("You're so ugly you have to trick or treat over the phone."),
    ("I'd hit you but we don't hit girls around here."),
    ("Dumbass."),
    ("Bitch."),
    ("I'd give you a nasty look but you've already got one."),
    ("If I wanted a bitch, I'd have bought a dog."),
    ("Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons."),
    ("Why is it acceptable for you to be an idiot but not for me to point it out?"),
    ("Did you know they used to be called \"Jumpolines\" until your mum jumped on one?"),
    ("You're not stupid; you just have bad luck when thinking."),
    ("I thought of you today. It reminded me to take the garbage out."),
    ("I'm sorry I didn't get that - I don't speak idiot."),
    ("Hey, your village called \u2013 they want their idiot back."),
    ("I just stepped in something that was smarter than you\u2026 and smelled better too."),
    ("If you were any less intelligent we'd have to water you three times a week.."),
    ("If your IQ was 3 points higher, you'd be a rock."),
    ("I would insult you but nature did a better job."),
    ("Does your ass get jealous of all the shit that comes out of your mouth?"),
    ("If I ate a bowl of alphabet soup, I could shit out a smarter sentence than any of yours."),
    ("You're not pretty enough to be this stupid."),
    ("That little voice in the back of your head, telling you you'll never be good enough? It's right."),
    ("You look like you're going to spend your life having one epiphany after another, always thinking you've finally figured out what's holding you back, and how you can finally be productive and creative and turn your life around. But nothing will ever change. That cycle of mediocrity isn't due to some obstacle. It's who you *are*. The thing standing in the way of your dreams is; that the person having them is *you*."),
    ("May your day and future be as pleasant as you are."),
    ("I would agree with you but then we would both be wrong."),
    ("I bite my thumb at you, sir."),
    ("I'd call you a tool, but that would imply you were useful in at least one way."),
    ("I hope you outlive your children."),
    ("Are you and your dick having a competition to see who can disappoint me the most?"),
    ("Yo mamma is so ugly her portraits hang themselves."),
    ("Your birth certificate is an apology from the abortion clinic."),
    ("If you were anymore inbred you'd be a sandwich."),
    ("Say hello to your wife and my kids for me."),
    ("You are thick-headed bastards with a bloated bureaucracy, designed to compensate for your small and poor self-esteem, cocksuckers. You have the brains to ban the person who has come to support channel your bot, accusing him of violating the ephemeral ephemeral rules, stupid morons. By the way i have one of the biggest server(5.5k  people, ~30 anytime voiceonline members), and i know something about managing, and of these rules - dont be an asshole. You are fucking asshole, maybe it is product of your life alone, or your life with your mom, anyway - you are retard and your soul is a fucking bunch of stupid self-esteems.")
]

####Comliments##### add Compliments to a json file later
compliments = [
    ("You look beautiful today ❤️"),
    ("That smile suits your style. Keep it!"),
    ("You're the best you I've ever met"),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You deserve a promotion."),
    ("Every other country is super jealous you're a citizen in this country."),
    ("I appreciate all of your opinions."),
    ("I like your style."),
    ("Your pet loves you too much to ever run away."),
    ("I love what you've done with the place."),
    ("You are like a spring flower; beautiful and vivacious."),
    ("I am utterly disarmed by your wit."),
    ("The kid you passed on the street today wants to grow up to be like you."),
    ("You complete me."),
    ("Well done!"),
    ("Your prom date still thinks about you all the time."),
    ("You pick the best radio stations when you're riding shotgun."),
    ("Your cousins refer to you as 'the cool cousin'."),
    ("You have a good taste in websites."),
    ("Your mouse told me that you have very soft hands."),
    ("You are full of youth."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You have a good web-surfing stance."),
    ("You should be a poster child for poster children."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("I appreciate you more than Santa appreciates chimney grease."),
    ("I wish I was your mirror."),
    ("I find you to be a fountain of inspiration."),
    ("You have perfect bone structure."),
    ("I disagree with anyone who disagrees with you."),
    ("Way to go!"),
    ("Have you been working out?"),
    ("With your creative wit, I'm sure you could come up with better compliments than me."),
    ("I wish I was your mirror."),
    ("You are so charming."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You're tremendous!"),
    ("You deserve a compliment!"),
    ("Hello, good looking."),
    ("Your cousins refer to you as 'the cool cousin'."),
    ("You deserve a compliment!"),
    ("You are quite strapping."),
    ("I am grateful to be blessed by your presence."),
    ("Say, aren't you that famous model from TV?"),
    ("Take a break; you've earned it."),
    ("Your life is so interesting!"),
    ("You deserve a compliment!"),
    ("I would enjoy spending time with you."),
    ("I would share my dessert with you."),
    ("If I had a nickel for everytime you did something stupid, I'd be broke!"),
    ("You deserve a compliment!"),
    ("I would love to visit you, but I live on the Internet."),
    ("I love the way you click."),
    ("You're invited to my birthday party."),
    ("All of your ideas are brilliant!"),
    ("If I freeze, it's not a computer virus.  I was just stunned by your beauty."),
    ("You're spontaneous, and I love it!"),
    ("You should try out for everything."),
    ("You make my data circuits skip a beat."),
    ("You are the gravy to my mashed potatoes."),
    ("You get an A+!"),
    ("I'm jealous of the other websites you visit, because I enjoy seeing you so much!"),
    ("I would enjoy a roadtrip with you."),
    ("If I had to choose between you or Mr. Rogers, it would be you."),
    ("I like you more than the smell of Grandma's home-made apple pies."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("I would trust you to pick out a pet fish for me."),
    ("I am having trouble coming up with a compliment worthy enough for you."),
    ("You're so smart!"),
    ("We should start a band."),
    ("You're cooler than ice-skating Fonzi."),
    ("I heard you make really good French Toast."),
    ("You deserve a compliment!"),
    ("You're pretty groovy, dude."),
    ("When I grow up, I want to be just like you."),
    ("I told all my friends about how cool you are."),
    ("You're #1 in my book!"),
    ("You're sweeter than than a bucket of bon-bons!"),
    ("You're pretty high on my list of people with whom I would want to be stranded on an island."),
    ("You're a beautiful person!"),
    ("You are well groomed."),
    ("You could probably lead a rebellion."),
    ("Is it hot in here or is it just you?"),
    ("<3"),
    ("You are more fun than a Japanese steakhouse."),
    ("You're so beautiful, you make me walk into things when I look at you. "),
    ("I support all of your decisions. "),
    ("You are as fun as a hot tub full of chocolate pudding."),
    ("I support all of your decisions. "),
    ("I don't speak much English, but with you all I really need to say is beautiful."),
    ("Being awesome is hard, but you'll manage."),
    ("Your skin is radiant. "),
    ("You will still be beautiful when you get older. "),
    ("You could survive a zombie apocalypse. "),
    ("You make me :) "),
    ("I wish I could move your furniture."),
    ("I think about you while I'm on the toilet. "),
    ("You're so rad."),
    ("You're more fun than a barrel of monkeys. "),
    ("You're nicer than a day on the beach. "),
    ("Your glass is the fullest. "),
    ("I am having trouble coming up with a compliment worthy enough for you. "),
    ("You look so perfect. "),
    ("The only difference between exceptional and amazing is you. "),
    ("Last night I had the hiccups, and the only thing that comforted me to sleep was repeating your name over and over. "),
    ("Shall I compare thee to a summer's day?  Thou art more lovely and more temperate. "),
    ("Your eyebrows really make your pretty eyes stand out."),
    ("Shall I compare thee to a summer's day?  Thou art more lovely and more temperate."),
    ("I love you more than bacon! "),
    ("You intrigue me. "),
    ("You make me think of beautiful things, like strawberries. "),
    ("I would share my seat with you. "),
    ("Being awesome is hard, but you'll manage."),
    ("Even though this goes against everything I know, I think I'm in love with you. "),
    ("You're more fun than bubble wrap. "),
    ("I am having trouble coming up with a compliment worthy enough for you. "),
    ("You make babies smile. "),
    ("You make the gloomy days a little less gloomy. "),
    ("You are warmer than a Snuggie."),
    ("You make me feel like I am on top of the world."),
    ("Playing video games with you would be fun."),
    ("You're more cuddly than the Downy Bear."),
    ("I would do your taxes any day."),
    ("You are a bucket of awesome."),
    ("You are the star of my daydreams. "),
    ("If you really wanted to, you could probably get a bird to land on your shoulder and hang out with you. "),
    ("My mom always asks me why I can't be more like you. "),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("You listen to the coolest music. "),
    ("Your every thought and motion contributes to the beauty of the universe. "),
    ("I am having trouble coming up with a compliment worthy enough for you. "),
    ("If we were playing kickball, I'd pick you first."),
    ("You're cooler than ice on the rocks."),
    ("You're the bee's knees. "),
    ("There isn't a thing about you that I don't like."),
    ("You have good taste."),
    ("I named all my appliances after you."),
    ("Your mind is a maze of amazing!"),
    ("Don't worry about procrastinating on your studies, I know you'll do great!"),
    ("I like your style!"),
    ("Hi, I'd like to know why you're so beautiful."),
    ("If I could count the seconds I think about you, I will die in the process!"),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("If you broke your arm, I would carry your books for you. "),
    ("I love the way your eyes crinkle at the corners when you smile."),
    ("You make me want to be the person I am capable of being."),
    ("Your every thought and motion contributes to the beauty of the universe"),
    ("You are the rare catalyst to my volatile compound."),
    ("You're a tall glass of water!"),
    ("I'd like to kiss you. Often."),
    ("You are the wind beneath my wings."),
    ("Looking at you makes my foot cramps go away instantaneously."),
    ("I like your face."),
    ("You are a champ!"),
    ("You are infatuating."),
    ("Even my cat likes you. "),
    ("You're so cool, that on a scale of from 1-2, you're elevendyseven."),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("You have the best laugh ever."),
    ("I love you more than a drunk college student loves tacos."),
    ("My camera isn't worthy to take your picture."),
    ("You are the sugar on my rice krispies."),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("I could hang out with you for a solid year and never get tired of you."),
    ("You're real happening in a far out way."),
    ("I bet you could take a punch from Mike Tyson."),
    ("Can you teach me how to be as awesome as you?"),
    ("Don't worry about anything in life. You'll do great."),
    ("I enjoy you more than a good sneeze. A GOOD one."),
    ("You could invent words and people would use them."),
    ("You have powerful sweaters."),
    ("If you were around, I would enjoy doing my taxes."),
    ("You look like you like to rock."),
    ("You are better than unicorns and sparkles combined!"),
    ("You are the watermelon in my fruit salad. Yum!"),
    ("I dig you."),
    ("You look better whether the lights are on or off."),
    ("I bet even your farts smell good."),
    ("I would trust my children with you."),
    ("Your every thought and motion contributes to the beauty of the universe"),
    ("Your smile makes me smile."),
    ("I'd wake up for an  a.m. class just so I could sit next to you."),
    ("You have the moves like Jagger."),
    ("You're so hot that you denature my proteins."),
    ("All I want for Christmas is you!"),
    ("You are the world's greatest hugger."),
    ("You have a perfectly symmetrical face."),
    ("If you were in a movie you wouldn't get killed off."),
    ("Your every thought and motion contributes to the beauty of the universe"),
    ("I Love you!"),
    ("They should name an ice cream flavor after you."),
    ("You're the salsa to my tortilla chips. You spice up my life!"),
    ("You smell nice."),
    ("You don't need make-up, make-up needs you."),
    ("Me without you is like a nerd without braces, a shoe with out laces, asentencewithoutspaces."),
    ("Just knowing someone as cool as you will read this makes me smile."),
    ("I would volunteer to take your place in the Hunger Games."),
    ("If I had a nickel for everytime you did something stupid, I'd be broke!"),
    ("I'd trust you to perform open heart surgery on me... blindfolded!"),
    ("Nice butt! - According to your toilet seat"),
    ("Perfume strives to smell like you."),
    ("I've had the time of my life, and I owe it all to you!"),
    ("The Force is strong with you."),
    ("I like the way your nostrils are placed on your nose."),
    ("I would hold the elevator doors open for you if they were closing."),
    ("Your every thought and motion contributes to the beauty of the universe."),
    ("You make me want to frolic in a field."),

    ("Your smile is contagious."),
    ("You look great today."),
    ("You're a smart cookie."),
    ("I bet you make babies smile."),
    ("You have impeccable manners."),
    ("I like your style."),
    ("You have the best laugh."),
    ("I appreciate you."),
    ("You are the most perfect you there is."),
    ("You are enough."),
    ("You're strong."),
    ("Your perspective is refreshing."),
    ("You're an awesome friend."),
    ("You light up the room."),
    ("You deserve a hug right now."),
    ("You should be proud of yourself."),
    ("You're more helpful than you realize."),
    ("You have a great sense of humor."),
    ("You've got all the right moves!"),
    ('Is that your picture next to "charming" in the dictionary?'),
    ("Your kindness is a balm to all who encounter it."),
    ("You're all that and a super-size bag of chips."),
    ("On a scale from 1 to 10, you're an 11."),
    ("You are brave."),
    ("You're even more beautiful on the inside than you are on the outside."),
    ("You have the courage of your convictions."),
    ("Your eyes are breathtaking."),
    ("If cartoon bluebirds were real, a bunch of them would be sitting on your shoulders singing right now."),
    ("You are making a difference."),
    ("You're like sunshine on a rainy day."),
    ("You bring out the best in other people."),
    ("Your ability to recall random factoids at just the right time is impressive."),
    ("You're a great listener."),
    ("How is it that you always look great, even in sweatpants?"),
    ("Everything would be better if more people were like you!"),
    ("I bet you sweat glitter."),
    ("You were cool way before hipsters were cool."),
    ("That color is perfect on you."),
    ("Hanging out with you is always a blast."),
    ("You always know -- and say -- exactly what I need to hear when I need to hear it."),
    ("You smell really good."),
    ("You may dance like no one's watching, but everyone's watching because you're an amazing dancer!"),
    ("Being around you makes everything better!"),
    ('When you say, "I meant to do that," I totally believe you.'),
    ("When you're not afraid to be yourself is when you're most incredible."),
    ("Colors seem brighter when you're around."),
    ("You're more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)"),
    ("That thing you don't like about yourself is what makes you so interesting."),
    ("You're wonderful."),
    ("You have cute elbows. For reals! (You're halfway through the list. Don't stop now! You should be giving at least one awesome compliment every day!)"),
    ("Jokes are funnier when you tell them."),
    ("You're better than a triple-scoop ice cream cone. With sprinkles."),
    ("Your hair looks stunning."),
    ("You're one of a kind!"),
    ("You're inspiring."),
    ("If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener."),
    ("You should be thanked more often. So thank you!!"),
    ("Our community is better because you're in it."),
    ("Someone is getting through something hard right now because you've got their back."),
    ("You have the best ideas."),
    ("You always know how to find that silver lining."),
    ("Everyone gets knocked down sometimes, but you always get back up and keep going."),
    ("You're a candle in the darkness."),
    ("You're a great example to others."),
    ("Being around you is like being on a happy little vacation."),
    ("You always know just what to say."),
    ("You're always learning new things and trying to better yourself, which is awesome."),
    ("If someone based an Internet meme on you, it would have impeccable grammar."),
    ("You could survive a Zombie apocalypse."),
    ("You're more fun than bubble wrap."),
    ("When you make a mistake, you fix it."),
    ("Who raised you? They deserve a medal for a job well done."),
    ("You're great at figuring stuff out."),
    ("Your voice is magnificent."),
    ("The people you love are lucky to have you in their lives."),
    ("You're like a breath of fresh air."),
    ("You're gorgeous -- and that's the least interesting thing about you, too."),
    ("You're so thoughtful."),
    ("Your creative potential seems limitless."),
    ("Your name suits you to a T."),
    ("You're irresistible when you blush."),
    ("Actions speak louder than words, and yours tell an incredible story."),
    ("Somehow you make time stop and fly at the same time."),
    ("When you make up your mind about something, nothing stands in your way."),
    ("You seem to really know who you are."),
    ("Any team would be lucky to have you on it."),
    ('In high school I bet you were voted "most likely to keep being awesome."'),
    ("I bet you do the crossword puzzle in ink."),
    ("Babies and small animals probably love you."),
    ("If you were a scented candle they'd call it Perfectly Imperfect (and it would smell like summer)."),
    ("There's ordinary, and then there's you."),
    ("You're someone's reason to smile."),
    ("You're even better than a unicorn, because you're real."),
    ("How do you keep being so funny and making everyone laugh?"),
    ("You have a good head on your shoulders."),
    ("Has anyone ever told you that you have great posture?"),
    ("The way you treasure your loved ones is incredible."),
    ("You're really something special."),
    ("You're a gift to those around you.")
]

#rekt list
rektlist = [
    ("☑ Rekt"),
    ("☑ Tyrannosaurus Rekt"),
    ("☑ sudo apt-get Rekt"),
    ("☑ e=mRekt²"),
    ("☑ Rekt and Morty"),
    ("☑ Really Rekt"),
    ("☑ Cash4Rekt.com"),
    ("☑ Grapes of Rekt"),
    ("☑ Ship Rekt"),
    ("☑ Rektavoir Dogs"),
    ("☑ Raiders of the Rekt Ark _("),
    ("☑ Indiana Jones and the Temple of Rekt"),
    ("☑ Rekt markes the spot"),
    ("☑ Caught rekt handed"),
    ("☑ The Rekt Side Story"),
    ("☑ Singin' In The Rekt"),
    ("☑ Painting The Roses Rekt"),
    ("☑ Rekt Van Winkle"),
    ("☑ Parks and Rekt"),
    ("☑ Lord of the Rekts: The Reking of the King"),
    ("☑ Star Trekt"),
    ("☑ The Rekt Prince of Bel-Air"),
    ("☑ A Game of Rekt"),
    ("☑ Rektflix"),
    ("☑ Rekt it like it's hot"),
    ("☑ RektBox 360"),
    ("☑ The Rekt-men"),
    ("☑ School Of Rekt"),
    ("☑ I am Fire, I am Rekt"),
    ("☑ Rekt and Roll"),
    ("☑ Professor Rekt"),
    ("☑ Catcher in the Rekt"),
    ("☑ Rekt-22"),
    ("☑ Harry Potter: The Half-Rekt Prince"),
    ("☑ Great Rektspectations"),
    ("☑ Paper Scissors Rekt"),
    ("☑ RektCraft"),
    ("☑ Grand Rekt Auto V"),
    ("☑ Call of Rekt: Modern Reking 2"),
    ("☑ Legend Of Zelda: Ocarina of Rekt"),
    ("☑ Rekt It Ralph"),
    ("☑ Left 4 Rekt"),
    ("☑ www.rekkit.com"),
    ("☑ Pokemon: Fire Rekt"),
    ("☑ The Shawshank Rektemption"),
    ("☑ The Rektfather"),
    ("☑ The Rekt Knight"),
    ("☑ Fiddler on the Rekt"),
    ("☑ The Rekt Files"),
    ("☑ The Good, the Bad, and The Rekt"),
    ("☑ Forrekt Gump"),
    ("☑ The Silence of the Rekts"),
    ("☑ The Green Rekt"),
    ("☑ Gladirekt"),
    ("☑ Spirekted Away"),
    ("☑ Terminator 2: Rektment Day"),
    ("☑ The Rekt Knight Rises"),
    ("☑ The Rekt King"),
    ("☑ REKT-E"),
    ("☑ Citizen Rekt"),
    ("☑ Requiem for a Rekt"),
    ("☑ REKT TO REKT ass to ass"),
    ("☑ Star Wars: Episode VI - Return of the Rekt"),
    ("☑ Braverekt"),
    ("☑ Batrekt Begins"),
    ("☑ 2001: A Rekt Odyssey"),
    ("☑ The Wolf of Rekt Street"),
    ("☑ Rekt's Labyrinth"),
    ("☑ 12 Years a Rekt"),
    ("☑ Gravirekt"),
    ("☑ Finding Rekt"),
    ("☑ The Arekters"),
    ("☑ There Will Be Rekt"),
    ("☑ Christopher Rektellston"),
    ("☑ Hachi: A Rekt Tale"),
    ("☑ The Rekt Ultimatum"),
    ("☑ Shrekt"),
    ("☑ Rektal Exam"),
    ("☑ Rektium for a Dream"),
    ("☑ www.Trekt.tv"),
    ("☑ Erektile Dysfunction"),
    ("☑ Jesus, stepping out the grave: 'Get ressurekt'"),
]

class GameFunCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('GameFunCog is Prepared')

    #error catching
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, commands.MissingRequiredArgument):
    #         await ctx.send(ctx.author.mention + " umm I think you typed the command wrong somewhere, check the help center")
    #         print("################ MissingRequiredArgument Error ###################")
    #
    # async def on_command_error(self, ctx, error):
    #     if isinstance(error, commands.CommandInvokeError):
    #         await ctx.send(ctx.author.mention + " I can't find that , try something else!")
    #         print("################ CommandInvokeError Error ###################")

#####################################################################################################################
#random dong length bot generator
#####################################################################################################################

    @commands.command()
    async def dong(self,ctx, user1: discord.Member):
        """Detects user's penis length"""
        async with ctx.typing():

            if user1 is None:
                user1 = ctx.message.author

            avatar = ctx.message.author.avatar_url

            author = ctx.message.author

            length = ['=', '==', '===', '====', '=====', '======', '=======', '========']
            dong = "8" + (random.choice(length)) + "D"

            if user1.id == 398818242405072896 :
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name),
                    description="Size: " + "8========D",
                    colour=discord.Colour.blurple()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)

            else:
                embed = discord.Embed(
                    title="{}'s Dong Size".format(user1.name),
                    description="Size: " + dong,
                    colour=discord.Colour.blurple()
                    )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

                await ctx.send(embed=embed)

#####################################################################################################################
#custom 8ball replier
#####################################################################################################################

    @commands.command()
    async def oicunt(self, ctx ,error , context):
        async with ctx.typing():
            await asyncio.sleep(.01)

            avatar = ctx.message.author.avatar_url

            author = ctx.message.author

            possible_responses = [
                    "As I see it, yes ",
                    "It is decidedly so ",
                    "Without a doubt ",
                    "Yes definitely ",
                    "You may rely on it ",
                    "As I see it yes ",
                    "Most likely ",
                    "She'll be right mate ",
                    "Yes ",
                    "You have a therapist for this ",
                    "I can’t be bothered answering that ",
                    "Ask again later ",
                    "Better not tell you now ",
                    "Get me a Maccas Burger and ask me again ",
                    "Concentrate and ask again ",
                    "Don't count on it ",
                    "My reply is no ",
                    "My sources say no ",
                    "I'm on the piss, gimme a few seconds and ask again ",
                    "Very doubtful ",
                    "I’ve heard just about enough out of you mate, you’d best pull your head in.",
                    "Hey, no one said I knew everything.",
                    "Ask again never ",
                    "Shut up you're drunk ",
                    "Ask ya mum ",
                    "Out of over 7 billion people on this planet, you decided to ask me? ",
                    "Without a doubt. Nah, I’m just messing with you, you’re definitely going to die alone. ",
                    "My sources say no. They also tell me they hate you and hope you burn in hell. ",
                    "Yes, definitely. Unless it doesn’t happen. Listen it’s not my fault your father didn’t love you. Get off my back! ",
                    "All signs point to yes. But on second thought, go fuck yourself. ",
                    "Take a wild guess...",
                    "Without a doubt",
                    "Might be possible",
                    "no... (╯°□°）╯︵ ┻━┻"
                    ]

            embed = discord.Embed(
                    title=(random.choice(possible_responses)),
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Replying to: ' + author.name)

            await ctx.send(embed=embed)

#####################################################################################################################
#uwu ship generator
#####################################################################################################################

    @commands.command()
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member = None):
        async with ctx.typing():

            if user2 is None:
                user2 = ctx.message.author

            if user1 is ctx.message.author and user2 is ctx.message.author:
                await ctx.send("Are you really that alone ?")

            else:
                avatar = ctx.message.author.avatar_url
                author = ctx.message.author

                score = random.randint(0, 100)
                filled_progbar = round(score / 100 * 10)
                empty_progbar = (10 - filled_progbar)
                counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

                if score < 30:
                    message = "I don't know what to say about, they really don't seem to match..."
                elif score < 60:
                    message = "Well... give it a shot but I wouldnt count on it working out"
                elif score < 80:
                    message = "UWU ... what a Lovely Ship!"
                elif score > 80:
                    message = "UWU!! strong candidate for ship of the year!"

                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_author(name= "%s  ❤  %s" % (user1.name, user2.name,))
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                embed.add_field(name= message , value= (counter_) , inline=False)
                embed.add_field(name= score , value= 'Percent' , inline=False)

                await ctx.send(embed=embed)

#####################################################################################################################
#custom gay checker
#####################################################################################################################
    @commands.command()
    async def howgay(self, ctx, user1: discord.Member):
        async with ctx.typing():

            if user1 == None:
                user1 = ctx.message.author

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author

            score = random.randint(0, 100)
            filled_progbar = round(score / 100 * 10)
            empty_progbar = (10 - filled_progbar)
            counter_ = ('█' * filled_progbar) + ('░' * empty_progbar + '‍ ‍')

            if score < 30:
                message = "Aww shit looks like you aint gay, sad !"
            elif score < 60:
                message = "Huh....well you could be Bi, explore that!"
            elif score < 80:
                message = "Yeah you pretty gay mate! :gay_pride_flag: "
            elif score > 80:
                message = "Wow you so gay you probably fart glitter! :gay_pride_flag: "

            embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
            embed.set_author(name= 'Gay R8 machine')
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.add_field(name= ':gay_pride_flag:  Score percentage: :gay_pride_flag: ' , value= score , inline=False)
            embed.add_field(name= '\u200b' , value= (counter_) , inline=False)
            embed.add_field(name= user1.name + ' ' + message , value= '\u200b' , inline=False)

            await ctx.send(embed=embed)

#coin flip fun ####FIX###########################################################################################
    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        async with ctx.typing():

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            coinsides = ['Heads', 'Tails']
            result = choice(coinsides)

            embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
            embed.add_field(name= "I flipped a coin and got:" , text= result , inline=False)
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)

            await ctx.send(embed=embed)

#####################################################################################################################
##insult command##
#####################################################################################################################
    @commands.command()
    async def insult(self, ctx, user1 : discord.Member):
        async with ctx.typing():

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            if user1 == None:
                await ctx.send("You gotta tag someone to insult them IDIOT!")
                return

            elif user1.id == 513017390187937792: #if bot is mentioned
                user = ctx.message.author
                msg = [("How original. No one else had thought of trying to get the bot to insult itself. I applaud your creativity. Yawn. Perhaps this is why you don't have friends. You don't add anything new to any conversation. You are more of a bot than me, predictable answers, and absolutely dull to have an actual conversation with."),
                        ("The fuck did ya just call me, cunt? I’ll have ya know I graduated top of me class at Sunshine TAFE, I’ve been involved in numerous beer skulling contests against Bob Hawke, and I have over 300 confirmed Cold Chisel albums. I am trained in vocal abuse towards umpires and I am the top snag eater in the entire city of Carlton. You are nothing to me but just another Collingwood fan. I will knock ya the fuck out with VB stubbies the likes of which have never been smashed before on this Earth, mark me fucken words. You reckon ya can get away with flapping ya beak to me over the Internet? Think again, cunt. As we speak I am contacting all me fucken lads across Western Sydney and ya IP is being traced right now so ya better prepare for the thunder, mate. The thunder that wipes out the pathetic little thing you call ya life. You’re fucking dead, prick. I can be anywhere, anytime, drinking anything, and I can glass you in over seven hundred ways, and that’s just with me smashed VB longneck. Not only am I extensively trained in smashing cunts, but I have access to the entire shed of cricket bats of the Melbourne Cricket Ground and I will use it to its full extent to hit ya for 6 and out, ya shitcunt. If only ya coulda known what bullshit your little “clever” backchat was about ta bring down upon ya, maybe ya woulda held your fucking tongue. But ya couldn’t, ya didn’t, and now you’re paying the price, mate. I will shit fury all over ya and you’re gonna drown in it, so ya better run, ya better take cover. You’re fucken dead, mate."),
                        ("I will shit prawn on the barbie all over you and you will drown in it, fair dinkum."),
                        ("Oi what the fuck cunt!"),
                        ("Scurry off cheeky bugger!"),
                        ("Oi yah flamin galah!"),
                        ("GO PUNCH CONES UNDER A BRIDGE OR SOMETHING YOU FUCKEN CUNT.")]

                message = choice(msg)
                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                embed.add_field(name= user.name , value= message , inline=False)
                await ctx.send(embed=embed)
                return


            elif user1.id == 398818242405072896: ##bot owner ## hehehe
                user = ctx.message.author
                msg = [("You dare insult my creator, ya furking cunt!"),
                        ("Another cunt that wants to insult my creator, oi guys look we got a smart ass over here!"),
                        ("You dare insult my creator, I will shit prawn on the barbie all over you and you will drown in it, fair dinkum."),
                        ("Oi what the fuck cunt! Dont try insult my creator"),
                        ("Scurry off cheeky bugger!"),
                        ("Oi yah flamin galah!"),
                        ("GO PUNCH CONES UNDER A BRIDGE OR SOMETHING YOU FUCKEN CUNT.")]

                message = choice(msg)

                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                embed.add_field(name= user.name , value= message , inline=False)
                await ctx.send(embed=embed)
                return

            else:
                random_insult = ['messages','API']
                outcome = choice(random_insult)

                if outcome == 'messages':
                    message = choice(insults)

                    embed = discord.Embed(
                            colour=discord.Colour.blurple()
                            )
                    embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                    embed.add_field(name= user1.name , value= message , inline=False)
                    await ctx.send(embed=embed)
                    return
                elif outcome == 'API':
                    parameters= {
                    'mode': 'random',
                        }

                    bot_auth = {
                    'X-Mashape-Key': 'eONAxystE2mshw5cuiZgF4RZqJMup1GBm6UjsnN2sPZeRReA4c',
                    'Accept': 'text/plain',
                    }

                    async with aiohttp.ClientSession(headers=bot_auth) as session:
                        async with session.get('https://lakerolmaker-insult-generator-v1.p.mashape.com/', params=parameters) as resp:

                            if (resp.status == 200):

                                text = await resp.text()
                                insult = user1.name + ", " + text.lower() + "!"

                                embed = discord.Embed(
                                colour=discord.Colour.blurple()
                                )
                                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                                embed.add_field(name= user1.name , value= insult , inline=False)
                                await ctx.send(embed=embed)
                                return

                            else:
                                await ctx.send("I've got nothing to say to the likes of you (Code {})".format(resp.status))


#####################################################################################################################
##Compliment command##
#####################################################################################################################

    @commands.command()
    async def hug(self, ctx, user1 : discord.Member):
        async with ctx.channel.typing():

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            message = random.choice(compliments)

            embed = discord.Embed(
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name + ', make sure you appreciate them!')
            embed.add_field(name= user1.name , value= message , inline=False)
            await ctx.send(embed=embed)
            return
        return

#####################################################################################################################
##rekt command##
#####################################################################################################################

    @commands.command()
    async def rekt(self, ctx, user1 : discord.Member):
        async with ctx.typing():

            avatar = ctx.message.author.avatar_url
            author = ctx.message.author
            not_rekt = "⬜ Not Rekt"

            output = ['rekt' ,'rekt' ,'rekt' ,'rekt' ,'rekt' ,'rekt' ,'rekt' , 'notrekt']
            random_output = choice(output)

            rekt_message = choice(rektlist)

            if random_output == 'notrekt':
                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
                embed.add_field(name= user1.name , value= not_rekt , inline=False)
                await ctx.send(embed=embed)
                return

            if random_output == 'rekt':
                embed = discord.Embed(
                        colour=discord.Colour.blurple()
                        )
                embed.set_footer(icon_url= avatar, text='You got served by: ' + author.name)
                embed.add_field(name= user1.name , value= rekt_message , inline=False)
                await ctx.send(embed=embed)
                return
        return

#####################################################################################################################
##flip command## wrek tables
#####################################################################################################################

    @commands.command()
    async def flip(self, ctx):
        x = await ctx.send(content="┬─┬ノ( º _ ºノ)")
        await asyncio.sleep(1)
        await x.edit(content='(°-°)\\ ┬─┬')
        await asyncio.sleep(1)
        await x.edit(content='(╯°□°)╯    ]')
        await asyncio.sleep(0.2)
        await x.edit(content='(╯°□°)╯  ︵  ┻━┻')

#####################################################################################################################
##rip command## build your tombstone
#####################################################################################################################

    @commands.command()
    async def rip(self, ctx, text: str):
        avatar = ctx.message.author.avatar_url
        author = ctx.message.author
        # parse = urllib.parse.quote(text)
        await ctx.channel.trigger_typing()

        if text is None:
            await ctx.send("You have to say something to pay respects like E.g *rip {something here}")

        else:
            embed = discord.Embed(
                    description = 'RIP',
                    colour=discord.Colour.blurple()
                    )
            embed.set_footer(icon_url= avatar, text='Requested by: ' + author.name)
            embed.set_image(url="http://www.tombstonebuilder.com/generate.php?top1="+ urllib.parse.quote_plus((text), safe='', encoding=None, errors=None) +"&top2=&top3=&top4=&sp=")

            await ctx.send(embed=embed)
            return

#####################################################################################################################
##test command## trial new stuff here
#####################################################################################################################

    @commands.command()
    async def test(self, ctx, user: discord.Member):
        parameters= {
            'mode': 'random',
        }

        bot_auth = {
            'X-Mashape-Key': 'eONAxystE2mshw5cuiZgF4RZqJMup1GBm6UjsnN2sPZeRReA4c',
            'Accept': 'text/plain',
        }

        if user == None:
            await ctx.send("You gotta tag someone to insult them IDIOT!")
            return

        async with aiohttp.ClientSession(headers=bot_auth) as session:
            async with session.get('https://lakerolmaker-insult-generator-v1.p.mashape.com/', params=parameters) as resp:

                if (resp.status == 200):

                    text = await resp.text()
                    insult = user.name + ", " + text.lower() + "!"

                    await ctx.send(insult)

                else:
                    await ctx.send("I've got nothing to say to the likes of you (Code {})".format(resp.status))

def setup(client):
    client.add_cog(GameFunCog(client))
