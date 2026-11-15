# Microwell® Commercial Mattress Systems — Development Guidelines & Architectural Standards

> **Version:** 2.4.0  
> **Target Production:** Contract-Grade B2B Wholesale Mattress Manufacturing Platform  
> **Live Server:** `http://localhost:3000/` (`serve.py`)  
> **Workspace Root:** `x:\KODENCORE\microwell`  

---

## 1. Executive Architecture & Core Doctrine

The Microwell® web platform is engineered as an ultra-high-performance, contract-grade commercial mattress wholesale portal. It serves volume commercial buyers, hospitality purchasing directors, healthcare facilities, and authorized contract furniture dealers.

### Core Engineering Principles:
1. **Zero Runtime Bloat:** Pure HTML5, Tailwind CSS utilities, modular vanilla JavaScript, and zero heavyweight external framework runtimes.
2. **Deterministic Layout Stability:** Zero Cumulative Layout Shift (CLS), zero font flashes (FOUT/FOIT), and instant local rendering.
3. **Lazy Senior Dev Rule (Ponytail Doctrine):** Boring over clever. The shortest working diff wins. Do not introduce abstractions, frameworks, or dependencies that were not explicitly requested.

---

## 2. Page & Routing Architecture

All primary routes use descriptive, SEO-optimized filenames with automatic 301 redirects configured in `serve.py` for backward compatibility with legacy endpoints.

| Route / Target File | SEO URL | Purpose |
| :--- | :--- | :--- |
| **`index.html`** | `/` or `/index.html` | Commercial flagship overview, full-screen kinetic mattress gallery, typographic echo stack, 12-column showcase grid, bespoke services, and logistics freight simulator. |
| **`commercial-mattress-catalog.html`** | `/commercial-mattress-catalog.html` | B2B catalog featuring monolithic cold foam, 5-zone pocket spring hybrids, and medical-grade waterproof mattresses with MOQ specifications. |
| **`commercial-mattress-spec-sheets.html`** | `/commercial-mattress-spec-sheets.html` | Architectural submittals, CAD cross-sections, ASTM compression ratings, and technical submittal downloads. |
| **`mattress-certifications-compliance.html`** | `/mattress-certifications-compliance.html` | Full-scale Title 16 CFR Part 1633 calorimeter burn curves, CertiPUR-US® certifications, and OEKO-TEX Standard 100 documentation. |
| **`wholesale-dealer-portal.html`** | `/wholesale-dealer-portal.html` | B2B dealer onboarding application, tiered trade pricing calculator, and dock-receiving authorization. |

### Legacy Aliases (Maintained in Sync):
- `catalog.html` $\rightarrow$ Mirrors `commercial-mattress-catalog.html`
- `spec-sheets.html` $\rightarrow$ Mirrors `commercial-mattress-spec-sheets.html`
- `compliance.html` $\rightarrow$ Mirrors `mattress-certifications-compliance.html`
- `onboarding.html` $\rightarrow$ Mirrors `wholesale-dealer-portal.html`

---

## 3. Strict Typography Doctrine

To maintain institutional authority and editorial elegance, the platform strictly enforces **two Google font families** across all pages. **No other fonts (such as Clash Display, Satoshi, Playfair Display, or JetBrains Mono) are permitted.**

```html
<!-- MANDATORY GOOGLE FONTS PRECONNECT & STYLESHEET -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Merriweather:ital,wght@0,300;0,400;0,700;0,900;1,300;1,400;1,700&family=Raleway:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,600;1,700&display=swap" rel="stylesheet">
```

### Font Usage Matrix:
| Element Category | Font Family | Tailwind Class | Weight / Spec |
| :--- | :--- | :--- | :--- |
| **Headings (`h1`–`h6`)** | `Raleway` | `font-raleway` | 700 to 900 (`font-bold` / `font-black`), tracking `-0.04em` |
| **Hero Echo Stack** | `Raleway` | `font-raleway` | 900 (`font-black`), uppercase, tracking `-0.05em` |
| **Navigation & Links** | `Raleway` | `font-raleway` | 700 (`font-bold`), uppercase, tracking `0.05em` |
| **Buttons & Badges** | `Raleway` | `font-raleway` | 700 (`font-bold`), uppercase, tracking `0.05em` |
| **Telemetry & Metrics** | `Raleway` | `font-raleway` | 700 to 900, tight tracking |
| **Body Copy & Prose** | `Merriweather` | `font-merriweather` | 400 (`font-normal`), leading `1.7` |
| **Editorial Quotes** | `Merriweather` | `font-merriweather` | 400 / 300 Italic (`italic`) |
| **Product Specifications** | `Merriweather` | `font-merriweather` | 300 to 400, crisp high-legibility serif |

