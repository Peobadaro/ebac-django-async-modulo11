# EBAC – Django Async Views

Projeto do curso **Profissão: Desenvolvedor Full Stack Python** da EBAC: views assíncronas no Django.

Autor: **Pedro Badaró Ferreira** ([@Peobadaro](https://github.com/Peobadaro))

## O que tem aqui

App `core` com duas views que fazem 3 tarefas de 1 segundo cada:

| Rota | View | Como roda | Tempo |
|---|---|---|---|
| `/sync/` | `sync_view` (def) | uma tarefa depois da outra, com `time.sleep` | ~3 s |
| `/async/` | `async_view` (async def) | as 3 ao mesmo tempo, com `await asyncio.gather` | ~1 s |

Cada tarefa faz `print` no terminal quando começa e quando termina, para ver a ordem de execução. Na view assíncrona as 3 começam juntas.

Saída real do terminal: [`docs/saida-terminal.txt`](docs/saida-terminal.txt)

## Como rodar

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn async_project.asgi:application --reload
```

Abra http://127.0.0.1:8000/async/ e http://127.0.0.1:8000/sync/ e veja os `print` no terminal.

> Também funciona com `python manage.py runserver`, mas rodando em ASGI (uvicorn) a view assíncrona roda de verdade no event loop.

## Testes

```bash
pip install -r requirements-dev.txt
pytest
```
