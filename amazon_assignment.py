##########################################################################################
# Write a routine that accepts a command from cmd_list, and replaces the
# elements enclosed by {} from the corresponding value in the dictionary "config"
# cmd_list = ["ls {path}/{file}.{1}","cd {path}.{3}","cat {file}.{4}","od -x {4}.{file}"]
# config = {"path":"/home/user","file":"binfile",1:"img",3:"bin",4:"debug"}
#
# For Example:
# Input = "cat {file}.{4}", Output = "cat binfile.debug"
# Input = "ls {path}/{file}.{1}" Output = "ls /home/user/binfile.img"
##########################################################################################

# ASSUMPTIONS -
# 1. There are no nested key mappings
#    Example -  cat {file{path}}.{4}
# 2. Any command with key between '{' and '}' that is not present in the dictionary, will not be
#    replaced, but will still be a part of the command string
#    Example = Input - "cat {file}.{2}"; Output - "cat binfile.{2}"

# pre-defined mapping of commands and their corresponding values
config = {
          "path":"/home/user",
          "file":"binfile",
          1:"img",
          3:"bin",
          4:"debug"
          }

# Function to replace the keywords mentioned in argument command to their mappings declared in
# config dictionary
#
# Args :
#   cmd : raw string command
#   cmd : raw string replaced with their subsequent mapping
def convert_cmd_to_val(cmd):

    if not cmd:
        return None

    if cmd.count('{') == cmd.count('}') == 0:
        return cmd

    for command, mapping in config.items():

        cmd_index = cmd.find(str(command))
        len_of_cmd = len(str(command))

        if (cmd_index != -1) and \
            (cmd[cmd_index - 1] == '{') and \
            (cmd[cmd_index + len_of_cmd] == '}'):

            cmd = cmd.replace('{'+str(command)+'}', mapping)

    return cmd


if __name__ == '__main__':

    cmd_list = ["ls {path}/{file}.{1}", "cd {path}.{3}", "cat {file}.{4}", "od -x {4}.{file}"]

    result = []
    for cmd in cmd_list:
        converted_cmd_str = convert_cmd_to_val(cmd)
        result.append(converted_cmd_str)

    for index in range(len(cmd_list)):
        print("Raw String - " +cmd_list[index])
        print("After conversion - "+result[index], end="\n\n")