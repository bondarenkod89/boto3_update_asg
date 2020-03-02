import boto3
import argparse

parser = argparse.ArgumentParser(description='Change Auto Scaling Group parameters')
parser.add_argument('name', type=str, help='Input name Auto Scaling Group')
parser.add_argument('--min', type=int, dest='asg_minsize', help='The minimum number of instances the Auto Scaling group should have at any time.')
parser.add_argument('--max', type=int, dest='asg_maxsize', help='The maximum number of instances the Auto Scaling group should have at any time.')
parser.add_argument('--descap', type=int, dest='asg_descap', help='Specify the number of instances you want to run in this Auto Scaling group, as well as the minimum and maximum number of instances the Auto Scaling group should have at any time.')
args = parser.parse_args()

asgname = args.name
asgmin = args.asg_minsize
asgmax = args.asg_maxsize
asgdescap = args.asg_descap

def change_asgmin():
    client = boto3.client('autoscaling')
    group = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asgname])['AutoScalingGroups'][0]
    if group['MaxSize'] < asgmin:
        print("Max bound must be greater than or equal to min bound")
    else: 
        new = client.update_auto_scaling_group(
            AutoScalingGroupName = asgname,
            MinSize = asgmin)
        return new

def change_asgmax():
    client = boto3.client('autoscaling')
    new = client.update_auto_scaling_group(
        AutoScalingGroupName = asgname,
        MaxSize = asgmax)
    return new

def change_asgdescap():
    client = boto3.client('autoscaling')
    new = client.update_auto_scaling_group(
        AutoScalingGroupName = asgname,
        DesiredCapacity = asgdescap)
    return new

def get_autoscaling():
    client = boto3.client('autoscaling')
    group = client.describe_auto_scaling_groups(AutoScalingGroupNames=[asgname])['AutoScalingGroups'][0]
    print("Minimum number of instances: " + str(group['MinSize']), "\nMaximum number of instances: " + str(group['MaxSize']))
    print("Desired Capacity: " + str(group['MaxSize']))

if __name__ == "__main__":
    if args.asg_minsize:
        change_asgmin()
    if args.asg_maxsize:
        change_asgmax()
    if args.asg_descap:
        change_asgdescap()
    if args.name:
        get_autoscaling()
