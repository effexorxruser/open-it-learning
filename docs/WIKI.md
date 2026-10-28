# Publishing the GitHub Wiki / Публикация Wiki

[← Repository](../README.md) · [Wiki source pages](../wiki-source/Home.md)

The **real GitHub Wiki** lives in a separate Git repository, `effexorxruser/open-it-learning.wiki.git`. It is not a directory in the main repo.

The pages under `wiki-source/` are the reviewed public sources that will be synchronized to the real Wiki. The initial Wiki has not been created from this folder automatically.

## One-time activation

1. Open [Open IT Learning → Wiki](https://github.com/effexorxruser/open-it-learning/wiki).
2. Click **Create the first page**. Leave the title `Home`, enter `# Open IT Learning` and save.
3. Open [Actions → Publish GitHub Wiki](https://github.com/effexorxruser/open-it-learning/actions/workflows/publish-wiki.yml).
4. Click **Run workflow**, choose `main`, and run it.
5. Open the [Wiki](https://github.com/effexorxruser/open-it-learning/wiki) again. The full Home page, sidebar and the other pages should appear.

The first page must be created in GitHub's UI before the separate Wiki repository can be cloned. This manual action is unavoidable with the current GitHub connector, which has no Wiki page creation endpoint.

## Editing and maintenance

Canonical managed pages are:

- `wiki-source/Home.md`
- `wiki-source/_Sidebar.md`, `wiki-source/_Footer.md`
- `wiki-source/Catalog.md`, `wiki-source/Achievements.md`
- `wiki-source/Verification.md`, `wiki-source/Resources.md`
- `wiki-source/Contributing.md`, `wiki-source/Research-Journal.md`
- `wiki-source/Roadmap.md`

Edit these files through a normal GitHub Pull Request, review the diffs, merge to `main`, then manually rerun the **Publish GitHub Wiki** workflow.

The workflow copies *only* Markdown pages with these filenames and does not remove unrecognized Wiki files. **Changes to those managed pages made directly in the Wiki web editor will be overwritten the next time the workflow is run.** For durable edits, change `wiki-source/` instead.

The workflow is intentionally **manual**, not triggered by every push. That prevents surprise publication when documentation is being drafted.

## Authorization and troubleshooting

The workflow uses GitHub's ephemeral `GITHUB_TOKEN` with `contents: write` scoped to the repository. It does not need a manually stored token. If GitHub rejects the Wiki push due to repository or organization policy, inspect the workflow log for `403` or access-denied errors; do **not** add personal API keys to files. Check that Actions and the Wiki are enabled and that the workflow has the necessary repository permissions.

To review and edit the Wiki locally after initialization (optional):

```bash
git clone https://github.com/effexorxruser/open-it-learning.wiki.git
```

Remember: this local clone is the **Wiki repository**, not the main project repository.

## Editorial scope

Wiki documents course selection, official reward types, source verification, public prompts, skills, roadmap and accessible research notes. It does **not** document private API keys, internal model routing, unpublished data or the maintainer's agent-development environment.
