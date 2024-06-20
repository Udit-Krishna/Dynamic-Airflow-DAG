import json
from jinja2 import Environment, FileSystemLoader

with open("templates/dag_config.json","r") as f:
    config = json.load(f)
    
environment = Environment(loader=FileSystemLoader("templates"),
                          trim_blocks=True,
                          lstrip_blocks=True)
template = environment.get_template("dag_template.j2")

for dag in config.values():
    filename = f'{dag["dag_id"]}.py'
    content = template.render(dag = dag)

    with open(f"dags/{filename}", "w") as py_file:
        py_file.write(content)
        print(f"Wrote {filename} successfully...")