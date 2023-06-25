import os

def compress_file(input_file, output_dir):
    # Get the base filename and directory of the input file
    base_name = os.path.basename(input_file)
    file_dir = os.path.dirname(input_file)

    # Compressed file name
    compressed_file = os.path.join(output_dir, base_name + '.gz')

    # Compress the file using gzip
    command = f"gzip -c {input_file} > {compressed_file}"
    os.system(command)

    print(f"File '{input_file}' compressed and stored in '{compressed_file}'")

def decompress_file(input_file, output_dir):
    # Get the base filename and directory of the input file
    base_name = os.path.basename(input_file)
    file_dir = os.path.dirname(input_file)

    # Decompressed file name
    decompressed_file = os.path.join(output_dir, base_name[:-3])  # Remove the '.gz' extension

    # Decompress the file using gzip
    command = f"gzip -d -c {input_file} > {decompressed_file}"
    os.system(command)

    print(f"File '{input_file}' decompressed and stored in '{decompressed_file}'")


# Example usage
input_file = './latent_files/lol.txt'  # Specify the path of the input file
output_dir = './zip_files'  # Specify the path of the output directory

compress_file(input_file, output_dir)
