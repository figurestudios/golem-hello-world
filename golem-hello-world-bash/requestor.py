#!/usr/bin/env python3
import asyncio
from typing import AsyncIterable

from yapapi import Golem, Task, WorkContext
from yapapi.log import enable_default_logger
from yapapi.payload import vm


async def worker(context: WorkContext, tasks: AsyncIterable[Task]):
    async for task in tasks:
        script = context.new_script()

        # upload & run the provider.sh script
        script.upload_file("provider.sh", "/golem/input/provider.sh")
        future_result = script.run("/bin/sh", "-x", "/golem/input/provider.sh")

        yield script

        task.accept_result(result=await future_result)


async def main():
    package = await vm.repo( 
        image_hash="b5b66f21a48ab81367ca7f9e5ecba75278b8a5abdeffb939529abfc2",
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