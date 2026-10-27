#!/usr/bin/env bash
set -e

# ==============================================================================
# Tea & Coffee Master Skill - Linux / macOS One-Click Installer for Gemini / Antigravity
# ==============================================================================

SKILL_NAME="tea-coffee-master"
TARGET_DIR="$HOME/.gemini/config/skills/$SKILL_NAME"
REPO_URL="https://github.com/BugMaker123/tea-coffee-master.git"

echo -e "\033[0;36m>>> [1/3] Checking target directory: $TARGET_DIR\033[0m"

if [ -d "$TARGET_DIR" ]; then
    echo -e "\033[0;33m>>> Updating existing skill directory...\033[0m"
    cd "$TARGET_DIR"
    if [ -d ".git" ]; then
        git pull origin main
    else
        echo "Removing old non-git directory..."
        rm -rf "$TARGET_DIR"
        git clone "$REPO_URL" "$TARGET_DIR"
    fi
else
    echo -e "\033[0;36m>>> [2/3] Cloning skill repository...\033[0m"
    mkdir -p "$(dirname "$TARGET_DIR")"
    git clone "$REPO_URL" "$TARGET_DIR"
fi

echo -e "\033[0;32m>>> [3/3] Installation successful!\033[0m"
echo -e "\033[0;32m---------------------------------------------------------\033[0m"
echo -e "\033[0;32mSkill 'tea-coffee-master' is now installed and active!\033[0m"
echo -e "\033[0;32mLocation: $TARGET_DIR\033[0m"
echo -e "\033[0;32mYou can now ask Gemini / Antigravity to make tea or coffee recipes!\033[0m"
echo -e "\033[0;32m---------------------------------------------------------\033[0m"
