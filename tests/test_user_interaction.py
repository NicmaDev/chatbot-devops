from chatbot import user_interaction

def test_receive_and_respond():
    assert callable(user_interaction.receive_message)
    assert callable(user_interaction.send_response)

