#!/usr/bin/env python3

import argparse
import hashlib
import os
import sys

def printerr(text:str,error_code:int=1) -> None:
     print(text,file=sys.stderr)
     exit(error_code)

def main():
     parser = argparse.ArgumentParser()
     
     commands = parser.add_subparsers(dest="command")
     commands.required = True

     init_parser = commands.add_parser("init")
     init_parser.add_argument("path", nargs="?", default=os.getcwd())

     hash_object_parser = commands.add_parser('hash-object')
     hash_object_parser.add_argument('file',nargs="?",help="Get hash for content for this file")
     hash_object_parser.add_argument('-w',required=False,action="store_true",help="Write it in the repository")
     hash_object_parser.add_argument('-t',required=False,action="store",choices=["blob","tree","commit"],help="Type of hash",default="blob")
     hash_object_parser.add_argument('-stdin',required=False,action="store_true",help="Read content from standard in")

     find_root_parser = commands.add_parser("find-root")

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
          # custom commands
          case "find-root"    : cmd_find_root(ARGS)
          case _              : printerr("Bad cgit command.")

def cmd_add(): pass
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

def util_find_root() -> str|None:
     current_directory=os.path.realpath(".")
     parent_directory = os.path.realpath(os.path.join(current_directory,".."))
     while current_directory != parent_directory:
          if os.path.isdir(os.path.join(current_directory,".cgit")):
               return current_directory
          current_directory = parent_directory
          parent_directory = os.path.realpath(os.path.join(current_directory,".."))
     return None

def cmd_find_root(ARGS:argparse.Namespace) -> None:
     print(util_find_root())

def cmd_init(ARGS:argparse.Namespace):
     if not os.path.exists(ARGS.path):
          printerr(f"the following path does not exists: {ARGS.path}")
     elif not os.path.isdir(ARGS.path): 
          printerr(f"the given path is not a directorypip : {ARGS.path}")
     elif os.path.exists(os.path.join(ARGS.path,".cgit")) and os.path.isdir(os.path.join(ARGS.path,".cgit")):
          printerr(f"the given path already a cgit repository")
     repo_path=os.path.join(ARGS.path,".cgit")
     os.makedirs(os.path.join(repo_path,"objects"),exist_ok=True)
     os.makedirs(os.path.join(repo_path,"refs"),exist_ok=True)
     print(f"Initialized empty cgit repository in {repo_path}")

def cmd_hash_object(ARGS):
     if ARGS.stdin:
          content = input().encode()
     else:
          with open(ARGS.file,"rb") as f:
               content = f.read()
     content = ARGS.t.encode() + b'\x00' + content
     sha1_hash = hashlib.sha1(content).hexdigest()
     if ARGS.w:
          repo_root = util_find_root()
          if repo_root:
               sha_dir = os.path.join(repo_root,".cgit","ref",sha1_hash[:2])
               sha_file = os.path.join(repo_root,".cgit","ref",sha1_hash[:2],sha1_hash[2:])
          else:
               printerr("current dir is not a cgit repository")
          
          os.makedirs(sha_dir,exist_ok=True)
          with open(sha_file,"wb") as f:
               f.write(content)
     
     print(sha1_hash)

def cmd_cat_file(ARGS:argparse.Namespace) -> None:
     pass

if __name__ == '__main__':
     main()