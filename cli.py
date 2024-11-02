import argparse
import os
import cgit_main as cgm

def main():
     parser = argparse.ArgumentParser()
     
     commands = parser.add_subparsers(dest="command")
     commands.required = True

     init_parser = commands.add_parser("init")
     init_parser.add_argument("path", nargs="?", default=os.getcwd())

     hash_object_parser = commands.add_parser('hash-object')
     hash_object_parser.add_argument('file')

     cat_file_parser = commands.add_parser("cat-file")
     cat_file_parser.add_argument('hash')
     
     ARGS = parser.parse_args()

     print(ARGS.path)
     exit(0)
     
     match ARGS.command:
        case "add"          : cmd_add(ARGS)
        case "cat-file"     : cmd_cat_file(ARGS)
        case "check-ignore" : cmd_check_ignore(ARGS)
        case "checkout"     : cmd_checkout(ARGS)
        case "commit"       : cmd_commit(ARGS)
        case "hash-object"  : cmd_hash_object(ARGS)
        case "init"         : cmd_init(ARGS)
        case "log"          : cmd_log(ARGS)
        case "ls-files"     : cmd_ls_files(ARGS)
        case "ls-tree"      : cmd_ls_tree(ARGS)
        case "rev-parse"    : cmd_rev_parse(ARGS)
        case "rm"           : cmd_rm(ARGS)
        case "show-ref"     : cmd_show_ref(ARGS)
        case "status"       : cmd_status(ARGS)
        case "tag"          : cmd_tag(ARGS)
        case _              : raise Exception("Bad cgit command.")

def cmd_add(): pass
def cmd_cat_file(): pass
def cmd_check_ignore(): pass
def cmd_checkout(): pass
def cmd_commit(): pass
def cmd_log(): pass
def cmd_ls_files(): pass
def cmd_ls_tree(): pass
def cmd_rev_parse(): pass
def cmd_rm(): pass
def cmd_show_ref(): pass
def cmd_status(): pass
def cmd_tag(): pass

def cmd_init():
     os.makedirs(".cgit",exist_ok=True)
     os.makedirs(".cgit/objects/refs",exist_ok=True)
     print(f"Initialized empty cgit repository in {os.getcwd()}/{cgm.GIT_DIR}")

def cmd_hash_object():
     with open(ARGS.file,"rb") as f:
          data = f.read()
     print(cgm.hash_object(data))

def cat_file():
     print(cgm.cat_file(ARGS.hash))

if __name__ == '__main__':
     main()