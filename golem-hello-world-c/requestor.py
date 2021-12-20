#!/usr/bin/env python3
import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm


async def worker(context: WorkContext, tasks: AsyncIterable[Task]):
    async for task in tasks:
        script = context.new_script()

        # run the provider.py script
        future_result = script.run("/provider_bin")

        yield script
 
        task.accept_result(result=await future_result)


async def main():
    package = await vm.repo( 
        image_hash="9ba449e948b3249732a67e2f557a17085101a7d60c9d7c27a4c93a20",
    )

    tasks = [Task(data=None)]

    async with Golem(budget=1.0, subnet_tag="devnet-beta") as golem:
        async for completed in golem.execute_tasks(worker, tasks, payload=package):
            # print out the console output
            print(completed.result.stdout)


if __name__ == "__main__":
    enable_default_logger(log_file="out.log")

    loop = asyncio.get_event_loop()
    task = loop.create_task(main())
    loop.run_until_complete(task)
