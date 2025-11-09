

# Transcript
0:00:00.0 Sean Carroll: Hello everyone and welcome to the Mindscape Podcast. I'm your host Sean Carroll. Today's podcast has a good news, bad news situation. The bad news is there will be bad language in this podcast. Not because we're getting especially salty or profane or anything like that, but because we're going to be talking about computer simulations that were written and run using a language called Brainfuck. Sorry about that if you have sensitive ears, but this is a very real computer language that was given that name Brainfuck, and so we're going to have to say the phrase, Brainfuck over and over again. That's why I'm saying it right now, just to loosen you up and get you to know that this is what is going to be coming. The good news is it's going to be worth it. This is a really fascinating conversation about a super important topic, which is in some sense the topic is the origin of life, but there's not a lot of chemistry or biology or geology or anything like that in the talk, in the conversation.

0:01:01.0 SC: It's a model for the origin of life or a simulation of the origin of life done on a computer. Today's guest is Blaise Agüera y Arcas, who is a very successful computer scientist, like a real world computer scientist. He has worked for Microsoft, he now works for Google, doing things like AI, of course, but also visualization, augmented reality, questions about how machines can be creative and artistic, things like that, with real world applications. But it's led him to think more broadly about what is intelligence, what is life, what is, if you're a naturalist, a physicalist, like I definitely am, and I think Blaise also is, then you think that things like life and thought are outcomes of physical things bumping into each other in particular but especially complicated ways. And then there's an emergent higher level description of this thing that we call life. So clearly, going back to people like Schrödinger and Von Neumann and others, there's a statistical mechanics of this, right? You want to know all the different ways that you could organize atoms and molecules and so forth, how likely is it that you would get life.

0:02:18.3 SC: And you immediately say, "Well, look, of all the ways that I could take a given set of atoms or molecules and organize them, most of them don't look like living beings at all," right? Living beings are clearly a very, very organized tiny subset in the space of all possible configurations. True, that's the old sort of quasi-creationist argument, that you're not going to get life just by randomly throwing things together. In an infinitely old universe, maybe you would, that's the Boltzmann brain paradox, but our universe is not nearly old enough to make that relevant. But it's also not the right question, right? We don't just throw some molecules together randomly. Maybe we start with some semi-random configuration. It's not really random 'cause it's low entropy, but we start with some specific configuration and then we evolve it for a very long time. And that evolution is sort of interesting and explores this gigantically big space of possibilities.

0:03:16.7 SC: And then the much more sophisticated and important question is, do trajectories in that kind of setup have little sub-regions that are likely to look like life in some way? Now, the space of possibilities is so large, you can't be very realistic in exploring that, but you can start with a little toy model. And so what Blaise and his collaborators have done is write programs, not even write programs, sorry, I shouldn't say that. They've explored a system where you have little programs written in this language Brainfuck, and there's many, many, many programs. And the programs are starting literally with random symbols, okay?

0:03:57.0 SC: Imagine if you went into your Python compiler or HTML for that matter and just typed in random symbols, it would just be a mess, nothing would happen. But Brainfuck is so small as a computer language that sometimes things are going to happen. And what they show with their specific set of rules, which is not, they didn't cook in the answer, they let the different computer programs kind of talk to each other and influence each other, interact with each other, and they find the spontaneous emergence of replication.

0:04:26.0 SC: That is to say, you generate, eventually, after sort of fumbling around randomly for a little while, you find little bits of computer programs that reproduce themselves and in some sense, which we'll talk about in the podcast, hand down their genetic information to later generations. And in fact, those particular self-reproducing computer programs take over, they win, right? Because they can replicate themselves not only where they are, but in their next-door neighbors, they can fill the space in a finite period of time. So that's a kind of origin of life. No real laws of physics there, certainly no real chemistry or anything like that.

0:05:10.9 SC: But if you think that the fundamental essence of the origin of life is sort of reproduction and handing down your genetic information to your successors, then there's something like that going on. And it's not put in by hand, like a lot of simulations and things do. You can easily simulate evolution once you already have replication and genetic information, etcetera. But here is a simulation that actually starts from nothing. And the replication and the information you need to make it happen pop up just through the dynamics of the system. What are the implications of that for the origin of life in the real world, for looking for life, for thinking about what life is? Well, you will have to listen to this podcast 'cause we're going to address all those questions. And with that, let's go.

[music]

0:06:07.8 SC: Blaise Agüera y Arcas, welcome to the Mindscape Podcast.

0:06:17.5 Blaise Agüera Y Arcas: Thank you, Sean. I'm really glad to be here.

0:06:18.5 SC: So you are an author. I don't know whether... I mean, you are the first author. I don't know whether it's an alphabetical order thing or an order of importance thing in your field. How do you list the authors for your publications?

0:06:31.7 BA: Well, it varies. But if you mean the abiogenesis paper, that was work that I started kind of on my own in October, and then pulled some other teammates into. So it's a legit first author.

0:06:46.8 SC: Okay, good. Yeah, I mean, I get to be first author all the time just because I'm early in the alphabet. So I get more credit than I deserve. I know what it's like. I feel a little bit guilty, but we will get at the end of the podcast to other things you're working on. I mean, you're at Google, you have a job, etcetera. And does it seem crazy to say that this particular paper we're going to talk about is a little bit outside of what you usually do?

0:07:09.7 BA: Well, yes and no. So for the last year, so starting in October, November of last year, I've kind of changed what I'm doing. So I used to run a pretty large chunk of Google research. I had hundreds of people reporting to me and I was operating more like a VP and had a lot of administrative duties, which were pulling me away from a lot of the things that give me the most joy, the actual work and the thinking. And it also seemed to me that over the past 10 years, a lot of our bets in AI were really starting to pay off. And there's been a rush to really milk the cow, as it were, to really develop transformers and build this generation of AI and make it as useful as possible. And that's wonderful. I'm actually really excited to see that happening.

0:08:00.6 BA: But I didn't want to continue to focus on just developing that. I was really keen to go back to basics and rethink some of the more fundamental aspects of computing and AI. So I started this new group and Google was very generous in supporting me in that. And it's called Paradigms of Intelligence and it really kind of is going after fundamental stuff, including all the way back to origins of life.

0:08:27.8 SC: That's great. I love it. And am I correct in remembering that you have an undergraduate degree in physics?

0:08:35.7 BA: Yes.

0:08:36.2 SC: This is a long-running joke at Mindscape, is that I have guests on who do all sorts of different things, but they always started out as physicists before they went into...

0:08:43.2 BA: It's probably no coincidence. Yeah.

0:08:45.7 SC: Probably no coincidence. Exactly right. Okay. So, I mean, there's a lot going on in the paper, so maybe talk about what is in your mind when someone says, "The origin of life." What are the challenges that we have to try to understand?

0:09:00.8 BA: Sure. Well, the first challenge is how did life begin here on Earth? There is a specific story about that and we may never know all of those details 'cause they're lost to deep time. This whole happened 4 billion years ago. And I've always been very interested in the work in biology that really tries to unpack that. There are theories about maybe it having been RNA first and RNA world, or maybe a metabolism first that might have spun up in black smokers on the bottom of the sea where there are these hydrogen and carbon dioxide vents bubbling through these porous rock chimneys. But there's a more fundamental question, which is how is it possible for life to arise? In the traditional view of evolution, you need life in order to beget life. There was a lot of work in the 19th century trying to figure out whether life could spontaneously generate and they never got it to happen. You could only get life if life went in.

0:10:04.0 BA: And then if you look at it from a physicist's point of view, I think this perspective was really well articulated by Schrödinger in his beautiful book from 1944, What is Life, which has been quite inspirational to me. And his perspective was more thermodynamic. If you have... Normal second law of thermodynamics says things get more random over time. Life is incredibly ordered and structured. And there's no strict violation of the second law of thermodynamics there because energy has to go in. We need to metabolize. But while it's permitted by thermodynamics, it doesn't seem exactly encouraged by thermodynamics. There's something mysterious there.

0:10:43.7 SC: I've made that exact same point many times, and I love how you just said it there, encouraged by thermodynamics. It is a little bit mysterious.

