# ll

A hinge between a signed-in Gemini Notebook and a public GitHub shelf.

The notebook stays closed from this side. GitHub stays the face that can be imported.

## The two directions

Forward. A file on `main` in this public repo has a raw URL. Gemini Notebook imports that URL as a web source. It takes the text of the page. It does not take images, and it does not follow links into other files. Each file is its own source.

Return. Notes leave the notebook only when they are pasted or exported. They land in `return/` and are committed. This repo cannot pull notebook `911dd39c-9e99-4d12-94f9-9e6ae130f88a`.

## Paste these into the notebook

Add source, then Web URL, one at a time:

- https://raw.githubusercontent.com/snowphamtom/ll/main/sources/HINGE.md
- https://raw.githubusercontent.com/snowphamtom/ll/main/sources/CAPS.md

The share that opened this work is https://notebooklm.link.google/vQvHB2dHGylz. It still requires a Google sign-in. Its sources were not readable from here, and they are not invented in this repo.

## What this is not

Not a NotebookLM API. Not a push into the notebook. Not a sync. A raw URL is a snapshot until someone deletes the source and adds it again. Drive files sync. GitHub web sources do not.

Private repos stay off this shelf. A private raw URL does not resolve for NotebookLM.

MAGPIE stays 19/658,750 pending. This hinge is not a filing.
