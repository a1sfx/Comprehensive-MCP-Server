# Comprehensive-MCP-Server
Многофункциональный MCP‑сервер с инструментами для математики, строк, данных, утилит, ресурсов и генерации промптов. Этот сервер демонстрирует возможности протокола MCP и библиотеки FastMCP, предоставляя богатый набор инструментов, ресурсов и промптов, которые можно использовать в Claude Desktop, Cursor, VSCode MCP и других MCP‑клиентах.

<img width="804" height="883" alt="image" src="https://github.com/user-attachments/assets/fd0baebc-1ef4-4307-9297-a6d394393fab" />
<img width="757" height="951" alt="image" src="https://github.com/user-attachments/assets/c3e3eec2-6cbf-45af-9836-bda7cdf7aaf8" />
<img width="725" height="310" alt="image" src="https://github.com/user-attachments/assets/d3012bf6-5bcd-4b72-8105-6fbe64811ec8" />

Через MCP‑клиент (рекомендуется)
Пример для Claude Desktop:

{
  "mcpServers": {
    "demo": {
      "command": "uv",
      "args": ["run", "server.py"],
      "cwd": "C:/Users/.../mcp-server-demo"
    }
  }
}

Локальный запуск (для отладки)
uv run server.py
 MCP‑сервер ожидает JSON‑RPC сообщения от клиента.
При ручном запуске без клиента он не будет работать как интерактивная программа.

