# Contributing to DeepThinner

Thanks for your interest in contributing to DeepThinner!

## Reporting Bugs

- Use the **Bug Report** issue template
- Include your Nuke version, OS, and compiler version
- Describe the deep data you're working with (renderer, approximate sample counts)
- If possible, attach a minimal .nk script that reproduces the issue

## Feature Requests

- Use the **Feature Request** issue template
- Describe the problem you're trying to solve, not just the solution
- Example deep data or screenshots are always helpful

## Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-improvement`
3. Make your changes in `src/DeepThinner.cpp`
4. Test against Nuke 16 on at least one platform
5. Verify that existing thinning passes still work correctly
6. Submit a pull request with a clear description of the change

### Code Style

- Follow the existing style in `DeepThinner.cpp`
- Use `_camelCase` for member variables
- Use `camelCase` for local variables
- Keep the pass structure consistent (check alive, process, update alive)
- Add tooltips for any new knobs

### Build Testing

Please confirm your changes compile cleanly on at least one of:

- Windows: Visual Studio 2022 + Nuke 16 NDK
- Linux: GCC 9+ + Nuke 16 NDK
- macOS: Xcode 12+ + Nuke 16 NDK

## Adding a New Pass

If you're adding a new thinning pass:

1. Add member variables for the knobs (with sensible defaults)
2. Add knobs in a new `BeginGroup`/`EndGroup` block
3. Wire up `knob_changed` for enable/disable toggling
4. Add the pass in `doDeepEngine` between the existing passes (order matters)
5. Update the Artist Guide and Technical Notes text
6. Update `README.md` and `NUKEPEDIA.md`
