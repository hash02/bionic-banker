# Bionic Control Desk design system

## Position

Bionic Banker uses **Bionic Control Desk** as its public design system.

The site should feel like a calm operating surface for AI, finance, evidence, and control work — not a generic blog, not a crypto dashboard, and not a decorative sci-fi page.

## Identity

Core palette:

- black / near-black base
- Bionic green for trust, evidence, action, and active controls
- soft white for reading
- blue for intelligence/model/system lanes
- pink only for warning, adversarial, prompt-injection, or exception lanes

Use blue and pink sparingly. They are category lanes, not a new brand identity.

## Design rule

Every important public surface should answer:

1. Where am I?
2. What is the source or input?
3. What control or review step exists?
4. What is the limit?
5. What can I inspect next?

## Component grammar

### Console shell

Use when a page needs orientation.

Parts:

- explorer/sidebar or compact route rail
- top path/command label
- grouped rows
- category lane colors
- grid/radial background field

### Evidence card

Use for articles, projects, and demos.

Parts:

- claim or project name
- input/source
- output
- boundary/limit
- inspection link

### Control flow diagram

Use when motion or 3D clarifies the idea.

Default flow:

```text
input/source -> model/system -> gate/review -> output/record
```

### Project package card

Use for public project surfaces.

Parts:

- what it does
- who it helps
- input
- output
- proof/verification
- boundary
- first revenue lane hypothesis

## Motion rules

Motion should explain control flow, not decorate the page.

Allowed:

- slow grid shimmer
- row hover shift
- scanline on console panels
- animated SVG arrows for source -> gate -> record
- CSS 3D stacks on hero/system overview surfaces

Avoid:

- moving body text
- constant distracting loops beside long reading sections
- heavy 3D on every page
- animation without `prefers-reduced-motion` support

## Page alignment priorities

1. Articles — intelligence library, not plain blog archive.
2. Projects — package shelf with proof, boundary, and revenue-edge framing.
3. AI Models — model/concept map with control boundaries.
4. AI Intelligence — source queue and control desk.
5. About — operator profile, public boundary, and system philosophy.

## Packaging principle

Bionic Banker should make projects legible to three audiences:

- risk/compliance/AI governance buyers
- hiring/collaboration reviewers
- builders comparing systems and execution taste

A project is not packaged until a reader can see:

```text
problem -> input -> system -> output -> evidence -> limit -> next step
```

## Revenue direction

Do not force monetization too early. First revenue lane should come from packaged trust:

1. public project packages that prove judgment and implementation quality
2. lightweight advisory/review offers around AI controls, agent safety, evidence records, and compliance-oriented AI workflows
3. repeatable templates/checklists later, only after enough proof accumulates

The design system should make that trust visible without turning the site into a sales page.
