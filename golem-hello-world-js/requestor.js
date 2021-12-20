const { Executor, Task, utils: { asyncWith }, vm } = require("yajsapi");

async function main() {
  const package = await vm.repo({
    image_hash: "48d399e06dba275294b642c4d1c9de10d84186ef0e6f91371b9d5fd2"
  });
  const tasks = [new Task({})];

  async function* worker(context, tasks) {
    for await (let task of tasks) {
      // upload & run the provider.js file

      context.send_file("provider.js", "/golem/input/provider.js");
      context.run("/bin/sh", ["-c", "node /golem/input/provider.js"]);

      const future_result = yield context.commit();
      const { results } = await future_result;
      task.accept_result(results[results.length - 1])
    }
  }

  await asyncWith(
    new Executor({ task_package: package, budget: "1.0", subnet_tag: "devnet-beta.2" }),
    async (executor) => {
      for await (let completed of executor.submit(worker, tasks)) {
        // console.log the console output of the provider machine
        console.log(completed.result().stdout);
      }
    }
  );
}

main();