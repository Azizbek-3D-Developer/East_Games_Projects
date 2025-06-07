# 🎨 TF-IDF Web App — Color Palette & Style Guide

## 📘 Color Palette

| Purpose           | Color (Hex) | Usage Class / Selector           |
|-------------------|-------------|----------------------------------|
| Background        | `#121212`   | `body`                           |
| Primary Text      | `#E0E0E0`   | `body`, `.a_a-main-content`      |
| Secondary Text    | `#B0B0B0`   | `.a_a-footer`                    |
| Accent Color      | `#BB86FC`   | `a`, `.a_a-nav-avatar` border    |
| Nav Background    | `#1F1B24`   | `.a_a-navbar`                    |
| Footer Background | `#1A1A1A`   | `.a_a-footer`                    |
| Hover / Focus     | `#3700B3`   | `a:hover`, `.a_a-navbar` border  |

---

## 🧩 Usage Examples

### 💡 Basic Background & Text

```css
body {
    background-color: #121212;
    color: #E0E0E0;
}
```


### 🔗 Links & Hover
```css
a {
    color: #BB86FC;
}

a:hover,
a:focus {
    color: #3700B3;
}
```

### Navbar
```css
.a_a-navbar {
    background-color: #1F1B24;
    border-bottom: 1px solid #3700B3;
}
```


### Avatar Border
```css
.a_a-nav-avatar {
    border: 2px solid #BB86FC;
}
```

### Footer
```css
.a_a-footer {
    background-color: #1A1A1A;
    color: #B0B0B0;
    border-top: 1px solid #3700B3;
}
```

### Suggested Font
```css
body{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
```


### 🔖Notes
All class selectors are prefixed with a_a- to prevent conflicts with global styles.

Consider using CSS variables for reuse:
```css
:root {
    --accent-color: #BB86FC;
    --hover-color: #3700B3;
}
```
### Then this
```css
a {
    color: var(--accent-color);
}

a:hover {
    color: var(--hover-color);
}
```
