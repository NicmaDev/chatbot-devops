from chatbot.ai_recognition import AIRecognitionModel

def test_prediction():
    model = AIRecognitionModel()
    model.train(['Hola', 'Soy un robot'], ['humano', 'IA'])
    assert model.predict('Hola') == 'humano'
    assert model.predict('Soy un robot') == 'IA'

