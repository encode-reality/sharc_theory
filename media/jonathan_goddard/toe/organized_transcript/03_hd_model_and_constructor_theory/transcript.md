# HD Model And Constructor Theory
## Timestamp: 00:11:21

# tactiq.io free youtube transcript
# Jonathan Gorard: Quantum Gravity & Wolfram Physics Project
# https://www.youtube.com/watch/ioXwL-c1RXQ
00:11:21.040 but the tools weren't available at the time?And you think back, like, maybe he had a sketch,
00:11:24.920 but it wasn't, well, it's Leonardo's sketchversus the Mona Lisa.
00:11:32.860 Right, right.I think the Leonardo sketch versus the Mona
00:11:34.610 Lisa analogy is probably the right one.So my suspicion, based on what I know of the
00:11:41.050 history of that book, and also based on whatI know of Stephen's personality, is that Stephen
00:11:45.070 had proved it to his own satisfaction, probablynot to the satisfaction of anyone else, right?
00:11:49.550 So I think, you know, many of us are likethis, right?
00:11:52.690 Like if you encounter some problem, or, youknow, some phenomenon you don't really understand,
00:11:59.250 and you go away and you try and understandhow it works, or you try and prove some of
00:12:02.070 the results about it, and eventually you convinceyourself that it can be done, or
00:12:06.020 that you convince yourself that there is anexplanation, and you don't necessarily tie
00:12:09.280 together all the details to the point whereyou could actually publish it and make it
00:12:11.959 understandable to other people.But kind of to your own intellectual satisfaction,
00:12:15.630 it's like, oh yeah, now I'm at least convincedthat that can work.
00:12:19.440 My impression is that that's basically, that'sessentially where the kind of physics project
00:12:24.550 formalism ended up in 2002, that Stephen thoughtabout it for a while, had some research assistants
00:12:28.589 look at it, and eventually they kind of convincedthemselves, yes, it would be possible to derive
00:12:32.980 Einstein equations from these kinds of formalisms.But I highly, from what I've seen of the material
00:12:37.149 that was put together and so on, I don't thinkanyone actually traced that proof, you know,
00:12:40.430 with complete mathematical precision.Eventually in 2019, Stephen, myself, and Max
00:12:46.950 Piskunov, we decided, for various reasons,that it was kind of the right time for us
00:12:52.360 to do this project in a serious way.Stephen had some new ideas about how we could
00:12:56.990 simplify the formalism a little bit.I'd made some recent progress in kind of understanding
00:13:01.280 the mathematical underpinnings of it.Max had just finished writing some really
00:13:05.520 quite nicely optimized kind of low-level C++code for enumerating these hypergraph systems
00:13:09.949 really efficiently.And so we decided like, okay, if we're not
00:13:13.750 going to do it now, it's never going to happen.And so that was then the beginnings of the
00:13:17.360 physics project.And so now I'm less, I guess, less actively
00:13:22.320 involved in the project as a kind of brandingentity.
00:13:27.190 But I'm still kind of actively working onthe formalism and still trying to push ahead
00:13:31.089 in various mathematical directions, tryingto kind of concretify the foundations of what
00:13:35.740 we're doing and make connections to existingareas of mathematical physics.
00:13:39.500 I see.I see.
00:13:40.899 So I also noticed a similar problem as yourselfacross society, so across history, that people
00:13:46.470 entwine this prevalent application with someontological status.
00:13:50.730 So what I mean by that is, you'll have a toolwhich is ubiquitous and usefulness, and then
00:13:56.720 you start to think that there's some realitysynonymous with that.
00:13:59.950 So another example would be an ancient poetwho would see the power of poetry and think
00:14:06.410 that what lies at the fundament is narrativepieces.
00:14:10.290 Or a mystic who sees consciousness everywherealmost by definition and then believes consciousness
00:14:14.209 must lie at the root of reality.And some people, Max Tegmark would be an example
00:14:20.930 of this, find that math is so powerful itmust be what reality is.
00:14:25.579 So it's also not clear to me whether computationis another such fashionable instance of a
00:14:30.220 tool being so powerful that we mistake itseffectiveness with its substantiveness.
00:14:36.040 And I understand that Stephen may think differently,I understand that you may think differently,
00:14:39.740 so please explain.That's a fantastic point, and I suspect, at
00:14:45.740 least from what you've said, I think ourviews may be quite similar on this, that I'm
00:14:49.769 reminded of this meme that circulated on Twittera little while ago about people saying, immediately
00:14:55.380 after the invention of writing systems andnarrative structure, everyone goes, ah, yes,
00:15:00.020 the cosmos must be a book.And then immediately after the invention of
00:15:02.802 mathematics, ah, yes, the cosmos must be madeof mathematics.
00:15:06.339 And then immediately after the invention ofthe computer, ah, yes, the cosmos must be
00:15:09.550 a computer.So I think that it's a folly that we've fallen
00:15:14.290 into throughout all of human history.And so, yeah, my feeling about this is always
00:15:19.779 that, you know, we build models using thekind of ambient technology of our time.
00:15:27.410 And when I say technology, I don't just mean,you know, nuts and bolts technology, I also
00:15:30.649 mean kind of thinking technology, right?So you know, there are kind of ambient ideas
00:15:36.589 and processes that we have access to, andwe use those as a kind of raw substrate for
00:15:41.829 making models of the world.So you know, it's unsurprising that when people
00:15:45.390 like Descartes and Newton built modelsof the cosmos, you know, of the solar system
00:15:49.339 and so on, they described them in terms ofclockwork by analogies to clockwork mechanisms,
00:15:53.610 right?And you know, Descartes even sort of more
00:15:56.630 or less directly wrote that he thought that,you know, the solar system was a piece of
00:15:59.649 clockwork.Whether he actually thought that in an ontological
00:16:02.170 sense or whether it was just a kind of poeticmetaphor, I don't completely know.
00:16:05.550 But you know, it's sort of obvious that thatwould happen, right?
00:16:08.120 Because you know, the 15th century, 16th century,that was sort of the height of clockwork technology
00:16:12.700 in ambient society.And so you know, we live right now in arguably
00:16:16.810 the zenith of kind of computational technology.And so again, it's completely unsurprising
00:16:21.139 that we build models of the cosmos based largelyon computation, or based largely or partly
00:16:25.949 on computational ideas.Yeah, I agree.
00:16:28.160 I think it would be a folly, and I think you'reright.
00:16:31.029 This is maybe one area where perhaps Stephenand I differ slightly in our kind of philosophical
00:16:36.209 conception.I personally feel like it's folly to say,
00:16:38.890 oh, therefore, you know, the universe mustbe a computer, right?
00:16:42.410 Or that, you know, that, yeah, my feelingabout it is, the strongest we can say is that,
00:16:50.069 you know, modeling the universe as a Turingmachine is a useful scientific model.
00:16:54.550 And it's a useful thinking tool by which toreason through kind of various problems.
00:16:59.680 I think it's, yeah, I would be uncomfortableendowing it with any greater ontological significance
00:17:06.410 than that.That being said, of course, you know, there
00:17:08.730 are also lots of examples where people havemade the opposite problem, right, where, you
00:17:11.839 know, made the opposite mistake, I mean.So, you know, the classic example is people,
00:17:16.220 you know, say Hendrik Lorentz, right, whoinvented, basically invented the whole formalism
00:17:19.970 of special relativity.But he said, oh, no, no, this is just a mathematical
00:17:23.859 trick, right?You know, he discovered the right form of
00:17:26.740 time dilation and length contraction.But he said, this is just some coordinate
00:17:29.660 change, it doesn't have any physical effect,it's just a formalism.
00:17:31.830 And then really, the contribution of Einsteinwas to say, no, it's not just a formalism,
00:17:35.160 this is an actual physical effect, and here'show we might be able to measure it.
00:17:38.600 And so, yeah, I'm just trying to indicatethat you have to thread a delicate needle
00:17:45.860 there.Yeah.
00:17:47.000 So you mentioned Turing, and there's anotherapproach called constructor theory, which
00:17:53.679 generalizes Turing machines, or universalTuring machines, to universal constructors,
00:17:58.039 so-called universal constructors.So I'd like you to explain what those are
00:18:01.530 to the degree that you have studied it, andthen its relationship to what you work on
00:18:05.510 at the Wolfram Physics Project.And by the way, string theory, loop quantum
00:18:09.090 gravity, they have these succinct names, butWPP doesn't have a graspable, apprehensible
00:18:15.610 name, at least not to me, to be able to echothat.
00:18:19.250 So is there one that you all use internallyto refer to it?
00:18:22.919 Okay, so on that, yeah, I agree.I'm not a fan of the naming of the Wolfram
00:18:29.900 Physics Project, or indeed even the Wolframmodel, which is a slightly more succinct version.
00:18:35.500 In a lot of what I've written, I use the termhypergraph dynamics, or sometimes hypergraphic
00:18:40.960 writing dynamics, because I think that's amore descriptive title for what it really
00:18:47.210 is.But no, I agree.
00:18:48.370 I think as a branding exercise, there's stillmore work that needs to be done.
00:18:51.880 So for the sake of us speaking more quickly,we'll say the HD model.
00:18:55.270 So in this HD model, what is its relationshipto, what was it, category?
00:19:00.120 No, it wasn't category.It was-
00:19:02.400 Constructor theory.Constructor, right.
00:19:03.929 So the HD model's relationship to constructortheory.
00:19:07.560 Although that's an interesting Freudian slip,because I think basically the relationship
00:19:10.720 is category theory, right?So yeah, okay, so I mean, with the proviso
00:19:15.960 that, you know, again, I know that you'vehad Chiara Maletto on TOE before, right?
00:19:20.280 So I'm certainly not an expert on constructortheory.
00:19:23.340 I've read some of Chiara's and David Deutsch's.papers on these topics, but so as you say,
00:19:29.929 I can give an explanation to the extent thatI understand it. So with, you know, as I understand
00:19:35.570 it, the central idea with constructor theoryis rather than describing physical laws in
00:19:40.280 terms of kind of, you know, equations of motion,right? So in the traditional conception of
00:19:44.380 physics, we would say, you know, you've gotsome initial state of a system, you have some
00:19:47.280 equations of motion that describe the dynamicsof how it evolves, and then you, you know,
00:19:51.390 it evolves down to some final stage. The ideawith constructor theory is you say, rather
00:19:54.690 than formulating stuff in terms of equationsof motion, you formulate things in terms of
00:19:58.560 what classes of transformations are and arenot permitted. So, and I think one of the
00:20:06.580 classic examples that I think Deutsch usesin one of his early papers, and I know that
00:20:10.030 Chiara's done additional work on, is the secondlaw of thermodynamics, and indeed the first
00:20:13.789 law of thermodynamics, right? So thermodynamiclaws are not really expressible in terms of
00:20:18.280 equations of motion, or at least not in avery direct way. They're really saying quite
00:20:22.190 global statements about what classes of physicaltransformations are and are not possible,
00:20:26.260 right? They're saying you cannot build a perpetualmotion machine of the first kind or the second
00:20:31.160 kind or whatever, right? That there is novalid procedure that takes you from this class
00:20:36.260 of initial states to this class of final statesthat, you know, reduce global entropy or that,
00:20:40.220 you know, create free energy or whatever,right? And that's a really quite different
00:20:43.800 way of conceptualizing the laws of physics.So constructor theory, as I understand it,
00:20:47.690 is a way of applying that to physics as awhole, to saying we formalize physical laws
00:20:53.970 not in terms of initial states and equationsof motion, but in terms of initial substrates,
00:20:59.289 final substrates, and constructors, whichare these general processes that I guess one
00:21:04.890 can think of as being like generalizationsof catalysts. It's really a kind of grand
00:21:09.250 generalization of the theory of catalysisin chemistry, right? You know, you're describing
00:21:15.580 things in terms of, you know, this enablesthis process to happen, which allows this
00:21:19.360 class of transformations between these classesof substrates or something. Now, you brought
00:21:25.490 up, inadvertently, you brought up this questionof category theory or this concept of category
00:21:29.740 theory. And I have to be a little bit carefulwith what I say here because I know that the
00:21:33.659 few people I know who work in constructortheory say that what they're doing is not
00:21:37.400 really category theory. But I would argueit has some quite, in terms of the philosophical
00:21:42.330 conception of it, it has some quite remarkablesimilarities. So to pivot momentarily to talk
00:21:51.560 about the duality between set theory and categorytheory as foundations for mathematics. So
00:21:58.870 since the late 19th century, early 20th century,it's been the kind of vogue to build mathematical
00:22:04.240 foundations based on set theory, based onthings like Zemillo-Fraenkel set theory or
00:22:08.900 Hilbert-Bernays-Gödel set theory and otherthings, where the idea, you know, your fundamental
00:22:13.620 object is a set, some collection of stuff,which then, you know, you can apply various
00:22:18.980 operations to. And the idea is you build mathematicalstructures out of sets. Now, set theory is