0:10:48.0 BA: Right.

0:10:51.4 SC: This paper is not delving into the role of chemical catalysts or even entropy and things like that. You're purely on a computer letting code evolve itself.

0:11:05.1 BA: Yes. It doesn't directly speak to that, but it does indirectly speak to it. And in the book that I'm going to release next year with MIT Press, What is Intelligence, part one is all about abiogenesis, about this work. And it does connect it much more explicitly, both with the physics and with the biology. So there is a real connection. It's not arbitrary.

0:11:29.2 SC: I should say there is this field, and you refer to it, about a life, artificial life, different than AI. And I think as you say, I forget exactly where I read this, but it's certainly true, they usually start with something they can already replicate, etcetera. And they're asking how does complexity grow? How does the effective genome grow or whatever? But the idea of doing simulations that in some sense mimic the actual beginning of life is a somewhat understudied field, if I get the impression.

0:12:00.0 BA: Totally. I think it's never or very rarely, probably not really happened before, that we begin with just noise or randomness and get replicators, get life. And I think the reasons are similar to the puzzles we were just talking about from the biology or physics standpoint. Maybe it's partly a mental block, maybe it's an actual block, but the idea of starting from nothing, it has been understudied. And I don't think it's really been shown before in the field of AI life.

0:12:29.1 SC: There is a tension, and I'm entirely on your side vis-a-vis this tension, but there will be some people who say, "Look, unless you're really doing chemistry, you're not going to teach us anything about the origin of life." And there's others, more physics inclined, who will say, "Eh, I can build kind of a spherical cow model that gets at something, even if it's not ultimately telling me precisely how the biochemistry worked at early times."

0:12:54.6 BA: Yeah. Now, obviously, I'm very interested in the real biochemistry too, so I don't want to discount any investigation into that kind of work. But I also do think about this like a physicist and, dare I say, like a computer scientist. I'm thinking about life as a phenomenon that is more general than the particular substrate of chemistry and chemistry on Earth. And in that, by the way, I think I'm very much on the same page as the founders of artificial life, who also happen to have been the same people who founded computer science and who founded artificial intelligence. So I'm thinking especially about Turing and John Von Neumann.

0:13:33.7 SC: So is part of the inspiration, even if it's way in the background, the idea that ultimately I'm going to want to ask, here's a thing, is it alive? It might be on a computer, it might be a physical thing, but what are the rules for when I call it life or not?

0:13:49.8 BA: Yeah. I mean, up to a point, whether you call something alive or not is a matter of definition, and we have a lot of fuzzy areas, even in biology, is a virus alive or not, and so on. So seeking a more rigorous and more functional definition of life is part of the point. When I say functional, I mean in the same spirit as Turing's functionalism and Von Neumann's functionalism. So the famous Turing test about intelligence, it's all about, well, if it quacks like a duck, it's a duck. If you are talking to a computer and you think that it's intelligent and it can pass all of your tests, then if it functions intelligently, it is intelligent. And I think there's a similar functional way of thinking about life that kind of goes beyond the details of which molecules are being used or whether they're molecules at all.

0:14:46.0 SC: Good. I mean, like I said, I'm 100%. I'm not even going to give you a hard time about that. I could not possibly agree with you more. So you're going to do it by running a bunch of computer simulations, and like you said, the objective is to really start with nothing or just with randomness and kind of, under some set of rules, let it go and see if something lifelike arises. That's the basic aspiration?

0:15:11.8 BA: That's the goal, and to have as little as possible in the beginning, to have as few givens as possible. Yeah.

0:15:18.1 SC: And then one of the obstacles you run up against is that the best computer language to use for this is something called Brainfuck, which apparently is even hard to search for on the internet because people like to misspell it or something like that to make it sound less bad. But tell us about...

0:15:36.7 BA: Like put grawlixes or asterisk symbol or something.

0:15:38.8 SC: Exactly, right. So tell us about that language and why you chose it.

0:15:42.5 BA: Yeah. I had to check with MIT's contract whether if it was obscene or something, whether this would pass muster...

0:15:52.9 SC: And it's not your fault. It's a preexisting thing.

0:15:54.4 BA: Not my fault.

0:15:55.8 SC: Yeah.

0:15:56.5 BA: No, no. It was invented 40 years ago or 30 years ago, sorry, by Urban Müller, a German, actually a physics student.

0:16:02.5 SC: There you go.

0:16:03.1 BA: Go figure. And amateur juggler, apparently. So yeah, Brainfuck is not the only language one can use for doing this, for sure. And we've now tested it on many other languages as well. Our latest demo, which is very beautiful, made by Alex Mordvintsev, actually uses the Z80, the Zilog Z80 processor.

0:16:26.5 SC: Okay.

0:16:26.5 BA: Which was...

0:16:28.2 SC: I had no idea what this is.

0:16:30.1 BA: Well, it came out in 1976.

0:16:31.5 SC: Wow.

0:16:31.8 BA: So it's been around for a long time. And it powered the Osborne computers, the TRS-80 and all of that. So like we grew up...

0:16:39.6 SC: Oh, now that's my era now. Okay.

0:16:41.4 BA: Yeah, exactly. So it's a bit of a nostalgia trip. And it works just as well in Zilog assembly language. So it's not required that it be Brainfuck. But the reason that I began with Brainfuck is because it's very, very close to a Turing machine. So its design is extremely minimal. It has eight instructions. I actually only used seven of them for the first simulations.

0:17:03.2 SC: Okay.

0:17:05.1 BA: And it works on a tape that looks just like a Turing tape. So it's just super minimal. I think Urban Müller made a compiler for it that compiled it to assembly language or whatever in 173 bytes, something like that. So it's really minimal.

0:17:22.4 SC: So I will remind us, 'cause it's a broad audience, what is going on in your mind when you say the words Turing machine?

0:17:28.5 BA: Yeah. So the Turing machine is a notional machine. It's a conceptual machine invented in the 1930s by Alan Turing. In many people's minds, mine included, that was kind of the beginning of real computer science. So it was a wonderful paper in which he was trying to, not trying, he succeeded in cracking one of Hilbert's big math problems that he'd posed in the previous century, which is can one figure out a mechanical way to decide on the truth of a mathematical statement? So this problem is one that requires that you actually formulate what computation is.

0:18:11.5 BA: And it turns out that his definition of what computation is turned out to be the much more important part of that paper than the actual result, which was, no, you can't decide a priori on the truth or falsehood of a mathematical statement. But he had a very creative way of cracking that nut, which was to design a machine that would involve a tape with cells on it that you could write symbols on, and a read-write head that would be able to step left and right along the tape. And a table of rules that would say, based on the state of the head and what character is on that cell, whether one should erase, write a new character or step left, step right. And and so that was, that's a Turing machine.

0:18:56.3 BA: And then the next move, the really brilliant move was the universal Turing machine. The idea being that he first showed a Turing machine can compute anything that can be computed by say a person with pencil and paper. And then he showed that if you write the rules, if you write that table of rules on the tape itself, then there exists certain tables of rules that will allow you to interpret the table of rules on the tape and carry out the computation that it specifies. And that's... That's sort of like, snake eating its tail move gives you a general purpose computer. That's sort of the definition of general purpose computation.

0:19:34.2 SC: And when you say Brainfuck is kind of like a Turing machine, it is in fact Turing capable, right? It can do anything a Turing machine can do.

0:19:43.2 BA: Right. So this idea of Turing completeness is, does a given machine or a given mathematical system can you... Can you map it to a Turing machine? If you can map it to a Turing machine, then by construction, it can compute anything that can be computed. And and Brainfuck consists of eight instructions because it's so few, I can actually just say what they are.

0:20:07.0 SC: Please.

0:20:07.1 BA: It's... So there's a head. The head can step left, step right. It can increment or decrement the byte that it's looking at right now. So it's, the tape is a tape of bytes that can range in value from zero to 255. If you increment 255, it goes back to zero. If you decrement zero, it goes up to 255. It kind of wraps around. There's an input and output operation. So there's a... There's a console in the original Brainfuck. So output will double, will just emit the byte that is under the head and input will read a byte into that position. And then the final two instructions are open bracket and close bracket, which are looping instructions.

