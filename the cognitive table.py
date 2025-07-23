ti=0
te=0
fi=0
fe=0
si=0
se=0
ni=0
ne=0
e=0
i=0
j=0
p=0
print("only choose 1,2,3,4 dont put any other or the program will crash and you will have to rewrite gl")
print("1. When making a tough decision, you rely most on—")
print("1. Internal logic — I need it to make sense in my head.")
print("2. Objective results — what works best, fastest, cleanest.")
print("3. Personal truth — if it feels wrong, it *is* wrong.")
print("4. Social impact — I ask who might be hurt or helped.")
q1 = int(input("Your choice (1-4): "))
if q1==1:
	ti=ti+3
	fe-=1
elif q1==2:
	te+=3
	fi-=1
elif q1==3:
	fi=fi+3
	te-=1
elif q1==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n2. You're asked to explain your opinion on a controversial issue. You—")
print("1. Break down the logic behind it step-by-step.")
print("2. Focus on what the most effective solution would be.")
print("3. Share your personal stance, even if unpopular.")
print("4. Emphasize how it affects people emotionally or socially.")
q2 = int(input("Your choice (1-4): "))
if q2==1:
	ti=ti+3
	fe-=1
elif q2==2:
	te=te+3
	fi-=1
elif q2==3:
	fi=fi+3
	te-=1
elif q2==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n3. Someone messes up a group task. You usually—")
print("1. Quietly analyze what went wrong and fix it yourself.")
print("2. Directly tell them how to fix it next time.")
print("3. Feel irritated if their effort lacked authenticity.")
print("4. Try to smooth things over and protect the group mood.")
q3 = int(input("Your choice (1-4): "))
if q3==1:
	ti=ti+3
	fe-=1
elif q3==2:
	te=te+1
	fi-=1
elif q3==3:
	fi=fi+3
	te-=1
elif q3==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n4. What motivates you to improve something?")
print("1. Making it more precise or efficient internally.")
print("2. Making it faster, scalable, and results-driven.")
print("3. Making it feel more meaningful or authentic.")
print("4. Making sure it benefits others and feels good to all.")
q4 = int(input("Your choice (1-4): "))
if q4==1:
	ti=ti+3
	fe-=1
elif q4==2:
	te=te+3
	fi-=1
elif q4==3:
	fi=fi+3
	te-=1
elif q4==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n5. What do you do when people strongly disagree with your decision?")
print("1. Explain your reasoning in a structured way.")
print("2. Stand by the results — if it works, it's valid.")
print("3. Defend your values — even if no one agrees.")
print("4. Try to ease their discomfort and maintain connection.")
q5 = int(input("Your choice (1-4): "))
if q5==1:
	ti=ti+3
	fe-=1
elif q5==2:
	te=te+3
	fi-=1
elif q5==3:
	fi=fi+3
	te-=1
elif q5==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("6. When planning your future, how do you approach it?")
print("1. I envision one clear path with deep meaning.")
print("2. I brainstorm tons of exciting possibilities.")
print("3. I build plans based on what worked in the past.")
print("4. I focus on what I can do right now, step by step.")
q6 = int(input("Your choice (1-4): "))
if q6==1:
	ni=ni+3
	se-=1
elif q6==2:
	ne=ne+3
	si-=1
elif q6==3:
	si=si+3
	ne-=1
elif q6==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n7. How do you usually remember past events?")
print("1. As themes or patterns that shaped who I am.")
print("2. As loose flashes, often rearranged or imagined.")
print("3. In detailed, accurate snapshots and sensations.")
print("4. As experiences I physically felt — sounds, sights, smells.")
q7 = int(input("Your choice (1-4): "))
if q7==1:
	ni=ni+3
	se-=1
elif q7==2:
	ne=ne+3
	si-=1
elif q7==3:
	si=si+3
	ne-=1
elif q7==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n8. You’re given a new project. What excites you?")
print("1. Predicting how it will evolve in the long run.")
print("2. Coming up with unexpected creative twists.")
print("3. Applying proven methods that you trust.")
print("4. Jumping in and figuring it out as you go.")
q8 = int(input("Your choice (1-4): "))
if q8==1:
	ni=ni+3
	se-=1
