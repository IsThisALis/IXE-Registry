# Component Categories

| Tag | Name | Description | Examples |
|-----|------|-------------|----------|
| `[MEM]` | Memory | Native memory, heap allocation, buffer management, memory leaks | LWJGL malloc/free, ByteBuffer, OOM errors |
| `[RND]` | Rendering | OpenGL pipeline, shaders, textures, camera, mesh | Shader compilation, texture binding, VAO/VBO |
| `[IO]` | Input/Output | File system, resource loading, NIO, asset pipeline | NIO.loadString, file paths, IOException |
| `[ARC]` | Architecture | Code structure, design patterns, thread safety, API design | Component system, ECS, singleton abuse |
| `[SEC]` | Security | Input validation, deserialization, injection, unsafe operations | Path traversal, unsafe reflection |
| `[INP]` | Input Handling | Keyboard, mouse, controllers, event system | GLFW callbacks, key mapping, dead zones |
| `[PHY]` | Physics | Collision detection, rigid bodies, physics simulation | RePhysics, AABB, gravity, velocity |
| `[NET]` | Networking | Multiplayer, sockets, serialization, latency | UDP/TCP, packet loss, sync issues |
| `[UI]` | User Interface | GUI, HUD, menus, text rendering | Font rendering, button states, layout |
| `[PER]` | Performance | Frame rate, GC pressure, algorithmic complexity | 60 FPS target, draw call batching |
| `[DOC]` | Documentation | README, JavaDoc, API references, tutorials | Missing docs, incorrect examples |
| `[TST]` | Testing | Unit tests, integration tests, test coverage | Missing test coverage, flaky tests |
