#!/bin/sh
# Post-deploy: link ~/.config/opencode/skill → ~/.config/agents/skills

AGENTS_DIR="$HOME/.config/agents/skills"
OPENCODE_LINK="$HOME/.config/opencode/skill"

if [ -d "$AGENTS_DIR" ]; then
  mkdir -p "$(dirname "$OPENCODE_LINK")"
  ln -sfn "$AGENTS_DIR" "$OPENCODE_LINK"
  echo "Linked: $OPENCODE_LINK → $AGENTS_DIR"
fi
