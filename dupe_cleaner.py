import os
import hashlib
import shutil
from collections import defaultdict
from datetime import datetime

def get_file_hash(path):
    """Reads only the first 1KB. Safe and read-only for hashing."""
    try:
        with open(path, 'rb') as f: # READ ONLY
            chunk = f.read(1024)
            return hashlib.md5(chunk).hexdigest()
    except:
        return None

def main():
    print("--- DUPLICATE INTELLIGENCE SUITE (CLEANER) ---")
    main_folder = input("Paste the folder path to CLEAN UP and press Enter: ").strip().strip('"')
    
    if not os.path.exists(main_folder):
        print(f"ERROR: The path '{main_folder}' does not exist.")
        return

    # Determine Recovery Folder (Located right next to the scanned folder)
    parent_dir = os.path.dirname(main_folder)
    folder_name = os.path.basename(main_folder.rstrip('\\/'))
    recovery_base = os.path.join(parent_dir, f"RECOVERY_{folder_name}")

    if not os.path.exists(recovery_base):
        os.makedirs(recovery_base)

    report_path = os.path.join(os.path.expanduser("~"), "Desktop", f"CLEANUP_REPORT_{folder_name}.txt")
    file_groups = defaultdict(list)
    
    print(f"\nPhase 1: Scanning EVERYTHING in {main_folder}...")
    for root, _, files in os.walk(main_folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                size = os.path.getsize(path)
                f_hash = get_file_hash(path)
                if f_hash:
                    file_groups[(size, f_hash)].append(path)
                    if len(file_groups) % 100 == 0:
                        print(f"Indexing files... {len(file_groups)} groups found so far.")
            except:
                continue

    # Identify duplicates
    duplicates = {k: v for k, v in file_groups.items() if len(v) > 1}
    
    if not duplicates:
        print("No duplicates found. Your folders are already clean!")
        return

    print(f"Phase 2: Moving duplicates to {recovery_base}...")
    
    moved_count = 0
    total_freed_bytes = 0

    with open(report_path, 'w', encoding='utf-8') as report:
        report.write(f"CLEANUP ACTION REPORT - {datetime.now()}\n")
        report.write(f"SOURCE FOLDER: {main_folder}\n")
        report.write(f"RECOVERY FOLDER: {recovery_base}\n")
        report.write("=" * 60 + "\n\n")

        for i, ((size, f_hash), paths) in enumerate(duplicates.items(), 1):
            master_file = paths[0]
            dupes_to_move = paths[1:]
            
            report.write(f"[GROUP {i}] MASTER KEPT: {master_file}\n")
            
            for d_path in dupes_to_move:
                if not os.path.exists(master_file):
                    report.write(f"  !! SAFETY SKIP: Master copy missing, skipping move for: {d_path}\n")
                    continue

                try:
                    file_name = os.path.basename(d_path)
                    timestamp = datetime.now().strftime("%H%M%S")
                    dest_name = f"Group{i}_{timestamp}_{file_name}"
                    dest_path = os.path.join(recovery_base, dest_name)
                    
                    shutil.move(d_path, dest_path)
                    
                    report.write(f"  -> MOVED: {d_path}\n")
                    moved_count += 1
                    total_freed_bytes += size
                except Exception as e:
                    report.write(f"  -> ERROR MOVING {d_path}: {e}\n")
            report.write("-" * 60 + "\n")

        report.write(f"\nTOTAL FILES MOVED: {moved_count}\n")
        report.write(f"TOTAL SPACE REMOVED FROM SOURCE: {total_freed_bytes / (1024**3):.2f} GB\n")

    print(f"\nSUCCESS! {moved_count} duplicates moved.")
    print(f"Report: CLEANUP_REPORT_{folder_name}.txt is on your Desktop.")
    input("\nPress Enter to close...")

if __name__ == "__main__":
    main()