elif q8==2:
	ne=ne+3
	si-=1
elif q8==3:
	si=si+3
	ne-=1
elif q8==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n9. How do you react to sudden change?")
print("1. I try to make sense of where it fits in the bigger picture.")
print("2. I adapt quickly and play with the new possibilities.")
print("3. I feel uneasy — I like to stick with the familiar.")
print("4. I take action immediately and adjust on the move.")
q9 = int(input("Your choice (1-4): "))
if q9==1:
	ni=ni+3
	se-=1
elif q9==2:
	ne=ne+3
	si-=1
elif q9==3:
	si=si+3
	ne-=1
elif q9==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n10. What do you trust more?")
print("1. Your personal vision of how things will unfold.")
print("2. The endless flow of new ideas and opportunities.")
print("3. Past experiences that guide what’s reliable.")
print("4. Direct experience — what’s real and in front of you.")
q10 = int(input("Your choice (1-4): "))
if q10==1:
	ni=ni+3
	fe-=1
elif q10==2:
	ne=ne+3
	si-=1
elif q10==3:
	si=si+3
	ne-=1
elif q10==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("11. Your friend just made a life-ruining decision. What’s your first move?")
print("1. Break it down analytically — they clearly missed some logic.")  # Ti
print("2. Ask them how they *feel*, but also quietly judge them.")        # Fi
print("3. Support them. Everyone’s a disaster sometimes.")               # Fe
print("4. Fix the mess. Emotionally or practically, whatever works.")    # Te
q11 = int(input("Your choice (1-4): "))
if q11==1:
	ti=ti+3
	fe-=1
elif q11==4:
	te=te+3
	fi-=1
elif q11==2:
	fi=fi+3
	te-=1
elif q11==3:
	fe=fe+3
	si-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n12. You’re arguing with someone who’s obviously wrong. What do you do?")
print("1. Present a logical argument, neatly dismantling their view.")   # Te
print("2. Ask if they’re okay — people lash out when insecure.")         # Fe
print("3. Speak your truth, even if no one gets it.")                    # Fi
print("4. Prove your point with a spreadsheet and slight condescension.")# Ti
q12 = int(input("Your choice (1-4): "))
if q12==4:
	ti=ti+3
	fe-=1
elif q12==1:
	te=te+3
	fi-=1
elif q12==3:
	fi=fi+3
	te-=1
elif q12==2:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n13. You’re asked to make a group decision. Your method?")
print("1. Weigh pros and cons. Efficiency wins.")                        # Te
print("2. You know what’s *right* in your gut — go with that.")         # Fi
print("3. Think through the long-term implications and inner logic.")   # Ti
print("4. Ask the group how they feel and adjust accordingly.")         # Fe
q13 = int(input("Your choice (1-4): "))
if q13==3:
	ti=ti+3
	fe-=1
elif q13==1:
	te=te+3
	fi-=1
elif q13==2:
	fi=fi+3
	te-=1
elif q1e==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n14. Someone says your work lacks soul. Your reaction?")
print("1. You nod. They probably missed the complexity.")                # Ti
print("2. You sulk quietly and reconsider your entire identity.")       # Fi
print("3. You explain that the goal wasn't ‘soul’, it was *results*.")  # Te
print("4. You smile and ask for feedback like a civilized, damaged person.") # Fe
q14 = int(input("Your choice (1-4): "))
if q14==1:
	ti=ti+3
	fe-=1
elif q14==3:
	te=te+3
	fi-=1
elif q14==2:
	fi=fi+3
	te-=1
elif q14==4:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it")
print("\n15. Your moral compass says one thing. The system says another. Who wins?")
print("1. The system — at least it’s measurable.")                      # Te
print("2. Your feelings — cold logic can be a little fascist.")         # Fe
print("3. Your internal code. It’s messy, but it’s yours.")             # Fi
print("4. The most elegant solution that doesn’t get anyone fired.")    # Ti
q15 = int(input("Your choice (1-4): "))
if q15==4:
	ti=ti+3
	fe-=1
