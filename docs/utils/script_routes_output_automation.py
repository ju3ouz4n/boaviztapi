import os
import json
from urllib.request import Request, urlopen
import re
from py_markdown_table.markdown_table import markdown_table
from uvicorn import Config
from boaviztapi.main import app, UvicornServerThreaded

"""
script_route_output_automation.py
Description : 
"""
file_to_check = []

def matchMdTablesToReplace(md_string):
    md_table = r"(\n\n(\|.+\|\s*\n)+\n)"
    #filter_table = r"((?P<get>GET\s*\|\s*/v1/server)|(?P<post>POST\s*\|\s*/v1/server)|(?P<conso>POST\s*\|\s*/v1/consumption_profile/cpu) | (?P<utils>GET\s*|\s*/v1/server/archetypes))"
    filter_table = r"(?P<get>GET\s*\|\s*/v1/server)|(?P<post>POST\s*\|\s*/v1/server)|(?P<conso>POST\s*\|\s*/v1/consumption_profile/cpu) | (?P<utils>GET\s*\|\s*/v1/server/archetypes)"
    re_md_table = re.compile(md_table,re.MULTILINE)
    re_filter_table = re.compile(filter_table,re.MULTILINE)

    ret = re_md_table.finditer(md_string)
    filtered_ret = [m for m in ret if  re_filter_table.search(m.group(0)) is not None ]
    return filtered_ret

def replaceMdTables(md_string):
    md_table = r"(\n\n(\|.+\|\s*\n)+\n*)"
    re_md_table = re.compile(md_table,re.MULTILINE)
    filter_table = r"(?P<get>GET\s*\|\s*/v1/server)|(?P<post>POST\s*\|\s*/v1/server)|(?P<conso>POST\s*\|\s*/v1/consumption_profile/cpu) | (?P<utils>GET\s*\|\s*/v1/server/archetypes)"
    re_filter_table = re.compile(filter_table,re.MULTILINE)
    md_replaced_string = md_string

    
    allroutes = getAllRoutes()
    post_routes = {k: {"Method":"POST","Routes":k,"Description": v["post"]["summary"]} for k, v in allroutes['paths'].items() if "post" in v.keys() and "get" in v.keys()} 
    get_routes =  {k: {"Method":"GET","Routes":k,"Description": v["get"]["summary"]} for k, v in allroutes['paths'].items() if "post" in v.keys() and "get" in v.keys()}
    consumption_cpu = {k: {"Method":"POST","Routes":k,"parameters": ' '.join([x["name"] for x in v["post"]["parameters"]]),"Description": v["post"]["summary"]} for k, v in allroutes['paths'].items() if k == "/v1/consumption_profile/cpu"}
    utils_route = {k: {"Method":"GET","Routes":k,"parameters": ' '.join([x["name"] for x in v["get"]["parameters"]] if "parameters" in v["get"] else []),"Description": v["get"]["summary"]} for k, v in allroutes['paths'].items() if k!="/" and "get" in v.keys() and "post" not in v.keys() }
    markdown_post = markdown_table(list(post_routes.values())).set_params(row_sep = 'markdown', quote = False).get_markdown()
    markdown_get = markdown_table(list(get_routes.values())).set_params(row_sep = 'markdown', quote = False).get_markdown()
    markdown_consumption_cpu = markdown_table(list(consumption_cpu.values())).set_params(row_sep = 'markdown', quote = False).get_markdown()
    markdown_utils_route = markdown_table(list(utils_route.values())).set_params(row_sep = 'markdown', quote = False).get_markdown()
    list_table_to_replace = (("get",markdown_get),("post",markdown_post),("conso",markdown_consumption_cpu),("utils",markdown_utils_route))

    for table_to_replace in list_table_to_replace:
        ret = re_md_table.finditer(md_replaced_string)
        filtered_rets = [m for m in ret if  re_filter_table.search(m.group(0)) is not None ]
        for filtered_ret in filtered_rets:
            if re_filter_table.search(filtered_ret.group(0)).group(table_to_replace[0]) is not None:
                md_replaced_string = md_replaced_string[:filtered_ret.span()[0]]+f"\n\n{table_to_replace[1]}\n"+md_replaced_string[filtered_ret.span()[1]:]

    with(open("../docs/Reference/routes_alt.md", "w+") as file):
        file.write(md_replaced_string)
        file.truncate()
    

    

def getAllRoutes():
    OPEN_API_URL = "http://localhost:5000/openapi.json"
    request = Request(OPEN_API_URL)
    try:
        with urlopen(request) as response:
            json_data = json.loads(response.read())
            return json_data
    except FileNotFoundError:
        print("my_file not found.")

def generate_tutorial_output(directory_to_check: str):
    list_of_files = [file for file in os.listdir(directory_to_check) if file.endswith(".md")]
    for file_name in list_of_files:
        with(open(f"{directory_to_check}/{file_name}", "r+") as file):
            changed_file = change_one_read_file(file.read())
            file.seek(0)
            file.write(changed_file)
            file.truncate()

if __name__ == "__main__":
    config = Config(app=app, host='localhost', port=5000, reload=True)
    server = UvicornServerThreaded(config=config)
    with server.run_in_thread():
        # run the script
        
        with(open("../docs/Reference/routes.md", "r+") as file):
              replaceMdTables(file.read())
        #     file.seek(0)
        #     file.write(changed_file)
        #     file.truncate()