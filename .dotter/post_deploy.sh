#!/bin/sh
# Post-deploy: link ~/.config/opencode/skill + ~/.config/codex/skills → ~/.config/agents/skills

AGENTS_DIR="$HOME/.config/agents/skills"
OPENCODE_LINK="$HOME/.config/opencode/skill"
CODEX_HOME="$HOME/.config/codex"
CODEX_LINK="$CODEX_HOME/skills"

if [ -d "$AGENTS_DIR" ]; then
  safe_link() {
    link_path="$1"
    target_path="$2"
    mkdir -p "$(dirname "$link_path")"
    if [ -e "$link_path" ] && [ ! -L "$link_path" ]; then
      rm -rf "$link_path"
    fi
    ln -sfn "$target_path" "$link_path"
  }

  safe_link "$OPENCODE_LINK" "$AGENTS_DIR"
  safe_link "$CODEX_LINK" "$AGENTS_DIR"
fi
