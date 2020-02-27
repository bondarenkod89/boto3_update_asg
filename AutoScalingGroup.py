import boto3
import argparse
import sys

parser = argparse.ArgumentParser(description='Change Auto Scaling Group parameters')
parser.add_argument('name', type=str, help='Input name Auto Scaling Group')
parser.add_argument('--min', type=int, dest='asg_minsize', help='The minimum number of instances the Auto Scaling group should have at any time.')
parser.add_argument('--max', type=int, dest='asg_mmaxsize', help='The maximum number of instances the Auto Scaling group should have at any time.')
parser.add_argument('--descap', type=int, dest='asg_descap', help='Specify the number of instances you want to run in this Auto Scaling group, as well as the minimum and maximum number of instances the Auto Scaling group should have at any time.')
args = parser.parse_args()

asgname = args.name
asgmin = args.asg_minsize
asgmax = args.asg_mmaxsize
asgdescap = args.asg_descap

def change_autoscaling():
    client = boto3.client('autoscaling')
    new =  client.update_auto_scaling_group(
        AutoScalingGroupName = asgname,
        MinSize = asgmin,
        MaxSize = asgmax,
        DesiredCapacity = asgdescap)
    return new

change_autoscaling()