elif q15==1:
	te=te+3
	fi-=1
elif q15==3:
	fi=fi+3
	te-=1
elif q15==2:
	fe=fe+3
	ti-=1
else:
	print("i said 1 to 4 dont type any other things as a punishment you will not retake it.")
print("16. You’re handed a new gadget. What’s your move?")
print("1. Read the manual. Every page. Twice. Maybe annotate it.")   # Si
print("2. Press all the buttons and hope it doesn’t explode.")       # Se
print("3. Imagine what it *could* become if hacked creatively.")     # Ne
print("4. Stare at it. See visions of what it will do in ten years.")# Ni
q16 = int(input("Your choice (1-4): "))
if q16==4:
	ni=ni+3
	se-=1
elif q16==3:
	ne=ne+3
	si-=1
elif q16==1:
	si=si+3
	ne-=1
elif q16==2:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n17. You’re given five random words. What do you do?")
print("1. Recall that one textbook from 4th grade they all appeared in.") # Si
print("2. Link them into an epic metaphor about society’s downfall.")     # Ne
print("3. Guess their symbolic connection and feel slightly haunted.")   # Ni
print("4. Say them out loud in different voices until one sounds cool.") # Se
q17 = int(input("Your choice (1-4): "))
if q17==3:
	ni=ni+3
	se-=1
elif q17==2:
	ne=ne+3
	si-=1
elif q17==1:
	si=si+3
	ne-=1
elif q17==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n18. Your friend tells you they saw a ghost. Reaction?")
print("1. Ask if the ghost had a predictable haunting pattern.")          # Si
print("2. Ask if the ghost had a message about the future.")             # Ni
print("3. Suggest it might represent unresolved trauma... or capitalism.")# Ne
print("4. Ask what it *felt* like and go ghost-hunting immediately.")    # Se
q18 = int(input("Your choice (1-4): "))
if q18==2:
	ni=ni+3
	se-=1
elif q18==3:
	ne=ne+3
	si-=1
elif q18==1:
	si=si+3
	ne-=1
elif q18==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n19. You’re in a totally new place. How do you explore?")
print("1. Sense everything: smells, sounds, that weird tile texture.")    # Se
print("2. Wander until a pattern emerges. Then follow it obsessively.")  # Ni
print("3. Compare it to 16 other places you’ve been. Make a list.")      # Si
print("4. Imagine how it would look in an alternate timeline.")          # Ne
q19 = int(input("Your choice (1-4): "))
if q19==2:
	ni=ni+3
	se-=q
elif q19==4:
	ne=ne+3
	si-=1
elif q19==3:
	si=si+3
	ne-=1
elif q19==1:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("\n20. You’re stuck in traffic. Where does your mind go?")
print("1. Why this always happens. What a *reliable* tragedy.")          # Si
print("2. How to redesign the city with hovercars and portals.")         # Ne
print("3. The symbolism of human stagnation. Deep stuff.")               # Ni
print("4. Out the window — is that a taco truck? I'm getting out.")      # Se
q20 = int(input("Your choice (1-4): "))
if q20==3:
	ni=ni+3
	se-=1
elif q20==2:
	ne=ne+3
	si-=1
elif q20==1:
	si=si+3
	ne-=1
elif q20==4:
	se=se+3
	ni-=1
else:
	print("stop it its ruining everything the same punishment")
print("21. A spontaneous group plan appears. You're free. You...")
print("1. Say yes instantly — life’s short, why not?")        # E
print("2. Need a moment to assess your energy and sanity.")   # I
print("3. Already know you’re going — you hate missing things.") # E
print("4. Already know you’re not — your bed has custody.")   # I
q21 = int(input("Your choice (1-4): "))
if q21==1:
	e=e+1
elif q21==2:
	i=i+1
elif q21==3:
	e=e+1
elif q21==4:
	i=i+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n22. You’re placed in a new team with strangers.")
