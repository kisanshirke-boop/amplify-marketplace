# amplify-marketplace

Private Claude Code plugin marketplace for the **Amplify AI Build Studio** rails.
Publish this folder as its own GitHub repository (for example `<your-org>/amplify-marketplace`).

| Path | What it is |
|---|---|
| `.claude-plugin/marketplace.json` | Marketplace catalogue (one plugin: `amplify`) |
| `plugins/amplify/.claude-plugin/plugin.json` | Plugin manifest – the strategy guide calls it *opm-amplify*; the plugin name is `amplify` so commands appear as `/amplify:…` |
| `plugins/amplify/commands/` | The approved prompt library as slash commands (`/amplify:intent`, `/amplify:spec`, …) |
| `plugins/amplify/agents/verifier.md` | Independent, read-only verifier subagent |
| `plugins/amplify/skills/opm-web-standards/` | Permitted technology, security & privacy, delivery and UX rules + brand tokens |
| `plugins/amplify/hooks/` | `protect_paths.py` (Gate G4, fails closed), `log_activity.py` (evidence), `selftest_hook.py` |

## How projects get it

Every repository created by the Studio contains `.claude/settings.json` with:

```json
"extraKnownMarketplaces": { "amplify-marketplace": { "source": { "source": "github", "repo": "<your-org>/amplify-marketplace" } } },
"enabledPlugins": { "amplify@amplify-marketplace": true }
```

When the developer trusts the project folder in Claude Code, the marketplace is added and the plugin is offered for install.

## Changing the rails

Changes are made by pull request in this repository, reviewed by the platform team (Gate G4), then released by raising
`version` in both `plugin.json` and `marketplace.json`. Test the hooks with `python plugins/amplify/hooks/selftest_hook.py`.
