#!/usr/bin/env python3
import os
import subprocess
import sys

DRIVE = "/dev/sr0"

def get_folder():
    while True:
        raw_path = input("\nDrag and drop folder here (or enter path): ").strip("'\" ")
        folder_path = os.path.expanduser(raw_path)
        if os.path.isdir(folder_path):
            return folder_path
        print("❌ Invalid directory. Please try again.")

def burn_cd():
    folder = get_folder()
    print(f"\n🔥 Burning to CD using cdrecord...")
    cmd = f'mkisofs -J -R "{folder}" | cdrecord -v dev={DRIVE} -'
    subprocess.run(cmd, shell=True)

def burn_dvd_bd():
    folder = get_folder()
    label = input("Enter disc label [default: MY_DISC]: ").strip() or "MY_DISC"
    print(f"\n🔥 Burning to DVD/Blu-ray using growisofs...")
    subprocess.run(["growisofs", "-Z", DRIVE, "-J", "-R", "-V", label, folder])

def eject_disc():
    print(f"\n⏏️ Ejecting {DRIVE}...")
    subprocess.run(["eject", DRIVE])

def main():
    while True:
        print("\n" + "=" * 32)
        print("      DISC BURNER UTILITY       ")
        print("=" * 32)
        print("1. Burn Folder to CD")
        print("2. Burn Folder to DVD / Blu-ray")
        print("3. Eject Disc")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()

        if choice == "1":
            burn_cd()
        elif choice == "2":
            burn_dvd_bd()
        elif choice == "3":
            eject_disc()
        elif choice == "4":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("❌ Invalid choice. Enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

