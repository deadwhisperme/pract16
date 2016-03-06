# pract16
import argparse 
import sys 
parser = argparse.ArgumentParser( 
    description='Calc' 
) 
parser.add_argument( 
    'values', 
    metavar='VALUES', 
    type=float, 
    nargs=2, 
    help='data' 
) 
parser.add_argument( 
    '-a', 
    '--action', 
    nargs=1,
    metavar='SIGN', 
    help='sign' 
) 
parser.add_argument( 
    '-v', 
    '--verbose', 
    action='store_true', 
    help='result' 
    ) 
args = parser.parse_args() 
if not args.action[0] in  ['+', '-', '*', '/']: 
    print(  
     'incorrect sign' 
    ) 
    sys.exit(-1) 

if args.action[0] == '+': 
    result = float(args.values[0]) + float(args.values[1]) 
elif args.action[0] == '-': 
    result = float(args.values[0]) - float(args.values[1]) 
elif args.action[0] == '*': 
    result = float(args.values[0]) * float(args.values[1]) 
elif args.action[0] == '/': 
    result = float(args.values[0]) / float(args.values[1]) 
 
print('Result', result) 
