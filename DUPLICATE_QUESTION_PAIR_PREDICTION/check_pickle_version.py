import pickle
import sys

def get_pickle_protocol_version(file_path):
    with open(file_path, 'rb') as f:
        # Load the pickle file header
        header = pickle.load(f)

        # Check the protocol version
        protocol_version = pickle.format_version
        return protocol_version

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python check_pickle_version.py <pickle_file_path>")
        sys.exit(1)

    pickle_file_path = sys.argv[1]
    protocol_version = get_pickle_protocol_version(pickle_file_path)
    print("Pickle protocol version:", protocol_version)
