import os
import time

# Create a simple HTML file to display the search input
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>GeoSearch Input Test</title>
    <style>
        /* Copy the relevant CSS from globals.css */
        /* Original GeoSearch Input */
        .ais-GeoSearch-input-original {
          -webkit-appearance: none;
          -moz-appearance: none;
          appearance: none;
          background-color: #fff;
          background-position: 50%;
          background-size: 180%;
          border: 1px solid currentcolor;
          border-radius: 3px;
          -webkit-box-shadow: inset 0 1px 4px 0 rgba(119, 122, 175, 0.4);
          box-shadow: inset 0 1px 4px 0 rgba(119, 122, 175, 0.4);
          color: #d6d6e7;
          cursor: inherit;
          height: 1rem;
          margin: 0 0.5rem 0 0;
          min-width: 1rem;
        }

        .ais-GeoSearch-input-original:checked {
          background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%235468ff%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%2220%206%209%2017%204%2012%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E');
          background-size: 14px;
          border-color: currentcolor;
          -webkit-box-shadow: rgba(35, 38, 59, 0.05) 0 1px 0 0 inset;
          box-shadow: rgba(35, 38, 59, 0.05) 0 1px 0 0 inset;
          color: #3c4fe0;
        }

        /* Updated GeoSearch Input */
        .ais-GeoSearch-input {
          -webkit-appearance: none;
          -moz-appearance: none;
          appearance: none;
          background-color: #fff;
          background-position: 50%;
          background-size: 180%;
          border: 2px solid currentcolor;
          border-radius: 0px;
          -webkit-box-shadow: inset 0 1px 4px 0 rgba(119, 122, 175, 0.4);
          box-shadow: inset 0 1px 4px 0 rgba(119, 122, 175, 0.4);
          color: #ff0000;
          cursor: inherit;
          height: 1.2rem;
          margin: 0 0.5rem 0 0;
          min-width: 1.2rem;
        }

        .ais-GeoSearch-input:checked {
          background-image: url('data:image/svg+xml;utf8,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20width%3D%2216%22%20height%3D%2216%22%20viewBox%3D%220%200%2024%2024%22%20fill%3D%22none%22%20stroke%3D%22%23ff0000%22%20stroke-width%3D%222%22%20stroke-linecap%3D%22round%22%20stroke-linejoin%3D%22round%22%3E%3Cpolyline%20points%3D%2220%206%209%2017%204%2012%22%3E%3C%2Fpolyline%3E%3C%2Fsvg%3E');
          background-size: 14px;
          border-color: currentcolor;
          -webkit-box-shadow: rgba(35, 38, 59, 0.05) 0 1px 0 0 inset;
          box-shadow: rgba(35, 38, 59, 0.05) 0 1px 0 0 inset;
          color: #ff0000;
        }

        /* Container for better visualization */
        .container {
            margin: 50px;
            padding: 20px;
            border: 1px solid #ccc;
        }

        h1 {
            font-family: Arial, sans-serif;
        }

        .input-container {
            margin: 20px 0;
        }

        label {
            display: block;
            margin-bottom: 10px;
            font-family: Arial, sans-serif;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>GeoSearch Input Test</h1>

        <div class="input-container">
            <label>Original GeoSearch Input (unchecked):</label>
            <input type="checkbox" class="ais-GeoSearch-input-original">
        </div>

        <div class="input-container">
            <label>Original GeoSearch Input (checked):</label>
            <input type="checkbox" class="ais-GeoSearch-input-original" checked>
        </div>

        <div class="input-container">
            <label>Updated GeoSearch Input (unchecked - more visible, less rounded, red):</label>
            <input type="checkbox" class="ais-GeoSearch-input">
        </div>

        <div class="input-container">
            <label>Updated GeoSearch Input (checked - more visible, less rounded, red):</label>
            <input type="checkbox" class="ais-GeoSearch-input" checked>
        </div>
    </div>
</body>
</html>
"""

# Write the HTML file
with open('/tmp/geosearch_test.html', 'w') as f:
    f.write(html_content)

print("Created test HTML file at /tmp/geosearch_test.html")
print("\nOriginal GeoSearch-input CSS properties:")
print("- Border radius: 3px (slightly rounded)")
print("- Color: #d6d6e7 (light gray)")
print("- Size: 1rem height and width")
print("- Border: 1px solid")
print("- Not very visible due to light color and small size")

print("\nUpdated GeoSearch-input CSS properties:")
print("- Border radius: 0px (not rounded)")
print("- Color: #ff0000 (red)")
print("- Size: 1.2rem height and width (20% larger)")
print("- Border: 2px solid (thicker)")
print("- More visible due to red color, larger size, and thicker border")

print("\nChanges made according to PR description:")
print("1. Made it more visible (larger size, thicker border)")
print("2. Made it less rounded (removed border radius)")
print("3. Changed the color to red (#ff0000)")

print("\nYou can view the comparison in the HTML file: /tmp/geosearch_test.html")