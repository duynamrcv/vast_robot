import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.io

if __name__ == "__main__":
    teb = scipy.io.loadmat('/home/duynam/vast_ws/src/vast_robot/vast_navigation/data/teb.mat')['ans']
    mpc = scipy.io.loadmat('/home/duynam/vast_ws/src/vast_robot/vast_navigation/data/ref.mat')['ans']
    ref = scipy.io.loadmat('/home/duynam/vast_ws/src/vast_robot/vast_navigation/data/ref1.mat')['ans']
    # print(len(ref))
    # print(np.diff(mpc, axis=0))
    # print(len(teb))

    plt.figure()
    plt.plot(np.array(ref)[:,0], np.array(ref)[:,1], '-b', linewidth=2, label='ref')
    plt.plot(np.array(teb)[:,0], np.array(teb)[:,1], '-r', linewidth=2, label='TEB')
    plt.plot(np.array(mpc)[:,0], np.array(mpc)[:,1], '--k', linewidth=2, label='NMPC')
    plt.legend()
    plt.title("Navigation: Tracked path")
    plt.xlabel("x [m]")
    plt.ylabel("y [m]")
    plt.grid(True)
    plt.show()

    dif_teb = np.diff(teb, axis=0)
    teb_path = np.sum(np.hypot(dif_teb[:,0], dif_teb[:,1]))

    dif_mpc = np.diff(mpc, axis=0)
    mpc_path = np.sum(np.hypot(dif_mpc[:,0], dif_mpc[:,1]))

    dif_ref = np.diff(ref, axis=0)
    ref_path = np.sum(np.hypot(dif_ref[:,0], dif_ref[:,1]))

    print(teb_path)
    print(mpc_path)
    print(ref_path)