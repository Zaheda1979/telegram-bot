import random

MESSAGES = [
    "Aaj bhi wahi excuse dega kya jo kal diya tha?\nWaqt kisi ka intezaar nahi karta.\nUth, kaam pe lag, warna sirf sochta reh jayega.\nABHI: apna sabse zaroori kaam shuru kar.",

    "Dusre log aage nikal rahe hain jab tu comfort mein pada hai.\nDard hoga sunke, lekin sach yahi hai.\nKal ki baatien bahut ho gayi, aaj action chahiye.\nABHI: uth aur pehla kaam start kar.",

    "Tu jaanta hai tu kya kar sakta hai, phir bhi ruka kyun hai?\nHar din jo waste hota hai, wapas nahi aata.\nKoi tera kaam karne nahi aayega.\nABHI: phone rakh, kaam pe focus kar.",

    "Sapne dekhna aasan hai, unke liye uthna mushkil.\nTu abhi bhi wahi hai jahan 6 mahine pehle tha.\nYe rukna ab bandh karna padega.\nABHI: apni to-do list ka pehla kaam pura kar.",

    "Log tere baare mein baatein karte honge, tu chup baitha hai.\nAaram karne ka time nahi hai abhi.\nJo mehnat karega wahi jeetega.\nABHI: 10 minute ka break khatam, wapas kaam pe lag.",

    "Tu apne aap se kiya wada bhool gaya kya?\nHar subah yehi sochta hai 'aaj se sudhrunga'.\nAaj wo din hai, kal nahi.\nABHI: apna sabse mushkil kaam sabse pehle kar.",

    "Excuses banane mein tu expert ho gaya hai, kaam karne mein nahi.\nJitna time bahane sochne mein lagta hai, utne mein kaam ho jata.\nAaj bhi tu wahi purani kahani dohrayega kya?\nABHI: bina soche, seedha kaam pe lag ja.",

    "Har raat sochta hai kal alag hoga, phir subah wahi routine.\nYe cycle khud tune banaya hai, khud hi todna padega.\nKoi bahar se aake tujhe nahi badlega.\nABHI: jo sabse zyada avoid kar raha hai, wahi kaam pehle kar.",

    "Comfort zone mein baithe baithe zindagi nikal jayegi.\nJin logo ko tu kabhi kum aankta tha, wo aage nikal chuke hain.\nAur tu abhi bhi wahi bahane dhoondh raha hai.\nABHI: apna phone side rakh, 30 minute sirf kaam kar.",

    "Tu khud ko dhoka de raha hai 'busy hoon' bolke.\nBusy aur productive mein fark hota hai, samajh.\nAaj ka din bhi waste hone wala hai agar abhi nahi utha.\nABHI: sabse important kaam likh aur usi pe lag ja.",

    "Kitni baar khud se wada kiya aur tod diya, gin sakta hai kya?\nTrust khud pe se bhi uthta ja raha hai dheere dheere.\nAb aur waqt barbad karne ka mauka nahi hai.\nABHI: ek chhota kaam abhi complete karke dikha.",
]

def generate_motivation() -> str:
    return random.choice(MESSAGES)


def run():
    from telegram_utils import send_message
    msg = generate_motivation()
    send_message(msg)


if __name__ == "__main__":
    run()
