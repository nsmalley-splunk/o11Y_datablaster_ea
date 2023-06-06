import sys
import subprocess
cmd_kill_1 = "pkill -9 -f \"/home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/itsi_ea_workshop_good_mix.yaml\""
cmd_kill_2 = "pkill -9 -f \"/home/centos/o11Y_datablaster_ea/eventgen-linux-amd64 generate /home/centos/o11Y_datablaster_ea/itsi_ea_workshop_bad_mix.yaml\""
cmd_1 = "nohup /home/ubuntu/o11y_base_core_ea/eventgen-linux-amd64 -c /home/ubuntu/o11y_base_core_ea/itsi_ea_workshop_bad_mix.yaml &"
cmd_2 = "nohup /home/ubuntu/o11y_base_core_ea/eventgen-linux-amd64 -c /home/ubuntu/o11y_base_core_ea/itsi_ea_workshop_good_mix.yaml &"

def main(args):
    if len(args) != 1:
        print("Incorrect arguments")
        return

    if args[0] == "on":
        subprocess.run(cmd_kill_1, shell=True)
        subprocess.run(cmd_kill_2, shell=True)
        subprocess.run(cmd_1, shell=True)
        print("Bad Events Turned On")
    elif args[0] == "off":
        subprocess.run(cmd_kill_2, shell=True)
        subprocess.run(cmd_kill_1, shell=True)
        subprocess.run(cmd_2, shell=True)
        print("Bad Events Turned Off")
    else:
        print("Invalid argument")

if __name__ == "__main__":
    main(sys.argv[1:])

