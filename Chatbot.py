import nltk
from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hi|hello|hey|HELLO|HI",
        ["Hello!", "Hi there!", "How can I help you today?"]
    ],
    [
        r"how are you",
        ["I'm just a computer program, but I'm here to assist you.", "I don't have feelings, but thanks for asking!"]
    ],
    [
        r"interview questions|job questions",
        ["Sure, I can help with interview questions. Could you please specify the job role or industry you're interested in?"]
    ],
    [
        r"(job role|industry)",
        ["Great! For the {} job role in the {} industry, you can expect questions related to skills, experience, and behavioral scenarios. Would you like more specific questions?"]
    ],
    [
        r"tell me more|specific questions",
        ["Of course! Here are some common interview questions:\n1. Tell me about yourself.\n2. What are your strengths and weaknesses?\n3. Describe a challenging project you've worked on.\n4. Where do you see yourself in 5 years?\nRemember, it's essential to prepare specific examples and practice your responses."]
    ],
    #Questions on BIET'
    [
        r"Where is BIET",
        ["BIET is located in Shamanur road,Davangere-577005"]
    ],
    [
        r"Where is the Shiva temple in BIET",
        ["It is located in infront of admin block"]
    ],
    [
        r"What is the capacity of SSM Cultural hall ",
        ["It has a Capacity of 700 people and with 2 VIP balconies"]
    ],
    [
        r"What are the sports available to play in the campus",
        ["The sports available are \n1.Cricket 2.Football \n3.Batminton \n4.Throwball \n5.Volleyball \n6.Carrom \n7.Chess"]
    ],
    [
        r"What is the AIM of BIET|AIM|aim",
        ["Building the budding generation with a noble mission of engineering a healthy and technologically developed society"]
    ],
    [
        r"What is the VISION of BIET|vision|Vision|VISION",
        ["To be a centre of excellence recognized nationally and internationally, in distinctive areas of engineering education and research, based on a culture of innovation and invention"]
    ],
    [
        r"What is the MISSION of BIET|MISSION|mission",
        ["BIET contributes to the growth and development of its students by imparting a broad based engineering education and empowering them to be successful in their chosen field by inculcating in them positive approach, leadership qualities and ethical values"]
    ],
    [
        r"(.*)",
        ["We appreciate your inquiry. We would get back to you later with more information."]
    ]
    # Add more pattern-response pairs here
]
chatbot = Chat(pairs, reflections)
def chat_with_bot():
    print("Hello! I'm your chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
        response = chatbot.respond(user_input)
        print("Chatbot:", response)
if __name__ == "__main__":
    chat_with_bot()
    #tkinter
    #pyqt 
    #py2.exe 
    #fuzywuzy