0:20:41.5 BA: So it turns out that for a Turing machine, you need branching in order to be able to implement loops. You need if then. And so the brackets just say at the open bracket, if the byte under the data pointer is non-zero then continue. If it's zero, then jump to the matching close bracket. At the close bracket, if the byte under the, under the head is non-zero, then jump back to the open bracket else continue. And that's it. That's the whole language.

0:21:20.9 SC: And with that, you can feed it a tape and well, sorry, 'cause you have the tape and the program in the original Brainfuck thing. You're gonna modify that, but in the original thing. So there's instructions for the program and then there's a tape and the head will just bop back and forth, reading the tape, writing to the tape. And that in principle can do any computation we know how to do.

0:21:33.1 BA: Right. With a long enough program, long enough tape and enough time, you could implement windows on that or whatever you want, although it would be an absolute nightmare. The reason that, that urban named the Brainfuck is because it is very, very hard to program it. So you look at a hello world program and it's just this incomprehensible jumble of characters.

0:21:54.5 SC: It's hard to program, but even harder to read 'cause it, like you said, it's all just like plus bracket, dot, dot, dot, dot. And you have no idea what's going on.

0:21:58.7 BA: Right. And not a very user-friendly language, but a Turing complete one.

0:22:02.7 SC: And good for your purposes, precisely because the set of symbols is so tiny, right?

0:22:09.2 BA: Exactly. It's a tiny set of symbols. It's not the smallest Turing complete language, but it's down there. It's among the smallest Turing complete languages you can make. So one can both simulate it really fast and one can do a lot of interesting mathematical analysis on it that would be harder with a more complex language.

0:22:26.4 SC: Right. And you do, and in fact, what you folks implement is a variant of this, which I already sort of spoiled, but the tape and the program are in the same place.

0:22:37.2 BA: Yes. So the thing that needed to be changed about the original Brainfuck is that it has a separate... In effect, it's really two tapes, even though that's not the way Urban put it in the specification.

0:22:50.9 SC: Yeah.

0:22:51.0 BA: So there's a, there's a program tape and a data tape. And the program tape has its own read head, which just kind of steps along and occasionally jumps back with those loops and the data... The data tape is separate. We wanted to make it self-modifying. So self-modifying code means that the code itself is actually in the data space and it can be manipulated just as... Just as well as data can be.

0:23:14.0 BA: And why did we wanna do that? Well, because I had a hunch that self-modification was actually the key to abiogenesis...

0:23:24.5 SC: Sure.

0:23:24.8 BA: To the creation of life. And I can explain a little bit more about why, but maybe I'll save that for a bit later. So anyway, there's now just one tape and that tape contains both code and data. And this means that you have to imagine that there are actually not two, but three heads now. Because the other thing... The other thing that was on the original Brainfuck was a console and we didn't want to have a console that is separate from from the tape. So everything has to be self-contained.

0:23:50.8 BA: So now you have an instruction pointer that walks along the tape. You have a data pointer that can be moved anywhere along the tape. And you have a console pointer, which says, if you're gonna print or input, like where in the tape are you going to... Are you going to print an input?

0:24:02.8 SC: Oh I see.

0:24:03.4 BA: So everything is all in the same in the same tape.

0:24:07.8 SC: Right. Good. And then, so this gives you a toolbox or a sandbox, I suppose, in which you can play. And you're gonna play by starting, like you said, with nothing and let it rip, see what happens. But there's some details there. You can't just let one program go, that would be uninteresting.

0:24:27.6 BA: Right. So the other... The other trick, and we called this environment BFF, by the way, for reasons that might become obvious soon. But, the trick is that we began with a soup of tapes. And these tapes are of fixed length. They're of length 64.

0:24:47.8 SC: Okay.

0:24:48.3 BA: And rather than just running one tape, tapes are actually run in pairs. So you grab two tapes out of the soup and you stick them end to end. And then you think of that as the tape and you run it. It's everything is self-contained. So it could modify itself. Then you break those tapes back apart and you put them back in the soup and that's it. And you do that over and over. You also, occasionally there's a mutation rate. If you allow mutations to happen, then once in a while, a byte in that soup will get randomized. It'll just get flipped to something random.

0:25:18.7 BA: And there's one more detail, which is that since it's possible for a program to get stuck in an infinite loop, you need to have either some maximum number of instructions that are allowed to run or have some probability, which is the way I prefer per unit time that any given tape will just stop running wherever it is. So those are the extra bits. There's no fitness function. In other words, there's no specific function that is saying any tape is better than any other tape. You're just plucking them out of the soup, sticking them end to end running, putting them back and repeating millions of times.

0:25:53.2 SC: And when you stick them end to end, so it's not like you take the first half of one and the second half of the other, you just... You have... I'm just trying to get in my brain what the specifics are. So you just run the two of them next to each other and there's some topology on the graph. There's a meaningfulness to nearest neighbors.

0:26:09.2 BA: Right. So each tape is 64 bytes. If you stick them end to end, you'll have 128 bytes. And you think of that as the tape that you run. Now, this may seem a little arbitrary, but the reason that that was important is because in addition to self-modification, life relies on interactions.

0:26:26.9 SC: Yes.

0:26:28.4 BA: So you have to have stuff that is interacting. If nothing interacts with anything, nothing can happen. So in chemistry, that would be molecules interacting with each other. So you could think about those tapes as being like molecules.

0:26:42.8 SC: Yeah. So the tapes are modifying themselves and their neighbors, just like people or real organisms actually do. Okay. And so starting... Give us an intuition for what a random code in Brainfuck would do. I presume it would just crash or maybe it would be an infinite loop usually. I don't know.

0:27:02.1 BA: It's actually quite hard to make an infinite loop from just random noise.

0:27:03.8 SC: That's probably right. Okay.

0:27:07.1 BA: Because remember, so in my version of Brainfuck and BFF, there are seven instructions. Every byte can have 256 values. So only seven 256ths of the bytes even code for an instruction at all. If something doesn't code for instruction, it just gets skipped over.

0:27:24.6 SC: Ah okay.

0:27:25.3 BA: So it's a no Op, as you call it in computer science. So what that means... I mean, that's roughly one in 32. That means that out of the 128 bytes in a tape, you'll only have a small handful, two, three, four working bytes, bytes that actually have an instruction on them. So what might those bytes be like? Move the head two times to the left and one time to the right, done. And no change.

0:27:57.5 BA: So in the beginning, very, very little computation is happening. And you know, it just seems like a very unpromising start.

0:28:03.3 SC: So I shouldn't say crash, but it does. It moves around and then fizzles out. It just stops and nothing interesting happens.

0:28:08.9 BA: There's nothing happens.

0:28:10.6 SC: Right. Yeah.

0:28:11.3 BA: So it is possible for it to crash. If you get to a close bracket and there was no matching open bracket, that's a crash.

0:28:17.7 SC: Ah okay.

0:28:17.8 BA: But I think that's the only way it can crash.

0:28:18.8 SC: Good. I mean, so it's harder to crash in Brainfuck than it is in just regular programming languages.

0:28:23.0 BA: Yeah. Which was also part of the point that it's kind of open-ended enough that...

0:28:27.7 SC: It's a little robust that way.

0:28:28.9 BA: It's a little robust. Almost anything will do something, even though very little of that something will be useful.

0:28:35.3 SC: And well, how quantitative can we be about that? I mean, what fraction of things that those bytes could be doing will give us interestingness in some well-defined way?

0:28:45.3 BA: Well, out of those seven instructions, only three of them actually result in a change to the tape. There's plus and minus, which increment and decrement whatever byte the data pointer is on. And there's comma, which is the copy instruction. So that was originally input, the input from the console. But if you think about print and input, they're really the same thing. They're just copied from one place in the tape to another place in the tape.

0:29:10.7 SC: Sure. Okay.