print("1. Start conversation — silence is unbearable.")       # E
print("2. Wait and observe — why waste words early?")         # I
print("3. Jump into action — bonding happens while doing.")   # E
print("4. Need to warm up. You don't download strangers that fast.") # I
q22 = int(input("Your choice (1-4): "))
if q22==1:
	e=e+1
elif q22==2:
	i=i+1
elif q22==3:
	e=e+1
elif q22==4:
	i=i+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n23. When do you feel most *you*?")
print("1. When others reflect your energy back at you.")      # E
print("2. When you're alone, and everything clicks internally.") # I
print("3. In deep conversation with one person, not a crowd.")# I
print("4. In a crowd where you're riding the chaos, not lost in it.") # E
q23 = int(input("Your choice (1-4): "))
if q23==1:
	e=e+1
elif q23==2:
	i=i+1
elif q23==4:
	e=e+1
elif q23==3:
	i=i+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n24. What do you do with silence?")
print("1. Break it. It's tension. Why let it grow teeth?")    # E
print("2. Embrace it. It's space to breathe and reset.")      # I
print("3. Analyze what it’s saying. Silence speaks too.")     # I
print("4. Turn up the music. Empty air feels heavy.")         # E
q24 = int(input("Your choice (1-4): "))
if q24==1:
	e=e+1
elif q24==2:
	i=i+1
elif q24==4:
	e=e+1
elif q24==3:
	i=i+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n25. The self is...")
print("1. A performance, shaped by others and environments.") # E
print("2. An internal compass, unbothered by noise.")         # I
print("3. A paradox — public chaos, private stillness.")      # I
print("4. A mirror ball — the more people around, the more light.") # E
q25 = int(input("Your choice (1-4): "))
if q25==1:
	e=e+1
elif q25==2:
	i=i+1
elif q25==4:
	e=e+1
elif q25==3:
	i=i+1
else:
	print("why ? why me? just choose 1 to 4")
print("26. How do you approach deadlines?")
print("1. Early prep. You like watching others panic while you sip coffee.")    # J
print("2. You try. But somehow it’s 11:59 every time.")                         # P
print("3. You plan, then change the plan, then follow the chaos.")             # P
print("4. You need a roadmap. Freefall isn't your thing.")                     # J
q26 = int(input("Your choice (1-4): "))
if q26==1:
	j=j+1
elif q26==2:
	p=p+1
elif q26==3:
	p=p+1
elif q26==4:
	j=j+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n27. Your room or workspace usually...")
print("1. Has a system. Not always tidy, but you know the logic.")             # J
print("2. Is a terrain of creativity. Also called a mess.")                    # P
print("3. Reflects your mood shifts. Sometimes clean, sometimes apocalyptic.") # P
print("4. Is maintained. You don’t function well in entropy.")                 # J
q27 = int(input("Your choice (1-4): "))
if q27==1:
	j=j+1
elif q27==2:
	p=p+1
elif q27==3:
	p=p+1
elif q27==4:
	j=j+1
else:
	print("why ? why me? just choose 1 to 4")

print("\n28. Plans change last minute. You...")
print("1. Hate it. Structure was the whole point.")                            # J
print("2. Shrug. New plans = new data.")                                       # P
print("3. Internally scream, externally smile.")                               # J
print("4. Roll with it. What’s life without curveballs?")                      # P
q28 = int(input("Your choice (1-4): "))
if q28==1:
	j=j+1
elif q28==2:
	p=p+1
elif q28==4:
	p=p+1
elif q28==3:
	j=j+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n29. When making decisions...")
print("1. You prefer closure. Even a bad decision is better than limbo.")      # J
print("2. You delay. What if new options show up last second?")                # P
print("3. You make mini-decisions until the big one reveals itself.")          # P
print("4. You map it out, cross off steps, and *then* decide.")                # J
q29 = int(input("Your choice (1-4): "))
if q29==1:
	j=j+1
elif q29==2:
	p=p+1
elif q29==3:
	p=p+1
elif q29==4:
	j=j+1
else:
	print("why ? why me? just choose 1 to 4")
