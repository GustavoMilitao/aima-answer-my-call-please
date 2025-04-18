from twilio.rest import Client

client = Client('TWILIO_SID', 'TWILIO_TOKEN')

# Liga pra AIMA
call = client.calls.create(
    to="+351NUMERO_DA_AIMA",
    from_="+NÚMERO_TWILIO",
    url="https://github.com/GustavoMilitao/aima-answer-my-call-please/espera-e-redireciona.xml"
)
