"""
Views do exercício do Módulo 11: comparativo entre view síncrona e assíncrona.

As duas fazem 3 "tarefas" de 1 segundo cada (simulando chamadas lentas,
como uma API externa ou um banco de dados).

- sync_view:  uma tarefa depois da outra com time.sleep  -> ~3 s
- async_view: as 3 ao mesmo tempo com asyncio.gather    -> ~1 s
"""
import asyncio
import time

from django.http import JsonResponse


# ------------------------------------------------------------------ async

async def tarefa_async(numero, segundos=1):
    print(f"[async] Tarefa {numero}: começou")
    await asyncio.sleep(segundos)  # não bloqueia: o loop atende outras tarefas
    print(f"[async] Tarefa {numero}: terminou (awaited)")
    return numero * 10


async def async_view(request):
    """View assíncrona: roda as 3 tarefas ao mesmo tempo."""
    inicio = time.perf_counter()
    print("[async] Iniciando a view assíncrona")

    resultados = await asyncio.gather(
        tarefa_async(1),
        tarefa_async(2),
        tarefa_async(3),
    )

    tempo = round(time.perf_counter() - inicio, 2)
    print(f"[async] Fim da view: {tempo} s | resultados = {resultados}")
    return JsonResponse({"tipo": "async", "resultados": resultados, "tempo_segundos": tempo})


# ------------------------------------------------------------------- sync

def tarefa_sync(numero, segundos=1):
    print(f"[sync] Tarefa {numero}: começou")
    time.sleep(segundos)  # bloqueia: nada mais acontece enquanto espera
    print(f"[sync] Tarefa {numero}: terminou")
    return numero * 10


def sync_view(request):
    """View síncrona tradicional: uma tarefa depois da outra."""
    inicio = time.perf_counter()
    print("[sync] Iniciando a view síncrona")

    resultados = [tarefa_sync(1), tarefa_sync(2), tarefa_sync(3)]

    tempo = round(time.perf_counter() - inicio, 2)
    print(f"[sync] Fim da view: {tempo} s | resultados = {resultados}")
    return JsonResponse({"tipo": "sync", "resultados": resultados, "tempo_segundos": tempo})
