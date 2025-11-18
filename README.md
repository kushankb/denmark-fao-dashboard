# Denmark FAO Policy Mapping Dashboard

An interactive dashboard for exploring Denmark's policy alignment with the FAO Global Roadmap.

## Features

- **10 FAO Domains**: Visualized as an interactive donut chart
- **129 Roadmap Actions**: Detailed breakdown by domain
- **436 Policy Linkages**: Linked to policy documents with source references
- **278 Targets**: Target, baseline, and target year data
- **Smart Search**: Find actions, policy linkages, or targets by keyword across all domains
- **Document Links**: Direct access to policy documents via FAOLEX and other sources
- **Deduplication**: Unique policy linkages and targets shown with all related actions

## Search Functionality

1. **Search Actions**: Find specific roadmap actions
2. **Search Policy Linkages**: Find all unique policy linkages matching a keyword - see which actions they're linked to
3. **Search Targets**: Find all unique targets matching a keyword - compare across different actions

## Domain Statistics

- **Clean Energy**: 18 actions, 24 unique policies (75 linkages), 34 targets
- **Crops**: 14 actions, 16 unique policies (53 linkages), 56 targets
- **Data**: 12 actions, 18 unique policies (32 linkages), 0 targets
- **Enabling Healthy Diets for All**: 11 actions, 11 unique policies (29 linkages), 4 targets
- **Fisheries and Aquaculture**: 10 actions, 15 unique policies (40 linkages), 5 targets
- **Food Loss and Waste**: 10 actions, 9 unique policies (20 linkages), 57 targets
- **Forests and Wetlands**: 14 actions, 11 unique policies (36 linkages), 37 targets
- **Inclusive Policies**: 15 actions, 24 unique policies (52 linkages), 0 targets
- **Livestock**: 10 actions, 12 unique policies (30 linkages), 47 targets
- **Soil and Water**: 15 actions, 22 unique policies (69 linkages), 38 targets

## How to Use

1. **Explore Domains**: Hover over the donut chart to see domain statistics
2. **Drill Down**: Click on any domain to view its roadmap actions
3. **View Details**: Select a roadmap action to see associated targets and policy linkages
4. **Search**: Use the search tabs to find specific actions, linkages, or targets by keyword

## Data Source

FAO Denmark Policy Document Analysis - Last updated: November 2024

## Technical Details

- Built with React 18 and Tailwind CSS
- Interactive SVG visualizations
- Responsive design with dark theme
- No backend required - runs entirely in the browser
