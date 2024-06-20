import json

with open("templates/dag_config.json","r") as f:
    config = json.load(f)
print(type(config))

for dag in config.values():
    print(dag["dag_id"])
    print(dag["default_args"])
    print(dag["schedule_interval"])

    for task in dag["tasks"]:
        print(task["task_id"])
        print(task["bash_command"])

    for task in dag["tasks"]:
        if "upstream_task_ids" in task.keys():
            for upstream_id in task["upstream_task_ids"]:
                print(task["task_id"]+".set_upstream("+upstream_id+")")
    
