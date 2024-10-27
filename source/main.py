import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        'args',
        help='Subprocess arguments to run after calling `pip-sync`. '
        'Args are called using `subprocess.run(<args>)`.',
        nargs='+',
    )
    parser.add_argument(
        '-r',
        '--requirement',
        type=str,
        help='Sync requirements from the given requirements file. '
        'Requirements are synced with `pip-sync <file>`.',
        default='requirements.txt',
        metavar='<file>',
    )
    args = parser.parse_args()

    if len(args.args) > 0:
        subprocess.run(['pip-sync', args.requirement], stderr=subprocess.STDOUT)
        try:
            subprocess.run(args.args, stderr=subprocess.STDOUT)
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Unable to run program '{args.args[0]}'. Is the program listed in '{args.requirement}'?"
            )


if __name__ == '__main__':
    main()
