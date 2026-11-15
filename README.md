# MICROWELL MATTRESS® — Commercial B2B Wholesale Systems

High-performance, editorial B2B commercial mattress digital infrastructure engineered for contract hospitality procurement, wholesale dealer distribution, institutional specifications, and factory-direct supply chains.

## Project Structure

```
microwell/
├── index.html                               # Core enterprise landing page
├── commercial-mattress-catalog.html        # Interactive 3D StoryBreeze commercial catalog
├── commercial-mattress-spec-sheets.html    # Engineering submittal matrices & CAD downloads
├── mattress-certifications-compliance.html # ISO 9001, BIS, ASTM & flammability compliance
├── wholesale-dealer-portal.html            # Tiered pricing, freight simulator & dealer intake
├── DEVELOPMENT_GUIDELINES.md               # Architectural principles & design system
├── vercel.json                             # Vercel deployment configuration & redirects
├── netlify.toml                            # Netlify routing & header rules
├── .github/workflows/deploy.yml            # GitHub Pages automated deployment pipeline
├── serve.py                                # Local threaded development server
└── assets/
    └── logo.jpg                            # Official brand emblem logo
```

## Quick Start (Local Development)

```bash
python serve.py
```
Open [http://localhost:3000](http://localhost:3000) in your browser.

## Deployment Options

### 1. Vercel
Connect this GitHub repository to [Vercel](https://vercel.com) for instant automatic zero-config deployments powered by `vercel.json`.

### 2. Netlify
Connect this GitHub repository to [Netlify](https://netlify.com) for edge-routed continuous deployments configured via `netlify.toml`.

### 3. GitHub Pages
Enable GitHub Pages in your repository settings:
`Settings -> Pages -> Build and deployment -> Source: GitHub Actions`.

---
© 2026 MICROWELL MATTRESS® INC. "EXPLORING THE WORLD IN COMFORT". ALL RIGHTS RESERVED.
