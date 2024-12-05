import requests

class WhatsappAPI:
    def __init__(self, token, phone_number_id):
        self.token = token  # Token de acceso generado por Meta
        self.phone_number_id = phone_number_id  # ID del número configurado en la API
        self.base_url = f"https://graph.facebook.com/v17.0/{phone_number_id}/messages"

    def send_message(self, to, message):
        """
        Enviar un mensaje de texto simple.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }

        response = requests.post(self.base_url, json=data, headers=headers)
        return response.json()

    def send_file(self, to, file_url, file_type="document", caption=None):
        """
        Enviar un archivo (PDF, imagen, etc.) mediante un enlace.
        """
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        data = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": file_type,
            file_type: {"link": file_url},
        }
        if caption:
            data[file_type]["caption"] = caption

        response = requests.post(self.base_url, json=data, headers=headers)
        return response.json()

# Ejemplo de uso
if __name__ == "__main__":
    token = "TU_TOKEN_DE_ACCESO"  # Reemplaza con tu token de acceso
    phone_number_id = "TU_PHONE_NUMBER_ID"  # Reemplaza con el ID del número
    api = WhatsappAPI(token, phone_number_id)

    # Enviar mensaje de texto
    response = api.send_message("+584120794577", "¡Hola! Este es un mensaje de prueba.")
    print(response)

    # Enviar un archivo PDF
    file_url = "https://example.com/document.pdf"
    response = api.send_file("+584120794577", file_url, file_type="document", caption="Aquí está tu archivo PDF.")
    print(response)

    # Enviar una imagen con un mensaje
    image_url = "https://example.com/image.jpg"
    response = api.send_file("+584120794577", image_url, file_type="image", caption="¡Mira esta imagen!")
    print(response)


