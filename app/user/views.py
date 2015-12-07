from app.models import User

@app.route("/", methods=['GET', 'POST'])
def main():
    """Respond to incoming calls with a simple text message."""
 	from_number = request.values.get('From', None)
 	user = User.query.filter_by(phone_number=from_number).first()
 	if user == None:
 		resp = twilio.twiml.Response()
        	resp.message("Hello my name is PAL, it is nice to meet you!"
        return str(resp)

    '''resp = twilio.twiml.Response()
                with resp.message("Hello, Mobile Monkey") as m:
                    m.media("https://demo.twilio.com/owl.png")
                return str(resp)'''


 