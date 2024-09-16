from http import HTTPStatus
from django.urls import reverse


def test_contacts_thanks(client):
    name = ["tiago"]
    response = client.get(reverse("contacts:thanks", args=(name,)))

    assert response.status_code == HTTPStatus.OK
    assert response.content.decode() == f"Obrigado {name}!!!"
