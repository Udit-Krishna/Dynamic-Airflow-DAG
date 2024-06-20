# Dynamic Airflow DAG generation using Jinja2

1. Edit `templates/dag_config.json` file according to the DAGs and its tasks information
2. Edit `templates/dag_template.js` file according to the output python file template
3. Run `setup.py` file to generate dags
4. Find the newly generated DAG files in `dags/` folder