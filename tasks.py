import asyncio

async def task(seconds):
    """
    task to do for n seconds
    """
    print(f'it will take {seconds}')
    await asyncio.sleep(seconds)
    return 'task finished'


async def task_que():kk


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print('task creation started')
        task_obj = loop.create_task(task(seconds=2))
        loop.run_until_complete(task_obj)
    finally:
        loop.close()

    print(f"result {task_obj}")
