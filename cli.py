import argparse
import os

def main():
     parser = argparse.ArgumentParser()
     
     commands = parser.add_subparsers(dest="command")
     commands.required = True

     init_parser = commands.add_parser("init")
     init_parser.add_argument("path", nargs="?", default=os.getcwd())

     hash_object_parser = commands.add_parser('hash-object')
     hash_object_parser.add_argument('file',nargs="?",help="Get hash for content for this file")
     hash_object_parser.add_argument('-w',required=False,action="store_true",help="Write it in the repository")
     hash_object_parser.add_argument('-t',required=False,action="store",choices=["blob","tree","commit"],help="Type of hash")
     hash_object_parser.add_argument('-stdin',required=False,action="store_true",help="Read content from standard in")

     cat_file_parser = commands.add_parser("cat-file")
     cat_file_parser.add_argument('hash')
     
     ARGS = parser.parse_args()
     
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

def cmd_init(ARGS):
     if not os.path.exists(ARGS.path):
          raise Exception(f"the following path does not exists: {ARGS.path}")
     elif not os.path.isdir(ARGS.path): 
          raise Exception(f"the given path is not a directorypip : {ARGS.path}")
     elif os.path.exists(os.path.join(ARGS.path,".cgit")) and os.path.isdir(os.path.join(ARGS.path,".cgit")):
          raise Exception(f"the given path already a cgit repository")
     repo_path=os.path.join(ARGS.path,".cgit")
     os.makedirs(os.path.join(repo_path,"objects","refs"),exist_ok=True)
     print(f"Initialized empty cgit repository in {repo_path}")

def cmd_hash_object(ARGS):
     with open(ARGS.file,"rb") as f:
          data = f.read()
     print(cgm.hash_object(data))

def cat_file(ARGS):
     print(cgm.cat_file(ARGS.hash))

if __name__ == '__main__':
     main()