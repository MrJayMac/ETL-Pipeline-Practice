
def main():
    pass


if __name__ == "__main__":
    toronto_bbox = (43.3, -79.8, 44.0, -78.8)
    data = extract_data(bbox=toronto_bbox)
    if data:
        print(f"Found {len(data['states'])} flights over Toronto.")
