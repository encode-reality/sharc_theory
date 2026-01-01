# Causality and Computational Irreducibility
## Timestamp: 00:55:47

# tactiq.io free youtube transcript
# Jonathan Gorard: Quantum Gravity & Wolfram Physics Project
# https://www.youtube.com/watch/ioXwL-c1RXQ
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
