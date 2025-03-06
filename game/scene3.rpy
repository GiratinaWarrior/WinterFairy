# Scene 3: Boss Visit

label s3_start:
    scene black 
    stop music
    play sound "fanfare.ogg"

    scene throneroom
    with Dissolve(1.0)

    mc "Honour to the Heart of Winter, Queen Maeve of the Court of Winter Fairies. I humbly request an audience."
    boss "I grant your request and invite you to the frost throne."
    boss "Yet, I have more than an inkling of why you are here."
    mc "I suppose you already heard about the disagreement between Alyssa and me."
    boss "Indeed I do know of it."
    boss "I have already reflected on the matter and have come to a decision."
    mc "Already? I was expecting- Very well."
    boss "You may comment on it, and I will reflect on those comments."
    mc "Thank you."
    boss "The disagreement is one matter that will have be addressed. But I am more concerned with how it was carried out."
    boss "You are both advisors of the court and yet that is not how your carried yourselves today."
    boss "An incident described to me as \"a complete slap-fest, almost a brawl\"."
    boss "Like some impulsive children, a pair of squabbling birds, a couple of worldly humans."
    mc "(In a small voice.) I get the point ma'am."
    boss "This is unacceptable behaviour from two of my advisors."
    boss "Your punishment is simple, you two will resolve this disagreement between the two of you alone."
    boss "You will come to me with your decision, but you two must be in unanimous agreement on the matter of the weather for Long Night."
    boss "This is my judgment. Do you wish to comment on it?"
    mc "..."
    mc "I can think of no objection. But I will ask for your advice."
    boss "You may talk to others, but you may not have anyone weight in on the matter officially."
    # "different-weather"
    boss "You may go back to the start, choose any weather that could have been chosen to begin with."
    mc "Thank you. It isn't just the weather though. It is-"
    boss "I know you have never gotten along in personal matters. Perhaps this should have been seen to before it reached this point. But you must resolve this matter."
    mc "How long do we have to do that."
    boss "You must do so with all haste."
    mc "I see."
    mc "..."
    mc "I thank you for your attention. If it pleases you I will now take my leave."
    boss "I have one last addition. I know you are a capable advisor Sylvie, but remember so is Alyssa."
    boss "And so-"
    boss "I grant your request and bless your days."
    jump s3_end

label s3_end:
    jump s4_start
