from model import cliArgument,candidate

def ca_route():
    if cliArgument.args.fimport:
        candidate.import_json_file(cliArgument.args.fimport)
    elif cliArgument.args.fexport:
        print("export")
    elif cliArgument.args.jsonformat:
        candidate.write_json_file(candidate.empty_json_template(),"template")