print("\n30. Structure feels like...")
print("1. Safety. It protects you from spiraling.")                            # J
print("2. Confinement. You prefer open mental tabs.")                          # P
print("3. Optional. Some days yes, some days full gremlin.")                   # P
print("4. A necessity. Even chaos should follow rules.")                       # J
q30 = int(input("Your choice (1-4): "))
if q30==1:
	j=j+1
elif q30==2:
	p=p+1
elif q30==3:
	p=p+1
elif q30==4:
	j=j+1
else:
	print("why ? why me? just choose 1 to 4")
print("perfect now let us calculate your type first  ")
intp=0
intj=0
infp=0
infj=0
entp=0
entj=0
enfp=0
enfj=0
istp=0
istj=0
isfp=0
isfj=0
estp=0
estj=0
esfp=0
esfj=0
if ti>te:
	intp=intp+2
	entp=entp+1
	istp=istp+2
	estp=estp+1
if te>ti:
	intj=intj+1
	entj=entj+2
	istj=istj+1
	estj=estj+2
if ni>ne:
	intj+=2
	infj+=2
	entj+=1
	enfj+=1
if ne>ni:
	entp+=2
	intp+=1
	enfp+=2
	infp+=1
if fi>fe:
	infp+=2
	enfp+=1
	isfp+=2
	esfp+=1
if fe>fi:
	infj+=1
	enfj+=2
	isfj+=1
	esfj+=2
if se>si:
	estp+=2
	istp+=1
	esfp+=2
	isfp+=1
if si>se:
	istj+=2
	estj+=1
	esfj+=1
	isfj+=2
if i>e and p>j:
	if (ni+ne)<(si+se):
		if istp>isfp:
			print('istp')
		else:
			print('isfp')
	else:
		if intp>infp:
			print('intp')
		else:
			print('infp')
if e>i and p>j:
	if (ni+ne)<(si+se):
		if estp>esfp:
			print('estp')
		else:
			print('esfp')	
	else:
		if entp>enfp:
			print('entp')
		else:
			print('enfp')
if i>e and j>p:
	if (ni+ne)<(si+se):
		if istj>isfj:
			print('istj')
		else:
			print('isfj')
	else:
		if intj>infj:
			print('intj')
		else:
			print('infj')
if e>i and j>p:
	if (ni+ne)<(si+se):
		if estj>esfj:
			print('estj')
		else:
			print('esfj')
	else:
		if entj>enfj:
			print('entj')
		else:
			print('enfj')
print("now let us calculate your cognative table")
scores={'ti':ti,'te':te,'fi':fi,'fe':fe,'si':si,'se':se,
'Ni':ni ,'ne':ne}
dominant = max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
auxilary=max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
tertary=max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
inferior=max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
opposing=max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
critical=max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
trickster=max(scores, key=scores.get)
scores.pop(max(scores, key=scores.get))
demon=max(scores, key=scores.get)
if dominant==auxilary:
	if i>e:
		ni+=1
		ti+=1
		fi+=1
		si+=1
	else:
		ne+=1
		se+=1
		fe+=1
		te+=1
if demon==trickster:
	if i<e:
		ni+=1
		fi+=1
		ti+=1
		si+=1
	else:
		ne+=1
		se+=1
		fe+=1
		te+=1
print("your dominent function is ,",dominant)
print("your auxilary function is, ",auxilary)
print("your tertary function,",tertary)
print("your inferior function or aspirent,",inferior)
print("your 5th function or opposing is ,",opposing)
print("your 6th function or critical parent,",critical)
print("your 7th function or trickster ,",trickster)
print("the final or the demon function is,",demon)
print("If you have thoughts or feedback on how I can improve this, let me know.")
print("This was built entirely using concepts from the 12th-grade  book — nothing fancy, no theories beyond that.")
print("So yeah, it might feel a bit crude in places, but I trust you learned something useful about how you think.")
print("To understand what it all means, check the README. If that’s not enough, YouTube has plenty of explainers.")
print("Good luck. Remember — the way you think always defines what you become.")