---

## 4. Color Palette & Surface System

The color architecture directly incorporates the signature chromatic palette extracted from the official **Microwell® Emblem Logo** (`assets/logo.jpg`):

### Official Brand Color Tokens:
* **Primary Brand Purple:** `#582C84` (Deep Royal Velvet Purple — emblem wing core & button base)
* **Vibrant Brand Magenta:** `#C0227B` (Radiant Berry Magenta — hover fill circles & active pulse dots)
* **Brand Gradient:** `linear-gradient(135deg, #582C84 0%, #C0227B 100%)`
* **Canvas:** `#ffffff` (Pure architectural white)
* **Text / Ink:** `#111111` (Deep contract black)
* **Subtle Dividers & Borders:** `#1e1e1e` at `10%` opacity (`border-[#1e1e1e]/10`)
* **Muted Badges & Subtitles:** `#838282`
* **Deep Architectural Surfaces:** `#080807` (Monolog Footer)

```css
:root {
  --brand-purple: #582C84;
  --brand-magenta: #C0227B;
  --brand-purple-dark: #3F1E60;
  --brand-magenta-light: #D62F8A;
  --brand-gradient: linear-gradient(135deg, #582C84 0%, #C0227B 100%);
  --bg-canvas: #ffffff;
  --text-ink: #111111;
  --font-heading: 'Raleway', sans-serif;
  --font-body: 'Merriweather', serif;
}
```

### Application in Interactive Components:
1. **Framer ArrowFillButton:**
   - Base idle: `#582C84` (Royal Purple pill).
   - Hover fill circle: `#C0227B` (Vibrant Magenta expands from the right icon).
2. **Floating Navbar:**
   - Active link pill: `#582C84` with subtle glow (`box-shadow: 0 4px 14px rgba(88, 44, 132, 0.28)`).
   - Hover highlight: `rgba(88, 44, 132, 0.08)`.
3. **Monolog Footer:**
   - Status pulse dot: `#C0227B` with radiant magenta shadow bloom.
   - Interactive link hovers: `#C0227B`.
4. **StoryBreeze Carousel:**
   - Active slider indicator dot: `#582C84`.

---

## 5. Framer ArrowFillButton Component Standard

All interactive action triggers across the platform implement the native CSS/SVG recreation of Framer's **ArrowFillButton** component (`https://framer.com/m/ArrowFillButton-XA9BdX.js@8FpuUU9JGHf6w7gl8m3c`).

### Mechanics & Anatomy:
* **Background Pill:** Rounded full (`border-radius: 9999px`) with 1px border.
* **Expanding Fill Circle (`.hpx-afb__circle`):** Originates from the arrow circular container on the right and smoothly expands over `450ms cubic-bezier(0.785, 0.135, 0.15, 0.86)` to flood the button background on `:hover`.
* **Masked Dual-Color Text (`.hpx-afb__mask`):** Utilizes `clip-path: inset(...)` synchronized to the expanding circle so the text changes color cleanly as the circle passes over it.
* **Dual-Translate SVG Arrows (`.hpx-afb__icon`):** Contains two SVG arrows; on hover, the exit arrow slides out to the right (`translate(70%, -50%) scale(0)`) while the enter arrow sweeps in from the left (`translate(-50%, -50%) scale(1)`).

### Component HTML Markup Template:

```html
<a href="wholesale-dealer-portal.html" class="hpx-afb hpx-afb--sm" style="--btn-bg: #111111; --btn-text: #ffffff; --btn-border: #111111; --btn-fill-bg: #ffffff; --btn-fill-text: #111111; --btn-fill-bg-hover: #ffffff; --btn-fill-text-hover: #111111; --btn-arrow: #111111; --btn-arrow-hover: #111111; --btn-duration: 450ms;">
  <span class="hpx-afb__label">Request Wholesale Quote</span>
  <div aria-hidden="true" class="hpx-afb__circle"></div>
  <div aria-hidden="true" class="hpx-afb__mask">
    <span class="hpx-afb__mask-label">Request Wholesale Quote</span>
  </div>
  <span aria-hidden="true" class="hpx-afb__icon">
    <svg class="hpx-afb__icon-svg hpx-afb__icon-svg--enter" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 12h14"></path>
      <path d="m12 5 7 7-7 7"></path>
    </svg>
    <svg class="hpx-afb__icon-svg hpx-afb__icon-svg--exit" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M5 12h14"></path>
      <path d="m12 5 7 7-7 7"></path>
    </svg>
  </span>
</a>
```

