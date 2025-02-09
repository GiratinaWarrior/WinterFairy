# Scene 3: Boss Visit

label s3_start:
    scene black 
    stop music
    play sound "fanfare.ogg"

    scene throneroom
    with Dissolve(1.0)

    mc "Honer to the Heart of Winter, Queen Maeve of the Court of Winter Fairies. I humbly request an audience."
    boss "I grant your request and invite you to the frost thrown."
    boss "Yet, I have more than an inkling of why you are here."
    mc "I suppose you already heard about the disagreement between Alyssa and me."
    boss "Indeed I do know of it."
    boss "I have already reflected on the matter and have come to a decision."
    mc "Already? I was expecting- Very well."
    boss "You may comment on it, and I will reflect on those comments."
    mc "Thank you."
    # Stop with the polish about here.
    boss "The disagreement is one matter that will have be addressed. But I am more concerned with how it was carried out."
    boss "You are both advisors of the court and yet was not (...)"
    boss "Like some impuslive children, a pair of squabling birds, a couple of worldly humans."
    mc "(In a small voice.) I get the point ma'am."
    boss "This is unacceptable behaviour from two of my advisors."

label s3_end:
    jump test
