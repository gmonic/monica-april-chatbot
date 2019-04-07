import sys, json, requests
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask("MyApp2")
ACCESS_TOKEN = 'EAAFrHY4C6aYBAKe615if1KdrP4unl8DSXs66x7ZBMviNIRZBG90flVBT52AUUjWUKu7cHE4UMgm068DO86wIc5hcBHkqO80NvYRSNZA2ZBTRRb8XRcXNQLa9APsOh18siwiuZBO8751qDx7m3OH10ZAL0jpqBA8qEu2ZCNxyi6EZBAZDZD'
VERIFY_TOKEN = 'monicasverifytoken'
bot = Bot(ACCESS_TOKEN)

@app.route('/', methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
        # get whatever message a user sent to  bot
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    # Facebook messenger ID for user so we know where to send response to
                    recipient_id = message['sender']['id']
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
                # if user sends a GIF, photo, video or another non-text item
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
    return "Message Processed!"

def verify_fb_token(token_sent):
    # take token sent from fb and verify it matches verify token you sent
    # if they match, allowe request, else retun error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    else:
        return "Invalid verification token"

# chooses a random message to send the user
def get_message():
    sample_responses = ["You are stunning!", "Great work!"]
    return random.choice(sample_responses)

# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


app.run(debug=True)