### Button Variants & Brand Logo Color Integration:
1. **Brand Royal Velvet Purple (`--btn-bg: #582C84`, `--btn-text: #ffffff`):**
   - **Idle State:** Deep Royal Velvet Purple pill with white text and a clean white circle (`--btn-fill-bg: #ffffff`) containing a purple arrow (`--btn-arrow: #582C84`).
   - **Hover Interaction:** Circle expands into Vibrant Berry Magenta (`--btn-fill-bg-hover: #C0227B`) with white text and white arrow, dynamically demonstrating the logo's purple-to-magenta chromatic transition.
2. **Size Modifiers:**
   - Default: `height: 44px`, font size `12px`
   - Compact: `.hpx-afb--sm` (`height: 38px`, font size `11px`)
   - Large: `.hpx-afb--lg` (`height: 52px`, font size `13px`)
   - Full Width: `.w-full` (`width: 100% !important`)

---

## 6. Header & Navigation Architecture

Every page incorporates the **Fixed Transparent Modern Navbar** (`https://framer.com/m/Modern-Navbar-VoWUeq.js@oVVLpffE3sD117Do5FBy`) recreation:

```html
<header class="modern-navbar-header" id="modernNavbar">
  <div class="modern-navbar-inner">
    <!-- Brand Identity on Left -->
    <a href="index.html" class="flex items-center gap-3.5 group flex-shrink-0">
      <div class="modern-brand-logo-box">
        <img src="assets/logo.jpg" alt="Microwell Mattress Logo" class="w-full h-full object-contain">
      </div>
      <div class="flex flex-col">
        <span class="font-raleway font-bold text-lg sm:text-xl tracking-[-0.04em] text-ink uppercase leading-none">
          MICROWELL<span class="text-[10px] align-super">®</span>
        </span>
        <span class="font-raleway text-[8px] sm:text-[9px] uppercase tracking-[0.22em] text-[#838282] font-semibold mt-0.5">
          Exploring the world in comfort
        </span>
      </div>
    </a>
    
    <!-- Right-Aligned Cluster: Capsule Nav Group + CTA Button + Mobile Toggle -->
    <div class="flex items-center gap-3 sm:gap-4 ml-auto">
      <nav class="modern-nav-group" aria-label="Primary Navigation">
        <a href="commercial-mattress-catalog.html" class="modern-nav-link">Catalog</a>
        <a href="commercial-mattress-spec-sheets.html" class="modern-nav-link">Spec Sheets</a>
        <a href="mattress-certifications-compliance.html" class="modern-nav-link">Compliance</a>
        <a href="wholesale-dealer-portal.html" class="modern-nav-link">Dealer Portal</a>
      </nav>
      <!-- CTA Pill Button (ArrowFillButton) -->
      <div class="hidden sm:flex items-center">
        ... (ArrowFillButton: "Request Wholesale Quote") ...
      </div>
      <!-- Framer Morphing 2-Bar Hamburger Toggle -->
      <button class="modern-menu-btn" id="modernMenuBtn" aria-label="Toggle Menu">
        <span class="modern-menu-bar"></span>
        <span class="modern-menu-bar"></span>
      </button>
    </div>
  </div>
  <!-- Framer Mobile Slide-Down Drawer -->
  <div class="modern-mobile-drawer" id="modernMobileDrawer">...</div>
</header>
<div class="modern-backdrop-overlay" id="modernBackdropOverlay"></div>
```

---

## 7. Hero Section Specification (`index.html`)

The Hero Section is strictly minimalist and focused on pure brand impact:
* **Background:** Full-screen (`min-h-screen`) right-to-left continuous moving marquee (`hero-bg-gallery-track`, 50s linear infinite loop) displaying 12 high-resolution commercial mattress photographs (Set A + Set B seamless clone).
* **Zero Grey Tint:** No dark wash, no grey tint, and no visual degradation over the imagery.
* **No White Background Card:** No card container, no sub-headline text, and no action buttons inside the hero viewport.
* **Foreground:** Strictly **ONLY `MICROWELL`** rendered in the 5-layer typographic echo stack (`Raleway 900`, `text-[14vw] lg:text-[180px]`).

---

## 8. Pre-Commit Quality & Verification Protocol

Before pushing or landing any changes, run the automated verification script:

```powershell
python scratch/comprehensive_audit.py
```

