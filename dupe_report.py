import os
import hashlib
from collections import defaultdict

def get_file_hash(path):
    """Reads only the first 1KB. Safe and fast."""
    try:
        with open(path, 'rb') as f: # READ ONLY
            chunk = f.read(1024)
            return hashlib.md5(chunk).hexdigest()
    except:
        return None

def main():
    print("--- DUPLICATE INTELLIGENCE SUITE (SCANNER) ---")
    main_folder = input("Paste the folder path here and press Enter: ").strip().strip('"')
    
    if not os.path.exists(main_folder):
        print(f"ERROR: The path '{main_folder}' does not exist.")
        return

    # Automatically name the report based on the folder name
    folder_name = os.path.basename(main_folder.rstrip('\\/'))
    if not folder_name: # Handle drive roots like D:\
        folder_name = "Drive_Root"
        
    report_filename = f"{folder_name}_dupe_report.txt"
    report_path = os.path.join(os.path.expanduser("~"), "Desktop", report_filename)

    file_groups = defaultdict(list)
    total_files = 0

    print(f"\nScanning: {main_folder}...")

    for root, _, files in os.walk(main_folder):
        for name in files:
            path = os.path.join(root, name)
            try:
                size = os.path.getsize(path)
                f_hash = get_file_hash(path)
                if f_hash:
                    file_groups[(size, f_hash)].append(path)
                    total_files += 1
                    if total_files % 100 == 0:
                        print(f"Scanned {total_files} files so far...")
            except:
                continue

    duplicates = {k: v for k, v in file_groups.items() if len(v) > 1}
    total_wasted_space = 0

    with open(report_path, 'w', encoding='utf-8') as report:
        report.write(f"DUPLICATE REPORT FOR: {main_folder}\n")
        report.write("=" * 50 + "\n\n")

        for i, ((size, f_hash), paths) in enumerate(duplicates.items(), 1):
            total_wasted_space += (len(paths) - 1) * size
            report.write(f"[GROUP {i}] - Size: {size / (1024*1024):.2f} MB\n")
            for p in paths:
                report.write(f"  -> {p}\n")
            report.write("-" * 50 + "\n")
            
        report.write(f"\nPotential Space to Save: {total_wasted_space / (1024**3):.2f} GB\n")

    print(f"\nSUCCESS! Found {len(duplicates)} duplicate groups.")
    print(f"Report saved to Desktop as: {report_filename}")
    input("\nPress Enter to close...")

if __name__ == "__main__":
    main()