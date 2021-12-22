#!/usr/bin/env python3
import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm


async def worker(context: WorkContext, tasks: AsyncIterable[Task]):
    async for task in tasks:
        script = context.new_script()

        # upload & run the provider.rb script
        script.upload_file("provider.rb", "/golem/input/provider.rb")
        future_result = script.run("/bin/sh", "-c", "ruby /golem/input/provider.rb")

        yield script

        task.accept_result(result=await future_result)


async def main():
    package = await vm.repo( 
        image_hash="399de4dad314c6bb6b54fbfb4c4dca4e310ea771f932dff6360a1862",
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