### Verification Checklist:
- [x] Tag closure balance (`<header>`, `<main>`, `<footer>`, `<nav>`, `<html>`, `<body>`) has zero mismatches.
- [x] Zero nested button markup (no `<a>` inside `<a>` or `<button>` inside `<button>`).
- [x] Strictly two fonts: `Raleway` & `Merriweather`.
- [x] All CTA buttons implement the native Framer ArrowFillButton.
- [x] Navigation items pushed right (`ml-auto`) with clean labels (`Catalog`, `Spec Sheets`, `Compliance`, `Dealer Portal`).
- [x] HTTP 200 on all endpoints via `serve.py`.


---

## 9. Framer StoryBreeze Component Specification (`catalog.html`)

The Commercial Mattress Catalog implements Framer's **StoryBreeze** component (`https://framer.com/m/StoryBreeze-Fvm3iX.js@PYF9PjicqZhGGefTO6k7`) for interactive model exploration.

### Mechanics & Anatomy:
* **Focal Card (`.is-active`):** Positioned front and center with crisp contrast (`scale(1)`, `opacity: 1`, `filter: blur(0px)`, `z-index: 30`).
* **Flanking Cards (`.is-prev`, `.is-next`):** Offset laterally by 65% with depth scale (`scale(0.88)`), reduced opacity (`0.45`), and subtle depth blur (`filter: blur(3px)`).
* **Breathe Transition:** Dynamic cubic-bezier easing (`cubic-bezier(0.785, 0.135, 0.15, 0.86)`) delivers kinetic motion with a subtle dip on transition.
* **Navigation Controls:**
  - Previous / Next circular arrow buttons (`.sb-round-btn`) with active scale feedback (`scale(0.92)`).
  - Pill dot progress indicators (`.sb-dot`).
  - Pointer/Touch drag with swipe-distance threshold (`diffX > 50px` or `diffX < -50px`).
  - Keyboard navigation (`ArrowLeft` / `ArrowRight`).
* **Integrated Sub-Components:** Each StoryBreeze card encapsulates high-resolution mattress photography, a frosted glass pill badge (`backdrop-filter: blur(8px)`), a technical spec matrix, and two native **ArrowFillButton** instances (`Add To RFQ Quote` & `Download Spec PDF`).


*Note on StoryBreeze Card Aesthetics (v2.4.1):*
- All photo overlay badges (`.sb-badge`), stock status pills (`● In Stock (Factory Direct)`), and pre-header category pill tags (`bg-[#111111]`) have been removed from the catalog cards to preserve an unobstructed view of the mattress photography and allow model titles to lead with prominence.


---

## 10. Framer Modern Navbar Component Specification (`Modern-Navbar-VoWUeq`)

The global navigation system is built upon the Framer **Modern Navbar** component (`https://framer.com/m/Modern-Navbar-VoWUeq.js@oVVLpffE3sD117Do5FBy`). It is engineered with a **Fixed Transparent** layout pinned to the top of the viewport.

### Key Architectural Characteristics:
1. **Fixed Transparent Layout (`.modern-navbar-header`):**
   - **Position:** `position: fixed; top: 0; left: 0; right: 0; width: 100%; height: 76px; z-index: 50;`
   - **100% Transparent Throughout:** The navbar remains completely transparent site-wide (`background-color: transparent !important; border-bottom: 1px solid transparent !important; box-shadow: none !important;`) both at rest and during scrolling (`.is-scrolled`), allowing page content and photography to show through seamlessly with zero white background.
   - **Transparent Nav Group (`.modern-nav-group`):** Center links sit directly and transparently on the page (`background-color: transparent !important; border: 1px solid transparent !important; box-shadow: none !important;`) without any white pill backing.

2. **Inner Container (`.modern-navbar-inner`):**
   - Full edge-to-edge max-width container (`max-width: 1600px; width: 100%; height: 100%; margin: 0 auto; padding: 0 20px; sm:padding: 0 36px; lg:padding: 0 48px;`).
   - Flex layout with brand anchored on the left and navigation elements pushed to the right (`ml-auto`).

3. **Pill Capsule Nav Group (`.modern-nav-group`):**
   - Frosted pill container: `border-radius: 9999px; background-color: rgba(255, 255, 255, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(30, 30, 30, 0.1);`.
   - Links render in **Raleway Bold** (`12px uppercase tracking-wider`).
   - Active link (`.is-active`): Royal Purple (`#582C84`) with soft brand glow (`box-shadow: 0 4px 14px rgba(88, 44, 132, 0.28)`).
   - Hover highlight: `rgba(88, 44, 132, 0.08)` with text `#582C84`.

4. **Mobile Slide-Down Drawer (`.modern-mobile-drawer`):**
   - Slides down directly under the 76px header with frosted glass (`rgba(255, 255, 255, 0.98); backdrop-filter: blur(24px)`).
   - Contains stacked navigation links and a full-width Royal Purple **ArrowFillButton**.

