from twilio.rest import Client

client = Client('TWILIO_SID', 'TWILIO_TOKEN')

# Liga pra AIMA
call = client.calls.create(
    to="+351217115000",
    from_="+16368371829",
    url="https://raw.githubusercontent.com/GustavoMilitao/aima-answer-my-call-please/refs/heads/main/espera-e-redireciona.xml"
)