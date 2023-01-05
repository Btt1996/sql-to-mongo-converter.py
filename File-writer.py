def write_to_file(results, filename):
    with open(filename, 'w') as f:
        for result in results:
            f.write(str(result) + '\n')
