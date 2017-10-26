import os
import shutil
import sys

AIRSIM_DIR = './AirSim/'
AIRLIB_PKG_NAME = 'airlib_catkin'
RPC_PKG_NAME = 'rpc_catkin'
MAVLINKCOM_PKG_NAME = 'mavlinkcom_catkin'


def main(argv):
    if len(argv) < 2:
        print("Please provide the catkin workspace location")
        return
    catkin_ws = argv[1]
    if not catkin_ws[-1:] == '/':
        catkin_ws += '/'
    catkin_src_dir = catkin_ws + 'src/'
    transform_airlib(catkin_src_dir)
    transform_mavlinkcom(catkin_src_dir)
    transform_rpc(catkin_src_dir)


def move_folders(orig_src_dir, catkin_src_dir, pkg_name, folders, display_name):
    print("***** COPYING %s *****" % display_name)
    pkg_dir = catkin_src_dir + pkg_name + "/"
    if not os.path.exists(pkg_dir):
        print("Directory \"" + pkg_name + "\" does not exists in the catkin workspace src folder."
                                               " Please clone the correct repository from GitHub before continuing.")
        return
    for source, target in folders:
        copy_dir(orig_src_dir + source, pkg_dir + target)
    print("***** %s COMPLETED *****" % display_name)
    print("")


def transform_airlib(catkin_src_dir):
    folders = [
        ("AirLib/include", "include"),
        ("AirLib/src", "src")
    ]
    move_folders(AIRSIM_DIR, catkin_src_dir, AIRLIB_PKG_NAME, folders, "AIRLIB")


def transform_mavlinkcom(catkin_src_dir):
    folders = [
        ("MavLinkCom/common_utils", "common_utils"),
        ("MavLinkCom/mavlink", "mavlink"),
        ("MavLinkCom/src", "src"),
        ("MavLinkCom/include", "include"),
    ]
    move_folders(AIRSIM_DIR, catkin_src_dir, MAVLINKCOM_PKG_NAME, folders, "MAVLINKCOM")


def transform_rpc(catkin_src_dir):
    folders = [
        ("external/rpclib/include", "include"),
        ("external/rpclib/lib", "lib"),
        ("external/rpclib/dependencies", "dependencies"),
    ]
    move_folders(AIRSIM_DIR, catkin_src_dir, RPC_PKG_NAME, folders, "RPC")


def makedir_ifnotexists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def copy_dir(source, target):
    if os.path.exists(target):
        print("Target at " + target + " already exists... Removing...")
        shutil.rmtree(target)
    sys.stdout.write("Copying from " + source + " to " + target)
    sys.stdout.flush()
    shutil.copytree(source, target)
    print(" Done!")


main(sys.argv)
