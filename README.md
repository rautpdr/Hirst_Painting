# HIRST PAINTING PROJECT

A Python program that recreates Damien Hirst's famous dot-style artwork using the Turtle graphics module. This project uses Object-Oriented Programming (OOP) and color extraction to automate the creation of visually appealing dot patterns.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

This project is inspired by Damien Hirst's spot paintings. It generates a grid of colored dots using Python's Turtle module and a palette extracted from an image using the `colorgram` library. The painting is automatically drawn with a modern, abstract art style.

## How it Works

1. **Run the Script**: Execute the `main.py` file.
2. **Color Extraction**: The `colorgram` library extracts a set of dominant colors from an input image.
3. **Dot Grid Generation**:
   - The turtle draws a grid of evenly spaced dots.
   - Each dot is randomly assigned a color from the extracted palette.
4. **Visual Output**: The result is a Hirst-style digital painting created right in the Turtle graphics window.

## Technologies Used

- **Python**: Core programming language
- **Turtle**: For drawing and graphics
- **colorgram.py**: For extracting color palettes from images
- **OOP**: To organize drawing logic cleanly and modularly

## Lessons Learned

Working on this project helped reinforce:

- **Object-Oriented Design**: Structuring drawing logic within a class
- **Automated Graphics**: Using loops and position tracking for consistent spacing
- **Color Processing**: Extracting and applying colors from images to visual output
- **Creative Programming**: Mixing logic with generative art concepts
