#!/usr/bin/env python3
import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm


async def worker(context: WorkContext, tasks: AsyncIterable[Task]):
    async for task in tasks:
        script = context.new_script()

        # run the Provider.jar file
        future_result = script.run("/usr/bin/java", "-jar", "/Provider.jar")

        yield script
 
        task.accept_result(result=await future_result)


async def main():
    package = await vm.repo( 
        image_hash="cc4d7097d7a5aa1cd2630e90c482b79e6a1a706165e7438b563b37a5" # java example
        # image_hash="d8df266007210b8ae5e1649f9ea68d1f17a3090a9fa9375331221c2f" # kotlin example
    )

    tasks = [Task(data=None)]

    async with Golem(budget=1.0, subnet_tag="devnet-beta") as golem:
        async for completed in golem.execute_tasks(worker, tasks, payload=package, max_workers=1):
            # print out the console output
            print(completed.result.stdout)


if __name__ == "__main__":
    enable_default_logger(log_file="out.log")

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
