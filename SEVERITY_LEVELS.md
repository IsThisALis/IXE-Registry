# Severity Levels

## S1 — Critical
**Definition:** Complete system failure, data loss, or fundamental component breakdown.

**Criteria (at least ONE must be true):**
- Application crashes on startup or during normal operation
- Core engine component is completely non-functional out of the box
- Native memory leak that exhausts RAM during runtime (not on exit)
- Data corruption or loss of user saves/configs
- Security vulnerability allowing remote code execution
- Infinite loop that hangs the process permanently

**Examples:**
- Camera.update() throws NPE immediately — cannot render any scene
- AssetManager fails to load textures, returns null buffer, crashes renderer
- Shader compilation error prevents entire rendering pipeline from working

---

## S2 — Major
**Definition:** Significant functionality is broken, but workaround exists or impact is limited.

**Criteria (at least ONE must be true):**
- Feature broken, but can be bypassed with manual intervention
- Memory leak that occurs only on application exit (OS reclaims memory anyway)
- Incorrect rendering output (visual artifacts, wrong colors)
- Performance degradation noticeable to user (30+ FPS drop)
- Non-critical exception thrown but caught and logged (no crash)

**Examples:**
- Engine cleanup not executing after user's cleanup() throws exception
- Texture loads upside down without flag to fix it
- Shader uniform not updating until next frame

---

## S3 — Minor
**Definition:** Small bugs, cosmetic issues, or minor inconveniences.

**Criteria (at least ONE must be true):**
- Visual glitch that doesn't affect functionality
- Incorrect log message or error formatting
- Minor API inconsistency (e.g., method naming doesn't follow convention)
- Performance issue only on very specific hardware/configurations
- Documentation doesn't match actual behavior

**Examples:**
- Log message shows wrong line number
- FPS counter displays 0 on first frame
- Method name typo in deprecated API

---

## S4 — Cosmetic / Chore
**Definition:** Code quality improvements, refactoring, documentation fixes.

**Criteria (at least ONE must be true):**
- Code refactoring with no functional change
- Documentation update or typo fix
- Dependency version bump
- Code style/formatting improvements
- Adding comments or JavaDoc

**Examples:**
- Renaming internal variable for clarity
- Updating README with new API examples
- Migrating from deprecated LWJGL methods