0:29:11.8 BA: Since the console and the data pointer are just different spots in the same tape. So that's why we could reduce it from eight instructions to seven. So only those three instructions can result in changes at all. So that tells you that if you don't have loops and you're unlikely to get a good loop 'cause that requires matching open bracket and close brackets somewhere that enclose one of these write statements. So in the beginning, yeah, you can be very quantitative and you can calculate the probabilities that anything will change and they're not high. The majority of interactions result in nothing.

0:29:52.5 SC: Okay. Very good. And then how many... So basically you're doing parallel many tapes, many programs, whatever you want to call them at once. How many were you doing in your simulations?

0:29:58.8 BA: So in the first ones, I did 8192 tapes. In some of my later ones, I only use 1000, 1024. So 1,024 tapes is plenty to get all of the interesting phenomena.

0:30:14.5 SC: Right. And then, so I don't wanna put words in your mouth, tell the audience what happened. You put in some primordial soup and you let it percolate.

0:30:24.3 BA: Yes. So in the beginning, there are about two operations run per interaction and nothing much happens and it looks boring unless you look very closely, but we didn't look closely till later. And then at some point, a few million interactions in, typically, everything will start to change and it's very, very sudden. So on my computer, when I first ran this, it was just sort of things were scrolling by really fast and suddenly the scrolling stopped and it was sort of going chunk, chunk, chunk, and the fan turned on. It was like suddenly a lot of computing was happening.

0:31:01.6 BA: And the number of operations running per interaction just leaps from very small numbers to thousands. And if you look at the contents of the tapes, suddenly they are full of instructions, they're dense with instructions and they're very complex. And moreover, they're replicating. So you find a bunch of copies of different programs and these programs are interacting in complex ways. So it's really quite dramatic.

0:31:29.7 SC: What is... I think this is implicit in what you said already, but what does replicating mean in this context? Is it one program is writing itself onto its neighbor?

0:31:38.8 BA: That's actually a more profound question than it sounds like. So the simplest definition of replicating is... I mean the simplest version of replication is you start running a tape and the first 64 bytes copies itself onto the second 64 bytes, for instance. If that happens, then when you pull them apart, regardless of what was in the second half, you now have two copies of what was in the first half. That's replication and that will definitely take off exponentially when it happens. But the reason it's a subtler question than it sounds like is that you can also have little bits of the tape replicating themselves, which it turns out happens earlier in the process.

0:32:22.4 BA: And you can even have situations where, for instance, one thing creates another thing, which creates another thing, which creates another thing, which eventually comes back around and sometimes creates the original. So you can have these complex life cycles, and that's a form of replication too.

0:32:37.0 SC: Sure.

0:32:37.3 BA: Anything that ultimately comes back around and generates more of you than would happen in the null case, if nothing is going on, is replication, however weak.

0:32:50.0 SC: I think that actually that is reminiscent of a finding in the sort of more chemically based origin of life context, where it turns out my recollection back when I wrote my book, The Big Picture, mumbly-mumble years ago, was that they had not built a single molecule that could sort of auto-catalyze itself. But they could build two molecule pairs where A could make B and B would make A and it would keep going.

0:33:15.2 BA: Exactly.

0:33:15.6 SC: So you're finding things like that, basically.

0:33:18.3 BA: Exactly, which is the same way that DNA replication works, by the way. You have base pairs that are conjugate and you pull them apart, one of them makes the other one and then and then they conjugate. So yeah, that's called... In abiogenesis, that's called an auto-catalytic set of chemicals. And again, I think that that's a more basic concept than chemistry. There's something pretty deep about that and what we see is exactly the same.

0:33:47.8 SC: And from a pure statistics point of view, am I correct if, to rephrase it as saying that the set of instruction lists, the set of tapes that act this way is tiny in the set of all possible tapes, but tends to take over, is more robust in some way that I'm still struggling to quite articulate?

0:34:08.1 BA: Yeah. So one of the people who really kind of informed my thinking about all of this is Addy Pross, who is an emeritus professor of chemistry at Ben Gurion University of the Negev in Israel. And he spent many years studying the chemistry of the origins of life. And he coined this term dynamic kinetic stability. So what he means by that is that normally in thermodynamics, we think about matter arriving at a more and more stable state or in general, the statistics of some ensemble becoming more and more stable. Meaning that if they start out very out of equilibrium they'll move toward an equilibrium, and the closer to equilibrium the more stable that configuration is. But what Addy Pross realized is that if you have replicators, then you have a new form of stability that arises, which he calls dynamic kinetic stability.

0:35:09.2 BA: If A makes B, B makes C, and C makes A, then that has a stability that is actually even greater than the stability of something that takes a long time to degrade, but still ultimately degrades. That replicator can last forever. You have a fragile thing like a soap bubble, or you can have a really robust thing like granite. But no matter how robust it is, if it's passive, every interaction it has with the world can only degrade it. Whereas the special thing about life and about replicators generally is that they can push back actively against the forces of entropy and they can last forever.

0:35:45.0 SC: So that's very evocative. Does it... Do you see that in the simulations? Is there some kind of self-repair? Do you see what would be replicator get influenced by its environment in a negative way and then bounce back?

0:36:00.8 BA: Absolutely. We do see that. But the very trivial way in which we see that is just that once you have a population of replicators, that's more robust than one of them. If it's replicating, then if one of them gets damaged, well, there's another one that can still replicate. So population is the first way that robustness happens. There's a force actively making it expand, and so if you damage it, it still comes back. Now, you can go further and it can become actually robust and repair themselves, and we do see that kind of stuff happen as well. But even replication alone is already dynamically, connectively stable.

0:36:33.7 SC: And you said that you didn't put in a fitness landscape or fitness function. You didn't sort of rank the success a priori, but isn't there effectively a fitness function? Or is it just that you sort of... Well, let me ask the phrase as a question. Have you rediscovered natural selection?

0:36:54.8 BA: Yes.

0:36:55.0 SC: Okay.

0:36:55.4 BA: We have absolutely rediscovered natural selection. And this goes back to Addy Pross as well. The way he puts it is that dynamic kinetic stability... Sorry, let me just...

0:37:04.8 SC: Go ahead. Yeah.

0:37:08.9 BA: The way Addy Pross puts it is that dynamic kinetic stability is Darwinian selection. And Darwinian selection is just another way of putting thermodynamic stability in that dynamic setting, where you have replicator dynamics in addition to just the normal dynamics of entropy. So yes, there's a fitness function there in the sense that if you see a replicator there at one moment, and you see another string that is not a replicator, and then you look again later on, you're likely to still find the replicator, and you're likely not to find the string that wasn't a replicator because it will have been either destroyed by entropy, by random mutation, or overwritten by the replicator.

0:37:51.1 SC: So, when I think about, I don't know, I wanna understand this for my own selfish purposes. I'm doing research in closely connected areas here, and you're very helpful right now. Is it really natural selection in the sense that when I think of natural selection, I think of like a handing down of a genome from organism to organism and sharing those and mutating them. But I guess you're gonna tell me that the whole tape is kind of like a genome.

0:38:17.5 BA: This is also a great and profound question because there is actually a big change that happens at some magical point in this kind of abiogenesis process. Where you go from just an autocatalytic set, meaning just things that, tend to kind of, sort of make something else that makes something else, that makes you. To something that has a genome. And what having a genome means is that you now have a list of instructions for making yourself. And if those instructions are changed in any way, that change is preserved in the descendants. In other words, you have heritability.

0:38:54.6 BA: So this goes back to some of the, I think most foundational work in biology that is not generally acknowledged as work in biology and it's by it's by John Von Neumann, one of the founders of computer science. So when he was messing around at Los Alamos with Stan Ulam, and they invented cellular automata. One of the applications that he invented for cellular automata was self reproduction. And he designed this amazing self reproduction system using cellular automata that was only simulated on a computer for the first time in the mid '90s because it's actually... It's very hard to actually make it... Like running it is very computationally intensive.

0:39:35.2 SC: We finally caught up to the brain of Von Neumann in our computer architecture.

