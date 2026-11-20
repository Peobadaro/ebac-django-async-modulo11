import asyncio
import inspect

import pytest
from django.urls import reverse

from core import views


def test_async_view_e_uma_corrotina():
    assert inspect.iscoroutinefunction(views.async_view)
    assert not inspect.iscoroutinefunction(views.sync_view)


@pytest.mark.asyncio
async def test_async_view_responde_e_roda_em_paralelo(async_client):
    response = await async_client.get(reverse("async_view"))
    data = response.json()
    assert response.status_code == 200
    assert data["resultados"] == [10, 20, 30]
    assert data["tempo_segundos"] < 1.5  # 3 tarefas de 1 s ao mesmo tempo


def test_sync_view_responde_em_sequencia(client):
    response = client.get(reverse("sync_view"))
    data = response.json()
    assert response.status_code == 200
    assert data["resultados"] == [10, 20, 30]
    assert data["tempo_segundos"] >= 3


def test_tarefa_async_retorna_valor():
    assert asyncio.run(views.tarefa_async(2, segundos=0)) == 20
