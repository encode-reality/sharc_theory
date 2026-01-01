# tactiq.io free youtube transcript
# Jonathan Gorard: Quantum Gravity & Wolfram Physics Project
# https://www.youtube.com/watch/ioXwL-c1RXQ

00:00:00.080 In a sense, we know that black holes or inthe Big Bang or something, that's probably
00:00:03.430 an abstraction that loses usefulness and eventuallywill be superseded by something more foundational.
00:00:08.170 Our universe seems to be neither maximallysimple, nor is it kind of maximally complicated.
00:00:13.219 There's some regularity, but it's not completelylogically trivial. It's not like every little
00:00:17.390 particle follows its own set of laws, butit's also not like we can just reduce everything
00:00:21.529 to one logical tautology.Jonathan Garrard is a researcher in mathematical
00:00:27.769 physics at Princeton University and in myopinion is the sharpness and the brains behind
00:00:32.689 the rigor at the Wolfram's Physics Project.Today's conversation is quite detailed as
00:00:37.660 we go into the meticulous technicalities,as if this were a conversation between two
00:00:41.590 friends behind closed doors.In this discussion, we elucidate the core
00:00:45.150 principles and claims of the Wolfram's PhysicsProject. We distinguish them from the surrounding
00:00:50.510 hype. Specifically, we explore potential connectionsbetween category theory and quantum gravity.
00:00:55.700 We also delve into refining truth and representations,the pros and the perils of peer review. And
00:01:01.730 furthermore, we highlight the differencesbetween Jonathan and Stephen Wolfram, particularly
00:01:07.600 in the context of computational and consciousnessrelated aspects.
00:01:11.100 You should also know that there are threeinterviews with Stephen Wolfram on this channel.
00:01:15.130 Each is linked in the description. In it,we detail the Wolfram's Physics Project with
00:01:19.050 Stephen Wolfram himself and why he thinksit's a potential candidate for a theory of
00:01:23.200 everything.My name is Curt Jaimungal. For those of you
00:01:26.230 who are unfamiliar, this is a channel calledTheories of Everything where we explore theories
00:01:31.369 of everything in the physics sense, usingmy background in mathematical physics from
00:01:35.380 the University of Toronto, but as well asexplore other large grand questions. What
00:01:40.619 is consciousness? Where does it come from?What is reality? What defines truth? What
00:01:44.800 is free will? And do we have it?Of course, increasingly, we've been exploring
00:01:48.360 artificial intelligence and its potentialrelationship to the fundamental laws.
00:01:52.640 Also, the string theory video that Jonathanmentions is called the Iceberg of String Theory
00:01:58.469 and I recommend you check it out. It tookapproximately two months of writing, four
00:02:02.630 months of editing with four editors, fourrewrites, 14 shoots, and there are seven layers.
00:02:08.139 It's the most effort that's gone into anysingle theories of everything video. It's
00:02:12.200 a rabbit hole of the math of string theorygeared toward the graduate level. There's
00:02:16.750 nothing else like it.If that sounds interesting to you, then check
00:02:20.360 out the channel or hit subscribe to get notified.Enjoy this episode with Jonathan Girard.
00:02:26.459 So Jonathan, what is the Wolfram's PhysicsProject and what's your role in it?
00:02:31.710 That's a really good question, Curt. So Iguess, I don't know, there are various people
00:02:37.050 involved and I think you'll get slightly differentanswers or perhaps very different answers
00:02:40.500 depending on who you ask. I'm someone who,you know, I think when we first launched the
00:02:46.129 physics project back in April 2020, we kindof, we lent hard on this billing of it's a
00:02:51.840 project to find the fundamental theory ofphysics. That was not really how I viewed
00:02:57.420 it at the time and it's become even less howI view it over time.
00:03:00.530 Interesting.And so, you know, I'm just, I'm saying this
00:03:05.170 as a kind of prelude to clarify that whatyou're about to hear is my own perspective
00:03:08.780 on it and it will probably differ quite alot from the perspective given by some other
00:03:13.299 members of the project. So essentially, myview is that the Wolfram Physics Project is
00:03:18.110 an attempt to answer a kind of counterfactualhistory question.
00:03:23.209 So back in the 17th century, Newton, Leibniz,a little bit earlier people like Descartes,
00:03:32.849 Galileo, you know, they kind of set the stagefor modern theoretical kind of mathematical
00:03:37.310 physics and more broadly for our kind of modernconception of how the exact sciences work.
00:03:42.650 And you know, so essentially the idea was,you know, rather than just describing phenomena
00:03:46.720 in these kind of philosophical terms, youcould actually construct kind of robust quantitative
00:03:51.709 models of what, you know, what natural systemsdo. And that was enabled by a particular piece
00:03:57.060 of mathematical technology or a particularpiece of, I guess, cognitive technology, which
00:04:00.569 was calculus, which later became, you know,mathematical analysis and the basis of differential
00:04:04.970 geometry and all the kind of machinery ofmodern mathematical physics. So, you know,
00:04:08.760 Newton, Leibniz, you know, building off earlierwork by people like Archimedes and so on kind
00:04:12.239 of, you know, they built up this formalismof calculus that sort of enabled modern physics.
00:04:18.279 And arguably, that choice of formalism, thatchoice to base physical models on, you know,
00:04:25.380 analytic calculus-based mathematical formalismshas had an impact on our physical intuition,
00:04:31.690 right? So, you know, it involves thinkingabout things in terms of smooth analytic functions,
00:04:36.250 in terms of continuously varying kind of gradientsof quantities. You know, it necessitates us
00:04:40.710 formalizing notions like space and time interms of, you know, smooth manifolds or real
00:04:46.150 numbers. It involves, you know, thinking aboutthings like energy and momenta as being continuously
00:04:50.550 varying quantities. And those are, of course,extremely good idealizations of what's really
00:04:56.000 happening. But I think there's always a dangerwhenever you have a model like that, that
00:04:59.870 you start to kind of believe in the ontologicalvalidity of the model. And so, for a lot of
00:05:03.400 physicists, I feel like, you know, it's kindof seeped in and percolated our intuition
00:05:08.160 to the extent that we actually think thatspace is a, you know, smooth Riemannian manifold.
00:05:13.080 We think that energy is a kind of real valuedfunction, rather than these just being idealizations
00:05:17.320 of some potentially quite different, you know,underlying reality. Okay, now fast
00:05:22.540 forward about 300 years, and you have peoplelike Alan Turing and Alonzo Church and Curt
00:05:27.330 Gödel in the early 20th century buildingup the beginnings of what became theoretical
00:05:30.870 computer science, right? As an offshoot ofmathematical logic. There were people interested
00:05:35.840 in the question of, you know, what is mathematics?What is mathematical proof? You know, what
00:05:40.600 are mathematical theorems? And that kind ofnecessitated them building this really quite
00:05:44.490 different mathematical formalism, which initiallyhad different manifestations. It had, you
00:05:50.012 know, Turing machines, lambda calculus, youknow, general recursive functions, etc., which
00:05:53.830 then gradually got unified thanks to thingslike the Church-Turing thesis. But so now,
00:05:59.350 so in a way, again, at least the way I liketo think about it is, you know, the sort of
00:06:03.639 stuff that Newton and Leibniz and people weredoing in the 1600s, that gave, you know, with
00:06:08.389 analysis, that gave you a systematic way ofunderstanding sort of an exploring continuous
00:06:13.030 mathematical structures. What Turing and Churchand Gödel and people did in the early 20th
00:06:17.349 century with computability theory gave onea systematic way of understanding discrete
00:06:21.470 mathematical structures. You know, the kindsof things that could be represented by simple
00:06:26.000 computations and simple programs. Now, bythat point, as I say, you know, calculus,
00:06:31.320 the sortof calculus-based approaches had had a 300-year
00:06:33.800 head start in terms of the exact sciences.And it took a little while before people started
00:06:38.080 thinking, hmm, actually, you know, maybe wecould use these formalisms from computability
00:06:41.360 theory to construct models of natural phenomena,to construct, you know, scientific models
00:06:45.880 and models for things like fundamental physics.But of course, that necessitates being a quite
00:06:50.190 radical departure in how we think about physicallaws, right? That, you know, suddenly you
00:06:54.120 have to deviate from thinking about spaceas some smooth continuous structure and start
00:06:58.080 thinking about it in terms of some discretecombinatorial structure, like a kind of network
00:07:01.970 or a graph. It necessitates you moving awayfrom thinking about dynamics in terms of continuous
00:07:07.280 partial differential equations and thinkingabout it in terms of kind of discrete time-step
00:07:10.870 updates, like, say, the kinds that you canrepresent using network rewriting rules.
00:07:15.690 And so, you know, a lot of physicists whoare kind of trained in the traditional mathematical
00:07:20.310 formalism find this quite counterintuitivebecause, as I say, you know, those ideas from
00:07:26.050 mathematical analysis have seeped so far intoour intuition that we think that's actually
00:07:30.250 how the universe works, rather than just thinkingof it as being a model.
00:07:33.740 And so, the way, the slightly poetic way thatI like to think about what the physics project
00:07:37.819 is doing is we're trying to address this kindof counterfactual history question of
00:07:41.900 what would have happened if, you know, Turingwas born 300 years before Newton, not the
00:07:46.260 other way around. In other words, if we had,if discrete mathematical approaches based
00:07:50.129 on computability theory had a 300-year headstart in the foundations of natural science
00:07:54.509 over continuous, you know, mathematical structuresbased on analysis. That's my kind of zoomed
00:08:00.039 out picture of what it is that we're tryingto do.
00:08:02.630 So, okay, that's, there's a lot more thatcan be said about that, of course, and I'm
00:08:07.560 sure we'll discuss more of it later. But that'sat least my kind of, that's my big picture
00:08:13.129 summary of what I think the physics projectis about. It's about trying to reconstruct
00:08:16.120 the foundations of physics, not in terms of,you know, Lorentzian manifolds and continuous
00:08:20.940 base times, but in terms of things like graphs,hypergraphs, hypergraphic writing, causal
00:08:25.650 networks, and, you know, the kinds of discretestructures that can be represented in a very
00:08:29.190 explicit, computable way. There are some niceconnections there, by the way, to things
00:08:32.419 like the constructivist foundations of mathematicsthat arose in the 20th century as well. And
00:08:37.649 again, we'll likely talk about that later,too.
00:08:41.429 In terms of my own role within it, so, youknow, Stephen Wolfram, who I know has appeared
00:08:46.540 on TOA a number of times and has been kindof the, by far the single most energetic evangelist
00:08:54.589 of these ideas for a very long time. He wroteback in 2002, this book, A New Kind of Science,
00:09:01.120 in which he first postulated these, you know,the beginnings of these ideas about, you know,
00:09:05.180 maybe it's useful to think of fundamentalphysics in terms of network automata and things
00:09:08.250 like that. And, you know, had some initialhints towards, okay, here's how we might be
00:09:13.000 able to get general relativity, you know,beginnings of quantum mechanics, those kinds
00:09:16.810 of things out of those systems. But then,you know, those ideas basically lay dormant
00:09:22.540 for a long time. I mean, NKS had, you know,had this kind of maelstrom of attention for
00:09:27.500 a couple of years, and then mostly, at leastphysicists mostly ignored it, is kind of at
00:09:31.690 least my impression. Where, you know, I, asa teenager, you know, I read NKS and I, like
00:09:39.380 many people, found certain aspects of theway the book is written a little bit off-putting.
00:09:43.260 But I thought that there were many, many coreideas in it that were really, really quite
00:09:47.880 foundationally important.And one of them was this idea about fundamental
00:09:50.940 physics.And so, for a while, I kind of advocated like,
00:09:54.870 we should be trying to build physics on thesekind of computable models, if only just to
00:09:58.850 see what happens, right?Just to see where that leads us.
00:10:03.440 And so I started to do some initial kind ofwork in those directions, nothing particularly
00:10:08.339 profound.But also, I would repeatedly badger Stephen,
00:10:12.839 you know, maybe every year or so and say,we should, you know, we should go and like,
00:10:16.330 actually try and do a more serious investigationof these things.
00:10:19.180 And then finally...Sorry, just a moment.
00:10:21.080 You said that you would be working on theseprior to going to the Wolfram School, the
00:10:24.959 summer school?Yes, yeah, exactly.
00:10:27.430 So I went to the Wolfram Summer School in2017, as a consequence of my interest in these
00:10:32.990 models.So I'd already been doing a little bit of
00:10:35.010 my own kind of work on this, the stuff, tryingin large part to, in a sense, to rediscover
00:10:40.649 what Stephen had already done, right?He had these big claims in NKS about being
00:10:45.400 able to derive, you know, Einstein equationsand things from these graph rewriting models.
00:10:50.590 But the details were never included in thebook.
00:10:52.410 And I tried to ask Stephen about them, andhe kind of said, oh, I can't really remember
00:10:55.990 how I did that now.And so I spent quite a lot of time trying
00:10:58.519 to kind of reconstruct that.And that eventually ended up, you know, that
00:11:02.160 was the thing that resulted in me, you know,ending the summer school and then being kind
00:11:06.970 of pulled into Stephen's orbit.And is it your understanding that Stephen
00:11:12.079 actually did have a proof?He just wasn't able to recall it like Fermat,
00:11:16.240 or it just was too small of a space to publish?Or that he thinks he was able to prove it,
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
00:22:27.230 a model of mathematics that depends very heavilyon internal structure, right? So for instance,
00:22:33.110 in the standard axioms of set theory, youhave things like the axiom of extensionality
00:22:37.380 that essentially says two sets are equivalentor two sets are identical if they have the
00:22:41.750 same elements. So it involves you identifyingsets based on looking inside them and seeing
00:22:47.120 what's inside. But there's another way thatyou can think about mathematical structure,
00:22:51.680 which is you say, I'm not going to allow myselfto look inside this object. I'm just going
00:22:56.909 to treat it as some atomic thing. And instead,I'm going to give it an identity based on
00:23:01.310 how it relates to all other objects of thesame type. So what transformations can I,
00:23:06.060 so, you know, to give a concrete example,right, suppose I've got some topological space.
00:23:12.780 So one, the kind of set theoretic view is,okay, that topological space is a set of points.
00:23:18.279 It's a collection of points that have a topologydefined on them. The kind of more category
00:23:22.539 theoretic view would be to say, actually,that topological space is defined as the collection
00:23:28.440 of continuous transformations that can beapplied to it. So that space can be continuously
00:23:33.660 deformed into some class of other spaces.And that class of other spaces that it can
00:23:37.461 be deformed into is what identifies the spaceyou started from. And so that's a, so, and
00:23:42.340 you can define that without ever having totalk about points or, you know, what was inside
00:23:46.730 it, right? In fact, there's this whole generalizationof topology called pointless topology or locale
00:23:51.600 theory, which is all about doing topologywithout an a priori notion of points. So in
00:23:57.530 a way, it necessitates this conceptual shiftfrom an internal structure view to a kind
00:24:02.630 of process theoretic view. And so that wasa viewpoint that was really advocated by the
00:24:08.570 pioneers of Catsby theory, Samuel Eilenbergand Saunders MacLean, and also some other
00:24:13.950 people who were working in topology, likeJean-Pierre Serres and Alexander Grotendieck
00:24:17.380 and others. There was a kind of radicallydifferent way to conceptualize the foundations
00:24:21.790 of mathematics.Sorry to interrupt. Just as a point for the
00:24:24.850 audience, you mentioned the word duality betweensets and categories. Now, do you mean that
00:24:28.220 in a literal sense or just morally there'sa duality? Because category theorists make
00:24:33.630 a huge fuss that what they're dealing witharen't always like small categories or sets,
00:24:39.670 but, or can be thought of as sets, but notcategories as such.
00:24:44.120 Right, right. Okay. And I shouldn't have said,I mean, yes, no. The short answer is no, I
00:24:50.399 don't mean duality in any formal sense. Andin particular, it's a dangerous word to use
00:24:55.260 around category theorists because it meanssomething very precise. It means that dual
00:24:59.909 concepts are ones that are equivalent up toreversal of the direction of morphisms. I
00:25:04.360 certainly don't mean that.Right, right, right.
00:25:05.840 No, I meant duality in the sense that, sothere is a precise sense in which set theory
00:25:12.120 and category theory are equivalently validfoundations for mathematics. And that precise
00:25:19.809 sense is, and hopefully, I mean, we can godeep in the weeds if you want. We'll see
00:25:26.520 where the conversation goes. But the basicidea is there's a branch of category theory
00:25:32.380 called elementary topos theory, which is allabout using category theory as a foundation
00:25:36.700 for logic and mathematics. And the idea thereis, so from a category theoretic perspective,
00:25:43.500 sets are just, they just form one particularcategory. There is a category called set,
00:25:48.830 whose objects are sets and whose transformations,whose morphisms are set-valued functions.
00:25:53.910 And so then you might say, well, you know,why is set so important? Like what's so great
00:25:57.710 about set that we build all mathematics onthat? It's just one random category in this
00:26:01.210 space of all possible categories.So elementary topos theory is all about asking
00:26:04.190 what are the essential properties of set thatmake it a quote-unquote good place to do mathematics?
00:26:11.390 And can we abstract those out and figure outsome much more general class of mathematical
00:26:15.850 structures, some more general class of categoriesinternal to which we can build mathematical
00:26:21.440 structures? And that gives us the idea ofan elementary topos. I'm saying elementary
00:26:25.950 because there's a slightly different ideacalled a Grothendieck topos that's related,
00:26:29.169 but not quite equivalent and whatever. Butgenerally when logicians say topos, they mean
00:26:35.021 elementary topos.So yeah, there's a particular kind of category
00:26:39.419 which has these technical conditions thatit
00:26:41.409 has all finite limits and it possesses a sub-objectclassifier or equivalently a power object.
00:26:45.490 But basically what it means is that it hasthe minimal algebraic structure that sets
00:26:50.250 have,that you can do analogs of things like set
00:26:52.740 intersections, set unions, that you can takepower sets, you can do subsets. And it kind
00:26:58.960 of detects for you a much larger class ofmathematical structures, these elementary
00:27:04.000 topos, which have those same features.And so then the argument goes, well, therefore
00:27:10.760 you can build mathematics internal to anyof
00:27:14.330 those topos. And the mathematical structuresthat you get out are in some deep sense isomorphic
00:27:19.309 to the ones that you would have got if youbuilt mathematics based on set.
00:27:23.350 So that's the precise meaning of, I guess,what I was saying. That in a sense,
00:27:28.330 there are these set theoretic foundations,there are these category theoretic foundations
00:27:32.830 thatcome from topos theory, and there is some
00:27:34.929 deep sense in which it doesn't matter whichone you
00:27:37.900 use. That somehow the theorems you prove areequivalent up to some notion of isomorphism
00:27:43.960 in the two cases.Yes. And now the relationship between constructor
00:27:47.250 theory and HD,which is the hypergraph dynamics or Wolfram's
00:27:51.280 physics project for people who are just tuningin.
00:27:53.900 Right, right. So yes, the excursion to talkabout category theory is in a sense,
00:28:01.620 my reason for bringing that up is becauseI think that same conceptual shift that I
00:28:04.900 wasdescribing, where you go from thinking about
00:28:06.250 internal structure to thinking about kindof
00:28:08.330 process theories, that's been applied to manyother areas. It's been applied, say,
00:28:11.780 in quantum mechanics, right? So where there's,in the traditional conception, you'd say quantum
00:28:16.620 states are fundamental, and you have Hilbertspaces that are spaces of quantum states,
00:28:20.730 and then you have operators that transformthose Hilbert spaces, but they're somehow
00:28:24.070 secondary.Then there's this rather different, and that's
00:28:26.500 the kind of von Neumann-Dirac picture.Then there's this rather different formalization
00:28:31.399 of the foundations of quantum mechanics that'sdue to Samson Abramski and Bob Coker, which
00:28:34.940 is categorical quantum mechanics,where the idea is you say, actually, the spaces
00:28:38.539 of states, those are secondary,and what really matters are quantum processes.
00:28:42.520 What matters are the transformations fromone
00:28:44.120 space of states to another. You describe quantummechanics purely in terms of the
00:28:48.640 algebra of those processes. There are manyother examples of that. Things like functional
00:28:56.150 programming versus imperative programming,or lambda calculus versus Turing machines,
00:28:59.470 in a sense that these are all instances ofthinking about things in terms of processes
00:29:04.150 and functions rather than in terms of statesand sets.
00:29:08.290 I view constructor theory as being the kindof processes and functions version of physics,
00:29:13.280 whereas traditional mathematical physics isthe kind of sets and structures version of
00:29:16.470 physics. In a sense, the hypergraph dynamicsview, slash Wolfram model view, however you
00:29:22.860 want to describe it, is one that nicely synthesizesboth cases, because in the hypergraph dynamics
00:29:29.090 case, you have both the internal structure,that you have an actual hypergraph, and you
00:29:34.529 can look inside it, and you can talk aboutvertices and edges and so on.
00:29:40.269 But you also have a kind of process algebra,because you have this multi-way system where
00:29:45.850 I apply lots of different transformationsto the hypergraph, and I don't just get a
00:29:49.750 single transformation path. I get this wholetree or directed acyclic graph of different
00:29:54.429 transformation paths. In a sense, you canimagine defining an algebra, and we've done
00:29:59.230 this in other work, where you have a rulefor how you compose different edges in the
00:30:06.279 multi-way system, both sequentially and inparallel. You get this nice algebraic structure
00:30:10.960 that happens to have a category theoreticinterpretation.
00:30:15.519 In a way, the pure hypergraph view, that'sa kind of set theory structural view. The
00:30:20.570 pure multi-way system view, that's a kindof pure process theory category theoretic
00:30:26.160 view. One of the really interesting ideasthat comes out of thinking about physics in
00:30:31.220 those terms is that general relativity andquantum mechanics emerge from those two limiting
00:30:36.149 cases. In a sense, if you neglect all considerationsof the multi-way system, and you just care
00:30:42.520 about the internal structure of the hypergraphand the causal graph, and you define a kind
00:30:47.350 of discrete differential geometric theoryover those, what you get in some appropriate
00:30:53.000 limit is general relativity for some classof cases. On the other hand, if you neglect
00:30:57.570 all considerations of the internal structureof the hypergraph, and you care only about
00:31:00.480 the process algebra of the multi-way system,what you get is categorical quantum mechanics.
00:31:04.430 You get a symmetric monoidal category thathas the same algebraic structure as the category
00:31:08.710 of finite dimensional Hilbert spaces in quantummechanics. In a sense, the traditional physics,
00:31:17.529 which is very structural, gives you one limit,gives you the general relativistic limit.
00:31:21.409 The kind of more constructive theoretic view,which is more process theoretic,
00:31:25.409 more category oriented, gives you anotherlimit, gives you the quantum mechanics limit.
00:31:28.711 JS Yeah, and do you need a dagger symmetricmonoidal category, or is the symmetric monoidal
00:31:33.179 enough?SIMON You do need it to be dagger
00:31:35.789 symmetric. Yeah, no, that's a very importantpoint. I'm going to assume not all of your
00:31:42.159 followers and listeners are card-carryingcategory theorists. Just as a very quick summary
00:31:47.380 of whatmeans by dagger symmetric. Actually, maybe
00:31:50.530 we should say what we mean by symmetric monoidal.If you have a category, if you just think
00:31:56.640 of it as some collection of simple processes,like in the multi-way system cases, just individual
00:32:00.620 rewrites of a hypergraph,then you can compose those things together
00:32:05.210 sequentially. You can apply rewrite one,then rewrite two, and you get some result.
00:32:09.290 There's also a case where you can do thatin
00:32:11.360 any category. There are also cases where youcan apply them in parallel. You can do rewrite
00:32:15.840 oneand rewrite two simultaneously. In a multi-way
00:32:18.440 system, that's always going to be possible.Then you get what's called a monoidal category,
00:32:21.750 or actually a symmetric monoidal category,if it doesn't matter which way around you
00:32:24.669 compose them. That kind of generalizes thetensor product structure in quantum mechanics.
00:32:30.889 Then you can also have what's called a daggerstructure. The dagger structure is the thing
00:32:35.570 that generalizes the Hermitian adjoint operationin quantum mechanics, the thing that gives
00:32:38.790 you time reversal. In that case, then youhave some
00:32:42.711 operation that you can take a rewrite andyou can reverse it. For hypergraph rewriting
00:32:47.570 rules,there's a guarantee that you can always do
00:32:49.380 that. There's yet another level of structure,which is what's called a compact closed structure,
00:32:55.830 which means that you can essentially do theanalog of taking duals of spaces. For those
00:33:02.450 people who know about quantum mechanics, that'sthe
00:33:04.889 generalization of exchanging brows for catsand vice versa. Again, you can do that in
00:33:10.440 the caseof hypergraphs. There's a natural duality
00:33:12.370 operation because for any hypergraph, youcan
00:33:15.820 construct a dual hypergraph whose vertex setis the hyperedge set of the old hypergraph,
00:33:21.080 and whosehyperedge set is the incident structure of
00:33:24.399 those hyperedges in the new case. That givesyou a
00:33:27.280 duality that satisfies the axioms of compactclosure. In a sense, the key idea behind
00:33:34.460 categorical quantum mechanics is that if youhave one of these dagger structures, you have
00:33:37.660 a compactclosed structure, you have a symmetric monoidal
00:33:40.280 structure, and they're all compatible, thenwhat
00:33:42.309 you've got is, again, by analogy to topostheory, some mathematical structure in which
00:33:49.260 you can builda theory that is isomorphic to quantum mechanics.
00:33:52.950 That's what we have in the case of multi-waysystems.
00:33:56.869 So when we spoke approximately three yearsago, I believe we had a Zoom meeting. It could
00:34:01.470 havebeen a phone call. I recall that you were
00:34:03.100 saying that you were working, maybe the yearprior,
00:34:07.179 on something where your operators, your measurements,don't have to be self-adjoint.
00:34:13.310 And the reason was, self-adjointness is therebecause we want real eigenvalues, and that
00:34:18.040 justmeans for people who are listening, you want
00:34:19.918 to measure something that's real, not imaginary.What is an imaginary tick? It usually comes
00:34:25.489 down to ticks or not ticks in the measurementdevice.
00:34:29.010 But then I recall you said that you were workingon constructing quantum mechanics with observables
00:34:34.409 that weren't. So self-adjointness impliesreal eigenvalues, but there were other ways
00:34:42.668 of gettingreal eigenvalues that aren't self-adjoint.
00:34:45.020 I don't know if I misunderstood what you said,or if I'm recapitulating incorrectly, but
00:34:49.659 please spell out that research if this ringsa bell to
00:34:53.329 you.So your memory is far better than mine. That
00:34:56.790 sounds like a very accurate summary of somethingI would have said, but I actually have no
00:35:03.540 memory of saying it. To be clear, that's byno means my
00:35:10.460 idea. There's a field called PT-symmetricquantum mechanics, and sometimes known as
00:35:14.700 non-Hermitianquantum mechanics, which have various developers.
00:35:18.580 Carl Bender is one of them. I think there'sa guy
00:35:21.540 called Jonathan Brody, or Jorge Brody. I can'tremember.
00:35:26.270 Carl Bender. So I just spoke to him abouta couple months ago, coincidentally.
00:35:29.800 Oh, well, you should have asked him this question.He's the expert, right?
00:35:34.119 Yeah.Yeah, so Bender and Brody and others. Jorge
00:35:37.130 Brody. I don't know why there's another person.Maybe Jonathan Keating is involved somehow.
00:35:42.250 Sure.But anyway, so it's been a little while since
00:35:45.940 I thought about this, as you can tell. Soyes,
00:35:48.990 there's a generalization of standard unitaryHermitian quantum mechanics. So yeah, as Curt
00:35:55.440 mentioned, in the standard mathematical formalismof quantum mechanics, your measurements seem
00:36:00.180 tobe Hermitian. So when you take the adjoint
00:36:04.540 of the operator, you get the same result.And your evolution operators are assumed to
00:36:09.600 be unitary, so that when you take the adjoint,you get the time reversal of the result. In
00:36:15.380 a sense, that's the key difference betweenevolution and measurement in standard formalism.
00:36:20.859 And we know that, yeah, if your Hamiltonianis
00:36:27.350 Hermitian, the thing that appears in the Schrodingerequation, if that's a Hermitian operator,
00:36:32.240 then the solution to the Schrodinger equationthat gives you the unitary evolution,
00:36:34.780 that gives you the evolution operator, sorry,is guaranteed to be unitary.
00:36:38.200 And also the eigenvalues of the measurementoperator, which is, as Curt said, are in a
00:36:42.490 sense, those are your measurement outcomes.Those are guaranteed to be real. That's a
00:36:47.271 sufficientcondition, Hermeticity, but it's not a necessary
00:36:50.079 one. So that you can have non-Hermitian measurementoperators that still give you real eigenvalues.
00:36:56.849 And where you don't get a unitary evolutionoperator in the algebraic sense, but you get
00:37:03.050 what is often called, I think in these papersit's referred to as kind of physical unitarity.
00:37:07.530 So unitarity means a bunch of things, right?So algebraically, as I say, it means that
00:37:11.180 when you apply the adjoint operator,you get the time reversal. And therefore,
00:37:17.230 if you take a unitary evolution operator andit's
00:37:19.079 adjoint, you get the identity matrix or theidentity operator. So as soon as you have
00:37:23.970 non-Hermitian Hamiltonians, that ceases tobe true. And also you end up with probabilities.
00:37:29.869 So in the interpretation where your quantumamplitudes are really kind of related to
00:37:36.150 probabilities, right? Where you take the absolutevalue of the amplitude squared,
00:37:39.320 and that gives you the probability. Now, assoon as you have non-unitary evolution operators,
00:37:44.240 your probability amplitudes or your probabilitiesare not guaranteed to sum to one.
00:37:48.859 So that looks on the surface like it's completelyhopeless. But actually, as I say, you can
00:37:57.110 stillget real measurement outcomes. The interpretation
00:37:59.920 of the norm squareds of the amplitudes asbeing
00:38:02.550 probabilities, that's simply an interpretation.It's not mandated by the formalism.
00:38:06.530 And what people like Bender and Brody showedwas that you could still have a consistent
00:38:11.430 theorywhere you have parity time symmetry. So you
00:38:15.150 still have a time symmetric theory of quantummechanics.
00:38:16.910 It's still invariant under parity transformations.And it's still possible, even when you apply
00:38:22.440 oneof these non-unitary evolution operators to
00:38:26.109 some initial state, it's still always possibleto
00:38:28.550 reconstruct what the initial state was fromthe final state. I mean, that's really what
00:38:32.140 timesymmetry means. And so it was widely believed,
00:38:36.040 I think, for a long time that if you didn'thave
00:38:37.859 amplitudes whose normal squareds sum to one,then you wouldn't be able to do that. And
00:38:42.349 whatBender and Brody showed was that no, you can.
00:38:44.100 You just have to be– you still have restrictions, but they're
00:38:47.161 just weaker than the restrictions we thoughtexisted.
00:38:50.750 So I was probably bringing that up becauseat the time – well, okay, two reasons. One
00:38:55.701 was it turnsout there are these nice connections, which
00:38:58.099 I was a little bit obsessed with a few yearsback,
00:39:02.260 between PT symmetric quantum mechanics andthe Riemann hypothesis.
00:39:05.650 So a colleague of mine, a former colleagueof mine from Wolfram Research, Paul Abbott,
00:39:10.230 was the person who actually told me aboutthis. And so the idea there is, there's this
00:39:15.570 thingcalled the – okay, let me get this right.
00:39:18.930 So there's a thing called the Hilbert-Polyaconjecture,
00:39:21.800 which is the conjecture that – which I thinkis reasonably well-known. At least some people,
00:39:28.280 people in our kind of area have often heardabout. Yeah, which is the idea that somehow
00:39:34.260 thenon-trivial zeros of the Riemann zeta function
00:39:37.680 should be related to the eigenspectrum ofsome
00:39:42.100 manifestly self-adjoint operator. And so it'ssomehow a connection between the analytic
00:39:48.140 numbertheory of the zeta function and the kind of
00:39:51.869 foundation, the operator-theoretic foundationsof quantum mechanics. And then there's the
00:39:55.621 thing called the Berry-Keating Hamiltonian.So Mike Berry and Jonathan Keating constructed
00:40:00.339 a case of what they conjectured to be a Hilbert-Polyatype Hamiltonian. So in other words, a Hamiltonian
00:40:07.780 where if you could prove thatit was manifestly self-adjoint, it would be
00:40:11.790 equivalent to proving the Riemann hypothesis.The problem is that Hamiltonian is actually
00:40:16.380 not – it's not self-adjoint. It's notHermitian in the traditional sense. But it
00:40:21.170 is Hermitian in this PT symmetric sense. Itis – so
00:40:24.280 it's not algebraically Hermitian. It's notequal to its own adjoint. But it's still a
00:40:29.930 validHamiltonian for parity time symmetric quantum
00:40:33.810 mechanics. And so by trying to think aboutthe Riemann hypothesis in terms of quantum
00:40:41.060 formalism, you end up being kind of inevitablydrawn into thinking about non-Hermitian foundations
00:40:45.540 and these kind of PT symmetricformulations. So that's how I first learned
00:40:49.190 about this. And I suspect I was talking aboutit at the
00:40:50.980 time partly because I was just interestedin that connection. It turns out that the
00:40:55.410 spectrum ofthese operators are related not just to the
00:40:58.329 Riemann zeta function, but also to what'scalled
00:41:00.160 the Hovitz zeta function and several otherobjects in analytic number theory. But also
00:41:05.859 at the time,this has turned out to be false, but at the
00:41:08.530 time I thought that the version of quantummechanics
00:41:12.089 that we would end up with from these multiwaysystems would be a PT symmetric
00:41:16.839 formalism for quantum mechanics, not standardquantum mechanics. As it turns out, actually,
00:41:21.010 there's a way you can do it where you getstandard quantum mechanics complete with proper
00:41:23.950 Hermeticityand Unitarity, so you don't really need to
00:41:26.500 worry about that. But at the time, I was quitenervous
00:41:28.540 that we weren't going to get that, but wewere going to get some weird non-Hermitian
00:41:31.910 versionof quantum mechanics, and we'd have to worry
00:41:33.410 about that.Jay, do you end up getting both or just one?
00:41:37.930 So there is a construction where you can get…I mean, what I want to stress is that there's
00:41:44.700 nocanonical… If you're just given a multiway
00:41:47.640 system and you're said,derive quantum mechanics, right? There's no
00:41:49.560 canonical way to do that.The approach that we ended up taking was to
00:41:53.069 show that, as I say, there's this algebraicstructure
00:41:55.940 that has this dagger symmetric compact closedmonoidal category feature. Therefore, you
00:42:03.079 canget standard quantum mechanics because standard
00:42:05.160 quantum mechanics is what's developed kindof
00:42:06.851 internal to that category. But in order todo that, we had to make a whole bunch of really
00:42:13.640 quite arbitrary choices. So I strongly suspectthat there are ways that you could define
00:42:19.800 analgebraic structure that is essentially a
00:42:21.450 non-Hermitian PT symmetric formulation. Ijust
00:42:24.000 I don't personally know the way to do it.So just as an aside, a pedagogical aside for
00:42:29.420 the people who aren't mathematicians or physicists,they hear terms like closed,
00:42:33.650 compact, symmetric, monoidal, dagger, unitary,adjoint, and they're wondering,
00:42:37.940 why are we using these words to describe physicalprocesses? And the reason is because the
00:42:43.350 mathematicians got there first. So physicistsare trying to describe something and then
00:42:48.001 they seethat there's some tools invented by other
00:42:50.020 people, goes by other names, and then theyend up applying
00:42:52.620 in the physical situations. But when the physicistgets there first, they're often intuitive
00:42:56.809 names,momentum, spin up, spin down. It's actually,
00:42:59.650 it makes more sense. So just in case peopleare
00:43:02.300 wondering, this terminology is needlesslycomplex. Well, it can be to the outsider,
00:43:06.800 but as you becomefamiliar with them, you just realize historically,
00:43:09.360 if you want to communicate to mathematiciansand
00:43:11.330 vice versa, then just use whatever terms wereinvented first. I would say there's the opposite
00:43:17.770 problem as well, right? I mean, there arecases where physicists discovered concepts
00:43:21.099 first thathave been subsumed into mathematics, and the
00:43:23.690 physical names don't really make any sensein
00:43:25.250 the mathematical context. There are thingslike physicists, because of general relativity,
00:43:29.790 were really the first people to seriouslythink about and formalize notions like torsion
00:43:34.390 indifferential manifolds and concepts like metric
00:43:37.609 affine connections. So the standard connectionthat you define on a manifold with torsion
00:43:44.960 is the spin connection, so named because itwas
00:43:47.161 originally used in these metric affine theorieswhere you have a spin tensor that describes
00:43:50.670 thespin of particles. So now there are these
00:43:54.819 ideas in algebraic and differential geometrycalled
00:43:56.690 spin connections and spin holonomies, andthey have nothing to do with spin, nothing
00:44:00.250 to do withparticle physics. But it's the relic of the
00:44:04.690 physical origins of the subject. There areseveral cases of that too. Yeah, I haven't
00:44:08.580 announced this, and I'm not sure if I'llend up doing this. I've been writing a script
00:44:12.040 for myself on words that I dislike in physicsand math.
00:44:16.770 Sometimes they'll say something like, what'sthe callback? Wow, what is it called? The
00:44:22.620 callback?Callback-Leibler divergence.
00:44:24.340 Callback-Leibler divergence. Okay, if youjust say that, it doesn't mean anything. You
00:44:28.350 have to knowwhat it's defined as. So calling something
00:44:31.990 the earth mover's distance is much more intuitive.And then I have this whole list of words that
00:44:37.260 I say, okay, it's so foolish to call it this.Why don't you just call it by its descriptive
00:44:42.550 name? And then I suggest some descriptivenames.
00:44:45.170 And there's another class of foolish namesto myself. Torsion is one of them,
00:44:50.870 but it's not because it's a bad name. It'sbecause it's used in different senses.
00:44:56.290 On an elliptic curve, there's torsion, butit has nothing to do with the torsion in differential
00:45:00.340 geometry, which as far as I can tell, maybeyou can tell me the difference here. In cohomology,
00:45:05.360 there's torsion where if you are using thefield of the integers and then you go to the
00:45:10.700 reals,if they're not equivalent, then you say it
00:45:13.130 has torsion.Yes, yes.
00:45:14.630 But it's not the same as the differentialgeometric torsion as far as I can tell.
00:45:19.800 I think that's true. Yeah, so I think thatconfusion has arisen because it's one of
00:45:24.280 these examples of independent evolution. Sothere was a notion of torsion that appeared
00:45:28.250 in grouptheory, but then because of that got subsumed
00:45:30.880 into, as you say, things like homology theoryand cohomology theory. So in group theory,
00:45:36.660 a group is defined as being torsion if it'sif it has only finite generators, generators
00:45:45.950 of finite order. So the generators of a group,the things that you multiply, you exponentiate
00:45:52.410 to get all elements of the group. If the groupis generated only by generators of finite
00:45:58.849 order, then you say it's a torsion group.You can talk about torsion subgroups, or you
00:46:02.520 could talk about the torsion part of a group.And so yeah, it appears a lot in the theory
00:46:06.250 of elliptic curves because there are thingslike the
00:46:09.819 Mordell-Weythe theorem that are talking aboutwhen you take rational points on elliptic
00:46:14.550 curves,you can ask about how large is the torsion
00:46:16.400 part, how large is the non-torsion part.And there are things like Birch-Swinson-Dyer
00:46:19.809 conjecture that are all about relating thoseideas. But then yeah, then quite independently,
00:46:24.869 there was a notion of torsion that appearedin
00:46:26.350 differential geometry that, as you know, isthat it's just essentially it's a measure
00:46:29.920 of,you know, I have points x and y, how different
00:46:33.540 is the distance from x to y and the differencefrom y to x. And the name there comes from
00:46:38.540 the fact that in the classical kind of Gaussiantheory
00:46:41.369 of geometry of surfaces, it's the conceptthat gives you the torsion of a curve, right?
00:46:46.980 You know,how much the curve is twisting. Yeah, as far
00:46:50.690 as I know, those two names are unrelated.And as you
00:46:53.869 say, there are these awkward areas like homologytheory where it's partly about spaces and
00:46:59.150 it'spartly about groups. And so it's kind of unclear
00:47:01.109 which one you're talking about.This is a great point to linger on here, particularly
00:47:04.870 about torsion,because I have a video that is controversially
00:47:08.349 titled that gravity is not curvature.For some context, here's the string theory
00:47:12.990 iceberg video that's being referenced whereI
00:47:15.329 talk about gravity is not curvature. The linkis in the description. If you listen to this
00:47:19.420 podcast,you'll hear me say often that it's not so
00:47:21.350 clear gravity is merely the curvature of space-time.Yes, you heard that right. You can formulate
00:47:25.750 the exact predictions of general relativity,but with a model of zero curvature with torsion,
00:47:31.720 nonzero torsion, that's Einstein-Cartan. Youcan
00:47:33.900 also assume that there's no curvature andthere's no torsion, but there is something
00:47:37.240 callednon-matricity. That's something called symmetric
00:47:39.430 teleparallel gravity. Something else I liketo
00:47:41.730 explore are higher spin gravitons. That iscontroversially titled that gravity is not
00:47:47.450 curvature. It's just the saying that thereare alternative formulations with torsion
00:47:51.050 ornon-matricity. For people who don't know,
00:47:54.160 general relativity is formulated as gravityis curvature
00:47:57.000 of space-time, but you can get equivalentpredictions if you don't think of curvature.
00:48:02.250 You can think of zero curvature, but the presenceof so-called torsion, or zero curvature and
00:48:07.000 zerotorsion, but the presence of so-called non-matricity.
00:48:10.210 Okay, these are seen as equivalent formulations,but I'm wondering if the Wolfram's physics
00:48:17.370 project or the hypergraph dynamical approachactually identifies one of them as being more
00:48:22.520 canonical.Unfortunately, I think at least based on stuff
00:48:30.550 that I've done, I think the answer is no.Also,
00:48:34.460 I think it actually makes the problem worse.If you're concerned by the fact that there's
00:48:41.780 this apparent arbitrary freedom of do youchoose to fix the contortion tensor or the
00:48:45.869 non-matricity tensor or the curvature tensoror whatever, thinking about things in terms
00:48:49.720 of hypergraphs, you actually get yet anotherfree parameter, which is dimension. In a hypergraph
00:48:58.820 setting, again, I know you've had Stephenon here before, and I know that he's covered
00:49:02.540 a lot of these ideas, so I'll just very brieflysummarize. Hypergraphs have no a priori notion
00:49:08.290 of dimension. They have no a priori notionof curvature. You can calculate those things
00:49:12.650 subject to certain assumptions where you say,I'm going to look at, I take a node and I
00:49:17.480 look at all nodes adjacent to it and all nodesadjacent to those nodes and so on. I
00:49:20.930 grow out some ball and I ask, what is thescaling factor of that ball as a function
00:49:23.800 of radius? I can take logarithmic differences.That gives me the exponent. That exponent
00:49:28.490 is like a Hausdorff dimension. Then I canask, what's the correction? Does that give
00:49:32.700 me some leading order term in the expansion?What are the correction terms? Those correction
00:49:36.299 terms give me projections of the Riemann tensor.That's just using the analogy to kind of classical
00:49:41.880 differential geometry. But the point is thatto get the curvature terms, as we do in, say,
00:49:45.869 the derivation of general relativity, youhave to assume that the hypergraph is kind
00:49:50.109 of uniform dimensional, right? Even to beable to take that Taylor expansion, you have
00:49:55.610 to assume that the dimension is uniform. Sothen an obvious question is, what happens
00:49:59.380 if you relax that assumption? And the answeris, well, you get a theory that is equivalent
00:50:05.109 to general relativity in the kind of observationalsense, but now you can have fixed curvature,
00:50:12.010 fixed contortion, fixed non-matricity, butyou just have variable dimension. The point
00:50:17.920 is that in the expansion for that volume element,the dimension gives you the kind of leading
00:50:24.240 order exponential term. The Ricci scalar curvaturegives you a quadratic correction to that,
00:50:29.849 and then you have higher order corrections.Because of this very basic mathematical fact
00:50:36.960 that if you're zoomed in really far, it'svery hard to distinguish an exponential curve
00:50:42.670 from a quadratic curve, right? You kind ofhave to zoom out and see it very globally
00:50:45.819 before you can really tell the differencebetween the two. And so in a sense, what that
00:50:49.020 translates to is if you're looking only atthe microstructure of space-time, there's
00:50:52.830 no way for you to systematically distinguishbetween a small change in dimension and a
00:50:58.050 very large change in curvature. So if youhad a region of space-time that was kind of
00:51:02.480 rather than being four-dimensional, was 4.00one-dimensional, but we were to kind of measure
00:51:08.140 it as though it were four-dimensional, itwould manifest to us as a curvature change.
00:51:12.690 It would be observationally indistinguishablefrom a curvature change. So what I would say
00:51:18.510 is that in the hypergraph dynamics view, yeah,you again have this arbitrarity of you have
00:51:24.450 to make choices of connections which fix torsionand non-matricity and so on. But you have
00:51:28.200 this additional problem that you also haveto make choices about trade-offs between curvature
00:51:31.490 and dimension.So let's go back to category theory for just
00:51:35.200 a moment. When I was speaking to Wolfram aboutthat, Stephen Wolfram, he said that he's not
00:51:39.829 a fan of category theory because he believesit circumvents computational irreducibility.
00:51:45.069 I said, why? He said, well, because you gofrom A to B, yes, then you can go from B to
00:51:49.859 C, but then you also have an arrow that goesdirectly from A to C. But when I was thinking
00:51:54.579 about it, that's only the case if you thinkthat each mapping takes a time step. But when
00:51:59.910 I look at category theory, I don't seeit as any time step. At least I don't. I see
00:52:04.150 it as just this timeless creation. So pleasetell me your thoughts.
00:52:08.880 Right. Okay. Well, so I'm in the fortunateposition of having written quite a long paper
00:52:15.260 on exactly this problem. So there's a paperthat I wrote back in 2022 called A Functorial
00:52:20.970 Perspective on Multicomputational Irreducibility,which is all about exactly this idea. So as
00:52:29.210 you say, category theory, as it's ordinarilyconceived, is just a kind of algebraic theory
00:52:34.561 that has no notion of, there's nothing computationalabout it, right? There's no notion of time
00:52:38.160 step. There's no statement made about what'sthe computational complexity of any given
00:52:42.640 morphism.But then an obvious question is, well, okay,
00:52:46.640 is there a version of category theory whichdoes care about those things, a kind of resource
00:52:49.890 limited version, or some version where individualmorphisms are kind of tagged with computational
00:52:54.849 complexity information? And it turns out theanswer is yes. And it has some very nice connections
00:52:59.280 to not just categorical quantum mechanics,but also things like functorial quantum field
00:53:03.460 theory. But also it gives you a new... I thinkStephen is wrong in that statement that it
00:53:12.530 doesn't care about computational irreducibility,because actually it gives you a very clean
00:53:16.050 way of thinking about computational irreducibility.So what I mean by that is, so computational
00:53:21.200 irreducibility, this idea that there are somecomputations that you kind of can't shortcut
00:53:25.210 in some fundamental sense. As far as I know,I was the first person to actually give a
00:53:29.800 formal definition of that in a paper backin 2018 or something.
00:53:33.400 Sorry, a formal definition of computationalirreducibility?
00:53:37.260 Of computational irreducibility. Nothing veryprofound, but just essentially you say, I've
00:53:42.290 got some Turing machine that maps me fromthis state to that state. Does there exist
00:53:45.570 a Turing machine of the same signature thatgets me to the same output state with fewer
00:53:49.570 applications of the transition function? Andso I mean, I needed that for another result
00:53:55.750 that I was proving. But having looked in theliterature, I'm not aware of anyone previously
00:54:00.280 who'd formalized that definition.Sorry, I don't mean to cut you off, so please
00:54:03.240 just remember where you are. Because it'smy understanding that Wolfram said that rule
00:54:07.869 30, something like that, maybe you would recallit more vividly because it's in his book,
00:54:12.190 rule 30 is computationally irreducible. I'vealways wondered, how do you prove that? Now,
00:54:16.740 I imagine that he proved it, or maybe it'sone of those Wolfram proofs, so proof to himself.
00:54:21.859 But in order for him to prove it, even tohimself, he would have had to have a definition
00:54:25.619 of it.Right. Okay. So that's an important point.
00:54:31.760 So rule 30 is not proved to be computationallyirreducible. And in fact, there's a prize.
00:54:36.720 So if you go to, I think it's rule30prize.org.I'm ostensibly on the prize committee. This
00:54:42.829 is a prize that Wolfram put out back in 2018.There's actually three prizes, none of which
00:54:48.339 have been claimed. Each one is $10,000. Andone of which is prove that rule 30 is computationally
00:54:53.940 irreducible. And so yeah, it's unproven. Andin fact, there's really only one, up to some
00:55:01.859 notion of equivalence, there's really onlyone of the elementary cellular automata in
00:55:05.059 NKS that's been proven to be computationallyirreducible in any realistic sense. And that's
00:55:10.520 rule 110. And that was proved by showing thatit's capable of doing universal computation,
00:55:15.930 that it's a Turing-complete rule. And so intuitively,you can kind of say, well, if it's Turing-complete,
00:55:23.160 then questions about termination are goingto be undecidable, and therefore it has to
00:55:26.540 be irreducible. But it's a kind of slightlyhand-wavy thing. But yeah, so in a way, it's
00:55:33.650 an interesting question. Can you prove thatsomething is computationally irreducible without
00:55:38.700 proving that it's universal? And of course,as you say, for that, you would need a formal
00:55:42.740 definition of irreducibility.Okay. And now going back to your paper on
00:55:47.680 functoriality and computational irreducibility,you were able to formalize this.
00:55:52.099 Yes. So sorry. Yes. So what I was saying was,yes, so there was this existing formal definition
00:55:57.760 of computational irreducibility. But I thenrealized that if you think about it from a
00:56:02.059 category theoretic standpoint, there's actuallya much nicer definition, a much less kind
00:56:04.940 of ad hoc definition, which is as follows.So imagine a version of category theory where
00:56:09.030 your morphisms, as I say, are tagged withcomputational complexity information. So each
00:56:12.920 morphism has a little integer associated toit. So you fix some model of computation,
00:56:17.200 you fix Turing machines, and you say, eachmorphism, I'm going to tag with an integer
00:56:21.819 that tells me how many operations was neededto compute this object from that object. In
00:56:26.520 other words, how many applications of thetransition function of the Turing machine
00:56:30.941 did I need to apply?So now if I compose two of those morphisms
00:56:37.680 together, I get some composite. And that compositeis also going to have some computational complexity
00:56:43.630 information. And that computational complexityinformation, it's going to satisfy some version
00:56:46.690 of the triangle inequality, right? So if ittakes some number of steps to go from X to
00:56:50.730 Y and some number of steps to go from Y toZ, I can't go from X to Z in fewer computational
00:56:56.270 steps that it would have taken to go fromX to Y or from Y to Z. So it's going to at
00:57:02.390 least satisfy the axioms of something likea metric space. There's some kind of triangle
00:57:06.549 inequality there.But then you could consider the case where
00:57:11.180 the complexities are just additive, right?Where to get from X to Z, it takes the same
00:57:16.240 number of steps as it takes to go from X toY plus the number of steps it takes to go
00:57:19.690 from Y to Z. And that's precisely the casewhere the computation is irreducible, right?
00:57:23.970 Because it's saying you can't shortcut theprocess of going from X to Z. Which then means
00:57:27.440 you could define the case of computationalreducibility as being the case where the algebra
00:57:34.240 of complexities is sub-additive under theoperation of morphism composition.
00:57:39.260 And there's a way that you can formulate this.So you take your initial category, and you
00:57:44.869 take a category whose objects are essentiallyintegers and discrete intervals between integers.
00:57:52.100 And then you have a functor that maps eachobject in one category to an object in another,
00:57:58.430 each morphism in one to a morphism in another.And then the composition operation in the
00:58:02.900 second category is just discrete unions ofthese intervals. And then you can ask essentially
00:58:08.280 whether the cardinality of those intervalsis discretely additive or discretely sub-additive
00:58:12.780 under morphism composition. And that givesyou a way of formalizing computational reducibility.
00:58:16.940 And the really lovely thing about that isthat not only can you then measure irreducibility
00:58:21.630 and reducibility in terms of defamation ofthis functor, but it also generalizes to the
00:58:27.030 case of multi-way systems. You can formalizenotions of multi-computational irreducibility
00:58:32.299 by essentially just equipping these categorieswith a monoidal structure, with a tensor product
00:58:35.690 structure.Aaron Powell So my understanding of computational
00:58:39.430 irreducibilityis either that a system has it or it doesn't,
00:58:41.990 but it sounds like you're able to formulatean index so that this system is more irreducible
00:58:46.369 than another. Like you can actually give adegree to it.
00:58:49.170 Tom Clougherty Exactly, exactly. So there'sa limit case
00:58:53.250 where it's exactly additive, and anythingthat's less than that, you know, where the
00:58:58.750 complexities are exactly additive, that'skind of maximally irreducible. But anything
00:59:01.800 less than that is sort of partially reducible,but not necessarily fully reducible.
00:59:06.010 Aaron Powell Now, are there any interestingcases of something
00:59:08.150 that is completely reducible, like has zeroon the index of computational irreducibility?
00:59:13.290 Is there anything interesting? Even trivialis interesting, actually.
00:59:16.700 Tom Clougherty Yes, I mean, well, okay, soany computation
00:59:24.280 that doesn't change your data structure, that'sjust a repetition of the identity operation
00:59:30.809 is going to have that property. I'm not sureI can necessarily prove this. I don't think
00:59:35.720 there are any examples other than that. Ithink any example other than that must have
00:59:39.200 at least some minimal amount of irreducibility.But yes, I mean, this also gets into a bigger
00:59:50.000 question that actually relates to some thingsI'm working on at the moment, which is exactly
00:59:55.809 how you equivalence objects in this kind ofperspective, right? Because even to say it's
01:00:01.339 a trivial case, right, where I'm just applyingsome identity operation, I'm getting the same
01:00:05.670 object, you have to have some way of sayingthat it is the same object. And that's actually,
01:00:11.040 I mean, that sounds like a simple thing, butit's actually quite a philosophically thorny
01:00:17.480 issue, right? Because, you know, in a verysimple case, you could say, well, okay, so
01:00:21.109 sorry, first thing to say is, everything we'retalking about at the moment, this is all internal
01:00:25.750 to this category, which in the paper I callcomp, this category whose objects are in a
01:00:30.200 sense elementary data structures, and whosemorphisms are the morphisms that freely generate
01:00:37.260 this category are elementary computations.And so the collection of all morphisms that
01:00:40.770 you get from compositions are essentiallythe class of all possible programs. So within
01:00:45.780 this category, when two objects are equivalent,and therefore when two programs are equivalent
01:00:50.099 is a fairly non-trivial thing, right? So youcan imagine having a data structure where
01:00:54.329 nothing substantively changes, but you'vejust got like a time step or something that
01:00:58.190 goes up every time you apply an operation.So it just increments from one, two, three,
01:01:01.770 four. So in that case, you're never goingto have equivalences. Every time you apply
01:01:04.099 an operation, even if the operation morallydoes nothing, it's going to be a different
01:01:09.069 object. So even that would show up as beingsomehow irreducible. But there are also less
01:01:14.450 trivial cases of that, like with hypergraphs,right? So with hypergraphs, you have to determine
01:01:19.930 equivalence, you have to have some notionof hypergraph isomorphism. And that's a complicated
01:01:24.700 to define, let alone to formalize algorithmically.And so you quickly realize that you can't
01:01:33.089 really separate these notions of reducibilityand irreducibility from these notions of equivalencing.
01:01:39.280 And somehow it's all deeply related to whatdata structures do you kind of define as being
01:01:46.619 equivalent or equivalent up to natural isomorphismor whatever. And that's really quite a difficult
01:01:51.090 problem that relates to definitions of thingslike observers in these physical systems,
01:01:56.089 right? If you have someone who is embeddedin one of these data structures, what do they
01:02:00.190 see as equivalent, which might be very differentto what a kind of God's eye perspective views
01:02:04.539 as being equivalent from the outside.JSON So are there close timelike curves in
01:02:08.309 Wolfram'sphysics project? Sorry, HD project.
01:02:11.660 SIMON No, we can say Wolfram physics. I mean,that's
01:02:15.550 how it's known, right? No, so yeah, that'sa really good question, right? Because in
01:02:20.849 a way, it's very easy to say no, because wecan do that trick that I just described, where
01:02:27.330 you just tag everything with a time step number.And then of course, even if the hypergraph
01:02:31.549 is the same, the time step is different. Sothere's no equivalence thing. In the multiway
01:02:35.450 system or the causal graph, you never seea cycle. But that's somehow cheating, right?
01:02:39.960 And when people ask about CTCs, what theycare about is not this very nerdy criterion
01:02:46.320 of, oh, do you actually get exactly equivalentdata structures? What they care about is…
01:02:50.770 JSON Nerdy criterions seems to define thisentire
01:02:53.160 conversation up until this point.SIMON Well, yes, I suppose. You know, you
01:02:59.099 take twopeople with math backgrounds and get them
01:03:01.230 to discuss stuff.JSON Yeah, exactly, exactly.
01:03:02.640 SIMON That's going to happen, right? But yeah,so…
01:03:05.750 JSON But yeah, what they care about, peoplewho
01:03:07.680 care about time travel.What one cares about is, yeah, exactly, is
01:03:12.230 time travel and causality violations and thingswhich don't necessarily care about your equivalency
01:03:18.010 or care about them in a slightly differentway. Yeah, I mean, so my short answer is I
01:03:25.359 don't know. Because I think we can't…My personal feeling is we are not yet at this
01:03:32.609 level of maturity where we can even pose thatquestion precisely for the following reason,
01:03:37.830 right? So even defining a notion of causalityis complicated. So in most of what we've done
01:03:46.549 in that project, in derivations of thingslike the Einstein equations and so on, we've
01:03:50.651 used what on the surface appears like a verynatural definition of causality for hypergraph
01:03:54.960 rewriting. So you have two rewrites. You know,each one is going to ingest some number of
01:04:01.400 hyperedges. It's going to output some othernumber of hyperedges. Those hyperedges have
01:04:04.430 some identifier. And then you can ask, okay,did this future event ingest edges that were
01:04:09.349 produced in the output of this past event?And so if it did, then the future event couldn't
01:04:13.630 have happened unless the past event had previouslyhappened. And so we say that they're causally
01:04:17.069 related. So somehow, if the output set ofone has a non-trivial intersection with the
01:04:20.760 input set of another, we say that they'recausally related. That seems like a perfectly
01:04:26.510 sensible definition, except it requires…It has exactly the problem we've been discussing,
01:04:31.140 right? It requires having an identifier foreach of the hyperedges. You need to be able
01:04:34.080 to say this hyperedge that this event ingestedis the same as this hyperedge that the other
01:04:39.650 event output. But if they're just hyperedges,they're just structural data, there's no canonical
01:04:44.470 choice of universal identifier, of UUID.And so what that means is you can have these
01:04:51.260 degenerate trivial cases where, for instance,you have an event that ingests a hyperedge,
01:04:56.730 changes its UUID, but doesn't actually changeanything structurally. The graph is still
01:05:00.210 the same. Nothing has actually changed, interestingly.But the identifier is different. But now,
01:05:05.579 any event in the future that uses that edgeis going to register as being causally related
01:05:11.319 to this other event that didn't do anything,right? And so you have a bunch of these spurious
01:05:14.690 causal relations. So it's clear that thatdefinition of causality isn't quite right.
01:05:19.770 And so what's really needed is some definitionof causality that isn't subject to this problem,
01:05:24.579 but it's very unclear what that is. And I'veworked a little bit on trying to formalize
01:05:28.650 that by recursively identifying hyperedgesbased on their complete causal history, right?
01:05:35.059 So the identifiers are not chosen arbitrarilyas random integers or something. But instead,
01:05:40.050 each hyperedge encodes, in a slightly blockchain-yway, a directed acyclic graph representation
01:05:46.000 of its complete causal history. And so thentwo hyperedges are treated as the same if
01:05:49.910 and only if they have the same history ofcausal relationships in the rewriting system.
01:05:54.319 And that's somewhat better, but again, isquite complicated to reason about. And it's
01:05:59.660 all deeply related to this question of whatdata structures do you ultimately treat as
01:06:04.119 being equivalent, which is really an observer-dependentthing. It depends on the computational sophistication
01:06:09.450 of the person or entity who is trying to decodewhat the system is doing. It's not a kind
01:06:14.231 of inherent property of the system itself.So what do you make of observer theory, which
01:06:19.809 is a recent large blog post by Stephen, anda theory, well, an outlook. So what do you
01:06:27.540 make of it?Yeah, so observer theory really has, it's
01:06:31.950 a rebranding of this thing that's been a featureof the physics project since before we started
01:06:36.360 it, right? So this idea that, yes, exactly,that you cannot sort of consider a computational
01:06:44.600 system independent of the observer that isinterpreting its results. And somehow, both
01:06:51.750 the computational sophistication of the observerand the computational sophistication of the
01:06:55.650 system have to be factored into that descriptionsomehow. So in a way, it's a very natural
01:07:01.119 idea, which is really the prelude to the workwe did on quantum foundations and other things
01:07:07.130 in the context of the physics project.I like to think of it as a kind of natural
01:07:11.510 extension of a bunch of stuff that happenedin 20th century physics, right? Because of
01:07:16.119 course, this is not how these things wereviewed at the time, but both general relativity
01:07:22.400 and quantum mechanics can in some sense bethought of as being theories that you arrive
01:07:27.070 at by being more realistic about what theobserver is capable of, right? So if you say,
01:07:35.540 okay, a lot of traditional scientific modelsmade this assumption.
01:07:39.829 That the observer was kind of infinitely farremoved from the system that they were observing.
01:07:43.560 That they somehow, you know, they were thesekind of omnipotent entities.
01:07:45.810 They didn't have any influence over the systems.They weren't constrained by the same laws.
01:07:49.540 But if you then say, okay, well maybe theobserver has some limitations.
01:07:52.290 Maybe they can't travel faster than light,right?
01:07:54.170 What does that imply?Well, in some, if you follow the right chain
01:07:57.230 of logical deduction, what that implies isgeneral covariance and therefore general relativity.
01:08:00.840 That as soon as you have observers who can'ttravel faster than light, they don't necessarily
01:08:05.280 agree on the ordering of space-like separatedevents and suddenly you get general relativity.
01:08:08.319 Equivalently, if you have observers who areconstrained by the same physical laws that
01:08:15.760 of the systems that they're observing, thenwhat that means is, you know, if you try and
01:08:19.870 measure some property of a system, what happenswhen you measure it?
01:08:22.930 Well, you have to have some interaction withit.
01:08:24.390 You have to kind of poke it somehow and, youknow, and the poke that you receive back is
01:08:28.210 going to be equal in magnitude to the pokethat you gave to the system.
01:08:31.219 And so anytime you try and measure some quantity,there's a minimum amount that you have to
01:08:34.729 disturb it.And again, if you kind of follow that chain
01:08:37.100 of reasoning to its logical conclusion, youget at least the kind of Heisenberg picture
01:08:41.899 of quantum mechanics.So in a way, both general relativity and quantum
01:08:45.390 mechanics are, as I say, you know, ways ofbecoming more realistic about what observers
01:08:48.759 are capable of and ways of coming to termswith the fact that observers are constrained
01:08:55.359 by the same physical laws as the systems thatthey observe.
01:08:58.410 So observer theory, which, I mean, I don't,I don't think it's yet a theory, so I'm not
01:09:04.790 sure it's, you know, I'm not, I'm sure I,I, I, I'm hugely fond of the terminology,
01:09:09.430 but I mean, it's, it's a, it's a, yeah, it'sa conceptual idea is really just the kind
01:09:16.899 of computational instantiation of that.And you know, so my feet, okay.
01:09:22.560 You mentioned before this very interestingthing about geometry that, that somehow, you
01:09:26.180 know, you, you have this freedom of, do youchoose to vary curvature, do you choose to
01:09:30.580 vary torsion, do you choose to vary non-matricity?My feeling is that there's a similar free
01:09:35.429 parameter that exists in our scientific modelswith regards to the role of the observer.
01:09:39.929 And this is again, maybe a point of philosophicaldeparture from, between me and Stephen is,
01:09:47.429 so you have these kind of, you can imaginethese two extreme cases, right?
01:09:51.260 You can imagine the case where all you careabout is the computation that the system is
01:09:54.830 doing.It's picking up some, some structure from,
01:09:57.540 from, you know, from, from bottom up rules.And so the observer, so to speak is just some
01:10:03.230 trivial object that's seeing the data structureand all of the kind of computational burden
01:10:07.080 is being shouldered by the system itself.And you know, that's kind of the, that's the
01:10:12.080 way that the physics project is often presented,right?
01:10:14.390 You just have a hypergraph and it's doingits thing and we kind of, we, we, we perform
01:10:18.330 analyses on it.That's one extreme.
01:10:20.739 There's another extreme where you could say,well, maybe the system itself is trivial.
01:10:23.510 You know, the computation it's doing is, is,is essentially trivial and all of the sophistication
01:10:28.140 is all the kind of computational burden isshouldered by the observer.
01:10:31.300 So the case of that would be what Stephenrefers to as the Ruliad, which is really
01:10:34.659 just this, what I was describing earlier,this kind of category of, you know, all possible
01:10:39.530 elementary data structures and all possiblecomputations.
01:10:43.600 And so in that picture, I mean, that, that'sa kind of, that's an object that minimizes
01:10:48.920 algorithmic complexity, right?It minimizes Kolmogorov complexity, the, you
01:10:52.060 know, the, the, the, the, the, the set ofall possible computations has the same algorithmic
01:10:57.520 complexity as the set of no computations justpurely for information theoretic reasons.
01:11:02.690 And so in that case, you know, the, the actualcomputation that generates it is trivial.
01:11:06.699 It's, you know, it's trivial to specify, butin order to get a particular computational
01:11:12.570 path or in order to restrict down to a particularmulti-way system, you have to have an observer,
01:11:17.940 some generalized observer who is making equivalencesbetween different paths.
01:11:21.800 And the sophistication of that observer canbe arbitrarily high.
01:11:25.170 And so you have these two extreme cases, one,one case where the observer is trivial, all
01:11:29.460 the computation is being done by the system.Another case where the system is trivial,
01:11:32.840 all the computations being done by the observer.And my argument is these two cases, I mean,
01:11:37.670 there's no observational way of distinguishingbetween them.
01:11:40.300 And in fact, there's the whole interstitialspace in the, in the middle where you have
01:11:43.639 some of the burden being shouldered by thesystem, some of the burden being shouldered
01:11:45.900 by the observer.And these are not really things that we can
01:11:49.060 observationally distinguish.And so in a sense, it's a, it's a genuinely
01:11:51.530 free parameter in how we construct our models.And I would even go so far as to say that
01:11:56.450 I think in some sense, this argument thatoccurred in early European philosophy between
01:12:03.900 the kind of empiricists and the rationalists,right, between people like, you know, Locke
01:12:08.380 and, and, and Hume on the kind of empiricistside and people like, you know, Descartes
01:12:13.380 and, and Bishop Berkeley and so on, and onthe, on the rationalist side, that's really
01:12:18.060 the kind of, this is really the modern versionof that same argument, right?
01:12:20.840 The empiricists saying, we need to get theobserver out of the picture as much as possible
01:12:25.159 and just describe the systems.The rationalists saying, no, no, you know,
01:12:28.670 what matters is the internal representationof the world.
01:12:30.719 And, you know, the, the external reality issomehow some secondary emergent phenomenon.
01:12:35.920 That's exactly this, this case, right?That, that, that, that, in a sense, the two
01:12:39.699 extremes of, you know, maximal algorithmiccomplexity of the observer versus maximal
01:12:43.949 algorithmic complexity of the system.I'm confused as to the difference between
01:12:48.210 observation and perception, because Stevenwould say that, look, because you're an observer
01:12:53.250 of the kind that you are, you then derivegeneral relativity or have that as a property
01:12:58.310 or quantum mechanics.But then firstly, we all don't perceive the
01:13:02.620 same.And then we also don't perceive quantum mechanics
01:13:05.050 nor general relativity.In fact, in many ways, we perceive the earth
01:13:07.760 as being flat and we don't perceive any ofthe other colors outside of the spectrum of
01:13:12.080 visible light.So yeah, it's a painstaking process to then
01:13:15.270 say, well, what are the laws of physics?We have to somehow derive that, test that.
01:13:20.460 And then the question is, well, does a catperceive the same laws?
01:13:24.340 Well, a cat doesn't perceive, perceive, thisis what I mean.
01:13:28.179 We don't perceive the same.The cat doesn't perceive the same, but presumably
01:13:33.060 it's on the same field.We're playing on the same field.
01:13:36.080 The cat is playing on the same field of generalrelativity and quantum mechanics as we are.
01:13:41.880 So sure, our perceptions are different, butthen would Wolfram say that our observations
01:13:46.820 are the same?Like delineate for me an observation and a
01:13:53.350 perception.Yeah, that's a really important distinction,
01:13:54.630 right?And it goes back to some really kind of foundational
01:13:58.199 ideas in early philosophy of science and peoplelike Thomas Kuhn and others and Karl Popper,
01:14:05.050 who stressed the idea of theory-ladennessof observation.
01:14:08.620 So I think in the way that you're using thoseterms, I think it's an important distinction.
01:14:14.140 The perceptions are kind of much closer tojust the qualia that we perceive, the qualia
01:14:18.810 that we experience.And the observations are some kind of interpretation
01:14:21.600 that we give to them.And so the important point, I think the point
01:14:25.160 that people like Kuhn and Popper were makingwith theory-ladenness is that, in a sense,
01:14:30.070 we perceive nothing as it, quote, really is.Anytime we make a scientific observation,
01:14:38.200 we're not perceiving the phenomenon.It's filtered through many, many layers of
01:14:41.830 observation and interpretation and analysis.So when we say that we have detected this
01:14:51.660 particle in this particle accelerator, whatdoes that actually mean?
01:14:54.390 Well, it means that there was some clusterof photons in this detector that were produced
01:14:59.780 by some Cherenkov radiation, which would thenstimulate some photovoltaic cells on the scintillator.
01:15:07.580 There may be a hundred layers of models andtheories and additional bits of interpretation
01:15:16.010 in between whatever was going on in that particleaccelerator and the bits of photosensitive
01:15:20.880 cells that were stimulated in the scientists'eyes as they looked at the screen and saw
01:15:25.510 this thing.And so if you actually try and trace out how
01:15:28.600 many levels of abstraction are there betweenthe quote-unquote perceptions and the quote-unquote
01:15:33.820 scientific observations, it's huge, right?And it only takes one of those to be wrong
01:15:39.750 or tweaked a little bit.And suddenly, the model that you have of the
01:15:43.550 world, which is still just as consistent withyour own perceptions, is completely different,
01:15:48.719 right?So yeah, I think that's an important thing
01:15:51.380 to bear in mind.It's a thing in a sense which annoys me a
01:15:56.440 little bit with regards to some criticismsof experimental validation, because I think
01:16:04.360 people tend to get...That's an area where people kind of get confused
01:16:07.389 in terms of that distinction.The people say...
01:16:10.659 It annoys you just a bit?Only a bit?
01:16:14.020 Well, maybe I don't have to deal with it asmuch as you do.
01:16:17.100 Well, no, I don't deal with it.I just mean, I'm curious if it annoys you
01:16:20.969 more than that, or if you're just being polite.Well, I mean, it maybe would annoy me if I
01:16:26.030 was being confronted with it all the time.But when you see people kind of saying that,
01:16:33.810 oh, the multiverse is fundamentally unobservable,that seems to me to make this exactly the
01:16:42.370 mistake that you're characterizing, right?It's not perceivable, sure.
01:16:47.410 Most things that we care about in sciencearen't perceivable, right?
01:16:49.990 I think David Deutsch has this nice examplethat no one has ever seen a dinosaur.
01:16:54.330 No one ever will see a dinosaur.We'll never get a dinosaur in a lab, right?
01:16:57.719 If you restrict science to only be about thingsthat we can directly perceive, or test in
01:17:03.190 the laboratory or something, then you can'tmake statements about dinosaurs.
01:17:05.679 You can make statements about the compositionand distribution of fossils, but that's not
01:17:09.699 very interesting.Or at least if you only care about the properties
01:17:12.409 of certain rocks, you would be a geologist,not a paleontologist.
01:17:15.850 The point is that when we look at the compositionand distribution of fossils,
01:17:19.690 that perceptual data is consistent with amodel of the world that logically implies
01:17:26.950 the existence of dinosaurs. And that's reallywhat we mean when we say we have evidence
01:17:31.010 of dinosaurs. To be clear, not that I'm particularlydefending the multiverse view or anything
01:17:35.120 like that, but there's a really importantdistinction between, yes, the multiverse is
01:17:39.700 not perceivable, which is true, and it's notpossible on the basis of perceptions that
01:17:45.750 we can have to validate a model of the worldthat is logically consistent with the existence
01:17:51.100 of a multiverse, which is a very differentstatement, and a much more reasonable statement.
01:17:55.560 And yet, in the popular discourse about thesethings, those are things that often get confused.
01:17:59.820 So yeah, it annoys me when I see it, and maybewould annoy me more if I saw it more often.
01:18:06.560 JSLSpeaking of points of annoyance, what are
01:18:08.870 your thoughts on the state of publishing?So what's your stance on peer review, and
01:18:16.000 where academic publishing is headed, evenin its current state?
01:18:21.830 PGYeah. So I had the slightly depressing experience
01:18:27.200 recently, I'm not sure whether you've donethis, of going to Google Scholar and searching,
01:18:30.719 you know, in inverted commas, as an AI languagemodel or, you know, some other similar thing,
01:18:35.949 right? And just seeing the sheer volume ofpapers that have passed so-called peer review
01:18:40.330 in so-called prestigious journals, that arejust obviously, you know, not human written,
01:18:45.670 with no indication of that fact. And thereare obviously plenty of examples, you know,
01:18:51.980 the Sokol affair, and, you know, other thingswhere, you know, this process that, on the
01:18:58.800 surface, sounds like a very reasonable idea,this, you know, the idea that, you know, you
01:19:02.389 claim some new result, you get people whoknow the field to kind of say, yes, that's
01:19:05.489 a reasonable result, or no, this is not quiteright. That's a perfectly reasonable model.
01:19:09.580 It's just not what peer review actually isin practice. And, yeah, it's important to
01:19:15.290 remember, as well, that in a sense, the modernsystem of scientific publishing, and indeed,
01:19:21.980 the modern system of academia, was not reallydesigned, right? Like, no one sat down and
01:19:26.470 said, this is how we should do science. Itjust kind of happened, right? This model of
01:19:29.870 scientific journals, and peer review, andeditors, and so on, you can trace that back
01:19:34.889 to a direct extension of these early proto-journals,like the Transactions of the Royal Society,
01:19:41.750 which, if you go back and look at them, werevery different to modern scientific journals,
01:19:45.880 right? It's always kind of entertaining whenyou go and read, you know, submissions to
01:19:49.720 the Transactions of the Royal Society thatwere made by Robert Hooke, and Robert Boyle,
01:19:52.989 and Isaac Newton, and so on, because theybasically read like blog posts. They're actually
01:19:57.500 very, very informal. You know, you have theseguys that just go in and they say, oh, I did
01:20:02.350 this, I did that, I mixed this chemicalwith this, and I saw this thing, and then
01:20:05.929 my cat knocked my experiment over, and whatever.It's very conversational. It's very discursive.
01:20:14.719 And yes, it was reviewed, but the review processwas much less formalized than it is. I'm not
01:20:20.139 saying that something like that could worktoday. I mean, science is much more sort of
01:20:23.670 industrialized, and so on. You clearly needa more systematic way of processing the volume
01:20:29.350 of scientific literature that's being produced.But still, it's pretty evident that there
01:20:35.050 was never any person who said, this is a goodmodel for scientific research and dissemination.
01:20:39.880 This is how it should be done. It naturallyevolved from a system that really wasn't set
01:20:43.469 up to accommodate what it's become.Another important thing to remember is that
01:20:50.760 the notion of scientific publishing and thenotion of peer review served a pair of purposes,
01:20:58.159 which in the modern world have essentiallybecome distinct. So it used to be that journal
01:21:02.719 publishers served two roles. They were therefor quality control, because of peer review,
01:21:06.470 and they were there for dissemination, becausethey actually printed the physical manuscripts
01:21:09.580 that got sent to libraries and things. Inthe modern era, with things like archive,
01:21:13.960 and sci-archive, and bio-archive, and generallypre-print servers, and people able to host
01:21:18.780 papers on their website, dissemination, whichwas always the expensive part of journal publishing,
01:21:24.740 we don't need that anymore. We'vegot that covered.
01:21:27.370 So peer review is for quality control?Yes, exactly. The real role for journals now
01:21:34.100 is quality control, in my opinion. The issuewith that is that's incredibly cheap, because
01:21:40.960 I review papers as does every other academic,and we do it for free. We do it because it's
01:21:45.500 public service and whatever, and it's an importantthing to do. So we don't get paid. The people
01:21:51.620 writing the papers don't get paid. The journalsshouldn't need to spend lots of money to print
01:21:56.170 physical copies. So really, journal publicationshould be not quite free, but basically incredibly
01:22:01.510 cheap, and it's not. The reason is becauseyou have these journals who are essentially
01:22:06.409 kind of holding on to this very outmoded model,where they're pushing the dissemination part,
01:22:11.540 I would argue, at the expense of the qualitycontrol part. And so that's why I've been
01:22:15.340 a great advocate. There are these new kindsof journals that are coming out. There's one
01:22:20.920 called Discrete Analysis and a few othersthat are these so-called archive overlay journals,
01:22:26.720 which I think are a fantastic idea. The ideais we say the content itself is going to be
01:22:32.230 hosted on the archive preprint server, sowe don't need to care about dissemination.
01:22:34.690 So that's all incredibly cheap. We just literallypost a link to an archive paper. And so all
01:22:38.970 we're going to do is worry about the qualitycontrol. And then once you start to think
01:22:43.520 about that, and once you're not bound to havingphysical copies that have to go to printers
01:22:47.030 and things, you can actually do peer reviewin a very different and, I would argue, much
01:22:50.280 more productive way. You can have open post-publicationpeer review, where rather than pre-publication,
01:22:58.230 the manuscript gets sent to some anonymousreviewers and then they spend six months deliberating
01:23:01.989 and they get the result back and no one eversees it. You can have something where someone
01:23:05.750 posts a preprint on archive, it goes on anopen review site, and then anyone in that
01:23:10.420 area, or anyone outside the area, can comein and say, I don't understand this, or this
01:23:14.190 doesn't make sense, or oh, this is a greatpaper or whatever. And then you can kind of
01:23:17.170 upvote, downvote, you can say, oh yeah, Iagree with your criticism, et cetera. And
01:23:20.970 the whole thing can be open and de-anonymized.And it would have to be anonymized by the
01:23:24.949 person who's publishing, who's posting itup there, because otherwise, if people see
01:23:28.860 that Ed Witten posted something, more eyeswill go toward that. But you can also, if
01:23:33.010 you're in the field, you can discern sometimeswho's publishing what.
01:23:36.110 Yeah, absolutely. And certainly in math andphysics, and computer science, in places where,
01:23:44.100 in those fields, it's been standard for manydecades now, for several decades, that everyone
01:23:48.410 posts their work on archive. And they posttheir work on archive typically before or
01:23:52.140 possibly simultaneously with submitting theirwork to a journal. So because of that, physics
01:24:00.690 journals, journals like J-HEP or ClassicalQuantum Gravity, et cetera, they don't even
01:24:03.770 try and anonymize their manuscripts, becausethey know if they anonymized it, you could
01:24:07.239 just Google the first sentence and go findthe archive paper and see who posted it.
01:24:10.870 So yes, I think double-blind peer review,et cetera, made sense in a particular era
01:24:17.630 to eliminate exactly the kinds of biases thatyou're characterizing and other ones. But
01:24:23.270 for math and physics, where the workflow is,you put your paper on archive and then maybe
01:24:26.610 a couple of weeks later you submit it to ajournal, it doesn't make sense at all. And
01:24:29.910 so people don't even try.So about the journal's inflated prices, outside
01:24:34.530 of an oligarchy or collusion, what's keepingit high?
01:24:42.600 I mean, I'm, I'm reticent to claim that it'sa collusion. I mean, so, you know, a lot of
01:24:52.240 it is just that a lot of it is tied into thepromotion structure in academia, right? So
01:24:58.510 a lot of it is tied into, if you want to geta permanent job in academia, if you want
01:25:03.160 to advance up that, that ladder, you needto get, you know, there's this general view
01:25:06.639 that you need to get published in the fancyjournals. And then that means that the journals
01:25:10.010 that are generally perceived by universityadministrators as being the fancy ones know
01:25:14.010 that they can charge essentially arbitrarilyhigh prices and people will pay them because
01:25:17.869 they kind of, because you know, their livelihoodsdepend on it, right?
01:25:22.909 It's a really quite sordid situation whenyou think about it.
01:25:26.360 I saw a talk recently by someone who was goinginto the academic world saying that
01:25:30.429 some of the applications for professorshipor postdocship, that the second question after
01:25:35.830 what is your name is how many citations doyou have? And then people try to game this
01:25:39.639 because you can publish something that isjust worthy of publication and do that many
01:25:44.810 times rather than produce something that youfeel like it's of high quality, but we'll
01:25:48.820 get less citations than if you were to splitthat up and then you just flood the market.
01:25:53.489 Yeah, absolutely. And you know, there arethese metrics, there's author level metrics
01:25:58.170 like the H index and so on, which measure,you know, so H index equals N means that you
01:26:03.370 have N papers that have been cited at leastN times. And that gets used actually quite
01:26:06.699 frequently in hiring committees and tenurecommittees and things like that. And yeah,
01:26:10.130 it's incredibly easy to game, right? It'sthis classic Goodhart's law example where,
01:26:14.239 you know, as soon as you know that you'rebeing measured on that criterion, you can
01:26:17.980 then say, oh, I'm going to just cite myselfin all, you know, every future paper I'm going
01:26:22.100 to write, I'm going to cite myself in allprevious ones. And then I can very easily
01:26:25.000 get some kind of N squared dependence on myH index and then I can get my friends to cite
01:26:29.120 me too. And I can, as you say, rather than,you know, rather than investing a year to
01:26:34.280 write this one really good polished definitivepaper on this subject, I'm going to write
01:26:39.240 10 like salami sliced mini, you know, minimumpublishable unit things.
01:26:43.330 Yeah, yeah, right. That's a great way of sayingit.
01:26:46.100 Right. And yeah, and all of that happens,right? And it requires, and I know I'm guilty
01:26:51.710 of some of that too, you know, not becauseI want to be, but because, you know, I need,
01:26:55.340 you know, I, I live in the academic systemand that's kind of how one has to operate
01:26:58.800 to a certain extent. If you're competing withother people who are doing that, it's, it's
01:27:01.930 awful. Right. And I don't, I don't want tobe in that situation. And you know, I, yeah,
01:27:06.540 if obviously if given the choice, I alwaystry to be someone who, yeah, if I'm going
01:27:10.619 to invest the time to write a paper on something,I want to write in as much as possible, the
01:27:15.429 definitive paper on that thing and have itclean and polished and, and something that
01:27:18.970 I'm proud of. But yeah, it's, I think it'smy impression at least is that it's becoming
01:27:23.369 increasingly hard for that to be a viablecareer strategy.
01:27:25.860 Yeah. What's fortunate in your case is thatyou were employed by Wolfram for some time.
01:27:30.239 And so you were able to work on the ideasthat were interesting to you and not have
01:27:34.560 to concern yourself. Maybe I'm incorrect,but at least from my perspective, you didn't
01:27:37.781 have to concern yourself with incrementalpublications on ideas that aren't innovative
01:27:42.500 in order for you to build the credit to yourname, but maybe I'm incorrect.
01:27:47.510 Well, I mean, there was certainly an elementof that, right? So during the time I was employed
01:27:53.130 at Wolfram, I, I, you know, I also was, Imean, initially I was a graduate student or
01:27:58.860 actually very early stages. I was an undergraduate,then I was a graduate student, and then I
01:28:01.830 was a kind of junior academic. So I stillhad some academic position during that time.
01:28:07.260 And for that reason, it wasn't something Icould completely ignore, right? I think because,
01:28:11.980 you know, that would have been kind of irresponsiblefrom a career standpoint, but yes, in a way
01:28:14.659 it did take the pressure off because it meantthat I, it meant that I had a kind of more
01:28:18.670 or less guaranteed funding source for at leastpart of my research. And I wasn't having to
01:28:23.330 repeatedly kind of beg, you know, governmentfunding agencies for more money and things
01:28:27.469 and show them long lists of papers. It wasalso useful in a different way, which is that
01:28:32.619 it meant that the stuff I was doing got muchmore exposure than it would have done otherwise.
01:28:36.680 I mean, like, you know, we wouldn't have met,you know, if, if it hadn't been for Steven,
01:28:40.469 right. And, and, and the, the kind of theadditional, both the additional cache and
01:28:44.949 the additional flack that is associated with,you know, with having his name attached to
01:28:49.920 the project. And so, yeah, in a way it meantthat there was for, you know, for my level
01:28:54.780 in the, in the academic hierarchy, my workended up being significantly overexposed and
01:28:59.970 yeah, that was good in a way, it was bad inanother way. It, why would it be bad? Well,
01:29:05.860 it meant that in a, okay. So, you know, soone negative aspect of it, which has not been
01:29:12.639 hugely problematic, but is, you know, Stevenhas a certain reputation, right. And that
01:29:17.301 reputation is positive in many ways and negativein many other ways. And by, you know, if you
01:29:23.531 are billed as, you know, you are the personwhere you are the other person or one of the
01:29:27.010 other people working on the Wolfram PhysicsProject, you get, there's a, there's a sense
01:29:30.510 in which you're elevated by association andyou get tainted by association. And people
01:29:34.460 assume that, you know, yeah. People assumethat, that many of the negative characteristics
01:29:39.090 associated with, you know, I don't know, notgiving appropriate credits to, to prior sources
01:29:44.980 or, you know, having slightly inflated egoissues, et cetera, right. Many of those things
01:29:49.050 kind of get projected on you rightly or wrongly,but yeah, by virtue of association.
01:29:53.300 Yeah. Or that you're supporting that. So maybeyou don't have those qualities.
01:29:56.760 Okay.Right. Right. And, and it's, it's a, yeah,
01:29:59.471 it's a difficult thing to, to throw. I mean,in a way it helped because it meant that a
01:30:05.070 lot of the criticism of the project got leveledat
01:30:08.230 Steven, not at the rest of us. Right. So ina way it was useful, but yeah, but in other
01:30:13.080 senses,you know, it was a, yeah, it's a delicate
01:30:15.440 balance.So how do you see academics engagement with
01:30:17.910 the ideas from the Wolfram Physics Project?Yeah, it's been mixed, very mixed. So on the
01:30:25.020 kind of traditional fundamental physics people,it's mostly been, you know, ignored. Right.
01:30:32.430 So like if you look at your average stringtheorist,
01:30:35.760 many of them will have, or you talk to them,many of them will have heard of the project
01:30:38.580 and willsay, oh, that's that weird kooky thing that
01:30:40.451 that guy did. And we don't really know anythingabout
01:30:42.369 it. Right. That's at least that's the generalresponse that I've seen.
01:30:45.889 They'll say they scrolled through the blogposts, but then didn't find anything
01:30:48.909 readily applicable to their field. And sothey're just waiting for it to produce results.
01:30:52.750 That'sthe general state. Right. Exactly. And then
01:30:55.560 they'll say the necessary, well, I wish himluck,
01:30:58.630 but firstly, I don't think they actually meanthat. Secondly, if they do, they only mean
01:31:02.260 thatbecause they're not competing for the same
01:31:04.119 dollars. Yes. And I've certainly had conversationswith people who are not quite so polite, but
01:31:10.790 yes. So there's that crowd. There are somepeople in
01:31:16.360 the quantum gravity community who have actuallytaken some interest and have started, you
01:31:19.909 know,have cited our work and have used it and it's
01:31:22.040 been incorporated in other things. So causalset
01:31:23.890 theory is one example of a, that's again,a slightly unconventional branch to quantum
01:31:30.930 gravitythat's really quite formalistically similar
01:31:33.230 in a way. Causal sets are really just, youknow,
01:31:36.120 they're partially ordered sets. They're reallythe same as causal graphs in some sense. And
01:31:39.360 sothere's a precise sense in which you can say
01:31:42.790 that the, you know, that the hypergraphicwriting
01:31:44.800 formalism is just giving you a dynamics forcausal set theory, which causal set theory
01:31:48.160 does notpossess a priori because it's essentially
01:31:50.179 a kinematic theory. And so in those communities,it's been somewhat more receptive. There's
01:31:56.060 been, again, there are in areas, this is essentiallyunsurprising, right? So in areas where there
01:32:02.130 is formalistic similarity, like say loop quantumgravity, where there's some similarity in
01:32:06.260 the setup of things like spin networks andspin
01:32:08.210 foams, there's been some interest in thesekinds of topological quantum field theory
01:32:12.011 models ortopological quantum computing models, where
01:32:14.650 again, there's this interest in this intersectionbetween, you know, combinatorial structure,
01:32:19.540 topology, et cetera, and fundamental physics.There's been some interest. An area where
01:32:23.900 we've got a lot of interest is in appliedcategory
01:32:25.940 theory. So, you know, people who, I wouldsay that's been, at least in terms of the
01:32:31.960 stuff thatI've worked on, that's been by far our kind
01:32:34.960 of most warm reception are people workingon
01:32:37.460 categorical quantum mechanics and particularlythese kinds of diagrammatic graph rewriting
01:32:41.290 approaches to quantum mechanics like ZX calculusand so on. We've had some very,
01:32:45.360 very productive interactions with that crowd.And also with people not directly on the physics
01:32:50.219 side,but interested in the formalism for other
01:32:52.430 reasons. So there are people likethe algebraic graph rewriting crowd, many
01:32:57.320 of whom are in areas like Paris and Scotland,who again, you know, have been very interested
01:33:02.550 in what we've been doing. Not necessarilyfor
01:33:04.889 physics reasons, but because they're interestedin the algebraic structure of how we're setting
01:33:08.290 things up or they're interested in how theformalism can be applied to other things like
01:33:12.159 chemical reaction networks or, you know, distributedcomputing and that kind of stuff.
01:33:16.440 Aaron Powell You're currently at Princeton,correct?
01:33:18.619 Tom CloughertyRight.
01:33:19.780 Aaron Powell Okay. So what do you do day today?
01:33:22.290 Tom CloughertySo mostly I work on computational physics.
01:33:26.469 So I work on, you know, developing algorithmsand
01:33:32.409 things for understanding physical phenomenathrough computational means, which is more
01:33:36.280 orless a direct extension of, you know, of the
01:33:39.040 stuff that I was doing at Wolfram Research.But
01:33:41.180 yeah, I'm in a sense, having been associatedwith the physics project and with Wolfram
01:33:47.110 Research forsome time, I now consider in part my role
01:33:51.330 to be trying to get some of those ideas moredeeply
01:33:53.989 embedded in sort of traditional scientificand academic circles. And, you know, not so
01:33:59.060 much tiedto, yeah, as you were putting it earlier,
01:34:02.080 you know, Stephen's own personal researchdollars
01:34:04.050 and that kind of thing.How do you feel when the popular press almost
01:34:08.170 invariably ascribes all,if not the majority, of the credit of the
01:34:12.790 Wolfram Physics Project to Wolfram himself?Tom Clougherty
01:34:16.650 Yeah, it's difficult, right? So as I say,in a way, there is a positive aspect to that,
01:34:24.030 which is that it means that, you know...Aaron Powell
01:34:28.730 You're shielded from direct criticism.Tom Clougherty
01:34:31.270 Right, right. Less likely to be blamed. Butno, I mean, yeah, it's emotionally difficult,
01:34:37.240 right? I think, I don't know, maybe not foreveryone, but certainly for me, I find it
01:34:42.790 quitepsychologically tough if, you know, if there's
01:34:46.690 an idea that I've had that I'm reasonablyproud of,
01:34:48.890 or a result that I've proved that I'm reasonablyproud of, etc., it's not the best feeling
01:34:52.850 to see,you know, headlines and Twitter threads and
01:34:55.639 whatever, where it's all being ascribed toone
01:34:57.639 person. And in my small way, I try to pushback against that. But sorry, go on.
01:35:03.810 Aaron PowellI love Wolfram. I love Stephen. But so this
01:35:07.300 goes without saying, he doesn't domany favors in that regard. So when someone
01:35:14.219 gives him the accolade, it's rare that I'llsee him say, oh, and by the way, that result
01:35:19.700 was from Jonathan Garrard.Tom Clougherty
01:35:22.040 Right, right. And again, I guess we're allguilty of that to a certain extent, right?
01:35:27.719 I mean,I'm acutely aware that in the course of this
01:35:30.020 conversation, I haven't mentioned,for instance, Manoganir Namaduri, who is the
01:35:32.800 person who I kind of did a lot of this workon categorical quantum mechanics with, right?
01:35:36.390 And who deserves, again, a reasonable fractionof the credit for that insight. So I'm guilty
01:35:41.530 of this too, and I guess everyone is to anextent.
01:35:47.300 Stephen, maybe more than many people, butit's a feature of this personality that
01:35:55.310 I can't claim to have been ignorant of.Aaron Powell
01:35:57.250 Sure, sure. So he has another claim, whichis that he solved the second law of thermodynamics.
01:36:03.440 And from my reading of it, I wasn't able tosee what the problem was with the second law
01:36:09.780 and how it was solved, other than you sayyou derive it from statistical mechanics,
01:36:15.420 which was there before. I must be missingsomething because I don't imagine Stephen
01:36:20.620 would make that claim without there beingsomething more to it. So please enlighten
01:36:25.200 me.Tom Clougherty
01:36:26.550 Yeah, okay. So I think, as with many of thesethings, that series of three blog posts about
01:36:36.409 the second law, I think there was interesting,just like with NKS, right? I think there was
01:36:41.659 a lot of interesting stuff there.After they got figured out, it wasn't quite
01:36:45.870 as grandiose as I think Stephen made it outto be. But again, that's the responsibility
01:36:50.929 of any scientist, right? It's to slightlyinflate the significance of what they're doing.
01:36:54.619 So my reading of it is as follows. So there'sa kind of standard textbook, popular science
01:37:03.739 type way that entropy increase gets explained,which is you say, if you define entropy as
01:37:10.400 being the number of microstates consistentwith a given macrostate or the logarithm of
01:37:15.830 that, which is Boltzmann's equation, thenthe fact that entropy has to increase is kind
01:37:19.949 of obvious in some sense because the numberof ordered microstates or the number of microstates
01:37:27.530 consistent with an ordered macrostate is alwaysgoing to be smaller than the number of microstates
01:37:31.850 consistent with a disordered macrostate. Andso if you're just ergotically sampling in
01:37:38.301 your space of states, you're going to tendtowards ones which are less orderly and not
01:37:42.639 towards ones that are more orderly. And thatargument or that explanation seems convincing
01:37:48.730 for a few seconds until you really start tothink about it and you realize that it can't
01:37:52.730 possibly make sense. And one reason, I meana very foundational reason why it can't possibly
01:37:57.119 make sense is because that explanation istime symmetric. So if it's the case that you're
01:38:03.369 ergotically sampling your space ofpossible states, and yes, okay, the less ordered
01:38:08.940 ones are always going to be more numerousthan the more ordered ones, then yes, it's
01:38:11.969 true that evolving forwards in time, you'regoing to tend towards the less ordered ones.
01:38:16.849 But it's also true that if you're evolvingbackwards in time, you would tend towards
01:38:19.580 the less ordered ones. But of course, that'snot what we observe in thermodynamic systems.
01:38:23.020 So that explanation can't be right, or atthe very least, that can't be the complete
01:38:27.660 answer. And so I think the conceptual problemis a real one. I think it is true that we
01:38:37.040 really don't fully understand the second lawof thermodynamics from a statistical mechanical
01:38:40.300 point of view. And as soon as you start tryingto apply it to more general kinds of systems,
01:38:45.980 the problems become worse. I mean, there'sa famous example that was brought up by Penrose
01:38:51.330 of what happens when you try and apply thesecond law of thermodynamics to the early
01:38:56.010 universe. And again, you seemingly get thesetwo contradictory answers. So as the universe
01:39:00.910 evolves forwards, if we believe the secondlaw, as we get further and further away from
01:39:06.960 the initial singularity, entropy should begetting higher and higher. And yet, when you
01:39:12.391 look back close to the initial singularityand you look at the cosmic microwave background
01:39:15.800 and so on, it looks very, very smooth. Itlooks basically Maxwellian, like a Boltzmann
01:39:20.659 distribution. It looks more or less like amaximum entropy state. So we have this bizarre
01:39:26.909 situation where as you move away from theBig Bang, entropy gets higher. But as you
01:39:30.409 go towards the Big Bang, entropy gets higher.So something must be wrong. And Penrose has
01:39:35.330 these arguments about conformal cyclic cosmologyand how the role of gravitational fields is
01:39:40.050 essentially to decrease global entropy andall that kind of stuff. But that's all, again,
01:39:44.409 fairly speculative. And I would say at somedeep level, that's still a story we don't
01:39:47.929 really understand. So that, I think, is theproblem that's being solved. And that series
01:39:55.210 of blog posts proposes... And again, thisis not really that... I mean, even in NKS,
01:40:02.739 there were indications of this idea. But yeah,the basic idea is that you can explain the
01:40:09.869 time asymmetry in terms of computational irreducibility.Where you say, okay, so even if you have a
01:40:15.380 system whose dynamics are exactly reversible,in practice, because of computational irreducibility
01:40:21.030 effects, the system can become pragmaticallyarbitrarily hard to reverse. And that you
01:40:26.630 can think about it essentially as being akind of cryptanalysis problem, right? So in
01:40:30.730 a sense, the dynamics of a computationallyirreducible system are progressively encrypting
01:40:35.150 certain microscopic details of the initialcondition. So that in practice, even if it
01:40:39.270 is in principle possible to reverse from acomputability standpoint, if you try and think
01:40:43.599 about the computational complexity ofthat operation, it's equivalent to solving
01:40:46.989 some arbitrarily difficult cryptanalysis problemto work out, okay, where exactly was that
01:40:51.360 gas molecule at time t equals zero? And thatgoes some way towards explaining this time
01:40:55.930 asymmetry problem. I don't think it's a completeexplanation. I think there's a yet deeper
01:41:01.750 mystery there, but I do think it's an interestingcollection of ideas.
01:41:04.490 Yeah, so that's observer-dependent. So itwould be difficult for you. Sorry, not difficult
01:41:09.920 for anyone, but difficult for an observer.But for the system itself, would there still
01:41:16.170 be that issue of having to decrypt for thesystem itself?
01:41:19.690 Well, no, I would argue not. Because, yeah,it's a very important point, right, that these
01:41:25.370 notions are all observer-dependent. Becausein a sense, the Boltzmann equation requires
01:41:31.550 the existence of a macro state, right? Andthe macro state is an observer. It's a synthetic
01:41:38.719 kind of observer theoretic idea, right? It'slike you've got a bunch of molecules bouncing
01:41:42.510 around in a box, and so they have some microstate details. But then you want to describe
01:41:48.219 that box in terms of gas kinematics. You wantto describe it in terms of a density, and
01:41:51.989 a pressure, and a temperature, and whatever.So those give you your macro states. But the
01:41:56.460 choice to aggregate this particular collectionof micro states and say, these are all consistent
01:42:01.949 with an ideal gas, with this temperature,and this adiabatic index, whatever, that's
01:42:06.150 an observer-dependent thing.And so, yeah, that's another point that, again,
01:42:10.810 I don't think is completely original, butI think has not been adequately stressed until
01:42:15.830 these blog posts, which is that differentdefinitions of an observer will yield different
01:42:20.060 definitions of entropy. Different choicesof coarse grainings yield different definitions
01:42:23.930 of entropy. And therefore, in that sense,it's kind of unsurprising that, as von Neumann
01:42:31.130 and Claude Shannon and people kind of pointedout, that the term entropy is so poorly understood,
01:42:36.040 and that there are so many different definitionsof it. There's entropy in quantum mechanics,
01:42:38.630 there's entropy in thermodynamics, there'sentropy in stat mech, there's entropy in information
01:42:43.710 theory. They're all similar vibes, but they'reformally different. You can have situations
01:42:49.409 where one entropy measure is increasing, oneentropy measure is decreasing, and that becomes
01:42:52.489 much more easy to understand when you realisethat they are all measures of entropy relative
01:42:57.179 to different formalisations of what it meansto be an observer.
01:43:01.540 And yeah, so with regards to the decryptionthing, yes, I would say there's an aspect
01:43:08.630 of it that is fundamental, that is purelya feature of the system. Even if you don't
01:43:15.929 have any model of the observer and you'rejust looking directly at the data structures,
01:43:19.210 you can have the situation where the forwardcomputation is much more easy or much more
01:43:23.500 difficult than the reverse computation. Andobviously those kind of one-way functions,
01:43:26.900 those get used in things like cryptography,right? And the existence of those is quite
01:43:31.960 well studied in cryptanalysis. So those certainlyexist, and those can give you some form of
01:43:36.330 time asymmetry.But arguably, the version of time asymmetry
01:43:39.800 that's relevant for physics is the observer-dependentone. It's the one where you say, actually,
01:43:45.920 for this particular aggregation of microstatesand this particular interpretation of that
01:43:49.360 aggregation as this macrostate, this is thecomputational complexity of the reversal operation.
01:43:54.170 And that is an observer-dependentthing.
01:43:56.349 You mentioned Penrose, and I want to get tosome of your arguments. I don't know if you
01:43:59.560 still have them, but I recall from a few yearsago, you mentioned that you have some issues
01:44:04.460 with Penrose's non-computational mind argument.So I want to get to that, but I want to say
01:44:10.530 something in defense of Stephen, that peopledon't realize what it's like when you're not
01:44:14.270 in academia to one, get your ideas taken seriouslyby academia, and then also what it's like
01:44:19.770 in terms of funding. So people will say that,yeah, sure, Stephen is rodomontade or self-triumphant,
01:44:26.570 but you have to be that to the public becausethat's your funding source. Whereas for the
01:44:31.560 academics, they are that to the grant agencies,to the people they're asking for money, you
01:44:35.660 have to big yourself up. It's just that youdon't get to see that.
01:44:38.739 Yeah, I know. I absolutely agree here.Great, great. Now for Penrose, please outline
01:44:44.590 what are your issues with, I think it's thePenrose-Lucas argument. Although I don't know
01:44:47.810 if Penrose and Lucas, I know Lucas hadan argument and it's called the Penrose-Lucas
01:44:52.619 argument. I don't know their historical relationship.Right, right. And yeah, there's an original
01:44:58.300 argument that's purely using kind of mathematicallogic and Turing machines and things. And
01:45:02.219 then there's the Penrose-Hameroff mechanism,which is the proposed biochemical mechanism
01:45:06.869 by which there exists this non-computabilityin the brain. Yeah, I mean, so, okay, there's
01:45:13.510 an, okay, how to phrase this. There's an elementof this, which I'm quite sympathetic to, which
01:45:19.680 goes back actually to one of the very firstthings we discussed, right? Which is the distinction
01:45:23.099 between what is model versus what is reality.Turing machines are a model. And so if you
01:45:30.090 say, well, the mind is not a Turing machine.I mean, if that's your only statement, then
01:45:36.080 I agree, right? But then nothing, you know,like the universe isn't a Turing machine in
01:45:39.489 that sense, right? The question is, isit useful to model the mind as a Turing machine,
01:45:43.560 or is it useful to model the universe as aTuring machine? And there, I think the answer
01:45:46.940 is emphatically yes. And, you know, okay,are you going to be able to model everything?
01:45:51.810 Well, not necessarily. So again, to that extent,I do have some sympathy with the Penrose-Lucas
01:45:57.930 argument. I'm open to the possibility thatthere may be aspects of cognition that are
01:46:04.300 not amenable to analysis in terms of Turingmachines and lambda calculus and that kind
01:46:07.762 of thing. I just don't think that the particularexamples that Penrose gives, for instance,
01:46:14.250 in his book, Emperor's New Mind, are especiallyconvincing examples, right? I mean, so he
01:46:18.119 has this argument that, you know, mathematics,the process of apprehending mathematical truth...
01:46:25.280 ...must be, you know, a non-computable process,because we know from Gödel's theorems that,
01:46:30.800 you know, for any given formal system, ifit's consistent, then there must be statements
01:46:36.230 that are independent of that system, whereboth the statement and its negation are consistent
01:46:41.830 with the underlying axioms. But we, you know,so Gödel's original argument proved that
01:46:48.560 for Peano arithmetic, for the standard axiomsystem for arithmetic, and later on it was
01:46:52.480 worked for any axiom system that's at leastas strong as Peano arithmetic.
01:46:57.020 And so Penrose's argument, I mean, I'm caricaturinga bit and it's a little unfair,
01:47:01.340 but, you know, the basic argument is, well,we can obviously see that arithmetic is consistent.
01:47:07.830 So when we construct this Gödel sentencethat says this statement is unprovable,
01:47:11.310 we can see that it has to be true. And yet,you know, within the formal axioms of arithmetic,
01:47:17.590 as they are computable, it cannot be decidedin finite time that that statement is true.
01:47:22.580 And, okay, so most of that is correct. Butthe part where you say, well, we as human
01:47:29.369 observerscan clearly see that that statement is true,
01:47:31.710 well, that presupposes that we are able to,you know, we are able to know the consistency
01:47:36.449 of integer arithmetic, which we have strongreason
01:47:38.449 to believe is consistent. But Gödel's secondincompleteness theorem says that, well, we
01:47:43.699 can'tknow that formally either. So in a sense,
01:47:46.780 he's presupposing the conclusion. He's alreadypresupposing that we can know the truth value
01:47:52.219 of an independent proposition, namely theconsistency
01:47:54.510 of Peano arithmetic, in order to prove thatwe can know the truth value of another independent
01:47:59.429 proposition, namely this Gödel sentence.And so for me, it just feels extremely circular.
01:48:03.570 So it doesn't...C.S.: Sorry, can he not use, like, what if
01:48:06.530 he didn't say that it's irrefutable,rather that probably, so far, it seems like
01:48:12.610 Peano arithmetic is consistent.And if it was to explode, it'd be so odd that
01:48:17.820 it hasn't exploded already.And we've explored it quite extensively. Every
01:48:22.719 day, we increase our credence in theconsistency of it. Can he not use an argument
01:48:26.690 like that?HB. He absolutely could, and that would be
01:48:29.670 correct. But then the problem with that is,there's nothing in that argument that a computer
01:48:34.199 could not replicate, right?A machine could also make that same argument.
01:48:38.489 You could also write a computer programthat says, okay, I'm going to test loads of
01:48:41.820 propositions in Peano arithmetic andsee whether I find an inconsistency. And the
01:48:46.150 more propositions I test,the less likely it is that Peano arithmetic
01:48:50.390 is inconsistent. So I can construct – thisis the machine speaking here – I can construct
01:48:54.560 some kind of Bayesian argument that says,you know, I'm this level of confident that
01:48:58.969 this proposition is true.So yes, human beings can do that kind of Bayesian
01:49:02.890 reasoning, but then so can a machine.And so the crux of the Penrose argument, or
01:49:08.699 the Penrose-Lucas argument, is thatthere is this additional non-computable step
01:49:14.889 where the human somehow knows – not assumes,but just knows – that Peano arithmetic is
01:49:19.470 consistent, and from that deduces that T hasto be true. And I don't see how you can justify
01:49:24.139 that without essentially presupposing theconclusion.
01:49:26.750 CW. So what's the difference between intuitionistlogic and constructivist logic?
01:49:31.670 Ah, okay, that's a fantastic question. Andit cycles back to the stuff we were talking
01:49:36.830 aboutat the beginning with regards to constructivist
01:49:38.469 foundations for physics, right? So I wouldsay
01:49:42.369 constructivism is really a kind of broad – okay,the simple answer is intuitionistic logic
01:49:46.770 is aspecial case of constructivist logic. So constructivism
01:49:50.800 is a broad philosophical movementwhere the idea is – so okay, for people
01:49:55.760 who don't know the history of this – soin the aftermath of Gödel's incompleteness
01:49:59.920 theorems, and Tarski's undefinability theorem,and Turing's proof of the undecidability of
01:50:03.640 the halting problem, and all theselimitative results in mathematical logic that
01:50:06.810 happened in the early 20th century,people started saying, okay, well, how can
01:50:10.940 we trust that anything is true in mathematics,right? So if we always have to make some unprovable
01:50:15.410 assumption about the consistencyof our axiom system, how can we ever be confident
01:50:19.429 of anything beyond just the kind of heuristicargument that we made before? And so then
01:50:24.830 various people, especially a guy called Brouwer,and later in his later years, David Hilbert,
01:50:30.590 coddled on to the idea that, okay, what youcould
01:50:32.900 do is you could say, well, if we strengthenour criterion for mathematical proof, if we
01:50:40.500 say thatwhen you reason about a mathematical object,
01:50:43.130 it's not enough just to reason about it abstractly.You actually have to give an algorithm a finite,
01:50:48.380 deterministic procedure that constructs thatobject before your statements can even make
01:50:54.050 sense. That's a much stronger condition,and it immediately rules out certain forms
01:50:58.179 of mathematical proof. So for instance,a proof by contradiction, it would not be
01:51:01.679 allowed in such a paradigm because if youprove a
01:51:05.340 statement, okay, so obviously, suppose I wantto convince you that this equation has a solution.
01:51:13.909 So one way I could convince you is to makea proof by contradiction. I could say,
01:51:16.489 assume it doesn't have a solution, and thenderive some piece of nonsense.
01:51:18.860 Yes, yes, yes.So then my assumption had to be wrong.
01:51:21.170 Yes. You can prove existence without construction.Right, right. But that only works if I assume
01:51:27.699 that the axiom system I was using to provethat
01:51:29.960 is consistent, and that the inference rulesI was using to derive that contradiction were
01:51:34.160 actuallysound. If they weren't, if it was an inconsistent
01:51:36.969 axiom system or the inference rules were notsound,
01:51:38.969 then I could derive a contradiction even froma statement that was true, and so it would
01:51:43.580 beinvalid. And of course, we know from Gödel's
01:51:47.110 theorems and from Turing's work that we cannot,for any non-trivial formal system, know conclusively
01:51:52.750 that the system is consistentor that the inference rules are sound. Whereas
01:51:57.000 instead, if I try and convince you by saying,look, here's a program, here's an actual algorithm
01:52:01.590 that constructs a solution for you,and you can just go and check whether it solves
01:52:05.880 the equation, somehow that's much more convincing.You don't have to assume anything except that
01:52:10.570 maybe the validity of the model of computationcan check that too, right? So you're placing
01:52:16.610 a much lower epistemological burden on theunderlying axioms of mathematics. You can
01:52:24.329 use those to guide you in how you search forthings,
01:52:26.869 but ultimately, the ultimate criterion, theultimate test for truth is, can you define
01:52:33.449 a deterministic algorithm that actually witnessesthe structure that you're talking about?
01:52:38.429 And so this was intended to be a kind of almosta get-out clause from these limitative results
01:52:43.969 tosay, this is a way that we can kind of bypass
01:52:45.849 many of these, not all of them, of course,but many of these issues. Now, it's a very,
01:52:50.480 very significant limitation because it immediatelymeans that there are very large classes of
01:52:54.070 mathematical structures that you just can'ttalk about at all, the structures where you
01:52:58.150 can't avoid undecidability and independence.But rather astonishingly, there are large
01:53:04.300 parts of mathematics, including areas likeanalysis,
01:53:07.120 which you maybe wouldn't have thought wouldbe amenable to constructivism, where many
01:53:10.950 of themost interesting results, the Heine-Borel
01:53:13.139 theorem or whatever, you can actually proveusing purely
01:53:16.580 constructivist means. So that's really whatconstructivism is about. Then intuitionism,
01:53:21.719 which is a particular flavor of constructivismthat's due to Brouwer. So once you've decided
01:53:28.329 that you want to work in constructivist mathematicalfoundations, then you still have
01:53:32.050 the problem of, okay, what are my underlyingrules going to be? How do I actually impose
01:53:37.000 those constraints in a systematic way? Andso intuitionism is just one approach to doing
01:53:41.570 that,where you say, okay, I want to outlaw non-constructive
01:53:46.150 proofs like proof bycontradiction. How do I do that? So one thing
01:53:52.449 that should be outlawed is any use of doublenegation. So the axiom of double negation,
01:53:57.050 that not not x is equivalent to x. I shouldn'tbe
01:53:59.199 able to do that because that allows me todo non-constructive proofs. And it turns out
01:54:03.060 thatif you're going to outlaw that, you also need
01:54:04.989 to outlaw what's called the law of excludedmiddle,
01:54:06.950 a statement that a or not a is true for anyproposition a.
01:54:09.679 Sorry, you need to outlaw it or it's equivalentto outlawing that?
01:54:15.040 It's equivalent to it. So one necessitatesthe other. And then in the kind of logical
01:54:23.270 foundations, that's what you need to do. Andthen that implies certain things like, say,
01:54:26.510 the axiom of choice in set theory. The statementthat if you have some collection of non-empty
01:54:33.210 setsand you assemble a new set by choosing one
01:54:35.990 element from each element of that collection,that that set is necessarily non-empty. Something
01:54:40.540 which is very intuitively obvious for finitecollections, but very not intuitively obvious
01:54:45.200 for finite and countable collections, butnot
01:54:47.960 intuitively obvious for uncountable collectionsof sets.
01:54:50.329 Is that the root of the word intuitionism?Is it actually meant to say that this is more
01:54:54.790 intuitively the case?It's more... So my understanding is that it's
01:55:01.980 more that these were meant to be the minimumrules that somehow... Yeah, I mean, in a way,
01:55:08.350 yes. These were meant to be kind of the minimumconditions that matched human mathematical
01:55:13.940 intuition.Yeah, I don't know. I know there's a whole
01:55:16.310 history of, like I mentioned, I want to doa
01:55:18.909 whole video on gripes with names. So it couldbe something philosophical about Kant and
01:55:24.020 intuition.I have no clue. But do intuitionists not have
01:55:28.250 a concept of infinity? Because you mentionedHeine-Borel, and so it's not embedded in the
01:55:33.830 infinitesimals?Right, right.
01:55:35.849 If you're saying you can do analysis, I don'tunderstand how that can be done.
01:55:40.270 Yeah, okay. This is a really important point.So I mentioned that intuitionism is just one
01:55:45.349 flavor of constructivism, and there are manyothers. And there are ones that are
01:55:49.250 more or less strict. There's a stricter versionof constructivism called finitism,
01:55:56.420 which is exactly that, where you say,not only am I going to be constructivist,
01:56:02.300 but my algorithms have to terminate in finitetime.
01:56:05.969 So if you're an intuitionist,and you don't subscribe to the kind of finitism
01:56:11.230 idea, you might say, well, I can write downan
01:56:13.260 algorithm that solves this. There is a deterministicprocedure, but it may not necessarily terminate
01:56:18.110 infinite time. So an example of that would be
01:56:23.239 the integers, right? So with the integers,I can write down an algorithm which provably
01:56:28.500 constructs the complete set of integers.That algorithm doesn't terminate. If I were
01:56:32.360 to run it on a finite machine, it wouldn'tterminate.
01:56:35.460 But any given integer can eventually be derivedby just repeatedly applying that procedure.
01:56:41.210 So there is actually a way, subject to thiskind of weaker version of intuitionism,
01:56:46.360 there is a way that you can reason about infinitemathematical structures. But if you then say,
01:56:51.219 oh no, I'm not going to allow myself to dothat. I want all the deterministic procedures
01:56:56.950 that Iwrite down have to be constrained so that
01:56:59.770 they always terminate in finite time. Thenyou become
01:57:02.100 a finitist. And then there's variants of that,like ultra-finitism, which I think is quite
01:57:06.630 fun,where one effectively believes that there
01:57:10.890 is a largest number and that that number isdecreasing
01:57:14.650 over time because of essentially physicalconstraints. Yeah, I like it. I don't believe
01:57:19.949 in it, but I like it. Well, again, it's thisquestion of what do you mean by belief, right?
01:57:26.500 I mean, if mathematics is intended to be akind of toolset for modelling certain processes
01:57:32.290 ofthought, then there are certain kinds of problems
01:57:37.139 where I think it's useful to take afinitist or ultra-finitist mindset. Yeah,
01:57:41.260 I agree. If you're a mathematical Platonist,which I'm not,
01:57:45.409 then you might say, okay, well, I believethat the mathematical universe is much larger
01:57:48.640 thanin some ontological sense than the universe
01:57:51.469 that's conceived by ultra-finitists. Butyou know, I at least am a pragmatist, and
01:57:56.440 I say, well, you know, I'm going to use whateverversion of mathematics I think makes sense
01:57:59.380 for this particular problem.So what do you believe to be the primary issue
01:58:04.230 between combining, well, the primarydifficulty? What do you believe to be the
01:58:08.980 primary difficulty between combining generalrelativity and quantum mechanics? Right, so
01:58:17.239 that's been formulated in many ways.So having just sort of slightly slated Penrose
01:58:22.750 for his consciousness views, let metry and right that wrong a little bit by saying
01:58:29.150 I think Penrose has a really, really niceargument
01:58:31.060 for why, even just at a conceptual level,quantum mechanics and general relativity are
01:58:37.790 incompatible,which is the following. That if you take two
01:58:41.159 of the most foundational principles,which in a sense delineate how quantum mechanics
01:58:51.849 is different from classical mechanics andhow
01:58:53.349 general relativity is different from classicalmechanics, those would be the superposition
01:58:57.550 principle in quantum mechanics. The principlethat if you have a system that can be in this
01:59:01.060 eigenstate or this eigenstate, it can alsobe in some complex linear combination of them.
01:59:04.760 And on the side of the Einstein equationsof general relativity, it's the principle
01:59:09.020 ofequivalence, right? It's the principle that
01:59:10.849 accelerating reference frames and gravitationalreference frames are really the same, or to
01:59:14.780 translate that into slightly more mathematicalterms, that anything that appears on the left-hand
01:59:19.599 side of the field equations in the Einsteintensor
01:59:21.290 you can move as a negative contribution tothe right-hand side in the stress energy tensor.
01:59:26.520 So Penrose has this really nice argument forwhy those two principles are logically
01:59:31.470 inconsistent. And the argument goes like this.So suppose that you've got something like
01:59:38.599 aSchrodinger cat-type experiment, where you've
01:59:40.329 got, I don't know, you have like a roboticarm
01:59:42.099 that contains a mass at the end that's producinga gravitational field. And it's connected
01:59:46.800 up to,I don't know, radioactive nucleus that has
01:59:49.550 some probability of decaying.So that arm can be in one of two positions.
01:59:52.810 It can be position A, position B. And theposition
01:59:56.159 that it's in depends on the quantum stateof that nucleus. So now, just naively, what
02:00:00.340 you appear tohave done is created a superposition of two
02:00:02.280 different gravitational field configurations.Okay. So if you do that, you can write down
02:00:08.410 the wave function that corresponds to thatsuperposition
02:00:10.340 and everything looks just fine. So far, there'sno problem. But then if you believe the equivalence
02:00:16.449 principle, then you should get the same wavefunction if you then do the same calculation
02:00:21.050 in an accelerating frame. So if you take thatwhole desktop apparatus, and rather than doing
02:00:24.820 it here on the Earth, you do it in a spaceshipthat's accelerating at 9.81 meters per second
02:00:29.800 square, and you have exactly the same experimentalsetup with the same robotic arm, you should
02:00:34.790 getthe same wave function. But if you calculate
02:00:37.320 it, which again is just a standard calculationin
02:00:39.320 relativistic quantum mechanics, you get almostthe same answer. The two wave functions differ
02:00:44.050 by a phase factor, which normally wouldn'tbe too much of a problem. Normally, if they
02:00:48.739 differ by aphase factor, you say that they're somehow
02:00:50.409 the same quantum system. But the phase factordepends
02:00:53.130 on time to the power four. And because ofsome slightly technical reasons that have
02:01:00.679 to do withthe fact that quadratics have two solutions,
02:01:03.030 if you have a phase factor that depends ontime to
02:01:04.510 the power four, that's telling you that thewave function you've written down corresponds
02:01:07.869 to asuperposition of two different vacuum states.
02:01:11.540 And one of the core axioms of quantum mechanicsis
02:01:13.840 that you can't superpose two different vacuumstates for the very simple reason that the
02:01:17.450 vacuumstate is the kind of zero point from which
02:01:19.400 you measure energies using your Hamiltonian.So if
02:01:22.820 you have a superposition of two differentvacuum states, there's no longer a uniquely
02:01:26.460 definedHamiltonian. There's no longer a uniquely
02:01:28.710 defined energy because there's no rule forhow you
02:01:31.130 superpose those vacua. So it is inherentlyillegal in quantum mechanics to produce those
02:01:36.190 superpositions. So somehow by just assumingthat you could superpose gravitational fields,
02:01:40.840 you've been able to use the equivalence principleto violate the superposition principle or
02:01:45.440 equivalently vice versa. There's a more mathematicalway of seeing the same thing,
02:01:50.130 which is to say that at a very basic level,quantum mechanics is linear and has to be
02:01:55.920 linearby the Schrodinger equation. The Schrodinger
02:01:58.110 equation has to be linear because of thesuperposition principle. So if I have two
02:02:01.520 solutions to the Schrodinger equation, thena
02:02:04.280 complex linear combination of those stateswith appropriate normalization has to also
02:02:08.989 be a validsolution to the Schrodinger equation. General
02:02:11.980 relativity is non-linear and has to be non-linearbecause in a sense, if you take the Einstein
02:02:18.220 field equations and you linearize them, youlinearize the gravitational interaction, then
02:02:22.480 what you get is a version of general relativitythat
02:02:25.099 doesn't possess gravitational self-energy.So in other words, the reason why general
02:02:30.100 relativityis a non-linear theory is because in Newtonian
02:02:33.909 gravity, if I have a mass, that mass producesa
02:02:36.371 gravitational potential, but the gravitationalpotential doesn't produce a gravitational
02:02:41.870 potential. But in general relativity, becauseof the mass-energy equivalence, I have a mass
02:02:45.690 thatproduces a gravitational potential, but that
02:02:46.980 gravitational potential has some energy associatedto it. So it also produces a gravitational
02:02:51.190 field, and that produces another gravitationalfield,
02:02:52.989 and so on. So there's actually a whole infiniteset of these smaller gravitational fields
02:02:57.500 thatare being produced. So this is often summarized
02:02:59.540 by the slogan that gravity gravitates.And that appears as a non-linear contribution
02:03:06.670 to the Einstein field equations,these off-diagonal terms that appear in the
02:03:09.869 Einstein tensor. And so it has to be non-linearbecause if you were to take two solutions
02:03:15.170 to the Einstein equations, two metrics, andjust
02:03:16.980 try and add them together, you quite clearlywouldn't get a third solution to the Einstein
02:03:21.050 equations in general. Because what you'vedone is you've added the gravitational potentials,
02:03:24.900 which is really what the metric tensors areindicating, but you haven't incorporated all
02:03:29.170 these additional non-linear contributionsinduced by the sum of the gravitational potentials
02:03:34.679 themselves. So the basic problem is that youcan't superpose gravitational fields,
02:03:41.469 and that's really what the Penrose argumentis indicating. That if I try and take two
02:03:44.650 metrictensors and just add them in a way that's
02:03:46.949 consistent with the Schrodinger equation,I'll violate the Einstein field equations.
02:03:49.929 And if I try and take two solutions to theEinstein field equations and combine them
02:03:53.900 in a non-linear way that's compatible withgeneral
02:03:55.930 relativity, I'll violate the linearity ofthe Schrodinger equation. And at some level,
02:04:00.110 that's the basic problem. The problem is thatthe linearity of Schrodinger versus the non-linearity
02:04:04.239 of Einstein means that superpositions of gravitationalfields cannot be described
02:04:08.969 without violating at least one of those twoformalisms.
02:04:12.640 Does the conceptual difficulty still persistin quantizing linearized general relativity?
02:04:19.949 So my understanding is that you can certainlyget further with quantizing linearized.
02:04:26.780 So if you just linearize your gravitationalinteraction, you can not only evolve quantum
02:04:33.800 fields on top of a curved space-time describedin terms of linearized gravity, which you
02:04:38.160 cando for Einstein gravity, but you can also
02:04:40.690 describe the back reaction of the quantumfields onto
02:04:45.449 the metric tensor. I actually don't know howmuch further than that you can go.
02:04:49.710 But what I do know is that it's definitelya lot easier. You can make much more rapid
02:04:53.460 progresswith quantizing gravity if you assume linearizations
02:04:56.719 than if you don't. I think thereare still some problems that persist, but
02:04:59.449 I think they're nowhere near as difficult.So how is it that higher category theory overcomes
02:05:04.770 this?That's a great question. The basic answer
02:05:11.510 is I don't know, but there's a very temptingkind of hypothesis. I mentioned towards the
02:05:18.260 beginning that there are these category theoreticmodels for quantum mechanics, and also I think
02:05:22.369 I even mentioned briefly that there are thesemodels for quantum field theory as well. The
02:05:26.290 way that that works is, so we talked at thestart
02:05:28.429 about these dagger-symmetric compact closedmonoidal categories, which are the basic
02:05:34.389 mathematical setup for categorical quantummechanics. The problem with that, though,
02:05:38.170 is that every time you apply one of thesemorphisms, every time you apply one of these
02:05:41.790 time evolution operators, you are essentiallypicking out a preferred direction of time,
02:05:46.639 right? You are assuming you've gotyou know, if you imagine each of your quantum
02:05:50.079 states, each of your spaces of states is aspace
02:05:52.929 of states on a particular space like hypersurface.Once you construct a unitary evolution operator
02:05:57.739 that's a solution to the Schrodinger equation,you are selecting a preferred direction of
02:06:01.770 time,which is of course not relativistic, that's
02:06:04.329 not covariant. So to go from the non-relativisticversion of quantum mechanics to a version
02:06:09.719 that's compatible at least with Lorentz symmetry,you need to have some systematic way of transforming
02:06:14.960 one time direction to another.Well, if you think about it in the category
02:06:18.619 theoretic perspective, through the categorytheoretic lens, there's a systematic way to
02:06:23.800 do that, which is through higher categories.So if you consider categories which have,
02:06:28.050 you know, objects and morphisms, you can alsoconsider
02:06:30.340 two categories that have two morphisms betweenthose morphisms that allow you to transform
02:06:34.610 morphisms to each other, not just objectsto each other. And so if you take the two
02:06:40.390 categoryversion of the one category picture of categorical
02:06:43.900 quantum mechanics,you can allow the two categories to correspond
02:06:47.139 to gauge transformations between your evolutionoperators. So you're transforming the direction
02:06:51.099 of time in a way that's consistent with, say,with the generators of the Lorentz group.
02:06:56.530 And so what you get in some appropriate specialcase
02:06:59.809 is what's called a functorial quantum fieldtheory. So Baez and Dolan constructed this
02:07:05.360 axiomatization of functorial and particularlytopological quantum field theories based on
02:07:10.159 what's called the Atiyah-Segal axiomatizationthat use these two categories and indeed even
02:07:15.270 higher categories as a way of formalizingthis notion of gauge transformations, of being
02:07:18.880 ableto transform between time directions. Okay,
02:07:22.910 so that's a nice piece of mathematics.And in my opinion, is one of the more promising
02:07:29.389 avenues towards constructing a kind ofmathematically rigorous foundation for quantum
02:07:32.780 field theory. What does it have to do withquantum gravity? Well, this is where it necessarily
02:07:38.159 becomes very speculative.But so there's an idea that goes back to Alexander
02:07:42.949 Grothendieck, who I mentioned,this amazing algebraic geometer from the early
02:07:47.139 20th century who really developed a wholebunch
02:07:49.230 of these ideas in higher category theory whilehe was sort of living as basically a hermit
02:07:54.659 inthe Pyrenees, I think. But so Grothendieck
02:07:59.260 made this hypothesis that's now called Grothendieck'shypothesis or the homotopy hypothesis, which
02:08:04.251 goes as follows. Okay, let me motivate itlike this.
02:08:06.800 So if I have a topological space, it has somecollection of points and it has paths that
02:08:13.380 connect those points. But I can also havepaths that connect the paths and those are
02:08:19.000 calledhomotopies, right? So I can continuously deform
02:08:21.750 one path into another and I can use that informationto tell me stuff about the topology of the
02:08:26.460 space. So you can use the homotopy informationto tell
02:08:28.989 you about the homology, right? You can findthat if you're in a donut, you can see that
02:08:33.240 there's ahole there because if you have a loop, a path
02:08:35.830 that loops around that hole, you can'tcontinuously contract it to a point without
02:08:40.719 encountering some discontinuity. So thosehomotopies you can formalize as kind of higher
02:08:47.719 order paths between paths. So in the languageof category theory, you could say my initial
02:08:52.349 topological space is a one category that haspoints and paths between the objects and morphisms.
02:08:58.610 The first homotopy type is the twocategories I construct from that, where the
02:09:02.639 two morphisms are the homotopies between thosepaths.
02:09:04.420 But then I can also consider homotopies betweenhomotopies and so on. So I can construct this
02:09:08.190 whole hierarchy of higher categories and higherhomotopy types. Then that terminates at this
02:09:14.699 infinity category level, which is that thehierarchy has some natural endpoint.
02:09:22.020 And somehow we know that from various resultsin higher category theory that
02:09:30.070 all the information that you care about upto weak homotopy equivalents, about not just
02:09:34.530 thespace you started from, but all of the intermediate
02:09:36.920 spaces that were in that hierarchy, all ofthat
02:09:39.090 information is somehow contained in the algebraicstructure of that infinity category. So the
02:09:43.940 infinity category determines up to weak homotopyequivalents everything that comes in the hierarchy
02:09:48.179 below it. And that's why kind of infinitycategory theory is so different to even just
02:09:52.219 normalfinite higher category theory. Infinity categories
02:09:54.980 somehow contain far more information. There'sactually a specific type of infinity category
02:09:59.909 called an infinity groupoid because the pathsare invertible. And Grotendieck was really
02:10:06.619 one of the first people who encouraged topologiststo stop thinking about fundamental groups
02:10:11.360 and start thinking about fundamental groupoidswithout needing to define distinguished base
02:10:16.469 points and things like that.But the homotopy hypothesis is this really
02:10:20.960 deep statement that kind of goes in the otherdirection.
02:10:23.429 So we know that starting from a space anddoing this hierarchical construction, you
02:10:29.480 build up tothis infinity category that tells you up to
02:10:32.360 weak homotopy equivalents, all the topologicalinformation about that space and all of its
02:10:35.349 homotopy types. Grotendieck then said, well,maybe that's really the definition of a topological
02:10:42.409 space, that infinity categories arejust spaces. Infinity groupoids are spaces,
02:10:47.849 or at least they define the structure of aspace and all
02:10:50.230 of its homotopy types up to weak homotopyequivalents. So it's kind of a converse
02:10:53.489 direction of that statement. And that's thehomotopy hypothesis. It's not proven. It's
02:10:58.179 noteven precisely formulated, but it's a very
02:11:00.929 interesting idea that I think is largelybelieved to be correct. It aligns well with
02:11:05.869 our intuitions for how algebraic topologyshould work.
02:11:08.849 So therefore, attempting speculation aboutthe relationship between that and physics…
02:11:14.840 So goingback to the quantum field theory picture for
02:11:17.489 a moment. So suppose you don't just stop attwo
02:11:19.869 categories, or indeed three categories, butyou keep going, right? You keep adding these
02:11:23.159 highergauge transformations. So not just gauge transformations
02:11:26.579 that deform time directionto time direction, but higher gauge transformations
02:11:30.989 that deform gauge transformation to gaugetransformation. You build up a higher homotopy
02:11:34.429 type that way. What happens when you get tothe
02:11:36.449 infinity category limit? Well, so what youend up with is something that has the structure
02:11:41.239 of atopological space. So starting from something
02:11:43.400 that's completely non-spatial, you've endedup
02:11:45.179 with a topological space. And so in the spiritof these kind of emergent space-time views,
02:11:53.730 you know, like ER equals EPR and so on, onehypothesis that's quite tempting to make is
02:11:58.099 maybe that infinity category defines the structureof our space-time, right? The topology and
02:12:04.210 geometry of space-time emerges in that infinitycategory limit that I take by just adding
02:12:08.949 higherand higher gauge transformations starting
02:12:10.889 from categorical quantum mechanics. And soif that's
02:12:14.619 true, which again, to be clear, we have noidea whether that's true or not, right? But
02:12:19.160 if thatwere true, then the coherence conditions,
02:12:21.730 the conditions that define how the infinitycategory
02:12:24.580 relates to all of the lower categories inthat hierarchy, those coherence conditions
02:12:29.550 wouldessentially be an algebraic parameterization
02:12:31.829 for possible quantum gravity models.And so if that ended up being correct, that
02:12:36.989 would be a really nice way to kind ofconceptualize and formalize the essential
02:12:40.910 problem of quantum gravity, that we're reallytrying to
02:12:42.389 nail down the coherence conditions that relatethat infinity category to all the higher categories
02:12:48.220 inthat hierarchy. Now what would it be like
02:12:50.989 to study the topology? So there's somethingcalled
02:12:53.079 stone duality, I'm sure you're aware of, whichrelates topology to syntax. So I've never
02:13:00.349 heardof someone studying stone duality at the infinity
02:13:03.520 categorical level, at the topology that'sinduced
02:13:05.639 from that category. What does that look like?Yeah, that's a really interesting question.
02:13:11.969 So yes, the way that stone duality works is…Again, as with many of these things,
02:13:20.530 there's a nice categorical interpretationin terms of Boolean topos and things. But
02:13:24.489 the basic idea is that if you have a Booleanalgebra, a kind of minimal algebraic axiomatization
02:13:31.430 for logic, there's a way that you can formalizethat in terms of this mathematical structure
02:13:35.449 ofa lattice, specifically an orthomodular lattice,
02:13:38.320 I think. I may be getting that wrong. I thinkit's
02:13:41.410 an orthomodular lattice. But so in which essentiallyevery point in that lattice is a proposition,
02:13:47.290 and then you have these meet operations andthese join operations that become equivalent
02:13:50.900 to your and and or operations in logic. Andthe reason that's significant is because those
02:13:56.440 sameclass of lattices also appear in topology
02:13:59.610 because there are specific spaces called stonespaces that
02:14:03.810 are essentially the… So okay, sorry, letme say that less confusingly. So if you take
02:14:09.429 a topologicalspace and you look at it, it's open. Doesn't
02:14:12.430 like topological spaces. No. Okay, let's trythat
02:14:15.969 again. Okay. That's being kept in. We'll takethat part in. So wait, wait, is it angry at
02:14:24.530 you?No, it was angry at someone. There's a gate
02:14:27.810 just outside, which sometimes opens and closes.And
02:14:31.020 this is my fiance's Dachshund, who is very,very territorial. And he was up until now
02:14:36.099 sleepingvery soundly and has just woken up. And so
02:14:39.099 we may get some interruptions.Well, congratulations on the engagement.
02:14:43.079 Thank you. Thank you. Yes. Anyway, so whatwas I saying? Yes. Okay. So if you take a
02:14:50.619 topologicalspace, then you can look at its open set structure.
02:14:54.920 So if you take the collection of all opensets,
02:14:56.409 you can look at, in particular, you can lookat the open set containment structure. You
02:15:00.030 can lookat which open sets are included in which others.
02:15:04.360 And when you do that, you again get the structureand orthomodular lattice, because the lattice
02:15:08.511 operations are essentially defined by theinclusion relations between the open sets.
02:15:13.780 And so there's this duality between topologicalspaces
02:15:15.869 and this class of lattices. So you could ask,what are the particular topological spaces
02:15:21.599 thatyou get if you look for topological spaces
02:15:24.469 whose open set lattices are the lattices thatyou get
02:15:27.530 from looking at Boolean algebras? And thoseare the stone spaces.
02:15:30.530 So they are the kind of topological spatialinterpretation of logic in some sense. And
02:15:36.079 in a way, you could say topos theory is reallyabout trying to generalize that idea, right?
02:15:40.960 That's another way to think about it. So everyelementary topos has an internal logic. And
02:15:48.260 also every elementary topos has some kindof spatial interpretation, because the axioms
02:15:53.650 of elementary topos theory, this finite limitaxiom and this existence of power objects
02:15:58.310 or subobject classifiers is really some generalizationof the axioms of point set topology, right?
02:16:04.510 Because they're the topos theoretic analogof saying that your open sets have to be closed
02:16:10.750 and the collection of open sets has to beclosed under arbitrary unions and finite intersections
02:16:15.409 and so on.So topos have spatial interpretations, and
02:16:19.659 they also have an internal logic. So there'sa particular kind of topos called a Boolean
02:16:24.219 topos whose internal logic is Boolean algebraand whose spatial interpretation is therefore
02:16:28.880 a stone space. But actually, you can do thesame construction for any elementary topos
02:16:34.090 that you like. And so then really what you'reasking is, okay, when you go to higher topos
02:16:38.490 theory, if we take the higher category, whichturns out that infinity category that you
02:16:43.019 get from the Grothendieck construction admitsa topos structure. So then you could ask,
02:16:47.318 what is the internal logic to that? And whatis its relationship to its spatiality? And
02:16:53.330 what you end up with is the spatial structureof an infinity homotopy type in homotopy type
02:16:58.240 theory. So in homotopy type theory, thisis another kind of logic interpretation of
02:17:05.129 higher categories, where, my apologies, cryingsomewhat. Hang on, wait. Okay, there we go.
02:17:13.968 I'm slightly more restricted in my emotionsnow. But if you imagine taking a proof system
02:17:20.609 and you say, okay, so now I'm going to interpretevery proposition in that proof system as
02:17:25.349 being a point in some space, and every proofas being a path, right? So a proof just connects
02:17:29.760 two propositions together. So I can proveone proposition for another, or I could prove
02:17:34.190 that two propositions are equivalent. I canalso prove that two proofs are equivalent,
02:17:37.780 right? I can take two paths and I can continuouslydeform them. But that proof exists in the
02:17:42.080 next homotopy type, right? Because that'sinterpreted topologically as a homotopy between
02:17:46.830 those parts. And so you can do exactly thesame construction. And so in the infinity
02:17:51.370 category limit, what you get is a logic whichallows not just for proofs of propositions,
02:17:57.170 but proofs of equivalence between proofs,and proofs of equivalence between those proofs,
02:18:01.340 and so on, right? So that's the internal logicof one of those higher topos. It's a logic
02:18:07.398 that allows for proofs of equivalence betweenproofs up to arbitrarily high order.
02:18:11.929 JS So in theories of truth, there's one calledTarski's theory of truth, where your truth
02:18:18.530 can only speak about the level that's beneathit. And then, right, and this is one of the
02:18:22.742 ways of getting around the liar's paradox,is that you say, well, it's truth level one,
02:18:27.120 and then you're speaking about a truth leveltwo or falsity level two, etc. And then the
02:18:31.568 criticism is, well, what happens Tarski whenyou go all the way up to infinity? And I don't
02:18:36.570 think he had an answer. But it's soundinglike there can be a metaphor here for some
02:18:41.840 answer.PW Yes, I mean, potentially. It's not something
02:18:47.820 I've thought about a huge amount, but it'scertainly the case that in these kind of higher
02:18:51.620 order logic constructions, there are thingsthat happen at the infinity level that don't
02:18:56.080 happen at any finite level. And it's conceivablethat, yes, you might be able to do a kind
02:19:01.580 of Tarski thing of evading the liar, or youmay be able to do some kind of Quine's paradox.
02:19:05.728 I think the same thing happens with Quine'sparadox, right? You try and construct liar
02:19:15.398 paradox type scenarios without self-reference,where you say, you know, the next sentence
02:19:19.709 is false, the previous sentence is true orsomething. But then the logical structure
02:19:24.638 of those things changes. As soon as you gofrom having a finite cycle of those things
02:19:28.898 to having an infinite cycle, the logical structurechanges. And I think the same is true of things
02:19:33.080 like the Tarski theory of truth. And yeah,it may be that there's some nice interpretation
02:19:37.370 of that in terms of what happens as you buildup to these progressively higher-order toposses
02:19:43.228 in homotopy type theory. I don't know. Butit's an interesting speculation.
02:19:47.129 JS What would be your preferred interpretationof truth?
02:19:52.200 PW So from a logic standpoint, I'm quite takenwith the definition of semantic truth that
02:20:00.040 exists in things like Tarski's undefinabilitytheorem, which is the idea that you say a
02:20:04.660 proposition is true if you can incorporateit into your formal system without changing
02:20:08.820 its consistency properties, right? So if youhave formal system S and your proposition
02:20:14.620 T, T is true if and only if S plus T is, youknow, if and only if con S plus T is the same
02:20:21.330 as con S. And that's a fairly neat idea thatI think, I mean, it's used a lot in logic
02:20:27.040 and it's quite useful for formalizing certainconcepts of mathematical truth, and particularly
02:20:30.790 for distinguishing these kind of conceptsof completeness versus soundness versus decidability,
02:20:36.580 which often get confused. Those become a loteasier to understand, in my experience, if
02:20:40.620 you start to think of truth in those terms.JS Yeah, great. John, that's a formal definition
02:20:44.720 of truth that works for formal statements,but what about colloquial informal ones?
02:20:48.609 PW No, no, no, I agree. It's extremely formal.But I was actually about to say that I think
02:20:53.780 it also aligns quite well with some basicintuition we have for how truth works when
02:20:58.500 we reason about things informally, right?So if, you know, we have some model of the
02:21:02.240 world, right? And that's like our formal systemor some informal system, right? And if you
02:21:07.910 take on board some new piece of information,generally speaking, the way that humans seem
02:21:12.561 to work is if we can incorporate that newpiece of information without fundamentally
02:21:16.290 changing the consistency properties of ourmodel of the world, we are much more likely
02:21:20.380 to believe that statement is true than ifit necessitates some radical reimagining of,
02:21:24.580 you know, of the consistency propertiesof our internal representation. And so I think
02:21:30.830 informally, there's a version of that samedefinition of truth that has a bit of slack,
02:21:36.510 right? Where you say, okay, a propositioncould be provisionally true, but how likely
02:21:41.950 I am to accept it as true depends on how radicallyI have to reformulate, you know, my foundations
02:21:47.840 of reality in order to incorporate it in aconsistent way.
02:21:50.670 I see. Well, John, I don't know what subjectwe haven't touched on. This is a fascinating
02:21:57.740 conversation. Thank you, man.No, this was fantastic. As you say, I'm really,
02:22:02.090 you know, it's been a long time coming, butI'm really glad we had this opportunity to
02:22:06.220 chat. And, yeah, I really look forward tostaying in touch. I've become, I have to confess,
02:22:11.740 when you first reached out, I hadn't heardof you, but in part because you reached out
02:22:16.160 and in part because, you know, of the explosionof your channel, I've been following a lot
02:22:20.130 of what you've been doing subsequently. AndI think, no, I think TOE is a really fantastic
02:22:24.410 resource. And the, yeah, your particular nicheis one that definitely, that desperately needs
02:22:31.210 to be filled. And I think you're doing a fantasticjob of filling it.
02:22:33.859 What would you say that niche is? And I askjust because it's always interesting for me
02:22:37.580 to hear, well, I have an idea as to what TOEis or what TOE is doing, what theories of
02:22:41.850 everything the project is. It doesn't alwayscorrespond with what other people think of
02:22:46.390 it.Right. So the reason I really like your channel
02:22:51.710 and the reason I like witnessing these conversationsand to some limited extent participating in
02:22:56.120 them as well is the following reason. It feelsto me like you've got these two extremes out
02:23:00.900 there, right? There are these really quitevacuous kind of popular science, popularization
02:23:07.359 or philosophy, popularization, YouTube channelsand documentary series and things where you
02:23:11.341 often have a host who, you know, goes veryfar to kind of play up the fact that they're
02:23:17.800 ignorant of what's being discussed and theydon't really have any strong opinions. And
02:23:21.510 it's just, you know, they go and ask somebrain boxes for what they think and it all
02:23:25.479 gets assembled in some nice documentary package.That's kind of one extreme. Then you have
02:23:29.750 the other extreme of, you know, you take somephysicist, some philosopher who's been working
02:23:34.620 on their own pet theory for 30 years and theygo make some, you know, some, you know, long
02:23:39.660 YouTube video about it, just advocating thatand shouting down all the competition and
02:23:43.040 being very kind of bigoted and dogmatic orwhatever.
02:23:46.920 And it feels like what you are managing todo by, you know, because you are an extremely
02:23:52.130 intelligent and well-read person with a backgroundin math and physics and who has
02:23:55.529 very wide interests outside of that and who,you know, more so than any other YouTuber
02:24:01.130 I'veencountered actually makes an effort to really
02:24:04.729 understand, you know, the stuff that they'retalking about and the stuff that their guests
02:24:07.530 are talking about. You know, that's even justin itself, that would be incredibly valuable.
02:24:12.930 But then what I think that allows you to dois
02:24:19.080 to do something that's somehow a really nicesynthesis of the best aspects of those two
02:24:23.511 approaches whilst avoiding their more unpleasantaspects, which is to be the kind of interested,
02:24:29.319 educated, motivated interlocutor who is, youknow, not completely inert, like in the
02:24:35.779 kind of the sort of popular science documentarycase, but also not, you know, dogmatically
02:24:41.660 pushingand saying, ah, you know, you're completely
02:24:43.790 wrong. You need to be thinking about the quantumgravity
02:24:45.560 or something, but just saying, oh, but howdoes this connect to that? Or is it possible
02:24:50.120 you couldthink of things in this, you know, being that
02:24:53.370 kind of Socratic dialogue partner in a waythat I think
02:24:57.240 you are almost uniquely placed because ofyour skill set and your personality to, you
02:25:01.510 know,that's a role you're almost uniquely placed
02:25:03.030 to play in that space. I've never really seenthat
02:25:05.860 work in any context outside of your channel.And I think that's something really quite
02:25:11.030 special.Well, man, that's the hugest compliment and
02:25:13.700 I appreciate that. Thank you so much. I thinkyou've captured, well, I don't know if I'm
02:25:17.880 the bigot in that, but I'll interpret thatas me not being a bigot just to sleep at night.
02:25:24.020 No, no, no, exactly. I mean, I think you handlethe balance really well as someone
02:25:28.990 who clearly has ideas and has opinions andhas views as, you know, as you have every
02:25:33.150 right to as someone who's thought about thisas much as anyone else, right? But you're
02:25:37.660 not, you're not trying to shout down opposition.You're not trying to force some view down
02:25:41.270 someone's throat. You are, as far as I cantell, you are actually, you know, in completely
02:25:49.580 good faith, just trying to explore with genuineintellectual curiosity, the space of ideas
02:25:55.580 and, you know, and present new perspectivesand point in directions that people may not
02:26:00.240 have previously thought of in a way that Ithink a lot of people say that they're trying
02:26:04.030 to do. But I've very rarely seen anyone actually,you know, and people might be able to simulate
02:26:10.601 that for a while, but after a while, you know,the mask kind of slips and you see, oh, really
02:26:14.700 they're kind of pushing this viewpoint orwhatever.
02:26:16.970 So part of that is that I don't have thatincentive structure of having to produce and
02:26:22.490 get citations in order for me to live. Becauseif I was, then I would have to specialize
02:26:27.910 much earlier and I wouldn't be able to surveyas much before I specialize. So currently
02:26:32.370 I'm still in the surveying mode. I'm likea gannet before I go down and eat. So I'm
02:26:37.370 lucky in that regard. And man, like, holymoly, super cool. So I have many questions
02:26:42.490 from the audience, by the way.I mean, just, just informally on the following
02:26:46.000 up on that. I mean, I think the, in many ways,I think the String Theory landscape video
02:26:49.450 is the, is the perfect embodiment of that,of that sort of side of you, right? It's the
02:26:55.740 fact that I don't know any other person reallywho could have done something like that because
02:27:00.160 it requires both, you know, you're not, youknow, you come across quite critical of String
02:27:06.240 Theory, right? So no, no, no String Theoristwould have made that video, but also no one
02:27:11.450 whose paycheck depends on them investigatingloop quantum gravity would have invested the
02:27:16.120 time to understand String Theory at the levelthat you had to understand it in order to
02:27:19.649 make the video. And so it's like, I don'tknow who else would have filled that, that
02:27:22.582 niche, right?Yeah, that was a fun project. I find it's
02:27:26.960 just, it's so terribly in vogue to say I dislikeString Theory, but then simultaneously to
02:27:32.490 feel like you're voicing a controversial opinion.And I wanted to understand String Theory before
02:27:37.850 I said, and I, by the way, I love String Theory.I think it may be describing elements of reality
02:27:43.620 correctly. And that may be why it has, I misspokeby the way, when I said in the video that
02:27:49.290 it has no predictions, it had mathematicalpredictions. Maybe it still does. And this
02:27:53.660 is something Richard Borcherds emailed mebecause he said, that's something I would
02:27:56.561 correct in the video. It has mathematicalpredictions. It doesn't have physical ones.
02:28:00.380 But anyhow, I think that's why it may proveso fruitful mathematically.
02:28:07.260 And it also, I mean, like parts of it havephysical predictions that are, but they just
02:28:13.550 happen to not strictly depend on the StringTheoretic interpretation, right? So there
02:28:17.450 are condensed matter predictions of ADS-CFTthat have been quite experimentally, you know,
02:28:21.609 validated, right? It's just that ADS-CFT camefrom String Theory, but it doesn't strictly
02:28:26.100 depend on String Theory.Oh, right. Exactly. Exactly. Okay. So one
02:28:29.810 of the questions from the audience is, hasJohn ever done psychedelics?
02:28:33.860 Yes. So I have tried psychedelics and actuallyI consider it, I don't want to come across
02:28:40.910 as too much of a kind of drug pusher, butI consider it's one of the most important
02:28:45.540 things I've ever done. I don't do it regularlybecause I'm afraid of the effect that it has
02:28:51.740 on the brain and things like that. So I hada list of things I wanted to try and I tried
02:28:56.540 each of them once and I'm very glad that Idid. And the main takeaway was, you know,
02:29:02.620 the stuff we were talking about before about,you know, there's kind of, there's the computation
02:29:08.310 that a system is doing and there's the computationthat the observer is doing and, you know,
02:29:12.180 so, you know, really what you've got is that,you know, you've got these two computations
02:29:15.990 and you've got a third computation that issort of the encoding function, the thing that
02:29:19.569 maps a concrete state of the system to anabstract state in the internal representation
02:29:24.710 of the observer. And really all three of thosethings are kind of free parameters.
02:29:28.350 And, you know, I'd been thinking about thatkind of stuff since I, you know, not in those
02:29:34.360 terms precisely, but in some form for a longtime, you know, from when I was a teenager
02:29:38.240 onwards and kind of in this very kind of nerdyintellectual way thinking about, oh, yes,
02:29:44.689 youknow, surely if my model of reality changes
02:29:47.950 even slightly, then, you know, the interpretationsof
02:29:50.660 the perceptions and qualia that I experiencedis going to be radically different. But it
02:29:55.700 doesn'tmatter how much you intellectualize that idea.
02:29:58.681 It's very, very different if you just likesubjectively experience it, right? And that's
02:30:02.120 in a sense, driving home the fact that ifyou make
02:30:05.980 what is, in the grand scheme of things, anabsolutely trivial modification to your brain
02:30:11.160 chemistry, your modes of decomposing and understandingthe world completely just dissolve,
02:30:18.609 as happens with things like LSD. Actuallyexperiencing that from a first-hand perspective
02:30:23.779 is really, really important. It kind of convincedme. I don't want to, again, I don't want to
02:30:27.911 seemtoo... Okay, it would be too strong to say
02:30:31.920 it ultimately convinced me of the validityof that
02:30:33.830 way of thinking about things, but it definitelyis something that occurs to me when I'm worried
02:30:40.160 that I'm overplaying this observer-dependence-of-phenomenaline. I kind of think,
02:30:45.689 well, no, actually, if you modify even justvery slightly neurotransmitter balances in
02:30:50.279 the brain,the internal perception of reality changes,
02:30:53.880 you know, kind of really, really radically.JS Yes. Okay, well, here's a physics question.
02:31:00.480 What would happen if an object wider thana wormhole throat flies into the wormhole?
02:31:05.430 Does the wormhole widen? Does the object corkthe wormhole? Does it deform the object?
02:31:11.170 If it deforms it, how? What about if the objectflies at an even faster speed, so 0.9 speed
02:31:16.340 of light?Okay, interesting question. So, I mean, wormholes
02:31:22.210 obviously are not known to be physical. Theyare
02:31:24.910 valid solutions to the Einstein equations.Einstein rows and bridges and extended Schwarzschild
02:31:30.380 solutions are valid solutions, but the Einsteinequations are incredibly permissive, and they
02:31:34.450 permit many, many more solutions than thingsthat we believe to be physical. So if you
02:31:39.031 just takethe Einstein field equations on face value…
02:31:42.490 Okay, one thing to remember is that when anobject is
02:31:46.370 falling into the wormhole, it's not like ithas to fit into the throat, so to speak, right?
02:31:53.330 If you imagine the topology of what's goingon, you've got this two-sheet sort of hyperboloid,
02:31:58.830 and the wormhole throat that's connectingthem, but any object you throw in is localized
02:32:02.750 to oneof the sheets. So it's traveling on that sheet
02:32:05.540 and follows the world lines on that sheet.It's not
02:32:09.410 like it's some plug that's trying to go throughthe throat, through the space in the middle.
02:32:15.110 So it may well be that the world lines…I mean, this will happen due to tidal deformations,
02:32:19.500 that the object will be stretched in the radialdirection and compressed in the angular directions
02:32:25.390 as it gets pulled in, just due to gravitationaltidal effects. But the fact that the object
02:32:31.180 isquote-unquote bigger than the wormhole throat
02:32:34.460 doesn't matter. From its perception, its worldlines are traveling on some smooth region
02:32:41.479 of space. It never encounters any kind ofdiscontinuity,
02:32:44.290 anything that has to sort of fit through,so to speak.
02:32:46.790 Okay. Would you kindly ask him, how wouldhe tie science and spirituality together?
02:32:59.100 I think one always has to be a bit carefulwith that, right? In the sense that I don't
02:33:05.650 want totake either of the two extreme positions of
02:33:07.710 saying, oh, science validates the existenceof an immortal soul or something, which I
02:33:13.330 don't believe. But nor do I want to say,oh, science invalidates whatever, the numinous
02:33:19.530 dimension. I think they're largely agnosticto one another. Okay, so actually it comes
02:33:27.279 back to the stuff we were talking about atthe beginning,
02:33:29.069 in a way, about the language that we use andthe models that we use for constructing reality,
02:33:36.109 right? Do you actually believe that the universeis a computer? Do you actually believe that
02:33:42.020 thesolar system is made of clockwork or something?
02:33:44.060 And again, the answer is no, right? My viewis
02:33:47.750 that these are just models we use based onthe ambient technology of our time.
02:33:52.670 And I kind of have a similar feeling abouta lot of theology and a lot of spirituality,
02:33:58.680 right? If you go and read writings by peoplelike John Duns Scotus or medieval scholastic
02:34:05.290 theologians, the questions they're grapplingwith are really the same questions that I'm
02:34:10.110 interested in. Okay, to take a concrete example,right? So I realize I'm talking about religion
02:34:16.880 here, not necessarily spirituality, but I'lltie it together in a sec. So you could ask
02:34:22.310 thequestion, so our universe, right? It seems
02:34:26.410 to be neither completely trivial, right? It'sneither
02:34:28.790 kind of maximally simple, nor is it kind ofmaximally complicated, right? So there's some
02:34:34.640 regularity, but it's not completely logicallytrivial. You know, it's not like every little
02:34:38.720 particle follows its own set of laws, butit's also not like we can just reduce everything
02:34:42.870 toone, as far as you can tell, we can just reduce
02:34:44.900 everything to one logical tautology. So asfar
02:34:50.390 as I can tell, the first people to reallydiscuss that question
02:34:53.390 in a systematic way, at least from Europeantheology and philosophy, I'm less, I'm more
02:34:58.569 ignorant of other traditions, were the scholastictheologians, were people like Duns Scotus,
02:35:04.660 who asked, you know, why did God create aworld which is neither maximally simple nor
02:35:09.620 maximally complex, effectively? And Duns Scotus'answer is a perfectly reasonable answer, right?
02:35:14.080 Which is because God created the world thatway because that world is the most interesting.
02:35:20.800 If I were to formulate that question in modernterminology, I would formulate it in terms
02:35:25.700 ofKolmogorov complexity, right? I would say,
02:35:28.120 why is the algorithmic complexity of the universeneither zero nor infinity? Why is it some
02:35:33.760 finite value? And the answer, as far as youcan tell,
02:35:36.820 is essentially because of information theory.Because we learned from Shannon that the kind
02:35:41.841 of the most interesting or the highest informationdensity, you know, the most interesting signal
02:35:46.890 is one that is neither completely noisy, maximuminformation, nor completely simple,
02:35:51.850 but somewhere in the middle. So really, DunsScotus hit upon a really foundational idea
02:35:56.390 inmodern algorithmic information theory. He
02:35:59.370 didn't formulate it in those terms because,you know,
02:36:02.420 he didn't know what Kolmogorov complexitywas. He had no way of, you know, that ambient
02:36:06.210 thinkingtechnology didn't exist. So he formulated
02:36:08.960 the answer in terms of the ambient thinkingtechnology
02:36:11.450 of the time, which was God and the Bible and,you know, all that kind of stuff.
02:36:15.490 And so, I don't want to be someone who sitshere and says, oh, look at those people. They
02:36:19.490 weretalking about, you know, God and whatever,
02:36:21.950 and weren't they so ignorant? Because I don'twant
02:36:24.160 people to look at, you know, not that I thinkthey're wrong. But I don't want people to
02:36:27.870 lookat my work in a thousand years and say, oh,
02:36:29.660 look, he thought the universe was a computer,how silly he was, right? I don't think the
02:36:33.130 universe is a computer. I think it's a usefulmodel just as they thought God was a useful
02:36:35.950 model, which it was and maybe to an extentstill is.
02:36:41.780 So that's kind of my general view about sortof theology and spirituality is that
02:36:46.060 I think there are, you know, there are someclasses of questions where it's useful to
02:36:48.990 think about things in terms of Turing machinesor, you know, fiber bundles or whatever it
02:36:53.370 is.And there are some classes of questions where
02:36:54.910 it is useful to couch them in terms of thesoul or,
02:36:57.240 you know, an immortal spirit or God or whatever.And you can do those things without believing
02:37:01.900 in the ontological reality of any of them,as indeed I don't. But that doesn't make them
02:37:06.450 notuseful.
02:37:07.529 Now, can you actually distinguish those twoif you're a pragmatist? Because it's my understanding
02:37:12.280 if you're like William James, the utilityof it is tied to the truth of it.
02:37:16.939 Yeah, I mean, that's, it's a tricky one. That'ssomething I, okay, being completely honest,
02:37:22.390 I don't know. It's something I've gone backand forth on over the years, right? Because
02:37:25.279 in a way,so yes, you might say, okay, do I believe
02:37:28.970 in God or do I believe in the soul in someontological
02:37:32.399 sense? And the answer is no. But if that'syour definition of exist, or that's your definition
02:37:38.100 of belief, then I also don't believe in electrons,right? I don't believe in space-time.
02:37:42.271 You know, I think all of these things arejust models, right? Like, do I think that,
02:37:46.100 you know, space-time is a useful mathematicalabstraction? But in a sense, we know that,
02:37:50.510 you know, in black holes or in the Big Bangor something, that's probably an abstraction
02:37:54.391 thatloses usefulness and eventually will be superseded
02:37:58.479 by something more foundational.So do I believe in space-time in an ontological
02:38:01.870 sense? No. Do I believe in particles in anontological sense? No. So whereas you might
02:38:07.960 say, okay, well, therefore, that means probablythat
02:38:11.010 my definition of the word exist is not veryuseful, right? I should loosen that definition
02:38:14.790 abit and be a bit more permissive. So then
02:38:17.250 you might take the William James view of,okay, well,
02:38:20.910 you could say, I believe that space-time existsin as much as I think it's a useful model
02:38:26.960 for alarge class of natural phenomena. Again, it's
02:38:30.069 a bit like the dinosaur thing we were talkingabout earlier. You could say, well, I don't
02:38:33.870 believe that space-time doesn't exist in anontological sense, but it's kind of consistent
02:38:37.540 with a model of reality that does have goodexperimental validation or observational validation.
02:38:43.950 But then, if that's your criterion,then I kind of have to admit that, okay, well,
02:38:47.979 in that sense, maybe I do believe in a soul,because there are… So for instance, I don't
02:38:56.530 believe that there's any hard-line distinctionbetween the computations that are going on
02:39:03.359 inside the brain and the computations thatare going on
02:39:05.770 inside lumps of rock or something. Really,the distinction is, it comes back to the point
02:39:11.000 youwere making earlier about what laws of physics
02:39:14.210 would a cat formulate? So in a sense, okay,maybe they exist in the same objective reality,
02:39:19.740 whatever that means.But whatever their internal model of the world
02:39:23.140 is, it's going to be quite different frommine,
02:39:25.601 because cats have not just different brainstructure, but they have a different kind
02:39:29.270 ofsocial order, their culture is different,
02:39:31.649 etc. Just like my internal representationof the
02:39:34.320 world would be different to a different humanwho was raised in a completely different environment
02:39:38.359 with a different education system, etc. Soit's not like some abrupt discontinuity.
02:39:42.710 There's a kind of smooth gradient of how culturallysimilar are these two entities,
02:39:48.550 and therefore, how much overlap is there intheir internal representation of the world.
02:39:52.280 So I have more overlap with you than I dowith a cat, but I have more overlap with a
02:39:58.110 cat thanI do with a rock, and so on. But there's no
02:40:02.100 hard-line distinction between any of thosethings,
02:40:04.040 at least in my view, right? So in a way, youcould say, well, therefore, I'm some kind
02:40:08.189 ofpanpsychist, or I'm an animist, right? I believe
02:40:11.690 that there's a kind of mind or spirit in everything.And again, I think that's not personally how
02:40:18.870 I choose to formulate it. I choose to formulateit in terms of computation theory, but it's
02:40:22.370 not a completely ridiculous way of translatingthat
02:40:24.780 view. And these kind of druidic, animisticreligions, a lot of what they're saying,
02:40:30.520 if interpreted in those terms, is perfectlyreasonable. So yeah, it's just a very verbose
02:40:38.080 way of saying, no, I don't have any particularlygood way of distinguishing between the two.
02:40:42.170 And so in a sense, I have to choose eitherbetween being ultra-pragmatist and basically
02:40:46.000 saying I don't believe in anything, or beingultra-remissive and saying,
02:40:48.832 yeah, I basically believe in everything, whichseem like equally useless filters.
02:40:53.670 JS Well, another commonality between us isthat the way that you characterized
02:40:59.510 the scholastics, I believe, and their ideasof God, and then being inspired,
02:41:04.471 and realizing that that's similar, not thesame, of course, but similar to ideas of computation
02:41:09.680 now,or at least how they were describing it. And
02:41:13.050 that's one of the reasons why on this channel,I interview such a wide range of people. It's
02:41:17.730 because I work extremely diligently to understandthe theories and to be rigorous. But I also
02:41:24.570 feel like much of the innovations will comefrom the
02:41:27.800 fringes, but then be verified by the center.In other words, like the fringes are more
02:41:32.779 creative,but they're not as strict. The center is much
02:41:35.590 more stringent, but then it has too fine ofa sieve.
02:41:39.750 Paul Right, right. It's like thosesimulated annealing algorithms that you get
02:41:45.300 in combinatorial optimization, right? Whereyou're
02:41:47.410 trying to find some local minimum of a function.So you set the parameter really high initially,
02:41:51.860 so you're kind of exploring all over the place,but being very, very erratic. And then gradually,
02:41:56.520 over time, you have to lower the temperatureparameter. And I think there's something in
02:42:01.830 thatas a model of creativity, that at the beginning,
02:42:04.280 you have to be kind of crazy and irrationaland
02:42:06.410 whatever. And then gradually, you have todrop that temperature and kind of become a
02:42:09.680 bit morestrict and precise and slowly start to nail
02:42:12.490 things down.Aaron Now the Santa Fe Institute has an interesting,
02:42:15.300 I don't know if it's a slogan, but it's theway that they operate, which is you have to
02:42:20.620 be solitaryand even loopy, inane, and then go back to
02:42:26.370 people to then be verified and actually havesome wall
02:42:29.150 to push against you, because otherwise you'rejust floating in the air.
02:42:32.840 Paul Sorry, since I was, to continue beingcomplimentary to you and the channel. I mean,
02:42:38.160 that's another thing which I think is veryrare,
02:42:40.460 and which you do extremely well, which isto actually take seriously, you know, I think
02:42:44.811 it's,again, it's something which I think a lot
02:42:46.110 of people say that they want to do or wouldlike
02:42:48.020 to think that they want to do. But a lot ofpeople seem to be, I'm bad at this too, right?
02:42:51.970 I try,but I think I fail. Where if you're presented
02:42:57.450 with some really crazy, very speculative idea,and it's hard to kind of make head or tail
02:43:02.000 of what the person is talking about, you know,for a lot of people, it's the kind of instinctive
02:43:06.370 reaction to say it's complete nonsense. Like,don't waste my time, right? And, you know,
02:43:11.420 certainly a lot of the mainstream physicscommunity has that opinion, and to an extent
02:43:14.540 has to have that, you know, view. Becauseif,
02:43:16.670 you know, one of the things you learn if youstart writing papers about fundamental physics
02:43:20.620 is youget a huge amount of unsolicited correspondence
02:43:23.960 from people trying to tell you their theoryof
02:43:25.410 the universe, right? But, you know, it's alsoimportant to be mindful of stories like the
02:43:30.470 story of Ramanujan, right? Like writing toG. H. Hardy and people, you know, who must
02:43:35.370 haveseemed like an absolute nutcase, but actually
02:43:38.061 was this kind of era defining genius. And,you know,
02:43:40.600 so again, you have to be careful not to setthe filter too strict. And yeah, I think,
02:43:45.520 you know,one thing that I think you do extremely well
02:43:47.750 is really to kind of, I think the expressionin the
02:43:52.109 post-rats community is, you know, steel man,these kind of arguments, right? It's to say,
02:43:56.900 you know, if you're presented with some ideathat seems on the surface completely nuts,
02:44:00.479 let's try and adopt the most charitable possibleinterpretation of what's happening. Like,
02:44:04.100 how might we be able to make this make sense?And yeah, it's something I try to do with
02:44:08.330 ideasin physics and in theology and other things,
02:44:10.020 but I think you certainly do it far betterthan anyone
02:44:12.210 else I've encountered. Is this related towhy you follow the Pope on Twitter?
02:44:16.620 No, it's not. That is a completely, yes. Okay.Well, well spotted. No, that's because,
02:44:24.700 so all right. The backstory to that is, sothat Twitter account was made when I was like
02:44:30.621 15 yearsold and I didn't use it.
02:44:34.840 I think I sent sort of two or three weirdtweets as a teenager and then let it die.
02:44:40.760 I didn't even realize it was still around.And then when the physics project got announced,
02:44:44.690 which was really the first bit of seriousmedia
02:44:46.630 attention I ever received, right, and I wasdoing interviews in magazines and other things.
02:44:50.580 And I got a message from the director of publicrelations at Wolfram Research saying, they
02:44:55.961 found your Twitter account and it's got likesome, you know, it's got 2000 followers.
02:45:00.590 I can't remember what it was.People have started following this Twitter
02:45:03.390 account.I was like, I don't have a Twitter account.
02:45:05.790 And then I figured out, oh, they found thisTwitter account that I made when I was 15
02:45:09.910 and never deleted and forgot existed.Now, when I was 15 years old, for some reason,
02:45:16.529 I thought it was funny.So this is some betrayal of my sense of humor.
02:45:22.210 So I tweeted kind of weird, nerdy math stuffand whatever.
02:45:26.590 And in my teenage sense of humor, I thoughtit'd be funny if I only followed two people,
02:45:31.200 the Pope and this person called Fern Britton,who is a sort of daytime television star in
02:45:36.420 the UK.And I don't know why I thought that was so
02:45:39.910 humorous, but I thought it was entertaining.And then I think Fern Britton left Twitter
02:45:44.630 or something.And so when I went back to this Twitter account,
02:45:47.399 the only account I followed was the Pope.And then I thought, oh, okay, well, forget
02:45:50.910 it.I'll just leave it.
02:45:51.910 And then I since then have followed a fewother people, but he's still there somehow.
02:45:55.620 Okay.So it's just a relic.
02:45:57.250 You can't bear to get rid of him.Some people can't bear to delete some deceased
02:46:01.561 person from their phone.It's for posterity.
02:46:04.340 What's the reason?Why do you still have it?
02:46:06.580 I think, yeah, it's partly posterity.And it's partly because there is still a part
02:46:10.311 of me that for whatever reason thinks it'skind of funny that I follow basically a bunch
02:46:13.850 of scientists and science popularizers.Christopher Hitchens and then the Pope.
02:46:17.870 Yeah.Yeah.
02:46:18.870 And then the Pope.Yeah.
02:46:20.200 Okay.So speaking about other people's theories,
02:46:22.899 this question is, does Jonathan see any connectionsbetween the Ruliad, Eric Weinstein's Geometric
02:46:27.921 Unity, and Chris Langan's CTMU, which is alsoknown as the Cognitive Theoretic Model of
02:46:34.990 the Universe?So on a very surface level, I guess I see
02:46:40.380 some connections.I have to confess.
02:46:42.500 So I'm not, I don't know really anything abouteither Geometric Unity or CTMU.
02:46:48.280 You know, I've encountered both.People have told me things about both.
02:46:51.990 I've been able to find very little formalmaterial about CTMU at all.
02:46:56.260 And the little I know says, okay, yeah, itprobably does have some similarity with, you
02:47:00.399 know, this general thing we were talking aboutearlier of, you know, having a model of reality
02:47:03.950 that places mind at the center.And that kind of takes seriously the role
02:47:08.450 that the observer's model of the universeplays in, you know, in constructing an internal
02:47:13.970 representation.I think that's certainly a commonality.
02:47:19.130 But I'm kind of, I'm nervous to comment beyondthat because I really don't understand it
02:47:22.680 well enough.With Geometric Unity, yeah, I don't really
02:47:27.620 know what, I mean, even if I were to understandit technically, which I don't, my issue would
02:47:32.990 still be a kind of conceptual one, which isI think it's kind of insufficiently radical,
02:47:36.359 right?I mean, it's like, it's really, the idea is,
02:47:41.950 you know, use the existing methods fromgauge theory to figure out, you know, if we
02:47:49.450 have a Lorentzian manifold with a chosenorientation and chosen spin structure, here
02:47:54.300 is the kind of canonical gauge theory thatwe get, you know, defined over that structure.
02:48:00.600 And the claim is that gauge theory is, youknow, unifies gravitation and the three other
02:48:06.120 gauge forces.Like I say, I certainly wasn't convinced that
02:48:10.570 that's formally true just by reading the paper,which even if it were true, I would find it
02:48:15.450 a little bit disappointing if it turnedout that the, you know, the key thing that
02:48:20.620 was needed for, you know, radical advancein physics just turned out to be a bigger
02:48:25.650 gauge group.That would be a little bit, you know, anticlimactic.
02:48:29.550 Now, we've talked about the pros of computationalmodels and you've even rebutted, at least
02:48:36.460 from your point of view, Penrose's refutationof computations.
02:48:39.189 But this question is about what are the limitationsor drawbacks for using computational models?
02:48:45.030 Minus complexity and irreducibility.Like that's just a practical issue.
02:48:49.100 Right.Sure.
02:48:50.250 Sure.But even conceptually, there may be issues.
02:48:53.260 Right.So I, and again, this is kind of what I mean
02:48:56.550 when I say I'm not dogmatically trying toassert that the universe is a Turing machine
02:48:59.760 or something.There may be physical phenomena that are fundamentally
02:49:04.149 non-computable as, you know, Penrose and otherpeople believe.
02:49:07.900 But I don't think we know that yet.And certainly the parts of physics that we
02:49:12.140 kind of know to be true, we know are computable.And so computation is therefore, you know,
02:49:17.850 again, going back to the pragmatist point,computation is therefore at least a very useful
02:49:21.880 model for thinking about a lot of physics.Whether it's useful for thinking about everything,
02:49:26.040 who knows?Probably not.
02:49:27.830 Right.But yeah.
02:49:28.830 I mean, there are open questions.Like, so for instance, it might be the case
02:49:33.780 that, so we know, we have known since Turing'sfirst paper on computable numbers, that most
02:49:41.311 real numbers are non-computable.So if you have, you know, if the universe
02:49:46.069 turned out to be fundamentally based on continuousmathematical structures and based on real
02:49:49.950 numbers, then, you know, at its foundationallevel it would be a non-computable structure.
02:49:55.970 But then you'd still have this open questionof, well, you've still got this issue of the
02:49:59.970 observer.You could imagine the situation where you
02:50:02.620 have a continuous universe that's based onnon-computable mathematics.
02:50:06.359 But all experiments that you can, in principle,perform within that universe would yield computable
02:50:12.840 values of the observables.And in that case, and in fact, you know, again,
02:50:18.380 there are papers by people like David Deutschwho've, you know, argued similar things, right,
02:50:21.739 that, you know, within, for instance, withinquantum mechanics you have, you know, arbitrary
02:50:27.210 complex numbers appearing in the amplitudes.And so, you know, most of those are going
02:50:30.320 to be non-computable.But eventually you project those onto a discrete
02:50:35.220 collection of eigenstates, and those are computable.So in the end, it doesn't matter that the
02:50:39.989 underlying model was based on non-computablemathematics because the part of it that you
02:50:43.310 can actually interface with as an observerstill has computable outcomes.
02:50:47.479 Which means that there is still going to bean effective model that's consistent with
02:50:51.319 observation that is nevertheless computable.So in a sense, I don't think we know that
02:50:57.750 yet.I don't think we know whether it's even possible
02:50:59.950 to set up, if the universe were non-computable,would it be possible to set up experiments
02:51:04.600 that are effectively able to excavate or exploitthat non-computability to do, you know, practical
02:51:09.560 hypercomputation or something?Wait, sorry, is David Deutsch suggesting that
02:51:13.700 quantum mechanics only has point spectrumsand that there are no continuous spectrums?
02:51:18.270 Oh, sorry, let me not malign, let me not malign,that's specifically in the context of, you
02:51:24.290 know, quantum information theory and finitedimensional Hilbert spaces, right?
02:51:27.020 So, you know, even if you have only a finiteeigenbasis, so all your measurements are computable,
02:51:33.220 you know, the eigenstates are discrete sets,but the amplitudes are still non-computable,
02:51:39.351 right, in general.Okay, I have a nettling point that I want
02:51:44.150 to bring up that I hear mathematicians andphysicists say, but I don't think it's quite
02:51:47.979 true.So when they're talking about discrete models,
02:51:50.070 they'll say discrete versus continuous, butit should technically be discrete versus continuum,
02:51:55.590 because you can have two graphswhich are discrete, and you can have continuous
02:51:59.050 maps between them, because you just need thepre-image to be open, and it's not a continuum,
02:52:04.859 but it's continuous.I hear that all the time, and I'm like, why
02:52:08.940 does no one say that?But I just want to know, am I understanding
02:52:11.479 something incorrectly?No, I think you're not understanding something
02:52:15.340 incorrectly.I think you're thinking about this more deeply
02:52:17.350 than most mathematicians do, which is perhapsa positive sign.
02:52:21.170 But nonetheless, the distinction between whatis discrete and what is continuum is
02:52:24.910 actually not very well-defined, right?So let me give you a concrete example.
02:52:31.060 And this is actually something that comesfrom a method of proof in logic called forcing.
02:52:34.490 It was developed by Paul Cohen, for whichI won the Fields Medal, right?
02:52:38.880 And one of the key ideas in forcing is thisidea called a forcing p-name, which is a slightly
02:52:44.790 technical idea, but basically what it allowsyou to do is to talk about the cardinality
02:52:48.720 of a set from a different set theoretic universe,from a different domain of discourse.
02:52:54.080 The significance of that is, so, okay, whatdo we mean when we say that something is discrete?
02:52:58.330 Well, what we mean is that it can be bijectedwith the natural numbers, right?
02:53:02.040 That it's countable.It consists of a countable collection of data.
02:53:04.990 And when we say that something is continuous,I mean modulo considerations of the continuum
02:53:08.819 hypothesis and something, basically what wemean is that it's uncountable, that you can't
02:53:12.479 biject it with the natural numbers.But what is a bijection?
02:53:16.940 Well, a bijection is a function.And what is a function?
02:53:19.800 Well, set theoretically, a function is justa set, right?
02:53:23.080 It's a set of ordered pairs that map inputsto outputs.
02:53:27.120 So if you have control over your set theoreticuniverse, you can control not just what sets
02:53:32.320 you can build, but also what functions youcould build.
02:53:34.022 So you can have the situation where you havea set that is countable from one larger set
02:53:42.430 theoretic universe in the sense that the functionthat bijects that set with the naturals
02:53:47.090 exists in that universe.But if you restrict to a smaller one, that
02:53:50.330 function can no longer be constructed.So internal to that universe, that set is
02:53:57.950 no longer countable.It's effectively gone from being discrete
02:54:01.390 to being continuous.The set itself is the same.
02:54:03.739 It's just that you've made the function thatbijected it with the naturals non-constructive.
02:54:08.140 So if you like, to an observer, to a generalizedmathematical observer internal to that universe,
02:54:13.330 it looks like it's continuous.And again, there are versions of this idea
02:54:17.410 that occur throughout topos theory.P.T. Johnston, one of the pioneers of topos
02:54:21.540 theory, did a lot of work on these topostheoretic models of the continuum, where you
02:54:27.979 can have a very similar phenomenon, whereyou can have
02:54:31.489 some mathematical structure that looks discretefrom a larger supertopos. But if you take
02:54:36.620 someappropriate subtopos, you make non-constructible
02:54:40.310 the functions that essentially witness itas being
02:54:42.950 discrete. And so internal to that, it becomesa continuous structure.
02:54:47.200 And so you can actually do things like localetheory and pointless topology in a manner
02:54:53.069 thatis fundamentally agnostic as to whether the
02:54:58.040 spaces you're dealing with are actually discreteor continuous. So yeah, even the question
02:55:02.450 of whether something is discrete or continuousis in a sense observer dependent. It's dependent
02:55:06.420 on what functions you can and cannot constructor
02:55:09.590 compute within your particular model of mathematics.So what I was saying is that continuity and
02:55:16.240 continuousness is the same to me, but continuousis not the same as a continuum. For continuum,
02:55:24.210 I would just say it's a spectrum with thereal
02:55:25.920 numbers, but continuous is just a functionthat has the property that it's continuous.
02:55:30.939 That can be there even when there's discretephenomenon.
02:55:33.100 Yes, exactly. And in fact, that's relatedto the fact that you can have a countable
02:55:38.540 spacethat's not discrete, right? So discreteness
02:55:41.370 in topology means that only the points themselvesrepresent open sets. So in a sense, I forget
02:55:52.990 whether it's the coarsest or the finest possibletopology, but one of the two. It's the dual
02:55:58.279 to the box topology, or the trivial topology.But you can perfectly well have countable
02:56:05.220 topological spaces that are not discrete.And you can have discrete topological spaces
02:56:09.239 that are not countable.Sorry, is this further complicated with the
02:56:16.220 Lowenheim-Skolem theorem, which in one waysays
02:56:19.880 if you have something that's countable, youhave a model where it's uncountable and
02:56:23.939 of every cardinality and vice versa?Right, right. Yes, it's certainly related.
02:56:28.529 I mean, so the downward Lowenheim-Skolemtheorem is used in the forcing construction
02:56:33.800 that I mentioned earlier.Ah, I see. Okay.
02:56:36.029 All of which is to illustrate exactly thepoint that I think you're making. So there's
02:56:39.660 the notionof continuity of pre-images of open sets that
02:56:42.970 comes from analysis and topology, but that'snot the same as the notion of continuum in
02:56:47.060 the sense that the thing is not countable.And even that notion is sort of dependent
02:56:52.649 on what functions are constructible. Yeah,one of them is essentially an analytic property.
02:56:56.359 You can have continuous maps between countablespaces, but you can't have countable maps
02:57:02.370 between continuous ones and so on.Again, John, I don't know what subject we
02:57:05.780 haven't touched on. This was fascinating.Yeah, this was fantastic. No, this was really
02:57:11.270 fun. I'm really glad we finally got the chanceto do this. And yeah, I hope I didn't become
02:57:16.520 too incoherent towardsthe end.
02:57:26.700 No, no, you're totally fine.Also, the string theory video that Jonathan
02:57:36.000 mentions is called The Iceberg of String Theory,and I recommend you check it out. It took
02:57:41.399 approximately two months of writing,four months of editing with four editors,
02:57:46.080 four rewrites, 14 shoots, and there are sevenlayers.
02:57:49.210 It's the most effort that's gone into anysingle theories of everything video.
02:57:53.229 It's a rabbit hole of the math of string theorygeared toward the graduate level.
02:57:57.750 There's nothing else like it.Thank you for watching. Thank you for listening.
02:58:02.070 There's now a website,Curt Jaimungal.org, and that has a mailing
02:58:05.870 list. The reason being that large platformslike YouTube,
02:58:09.280 like Patreon, they can disable you for whateverreason, whenever they like. That's just part
02:58:14.850 ofthe terms of service. Now, a direct mailing
02:58:17.359 list ensures that I have an untrammeled communicationwith you. Plus, soon I'll be releasing a one
02:58:22.710 page PDF of my top 10 TOEs. It's not as QuentinTarantino as it sounds like. Secondly, if
02:58:28.630 you haven't subscribed or clicked that likebutton,
02:58:31.569 now is the time to do so. Why? Because eachsubscribe, each like helps YouTube push this
02:58:38.020 content to more people like yourself. Plus,it helps out Curt directly, aka me.
02:58:43.590 I also found out last year that external linkscount plenty toward the algorithm,
02:58:47.780 which means that whenever you share on Twitter,say on Facebook, or even on Reddit, etc.,
02:58:52.990 it shows YouTube, hey, people are talkingabout this content outside of YouTube,
02:58:58.060 which in turn greatly aids the distributionon YouTube.
02:59:01.560 Thirdly, there's a remarkably active Discordand subreddit for Theories of Everything where
02:59:05.960 people explicate TOEs, they disagree respectfullyabout theories, and build as a community our
02:59:11.601 ownTOE. Links to both are in the description.
02:59:14.670 Fourthly, you should know this podcast ison iTunes,
02:59:17.450 it's on Spotify, it's on all of the audioplatforms. All you have to do is type in
02:59:22.130 Theories of Everything and you'll find it.Personally, I gain from re-watching lectures
02:59:26.200 and podcasts. I also read in the commentsthat, hey, TOE listeners also gain from replaying.
02:59:31.510 So how about instead you re-listen on thoseplatforms like iTunes, Spotify, Google Podcasts,
02:59:36.500 whichever podcast catcher you use. And finally,if you'd like to support more conversations
02:59:41.530 likethis, more content like this, then do consider
02:59:44.320 visiting patreon.com slash CURTJAIMUNGAL anddonating with whatever you like. There's also
02:59:49.649 PayPal, there's also crypto, there's alsojust
02:59:51.970 joining on YouTube. Again, keep in mind, it'ssupport from the sponsors and you that allow
02:59:57.540 meto work on TOE full-time. You also get early
03:00:00.470 access to ad-free episodes, whether it's audioor video. It's audio in the case of Patreon,
03:00:04.880 video in the case of YouTube. For instance,this episode that you're listening to right
03:00:08.460 now was released a few days earlier. Everydollar
03:00:11.420 helps far more than you think. Either way,your viewership is generosity enough. Thank
03:00:16.000 you so much.