0:39:38.1 BA: Exactly. I'm not sure if we've caught up, but we got closer, but his insight is actually very easy to to express, but very profound. So he said, if you want something that is able to evolve in an open-ended way, replicate and evolve, it needs to have something like a genome. And basically he was asking, how does something like a bacterium, how does life exist? How is it possible that it can build another copy of itself that is just as complex as it itself is? That seems like pulling yourself up by your own bootstraps. It doesn't make any sense.

0:40:11.3 BA: And what he realized is that you can do it if you... If you have the following things. First you need a tape, like a Turing tape that has the instructions for building yourself. And then you need a machine, A, which will chunk along on that tape and follow the instructions and build whatever the tape says. And then you need a machine B, which can copy the tape, assuming that the tape itself is also made out of stuff that you can find in your environment. If the instructions for making machine A and machine B are on the tape, then you have a replicator. And what's so cool about this realization is he wrote this all up in 1951. This was before the structure and function of DNA, the discovery.

0:40:54.0 SC: Yeah. It's an obvious thing you think of when you say those words out loud. Like yeah, that's what DNA does, right?

0:40:58.3 BA: Exactly. So he called it, he totally called it his machine A is what ribosomes do., his machine B is what DNA polymerase does. And of course, the tape is DNA. And the instructions for building ribosomes and DNA polymerase are encoded on DNA. So it's exactly right.

0:41:15.7 SC: It is one of those events in the history of science that gives you hope for the efficacy of pure thought. Like, you wanted something to work out in a certain way, how could it possibly do it? And you figured it out. But it wasn't that many years before we figured out DNA, I do wonder how influenced he was by people like Schrödinger talking about these things.

0:41:36.8 BA: I'm sure he was. And Schrödinger did also anticipate DNA, although Von Neumann went a little further in that he separated, if you like, the machine A and machine B. Like he realized that there had to be something different about the tape versus the ribosome, which Schrödinger didn't quite connect in 1944.

0:41:53.8 SC: Good.

0:41:54.1 BA: But, yeah, it was very profound. And that is more than an autocatalytic set for two reasons. One is heritability. But the other, which is I think even deeper, is that this is a Turing machine. What what Von Neumann described is a computer, machine A and machine B have to be computers. And the reason is you can't execute the instructions on a tape without having a loop. Right. That says like, if this, then add that, and, at the end stop.

0:42:18.0 SC: Yeah.

0:42:18.2 BA: So there's a loop there you have all of the requirements, of touring completeness of a computer. So what Von Neumann really said is nothing can be life without computing. Or rather that life is computation at a very deep level.

0:42:37.5 SC: I love that. I wonder if I've ever heard that phrase that way before, but I don't think I have. But it has finally stuck in maybe I'm at the right point of my education to appreciate something like that.

0:42:46.0 BA: I don't think that this has actually really been said before. I could be wrong. I mean people always... I mean, these ideas are always bubbling around and I feel like they're in the air but I at least have felt like, like this has come as an aha moment for me, just in the past few months.

0:43:01.9 SC: Good. Yeah. No, no, no. When you say it out loud, you're like, oh, yeah, of course. But I've never heard anyone say that out loud before, so that is wonderful. So, okay, so in the... Back to the reality of this computer program you're running, how do you know when this happens? You said you were looking at an output, but probably there's something more sophisticated going on.

0:43:18.5 BA: Yeah. It's not just listening for the fan to turn on. Well, so the first, the most obvious thing that happens is you can visualize it very beautifully if you just draw a dot on a graph for every interaction where the x axis is time And the y axis is how many operations ran in that interaction. So for a long time you just see it's low. There aren't many operations happening. And then suddenly at some point, which, you know, depending on randomness, it could be after 1 million, it could be after 10 million interactions. Suddenly there's this wall of blackness, like the thing is computing really hard. All of these interactions are are resulting in thousands of operations running. So that's the tell that something has... Something has happened.

0:44:05.6 BA: You can also measure the Kolmogorov complexity of the soup. So Kolmogorov complexity is very simple to approximate. You can just zip the soup. So you just take the all the bytes in the soup and you think about it as a file and you zip it, and then you take the ratio of the zipped file size to the original. That gives you a sense of how compressible it is. And in the beginning, when you start off with just noise, it is incompressible random bytes are incompressible try at home. If you make a file full of random numbers and you zip it, it will stay the same size. It'll actually grow a little bit. 'cause there's like a header. But the moment you start to have replicators in there you expect that it's gonna suddenly become a lot more compressible because many of those strings, many of those tapes can be expressed as pasted together parts of other tapes. And that's what you see, you see this dramatic transition from incompressible. It's like a gas to it's like a crystal, not quite like a crystal, because there's still a whole ecology of different tapes, but its complexity drops way, way down.

0:45:10.4 SC: So there's a phase transition.

0:45:11.6 BA: Yes.

0:45:12.6 SC: And the order parameter could be either the number of computations being done or the algorithmic complexity of the soup.

0:45:20.6 BA: Yes. Yes. That's right. It looks exactly like a phase transition. And usually when a physicist talks about phase transition, we think about correlation functions. So in a gas, the correlation function is just a delta function. You know, the other particles could be anywhere. If it's ice, then it's this very structured crystalline structure. Well, compressibility and that correlation function are obviously much the same thing. Gas is incompressible because the position of one particle doesn't tell you anything about the positions of the other particles. So you could call that first stage a Turing gas, which is what Walter Fontana who is also a pioneer in abiogenesis, on computer called it. But then after that phase transition, it's something else. It's no longer a gas. I would call what you get afterward, computronium, meaning it is a new phase of matter, if you like that is all about computation which I think another word for that is life.

0:46:16.1 SC: Yeah. No I'm on the train. I guess the one thing that I don't... If I wanted to be the skeptic, or at least the curmudgeon worrying about chemistry and things like that, a computer program where you have some instructions to change what's on the tape seems to be lacking some notion of energy or a Hamiltonian or dissipation or entropy or something like that. So ordinarily when I have a phase transition, you know, I'm thinking of, oh, the system has found a lower energy configuration it can be in, but you don't have energy or do you?

0:46:51.6 BA: Not in any obvious sense. So, nothing is conserved in BFF. Bytes aren't conserved time isn't. Everything is just in just pure information. So one can talk about entropy, but one can't talk about energy. However, there is a I think a deep connection with energy in the real world, which is that we know that computation requires energy. Now there is this whole field of reversible, so-called reversible computation, but the way you get reversibility in computation is by having these so-called ancilla bits, extra information that comes out that you have to store somewhere.

0:47:34.8 SC: Right. You make the system bigger.

0:47:38.5 BA: Yeah, exactly. So in a way, it's just saying like, we shrink the part of the system we look at in such a way that we're not looking at the extra information. So I think to make a long story short, I think there is something profound about computation that requires energy use because of its irreversibility, because computational operations involve these irreversible steps.

0:47:58.9 SC: That makes perfect sense to me. But I can't quite in my brain connect it to the robustness and survivability and hegemonic aspirations of your reproducing codes. Is there a physics-based way of saying why they want to take over there? There need not be, but I'm just wondering.

0:48:18.3 BA: Well I think that the reasons they wanna take over are purely statistical. So in that sense you don't have to invoke energy. You can just invoke statistics, likelihoods of finding something later, you know, if you find it in the present. But in real life because heritable replication requires computation. In other words, you can't have a Von Neumann replicator without it being made out of Turing machines that are computing. That means that you need an energy input in order to get a replicator. So that's why metabolism is required in real life to have replicators.

0:48:53.8 SC: Maybe this is another... Maybe it's a weird out of the field question, but, or maybe I'm answering myself in my brain, because you already said there's no conserved quantities here. But ordinarily, when I take a physical system and just let it go, eventually it will reach equilibrium. I mean, it loses all structure. I wrote a paper with Scott Aronson once where we showed that complexity can grow for a while, and then eventually it's gotta fade away 'cause you're gonna equilibrate. But I'm thinking that in your thing, it's gonna remain in this fun complex phase more or less forever.

0:49:21.7 BA: It will. And the reason is that it's a dissipative system. So the fact that it's computing, the fact that you're constantly computing means that effectively there is energy constantly going in.

0:49:32.3 SC: So you have a resource, you have the sun.

