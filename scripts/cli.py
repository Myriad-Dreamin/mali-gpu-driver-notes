
import argparse
import subprocess


class EntryPoint(object):
    def __init__(self):
        self.args = None

    def exec(self, cmd):
        proc = subprocess.Popen(cmd,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.STDOUT)

        for line in iter(proc.stdout.readline, b''):
            print(line.rstrip().decode())

    def listen_wiki(self):
        return self.exec('wt.exe tiddlywiki.cmd wiki --listen host=0.0.0.0'.split())


if __name__ == '__main__':

    entry = argparse.ArgumentParser()
    ep = EntryPoint()
    sp = entry.add_subparsers()

    listen_cmd = sp.add_parser('listen')
    listen_cmd.set_defaults(func=ep.listen_wiki)

    args = entry.parse_args()
    cmd = args.func

    if cmd:
        ep.args = args
        cmd()
    else:
        entry.print_help()
