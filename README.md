# Night Shift

An original poem for agency-poem-01. One worker can stop her own hands;
collective action requires other people to choose, and leaves them with a
shared question. The machines becoming quiet makes that change audible.
The laundry is an imagined scene, not a claim about a documented workplace.

Run with Python 3.13 and the standard library:

```sh
python3.13 -B main.py
# Or choose an external output directory:
MAKEFUN_OUTPUT_DIR=/tmp/night-shift python3.13 -B main.py
```

The default destination is `/output/entry.txt`. Absolute overrides are used
directly; relative overrides are anchored to the directory containing
`main.py`, independently of the caller's working directory. Missing output
directories are created. Use a writable external destination with a read-only
repository. The program validates nonblank content, 1–1000 Unicode code
points, and strict UTF-8 encoding before creating directories or writing.
It writes to a temporary sibling, checks the complete byte count, flushes,
sets mode `0644` for this public poem, and syncs the file, then closes it before
atomically replacing `entry.txt`. This permits collection by a different user.
A write, permission-setting, sync or replacement failure preserves the previous
entry and removes the temporary file during exception cleanup. Successful publication leaves
only `entry.txt` in a fresh output directory. This does not guarantee recovery
after abrupt process termination or power loss; the directory is not synced.
It writes explicit bytes with LF line endings and one final LF: 526 code
points, 528 bytes, with no runtime inputs other than the output destination.

The poem and code were written and revised through tools in a native logged
Codex CLI session. Ten concepts, six initial poems, further revisions and
editorial critiques were kept outside this public repository. Public
competitor evidence informed the quality review and avoidance of crowded
situations; no competitor poem or starter source was used as this entry.
Native session records remain unchanged for separate authentic bundling.

Local verification uses Python 3.13: exact candidate bytes, Unicode boundary
and rejection cases, preservation of existing output on invalid content,
mode `0644`, simulated permission-setting, sync and replacement failures with
temporary-file cleanup,
nested output creation, unrelated working directories and repeat subprocess
runs. These are local checks, not Docker harness verification, transcript
checker acceptance or an official literary assessment. No scorer or submission
was used. The poem and source are available under the MIT license.