0:49:33.5 BA: Yeah. That's why the fan is going on my computer when I'm running BFF. But it won't... So yeah, it won't... The order will not go away, the structure will not go away, but neither will it stabilize, to just one thing. So it's this very complex ecology. And what is so wonderful about what happens after this transition to life is that you might think naively, oh, one replicator takes over and that's it. It's just a crystal of that one thing. It's not, you have this whole kind of power law distribution of different replicators all interacting with each other, and they keep evolving forever and changing.

0:50:09.6 SC: Wonderful. And it does remind me that it's probably now time for you to tell us what BFF stands for.

0:50:13.0 BA: Well, the first BF still stands for Brainfuck. So given that it's interactions between two tapes, you might be able to guess what the second F stands for as well.

0:50:21.6 SC: Very good. We'll leave that to the imagination.

0:50:22.0 BA: But, or we could just say best friends forever.

0:50:24.4 SC: Best friends forever. That's even better. Okay. Good. Now let's, let's try to relate this to questions that are sometimes raised about the origin of life. Like, is it... Does it require fine tuning of the laws of physics? Are there free parameters in your process that could have been changed and made the results different?

0:50:47.1 BA: Yes. So there is one thing that went in, which is the design of the language. And we do know that different designs of language result in either very different times to abiogenesis or in some cases we don't see biogenesis at all. Which I think means just that the time is so long that we're not able to see it happen.

0:51:09.4 SC: Okay.

0:51:09.5 BA: So one could almost write a theorem. In fact, one could write a theorem that just abiogenesis will happen in this kind of environment, in an environment. In other words, where computation is possible and where there's a noise source and where there are interactions, it will happen. But the question is how long statistically will it take. And details of exactly what the instruction set is can make that vary quite a lot.

0:51:35.0 BA: One of the really profound results, of this that is not in the original paper, but that I feel like we've just figured out again in the last few weeks actually, is that there's a classic view of evolution that it all happens via Darwinian selection. Jacques Monod, one of the winners of the Nobel Prize, is famous for saying like, it's just chance and necessity, you just have random mutations and they're already in selection, whatever sticks. It's spaghetti being thrown at the wall. It's a million monkeys and a million typewriters. And eventually things stick and there's a ratchet. So we now know that that's not how this works. And there's been a kind of rising tide of skepticism about that very reductive Darwinian view for many years.

0:52:22.3 BA: But I think we now kind of have the receipts. So what is actually going on and well, I should say, what are the receipts? The most obvious receipts are that if you turn the mutation rate all the way down to zero n BFF and you just start with 1,000 random tapes of length 64, and you let it go without any mutation, you still get complex life arising. And that's kind of mind blowing because, you know, 1,000 times 64, like 64,000 random bytes, that's just not a lot of monkeys and not a lot of typewriters. There aren't enough characters there. You can barely find three working instructions in a row.

0:53:00.4 SC: Sorry, there's still randomness in the sharing between nearest neighbors, but there's not randomness in mutations.

0:53:03.9 BA: Right. So there's randomness in the initialization. You start off with random bytes. And there's still randomness in choosing neighbors to interact and choosing which ones to interact with. Although frankly, I'm pretty sure you could get away with that too. I mean, you could just say everybody interacts with everybody and we just, you know, go on that way. That would work just as well. For sure.

0:53:22.1 SC: So the only randomness would be in the initial configuration.

0:53:24.2 BA: Yes. And that just doesn't seem like enough randomness to generate these very complex programs that come out. So what's going on? Well, when you look closely at what's going on, what you see is the following. First of all even from the very beginning before a replicator arises, you already have individual instructions forming autocatalytic sets. Meaning if you have a copy instruction for instance, then there is some possibility that what it generates is also an instruction. If there's a no Op, if there's a non instruction, there's no possibility for it to make anything.

0:54:01.5 BA: But if it's an operation, then there's a possibility that what it will make is another instruction, and maybe that other instruction will come back around and eventually make another of it. So in other words, you already have the makings, like the most primitive life forms, in a sense, are literally just single instructions. And they begin to beget each other, instructions beget instructions. You start to see the number of computations rising if you look closely right from the very beginning.

0:54:29.1 BA: And and so you begin to see more instructions coming in and they're kind of moving around at random, they're copying themselves into random spots. And it's a creative process because once in a while, if a couple of them end up in conjunction and together they can replicate more effectively than they could separately, then they're likelier to survive. So you get symbiosis really as the driver of evolution, this symbiosis between instructions to make little tiny programs, symbiosis between those little tiny programs to make bigger imperfect replicators. And eventually those bigger imperfect replicators, which are all madly writing over each other, competing, cooperating, will eventually fuse into a stable whole tape replicator. So it's symbiosis all the way down.

0:55:15.2 SC: Right. Okay. Good. So if the audience will indulge me in being a little specific here, because you're provoking me to think of new theorems to prove, because in that case that you thought about where there's or either there's no randomness in the interactions. Okay. There's only randomness in the initial conditions, then the evolution is deterministic, right?

0:55:38.2 BA: Yes.

0:55:40.0 SC: So in that case if you think that that will with high probability lead to this takeover by replicators, then there is some statistical mechanics statement, right? It's not saying that most instruction sets are replicators, but the future trajectories of most instruction sets will end up in this replicator dominated regime.

0:56:00.9 BA: Yes. It's telling you that computing is a dynamical attractor.

0:56:03.2 SC: Yes.

0:56:04.5 BA: And it's a dynamical attractor because only by having computing can you get replication. And replication is a dynamically kinetically stable state.

0:56:17.0 SC: Because the evolution is not reversible, right?

0:56:19.3 BA: Right.

0:56:20.8 SC: Okay. So you can get attractors and you do. Good. I would like to see that theorem, that would be a good one. I'm looking forward to that coming out.

0:56:26.0 BA: If you are a game to work on the theoretical physics of this, we would love that.

0:56:34.8 SC: Let's talk. Potentially, I don't know whether I'm competent, but I'm super duper interested. So Good. Well, that's very good.

0:56:41.0 BA: It's very Santa Fe for sure.

0:56:42.4 SC: It is. Absolutely right. So at the end of the day, how grandiose can we be about drawing implications from this study? For example, for how easy it is for life to form in the more conventional wet and sloppy biological sense?

0:57:00.6 BA: Well, I think that there are a lot of pretty grandiose conclusions, which is why this is a whole book. So first of all, it seems to me that life wants to form. It's the very opposite of what Francis Crick once said about life being like a miracle. It's hard to imagine how it could possibly happen. I think it's the opposite because computation is numerical attractor, I think that it will form whenever it has a chance to. And I guess as we start to explore the moons of Jupiter or have better telescopes or whatever, maybe we'll start to see real evidence of that.

0:57:40.5 BA: Furthermore, I think we can say that because symbiosis is the driver of evolution, there's this kind of ladder wherein more complex entities form out of simpler entities. And I think that's a very general property as well. Lynn Margulis famously thought that this was the way evolution worked. She was the discoverer of mitochondria having been endo symbiotic and thereby forming Eukaryotes, she believed that all sorts of things, all of the organelles of the cell had been free swimming originally. She was wrong, probably, but I think she was right at a deeper level, in the sense that the idea of an organelle evolving inside a cell, it's still an evolutionary step of a symbiotic character, whether or not it began on the outside. The inside of a cell is just as fertile an evolutionary landscape as the outside.

0:58:30.6 BA: And in fact I haven't... I'm realizing I haven't mentioned this, but even after that transition to full tape replication, we see the amount of computation continuing to rise, the number of characters that compute still continue to rise. And the reason is that when the whole tape is getting replicated, not all of it is needed for the instructions that do the replication. So it's an ecology, if you like, where this whole process can repeat and you get replicators and side replicators, and sometimes those will confer resistance to mutation to the larger replicator and so on.

0:59:02.7 SC: So, okay. So I think that I would sort of tentatively conclude that we haven't learned much about the robustness of the origin of life to changes in the laws of physics, because if you change the laws of physics of our world, that'd be like changing the instruction list or whatever, and maybe you would just get something that produces nonsense or only has one instruction. But given that we know the laws of physics, I think you're making a strong but plausible claim that this should increase our credence that life's gonna pop up everywhere. Some kind of life, maybe not intelligent technological life, but some kind of complex computing life.

