# Product Backlog — Sistema de Préstamo de Equipos Tecnológicos

## HU01 — Registrar equipos tecnológicos

**Historia de usuario:**

Como administrador, quiero registrar equipos tecnológicos para mantener actualizado el inventario.

**Prioridad:** Alta  
**Story Points:** 3

### Criterios de aceptación

- El sistema permite registrar un equipo con código, tipo, marca, modelo y estado.
- No permite registrar campos vacíos ni un código de equipo duplicado.
- El equipo queda guardado y disponible para consultarlo después.

---

## HU02 — Consultar equipos registrados

**Historia de usuario:**

Como administrador, quiero consultar los equipos registrados para ver su disponibilidad.

**Prioridad:** Alta  
**Story Points:** 2

### Criterios de aceptación

- El sistema muestra el listado completo de equipos registrados.
- Cada equipo se muestra junto con su estado de disponibilidad.
- Si no hay equipos registrados, el sistema informa que el inventario está vacío.

---

## HU03 — Registrar estudiantes

**Historia de usuario:**

Como administrador, quiero registrar estudiantes para asociarlos a los préstamos.

**Prioridad:** Alta  
**Story Points:** 3

### Criterios de aceptación

- El sistema permite registrar documento, nombre, correo y programa académico.
- No permite campos obligatorios vacíos.
- El estudiante queda almacenado para utilizarlo posteriormente en un préstamo.

---

## HU04 — Registrar préstamo

**Historia de usuario:**

Como administrador, quiero registrar el préstamo de un equipo a un estudiante.

**Prioridad:** Alta  
**Story Points:** 5

### Criterios de aceptación

- El sistema valida que el estudiante exista.
- El sistema valida que el equipo exista.
- El sistema verifica que el equipo esté disponible.
- El préstamo queda registrado.
- El estado del equipo cambia a "Prestado".

---

## Resumen

| ID | Historia | Prioridad | Story Points |
|---|---|---|---:|
| HU01 | Registrar equipos | Alta | 3 |
| HU02 | Consultar equipos | Alta | 2 |
| HU03 | Registrar estudiantes | Alta | 3 |
| HU04 | Registrar préstamo | Alta | 5 |

**Total: 13 Story Points**