---

## 11. Framer Web-Preload Component Specification (`Web-Preload-UaqAMh`)

The entrance experience incorporates the Framer **Web-Preload** component (`https://framer.com/m/Web-Preload-UaqAMh.js@R7u4jLJXp3giqh8d4qJn`). It is engineered in pure semantic HTML5, CSS animations, and modular vanilla JavaScript.

### Key Architectural Characteristics:
1. **Theatrical Curtain Elevation (`#preloadCurtain`):**
   - Fullscreen overlay (`position: fixed; inset: 0; width: 100vw; height: 100vh; z-index: 99999;`).
   - Pure white background (`#ffffff`) with zero transparency bleed until exit.
   - Exit Animation: Smooth vertical curtain lift (`transform: translateY(-100%);`) powered by Framer's bespoke bezier curve `cubic-bezier(1, 0.01, 0.38, 1.01)` over a 1000ms duration.
   - Upon completion, the element is removed from the accessibility tree (`aria-hidden="true"; display: none;`) and standard viewport scroll locks (`overflow: hidden`) are released.

2. **Ambient Brand Blooms:**
   - Soft pulsing radial glows positioned behind the typography:
     - **Microwell Purple (`#582C84`):** Bottom-left bloom (`rgba(88, 44, 132, 0.22)` with `filter: blur(70px)`).
     - **Microwell Magenta (`#C0227B`):** Top-right bloom (`rgba(192, 34, 123, 0.18)` with `filter: blur(70px)`).

3. **Staggered Character Typographic Entrance:**
   - Brand Emblem: Circular floating badge (`.preload-brand-badge`) scales into place with a subtle spring.
   - Main Title (`MICROWELL®`): Rendered in **Raleway 900**. Each letter (`.preload-char`) begins at `scale(1.8)`, `filter: blur(12px)`, and `opacity: 0.001`, resolving into crisp, high-impact solid black typography via character-index staggered delays (`calc(300ms + (idx * 55ms))`).

4. **Staggered Kinetic Slogan Cycle:**
   - Slogans dynamically split into characters and cycle through Microwell brand commitments:
     - `"Exploring the world in comfort"`
     - `"Engineering commercial sleep systems"`
     - `"Precision contract manufacturing"`
   - Font: **Raleway Bold** (`text-[11px] sm:text-[14px] uppercase tracking-[0.22em] text-[#838282]`).

5. **Timing & Instant Skip Controls:**
   - Auto-dismisses at 2600ms on desktop (2900ms on mobile).
   - Instant skip capability: Clicking anywhere or pressing `Escape`/`Space` triggers immediate curtain lift.


---

## 12. Monolog Footer Composition Specification (`footer.design/sites/monolog`)

The site-wide footer is an exact replica of the minimalist **Monolog** footer architecture (`https://www.footer.design/sites/monolog`), stripped of all extraneous marketing fluff, meta headings, or unnecessary boxes, cleanly tailored to Microwell data.

### Key Architectural Characteristics:
1. **Color Palette & Surface:**
   - Minimalist brutalist deep tone: `#0a0a0a` with hairline top border (`border-t border-white/10`).
   - Clean Raleway typography in high-contrast crisp white (`#ffffff`) and soft zinc (`#ddddd5` / `text-zinc-400` / `text-zinc-500`).

2. **Top Metadata Header Line:**
   - Left: `● Navigation` with subtle bullet dot.
   - Right: `(COMPANY DETAILS)`.

3. **Two-Column Main Composition:**
   - **Left Column (Stacked Nav Links):** Large editorial navigation links (`About`, `Catalog`, `Specifications`, `Compliance`, `Wholesale`, `Contact`) separated by subtle 1px hairline dividing borders, smoothly translating on hover.
   - **Right Column (Socials & Direct Contact):**
     - Outbound directional links with diagonal arrows (`LinkedIn ↗`, `Instagram ↗`, `Wholesale Desk ↗`).
     - Accreditation badge (`ISO 9001:2015 & BIS Certified`).
     - Clear geographical facility location (`Based in Mohali, Punjab, India. Working Worldwide.`).
     - Clean email link with directional arrow (`↳ contact@microwell.in`).

4. **Bottom 3-Column Metadata Bar:**
   - **Left:** Manufacturing location & time zone (`Mohali City [IST]`).
   - **Center:** Smooth scroll trigger (`Back to top ↑`) with active production run status.
   - **Right:** Trademark declaration (`©2026 MICROWELL MATTRESS`).