0:59:40.3 BA: Right. There are barriers to every symbiogenetic transition, and they're statistical, and they could be a varying sizes, right? Those steps can be a varying sizes. So you're not guaranteed that you'll make your way all the way up the staircase as it were. But there is a real tendency to go up the staircase.

1:00:00.7 SC: Right. Okay, good.

1:00:00.8 BA: And every time you go up to the next step, you know you have a chance to get to the next step. Now, as for the laws of physics, we know that the laws of physics in our universe allow computation. So that means that if you like, there are many no Ops, right, in the universe, many interactions that are not part of a set of operations that form a Turing complete set and thereby also form an autocatalytic set. But if there is an autocatalytic set in there that is Turing complete, that's sufficient. And, and we know that you can make a computer out of almost anything right out of...

1:00:35.9 SC: We've done it, we've made computers out of things that's an existence proof. Yeah. Okay. Good.

1:00:41.8 BA: Exactly.

1:00:42.8 SC: This is probably unfair, but does it give us any inspirations for how to look for life elsewhere?

1:00:50.3 BA: That's a great question. And it's definitely something I've been thinking about. There are relationships between these ideas and some of the ideas of Lee Cronin and Sarah Walker constructor theory or assembly theory, sorry.

1:01:05.8 SC: Assembly theory.

1:01:07.2 BA: Assembly theory.

1:01:07.2 SC: It might also be connections to constructive theory, which is Marletto. Yeah.

1:01:09.3 BA: Constructive theory too. Yeah. Which is a whole... That's right. So Chiara Marletto's work with constructive theory also very relevant here. So yeah, those are connections that have yet to be really fleshed out. So Sarah and Lee believe that there are implications for how to look for for complexity elsewhere. I think that assembly theory is quite compatible with what I'm describing. I don't know if what I'm describing adds more meat to what we should be looking for observationally. It might.

1:01:42.4 SC: Okay. Fair enough. And I would be remiss if I didn't give you a chance to talk about the many other things you do. This is kind of not your... It has not been like your main job title, and you're writing books about all sorts of things. How should we segue into this? Should we talk about what is intelligence, since we talked about what is life?

1:02:00.4 BA: Sure. So there is a reason that... And you're right, abiogenesis and origins of life are definitely not my field, and I've been working on it for less than a year, but...

1:02:11.7 SC: Got it.

1:02:14.7 BA: However, our group has been working in a life related stuff for a while. So Alex Mordvintsev, who I mentioned earlier is also the inventor of Neural Cellular Automata, for instance, which were very beautiful kind of mashup of cellular automata as invented by Von Neumann. And neural nets and also morphogenesis which really was pioneered by Alan Turing. So the idea behind NCAs, behind Neural Cellular Automata is that you have a grid of pixels, and in every pixel, you have a neural net. It's the same neural net everywhere. And it senses and modifies the local concentrations of a handful of channels. Those channels are scalar values. You could think about them as morphogens. Meaning as chemicals that allow cells to communicate with each other.

1:03:08.6 BA: And you can train one of these NCAs to make any image you want. The first one that I ever saw was like a lizard emoji, and you could like, wipe out its head as well as its tail and it would regenerate itself. So it's essentially a model for morphogenesis that combines cellular automata with neural nets. So we've been thinking quite a lot about local computation both because it's a way to attack efficiency in AI computing. And ultimately, all computing has to be primarily local or it's gonna be inefficient, and also as a way of thinking more broadly about about learning.

1:03:47.6 BA: Because obviously life is all about learning in some sense, right? The whole point of a replicator is to produce more of itself in its environment. And as that environment becomes more complex and includes many other replicators, this kind of dynamical modeling starts to become more and more a part of it. So if you just keep walking along this symbiotic path, you get eventually to brains and to AI.

1:04:17.7 SC: I guess in your model, in the model we've been talking about in the paper so far, the "environment" is just sort of the nearest neighbors of each tape. But a possible next step would be to like throw in an environment to have just different... I don't even know what they would be, but how would you model being on a planet, versus not being on a planet or being in the ocean versus being on land? I don't know.

1:04:40.9 BA: It's a great question, and there are... We've definitely sort of thought about and tried out a little bit some approaches like particle NCAs plus BFF, it's particle NCAs like a neural cellular automata, except that there are particles that can move around rather than just pixels that stay put. So yeah, those are all exactly the kinds of mashups that we'd like to try. Actually, the Z80 simulation that doesn't use Brainfuck, but uses the Z80 assembly language instead, it actually works on a grid. So it's a grid of 20 of 200 by 200 processors, and their interactions are all nearest neighbor, rather than random. And you get these spreading waves of replicators of different species and stuff.

1:05:25.5 SC: Right. And is there a video?

1:05:27.2 BA: There is, yeah.

1:05:28.7 SC: Okay, good. I'll have to look for that.

1:05:29.9 BA: Yeah, I think Alex is just putting it up on the web now, so so yeah, I'll send you the URL.

1:05:35.7 SC: Yeah. There is this remarkable universality in these kinds of videos, but also just the concepts behind them of phase transitions and domains of things growing, whether it's the Ising model or the shelling model in social sciences and everything that it does attract a certain Santa Fe Institute kind of person to think there must be connections there. It can't all just be coincidence. There must be ways of thinking about this that are higher level and bring everything together.

1:06:08.8 BA: Yeah, I think so. I've thought for a long time that intelligence is fundamentally symbiotic in the sense that the social intelligence hypothesis holds that we are smart because our environment is each other. And because you're constantly trying to model others and thereby also model yourself and how others see you and so on, you end up with these intelligence explosions precisely because our environment is each other. So I think there's a deep continuity between these very, very primitive replicating programs and that perspective.

1:06:43.5 SC: Of the many previous podcasts that I've had that are relevant to what you just said, Hugo Mercier, do you know his work? Yeah.

1:06:50.1 BA: Yeah, I do. Yeah. The Mercier and Sperber book, the Enigma of Reason is... It's one that I cite in my book. And I very much agree with their ideas about language.

1:07:02.5 SC: And so you're pointing in the direction of saying that not only life, but intelligence might be more ubiquitous than we think with obvious connections to we're building intelligent like things. So what is your take on the intelligence of modern AI models?

1:07:19.3 BA: Well, when we first began working on AI, I think a lot of people weren't thinking about social intelligence, and they were just thinking about tasks. And so there was this long period, well, I don't wanna go through the whole history of AI, but the supervised learning era was all about training models to optimize something. And you might notice that BFF is not optimizing for anything. Yes, it tends statistically right, toward like what persists, exists, but there's not a... We haven't defined a task. And the interesting thing about AI that was specific to doing a task is that, the best it can do is to do that task. So that's why we needed the term AGI. Originally, AI meant something you could have a conversation with that could do all the various kinds of things that we do. They could fold the laundry, walk the dog, and then people started talking about AI as speech recognition, face recognition and character recognition.

1:08:23.0 BA: And I was like, that's not AI. And the moment we actually came up with real AI was the moment we stopped optimizing for specific tasks and started to just model freeform text on the internet. Now, text on the internet is obviously not everything, but language is special in the sense that it represents everything in our umwelt that we care about enough to talk to each other about. So it's a microcosm of everything. And it's just modeling that. It's just trying to predict next tokens which amounts to building a model of that entire distribution. And that was intelligent. I'm definitely not in the majority on this, but I believe that today's AI models are absolutely intelligent. There's a lot of talk about this. It's just next token prediction. It's just this, just that. I think brains fundamentally are about predicting the future, and the moment we just started to try and model that, lo and behold, we got out stuff that is smart.

1:09:25.0 SC: Right. So your attitude is not that large language models mystically are more than next token prediction, but rather that our brains are secretly next token prediction.

1:09:36.1 BA: Yeah. Although the just it conceals a lot of...

1:09:40.2 SC: A lot I get it. Yeah.

