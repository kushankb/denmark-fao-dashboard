# Denmark FAO Policy Mapping Dashboard

An interactive dashboard for exploring Denmark's policy alignment with the FAO Global Roadmap.

## Features

- **10 FAO Domains**: Visualized as an interactive ring of official FAO Roadmap domain icons
- **129 Roadmap Actions**: Detailed breakdown by domain
- **390 Policy Linkages**: Linked to policy documents with source references
- **103 Targets**: Target, baseline, and target year data
- **Smart Search**: Find actions, policy linkages, or targets by keyword across all domains
- **Document Links**: Direct access to policy documents via FAOLEX and other sources
- **Deduplication**: Unique policy linkages and targets shown with all related actions

## Search Functionality

1. **Search Actions**: Find specific roadmap actions
2. **Search Policy Linkages**: Find all unique policy linkages matching a keyword - see which actions they're linked to
3. **Search Targets**: Find all unique targets matching a keyword - compare across different actions

## Domain Statistics

- **Clean Energy**: 18 actions, 21 unique policies (56 linkages), 13 targets
- **Crops**: 14 actions, 16 unique policies (54 linkages), 24 targets
- **Data**: 12 actions, 13 unique policies (24 linkages), 0 targets
- **Enabling Healthy Diets for All**: 11 actions, 11 unique policies (25 linkages), 6 targets
- **Fisheries and Aquaculture**: 10 actions, 14 unique policies (37 linkages), 0 targets
- **Food Loss and Waste**: 10 actions, 8 unique policies (24 linkages), 7 targets
- **Forests and Wetlands**: 14 actions, 12 unique policies (36 linkages), 22 targets
- **Inclusive Policies**: 15 actions, 21 unique policies (50 linkages), 0 targets
- **Livestock**: 10 actions, 10 unique policies (22 linkages), 15 targets
- **Soil and Water**: 15 actions, 20 unique policies (62 linkages), 16 targets

## How to Use

1. **Explore Domains**: Hover over a domain icon in the ring to see its statistics
2. **Drill Down**: Click on any domain icon to view its roadmap actions
3. **View Details**: Select a roadmap action to see associated targets and policy linkages
4. **Search**: Use the search tabs to find specific actions, linkages, or targets by keyword

## Data Source

FAO Denmark Policy Document Analysis - Last updated: June 2026

Generated from `Database_Denmark_dashboard.xlsx` via `build_data.py`, which produces
`dashboard_data.js`. To refresh the dashboard with new data, update the spreadsheet and
re-run `python3 build_data.py`.

## Technical Details

- Built with React 18 and Tailwind CSS
- Interactive SVG visualizations; domain ring uses the official FAO Roadmap icons (`icons/`)
- Responsive design with dark theme
- No backend required - runs entirely in the browser
- Babel standalone is pinned to `@babel/standalone@7.25.6` (classic JSX runtime) so the
  in-browser transform works without a build step
