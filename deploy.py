import subprocess
import datetime
import sys

def run_command(command):
    """Utility to run shell commands and print output."""
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True, encoding='utf-8')
    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        return False
    print(result.stdout)
    return True

def deploy():
    print("Starting One-Click Deployment Pipeline...")
    
    # 1. Run the static export script
    if not run_command("python export_static.py"):
        print("Static export failed. Deployment halted.")
        return

    # 2. Add all changes to Git
    if not run_command("git add ."):
        print("Git add failed.")
        return

    # 3. Create a commit with a timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"Site Update: {timestamp}"
    if not run_command(f'git commit -m "{commit_msg}"'):
        print("Warning: No changes to commit or commit failed.")
        # If no changes, we can still try to push if needed, but usually we stop here.
        # But we'll continue to push just in case the remote is behind.
    
    # 4. Push to GitHub
    if not run_command("git push origin master"):
        print("Git push failed. Ensure you have internet access and SSH/Auth set up.")
        return

    print("\nDeployment Successful! Your updates should be live at neoscona.xyz shortly.")

if __name__ == "__main__":
    deploy()
