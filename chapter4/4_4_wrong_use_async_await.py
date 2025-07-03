import asyncio
# from util import async_timed, delay
import sys
from pathlib import Path

# Добавляем корень проекта в путь
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# Абсолютный импорт
from util.async_timer import async_timed
from util.delay_functions import delay


@async_timed()
async def main() -> None:
    delay_times = [3, 3, 3]
    [await asyncio.create_task(delay(seconds)) for seconds in delay_times]

    # мы применяем await сразу же после создания задачи. Это значит, что мы 
    # приостанавливаем списковое включение и сопрограмму main для каждой созданной задачи delay до момента,
    # когда она завершится

asyncio.run(main())