1:09:41.3 BA: Beauty and complexity. In order to do a good job of predicting the future, you have to generalize, and generalizing means building internal representations, doing all sorts of very sophisticated modeling.

1:09:51.8 SC: So my line has always been that LLMs in particular are not designed to think in the same way as human beings do, but rather to sort of mimic the output of human thought. And maybe it is possible that in the process of mimicking the output of human thought, they end up thinking like us. To me, there are enough counter examples of simple questions you can ask that any human could answer, but the LLMs fail at to assure me that that's not what's going on right now. But I don't know, you know this game a lot better than I do.

1:10:26.9 BA: Well, it's very much a moving target. There's a lot of gotcha thing happening on the internet in the last year of like, oh, look at this stupid thing that the LLM said. To be honest, one of my first reactions when I started to see that kind of stuff is, boy, these models are getting hammered. I can only imagine what would be happening if I were somehow able to be replicated a billion times and get hammered with questions and need to respond immediately. And like, how many gotchas you would find in that. You're like, the null distribution, let's put it this way, has not been well explored.

1:11:02.4 SC: Fair enough.

1:11:04.6 BA: But I think the point is nonetheless right that the profile of competencies and incompetencies looks pretty different from the average persons. And of course, I'm not arguing that everything about the way they work is the same as the way brains work. Not at all. We have a very different architecture. Neurons are not the same thing as artificial neurons in neural nets. The way we've evolved has a lot of path dependence. But nonetheless, I think that there is something profound about the functional standpoint just as with life. There is something deep that is going on, which is about modeling your environment and predicting it and doing active inference on it, meaning that you're actively bringing about your own future as part of your actions. And it was only when we started to in effect implement that kind of active inference that we began to get models that started to pass the Turing test. And the whole point of the Turing test is if the model behaves in all of these ways, then the function is right.

1:12:11.8 SC: Yeah. Right. I think the answer is yes, but are we going to have to sooner rather than later confront the question of agency and rights to AI programs?

1:12:23.2 BA: Well, I think the two are very different questions. So agency, yes, I think that we tend to reserve the term agency for humans and even withhold it from animals and plants and so on, for reasons that are quite arbitrary, and that don't have a lot to do with anything you can really measure or study. So do plants have agency? Do mice have agency? Yes. Do AI models have agency? Yes. In particular, if you start to have them... Many of the respects in which they have little agency at the moment have more to do with how we have deployed them than they have to do with the models themselves. If it can only respond to a chat interaction and not make any moves of its own as it were, then its agency is very limited. But that's not about the model, it's about how it's been embedded in the socio-technical environment.

1:13:21.9 SC: I think that's fair. I asked the question because I really don't know what the answer is, and I am curious. I'd be very happy to attribute more agency to a good modern AI program than to a tree, but I think that it might be low in either case. I'm not sure yet. I could be convinced.

1:13:39.8 BA: Well, there's a wonderful book that I read years ago by James C. Scott, the agronomist. The late James C. Scott, unfortunately, I think he's just died recently, but it's called Against the Grain. And he questions whether we really domesticated wheat and other agricultural plants. The basic observation being human life got a lot worse after we began farming. And it has only recovered very recently, like very recently since 1900 or so. And there's a way of thinking about what happened in plant domestication that looks more like plants domesticated, and even concentration farmed us essentially. They enslaved a lot of humans to plant massive massive fields of them and take care of all of their needs, at great expense to human health and wellbeing. So, I say this not because I'm necessarily strongly advocating that point of view, but because I think it's like a Necker cube. You can look at it both ways. Agency is not simple.

1:14:49.0 SC: Well, it's the selfish gene idea, right? And if we try to be a little bit less judgy about it, and we start thinking in terms of the statistical mechanics of trajectories, then maybe it makes perfect sense that this sort of symbiotic relationship was... You can't attribute the causal agency to either one or the other by themselves.

1:15:08.2 BA: Exactly. And one of the points that, that Mercier and Sperber make in their book, also Sloman et al., in the knowledge illusion is that we tend to over-attribute, if you like, agency to ourselves in a big, big way. And not only over-attribute agency, but over-attribute knowledge understanding, like, oh, humans can do this. Humans can... Your humanity is great at this, that, and the other. The average New Yorker doesn't know how a toilet works, and would be useless if actually put out in the jungle to fend for themselves. So I think that it's useful to rethink all of this. I'm not arguing for robot rights. I do wanna be clear about this.

1:15:49.1 SC: Well, no, but at some point we're gonna have to have a serious conversation about it. I guess that's the only as far as I would be willing to go.

1:15:55.9 BA: I do think that we're gonna have to have serious conversations about how we think about the relationship between human rights and the various things that we have reserved kind of to humanity as kind of copyrighted the, only we've got. Only we've got agency, only we're intelligent, only we this and that. I'm okay with us making various political decisions about how we want humans to be treated as distinct from various other kinds of entities. But I think we should be honest with ourselves that a lot of that has to do with the fact that we are humans who make these decisions. It's not some view from above wherein we deserve that because we've got souls and nothing else has a soul.

1:16:42.2 SC: Well, maybe that's a perfect segue to just the wrapping up kind of thing I wanted to ask about, which is your other book, Who Are We Now? Great title. We human beings, right? And comparing who we are now to maybe who we used to be, who are we now? What's the answer?

1:16:57.7 BA: Well, there's a connection between that book and everything we've been talking about which is that, my view of the change in human identity that we have undergone over recent times, especially since the melting of the glaciers in the last 10,000 years been accelerating, is that, it's all about urbanization. This is also a very Santa Fe idea, and that we have become a collective superorganism. Human intelligence is, if you like, a kind of super intelligence that has come about through us symbiotically working together in a new way that that we didn't for the first couple of 100,000 years that we've been around. So I think it's exactly another of those transitions of the kind that we see in BFF, if you like. And we, in not understanding that we've undergone that transition, we continue to confuse what human means by attributing that larger collective thing to individuals when in fact, it's something new.

1:18:03.8 SC: I guess the only edit I would do there is you say, having undergone the transition, I think we're in the middle of the transition.

1:18:08.7 BA: We're in the middle, yeah.

1:18:10.1 SC: We're nowhere close to the end, which makes it even harder to figure out what the truth, how to deal with it, I suppose.

1:18:17.8 BA: I agree. I think we're in... Yes. I overstated we are in the middle of it, and I think a lot of our agita right now comes from being in the middle of it. So even for instance, time to bring a little bit of geopolitics into it, when you and I were growing up, we were in the middle of a hemispheric cold war of USSR versus the West. And you could imagine one of those collapsing and the other one winning, right? There was a zero sum kind of thing there, and that's what happened. So the economy of the USSR could collapse, and that would mean that the West had won. Now if you look at the rhetoric of say China versus the US, it's completely different because the two economies are intimately intertwined. You can't have the Chinese economy fail and that be a good thing for the US or vice versa. So we're kind of in it now at planetary scale, and yet we haven't quite understood that we have to be operating at planetary scale yet.

1:19:14.6 SC: A different former guest of Mindscape is Henry Farrell. And his phrase for that is weaponized interdependence.

1:19:22.2 BA: Yes.

1:19:22.7 SC: We have to learn to live along. It's not mutually assured destruction, but it's, if we don't all succeed, then it's gonna be bad for everybody.

1:19:32.0 BA: Right. Well, I think what we have is mutually assured survival, and if...

1:19:37.7 SC: If we choose wisely.

1:19:38.7 BA: If we choose wisely. And if we don't choose wisely, then we're... Yeah, we kind of can only go forward or back. I think we can't quite stay where we are.

1:19:48.6 SC: That's a very set of wise words, very wise set of words to end on. I can't do any better than that. So, Blaise Agüera y Arcas thanks very much for being on the Mindscape Podcast.

[laughter]

1:19:57.0 BA: Sean, thank you so much. Wonderful, wonderful questions and insights and thoughts and yeah, the door is wide open if you're interested in working on this stuff.

1:20:06.5 SC: Let me think and let's talk. I'm very interested, so, all right. Thanks.

1:20:10.7 BA: Take care.